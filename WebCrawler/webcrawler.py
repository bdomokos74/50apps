# webcrawler.py
# Usage: python webcrawler.py <seed url> <depth> <search word> 
# e.g.: python webcrawler.py http://www.hackernews.com 5 Python > hackernews.crawl.out
# It will display progress and status to stderr, the result is written to stdout.

import httplib
from HTMLParser import HTMLParser
from sets import Set
import sys
import re
import socket

def is_invalid_protocol(link):
	return link.startswith("https://") or link.startswith("mailto:") or link.startswith("webcal://") or link.startswith("#")

class LinkParser(HTMLParser):
	"""Html parser class"""
	def __init__(self, url):
		HTMLParser.__init__(self)
		self.ina_flag = 0
		self.url = url
		# only keep the server part, this will be used as a prefix for relative urls
		index = url.find("/",7)
		if index != -1:
			self.url = url[:(index+1)]
		self.links = Set()
		
	def handle_starttag(self, tag, attrs):
		if tag=="a":
			for a in attrs:
				if a[0]=="href":
					link = self.preprocess_link(a[1])
					if len(link) > 0:
						self.links.add(link)
						
	def preprocess_link(self, link):
		result = link
		if len(link) == 0:
			return ""
		if is_invalid_protocol(link):
			return ""
		if not link.startswith("http://"):
			if link[0] != '/' and self.url[-1] != '/':
				result = self.url+"/"+link
			elif link[0] == '/' and self.url[-1] == '/':
				result = self.url[:-1]+link
			else:
				result = self.url+link
		return result
		
	def get_links(self):
		return self.links

class Crawler:
	@staticmethod
	def split_url(url):
		index = url.find("/",7)
		if index == -1:
			return url, "/"
		server = url[:index]
		path = url[index:]
		if len(path) == 0:
			path = "/"
		return server, path

	@staticmethod
	def get_html(curr, follow_redirect=2):
		(server, path) = Crawler.split_url(curr)
		timeout = 0
		if server.startswith("http://"):
			server = server[7:]
		try:
			conn = httplib.HTTPConnection(server, timeout=5)
			conn.request("HEAD", path)
			result = conn.getresponse()
		except (httplib.HTTPResponse, socket.error) as ex:
			timeout = 1
		if timeout:
			return 0, "", timeout, ""
		text = ""
		status = result.status
		ctype = ""
		if status == 200:
			ctype = result.getheader("Content-Type")
			if (ctype is None) or (not ctype.startswith("text/html")):
				return result.status, ctype, timeout, ""
			try:
				conn = httplib.HTTPConnection(server, timeout=5)
				conn.request("GET", path)
				result = conn.getresponse()
				text=result.read()
			except (httplib.HTTPResponse, socket.error) as ex:
				timeout = 1
				text = ""
		elif follow_redirect>0 and ( status == 301 or status == 302):
			if is_invalid_protocol(result.getheader("Location")):
				text = ""
			else:
				(status, ctype, timeout, text) = Crawler.get_html(result.getheader("Location"), follow_redirect-1)
		return status, ctype, timeout, text
	
	# to remove CDATA parts, which makes the html parser fail
	@staticmethod
	def fix_html(str):
		result = str.replace('\n', '')
		result = re.sub(r'<!\[CDATA\[//>.*?<!\]\]>', r'', result)
		return result

	def crawl(self, curr, depth, maxdepth, target, done):
		curr = re.sub(r'#.*', r'', curr)
		if curr in done:
			return
		done.add(curr)
		(status,ctype, timeout, html) = Crawler.get_html(curr)
		prefix = "OK"
		if status != 200 or (not ctype.startswith("text/html")) or len(html) == 0:
			prefix = "SKIP"
		if timeout:
			prefix = "TIMEOUT"
		sys.stderr.write("{} {} {} - {} {} ({})\n".format("\t"*(maxdepth-depth), prefix, curr, str(status), ctype, str(depth) ))
		if status != 200 or len(html) == 0 or (not ctype.startswith("text/html")):
			return
		if target.lower() in html.lower():
			print curr
			sys.stdout.flush()
		if depth > 0:
			parser = LinkParser(curr)
			parser.feed(Crawler.fix_html(html))
			links = parser.get_links()
			for l in links:
				self.crawl(l, depth-1, maxdepth, target, done)	

if len(sys.argv) < 4:
	exit("Usage: python webcrawler.py <seed url> <depth> <search string>")
seed = sys.argv[1]
depth = sys.argv[2]
target = sys.argv[3]
if not seed.startswith("http://"):
	exit("Wrong url format, should start with http://...")
depth = int(depth)

sys.stderr.write( "Crawling: "+seed+"\nSearching: "+target+"\n")

done = Set()
Crawler().crawl(seed, depth, depth, target, done)
