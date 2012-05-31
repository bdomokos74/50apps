-- Returns the min/max length of words on a website, also the number of 
-- the different word occurrences
--
-- Usage: word_stats [url]

import Text.HTML.TagSoup
import Network.HTTP
import Data.List
import Data.Char
import System.Environment  

openURL x = getResponseBody =<< simpleHTTP (getRequest x)

data Op = Skip | Keep deriving (Eq, Ord, Show, Read, Bounded, Enum)

main = do
  args <- getArgs
  let host = if (length args) == 0 then "http://www.haskell.org/haskellwiki/Haskell" else args !! 0
  putStrLn $ "Processing host: "++host
  tags <- fmap parseTags $ openURL host
  let tags_noscript = dropTag "script" [] tags Keep
      tags_nostyle = dropTag "style" [] tags_noscript Keep
      tags_final = filter isTagText tags_nostyle
      word_list = foldl (\acc tag -> acc ++ (words (fromTagText tag))) [] tags_final
      word_list_lower = map (\x -> map toLower x) word_list
      to_skip = ["a", "an", "the", "on", "in", "for", "and", "to"]
      word_list_filt1 = filter (\w -> not $ elem w to_skip ) word_list_lower
      word_list_filt2 = sort $ filter (\w -> all isAlphaNum w) word_list_filt1
      maxlen = foldl (\acc x -> max acc (length x)) 0 word_list_filt2
      minlen = foldl (\acc x -> min acc (length x)) 1000 word_list_filt2
      result = map getRunLen (group word_list_filt2)
      result_sorted = sortBy (comparingRev snd) result
      result_arr = map (formatResult maxlen) result_sorted
  putStrLn $ "Min wordlen: "++ show minlen ++ ", max wordlen: " ++ show maxlen
  putStrLn "Word occurrences:\n------------------"
  mapM_ putStrLn result_arr

comparingRev p x y = compare (p y) (p x)  

dropTag :: String -> [Tag String] -> [Tag String] -> Op -> [Tag String]
dropTag _ a [] _  = a
dropTag tagStr a (TagOpen currTag _:rest) Keep
  | currTag == tagStr = dropTag tagStr a rest Skip
dropTag tagStr a (TagClose currTag:rest) Skip 
  | currTag == tagStr = dropTag tagStr a rest Keep
dropTag tagStr a (_:rest) Skip = dropTag tagStr a rest Skip
dropTag tagStr a (b:rest) Keep = dropTag tagStr (a++[b]) rest Keep

getRunLen :: [String] -> (String, Int)
getRunLen l@(a:rest) = (a, length l)

formatResult :: Int -> (String, Int) -> String
formatResult maxlen (a,b) = a++(replicate (maxlen - length a) ' ')++": "++ (show b)
