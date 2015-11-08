
## 50 Apps in 50 Weeks Challenge
It was on 50apps.org, these were the problems:

### Week 1 details (16-22 Jan 2012)

Language: Python

Problem Statement:

App Category: Networking 

DB: None 

Simple part: 

Create a web crawler app in python which, given a url seed, can crawl through all links on the page and scan deep for a given level of depth. While crawling the app should be able to return the url page containing a specific search text.

Input: 
1 - Url seed e.g. www.hackernews.com 
2 - Depth e.g. 5 (this means go into links on a page till 5 levels) 
3 - search text e.g. "python" 

Output: 
the list of url that contains the specified text The Simple part is mandatory to be completed. If you finish the simple part and are eager to take up something challenging, then here's a little complex angle to the problem:

Complex part: (Optional, if you complete simple part and want to take up something more challenging) 

Write rules around the app for searching. 
Rule 1: The return Url should contain a specific substring 
Rule 2: Highlight in output if the url is amongst a long list of blacklisted urls (about 10000 blacklisted urls) 
Rule 3: Search for multiple search strings and rank Urls as per the number of different search strings found and occurances of each search string in the page 
Rule 4: Rank as per level of the Url w.r.t. seed url 

### Week 2 details (23-29 Jan 2012)

Language: Python

Problem Statement: 

App Category: Networking/Web Application 

DB: None (Use any DB for complex part)

Simple part: 

Develop a web application using Python. You can use any Web framework if you want to. The website should use the web crawler application you created in Week 1, as a backend tool. The site will have a home page that will ask the user for a URL seed, depth of crawling and a search string. On click of Search button, it should show the results in a tabular form. The results should show the URL's whose page content contains search string and also the depth at which the URL is found. Preferably host this site in google app engine. It's free and supports Python. If you have difficulties hosting it, you can submit only the code.

Complex part: (Optional, if you complete simple part and want to take up something more challenging) 

-> Show results using a bar graph on the web site. The graph should show the number of occurances of the search string on a particular URL. 
-> Since crawling may take time to fully execute, keep showing results as and when they are found by crawler (asynchonously).
-> User should be able to click on Url link from search results to go to that page.
-> Show time spent to get results.
-> Store input and results in DB and show Search History in a different page.


### Week 3 details (30 Jan - 5 Feb 2012)

Language: Python

Problem Statement: 

App Category: Text Parsing and 2D Graphics 

DB: None (Use any DB for complex part)

Simple part: 

- Use the Python website that you created in week 2 assignment. 
- Accept a url as input
- Read page content of the url 
- Split the content into words and find out the number of occurences of every word in the page.
- Do not consider the following words: a, an, the, on, in, for, and, to
- Show a simple bar graph on the ui showing the top 10 words with respective count (X axis - words, Y axis - height of the bar as per count of word in page) (Do this using HTML5. Add whatever transitions or effects if you want to beautify it)
- Also find out the longest and the shortest word in the page and mention in UI. (Longest and shortest - as per number of characters in a word)
ONE BIG CONDITION - YOU CANNOT USE ANY LOOPING CONSTRUCTS LIKE FOR AND WHILE. (Hint: use map and lambda expressions)
Try to use map, filter, reduce functionality of Python. Explore use of lambda, pure functions, generators, etc.

Complex part 1: (Optional, if you complete simple part and want to take up something more challenging) 

- Store word counts of the url in database, e.g. in sqlite3
- If the user enters more such urls consecutively, do same processing and store word counts per site in the db
- There will be a search textbox in UI. The user can enter a word in the text box and click "Search Url" button
- On click of "Search Url", show the urls from db in order as per the number of occurences of that word in that url
Yet more.. Complex part 2:
Demonstrate how MapReduce framework can be used for the above example in a distributed environment


### Week 4 details (6-12 Feb 2012)

Language: HTML5

Problem Statement: 

App Category: Graphics and Storage using rich clients

DB: (Use of in-built storage facility in HTML5)

Simple part: 

- Create a sticky notes application using HTML5 
- User should be able to create a blank sticky note and add text into it. The sticky notes look like small colored rectangles holding user defined text 
- User can create multiple such sticky's and all of them appear in the same browser page 
- User can drag sticky's around in the browser page and place them wherever convenient 
- All these data are saved on the client side as and when the user types in. (For details of how you can save data using HTML5, please see http://www.html5rocks.com/en/features/storage) 

Complex part 1: (Optional, if you complete simple part and want to take up something more challenging) 

- Allow user to select one of 4 predefined background colors for sticky to depict its priority/importance 
- Show gradient coloring for sticky's background 
- Ability to delete sticky 
- Add current time to sticky header 

### Week 5 details (13-19 Feb 2012)

Language: HTML5

Problem Statement: 

App Category: WebSocket Communication, Offline Application Cache, Animation, Multimedia

DB: None

Simple part: 

- Use last week's assignment of Sticky notes and create a Collaborative sticky notes app 
- Multiple browser instances of the application will show the same sticky notes. Changes in one instance reflects the change in all other browser instances. Make use of WebSocket to achieve this. 
- For instance let's say user1 and user2 access the sticky notes website. User1 creates a sticky note. The user2 can instantly see it in her browser (without doing anything like refreshing the page). 
    Now if user2 enters any text into the sticky, user1 can see it immidiately, and vice versa.
- If user closes the browser, disconnects internet and open the browser again at a later point of time, she can view the last updated sticky notes and work with it. (Use AppCache to achieve this) 

Complex part 1: (Optional, if you complete simple part and want to take up something more challenging) 

- The user can set time based reminder in sticky notes. When the time is reached, the sticky note vibrates and creates an alarm noise. A stop button stops the sound and vibration. A snooze button makes the alarm ring again after 10 minutes. 
- Show animation when notes are created and deleted. Effect of scaling up from zero height and width to regular sticky size on creation of a sticky and fading away when a sticky is deleted. 

### Week 6 details (20-26 Feb 2012)

Language: HTML5

Problem Statement: 

App Category: Games, Animation, Multimedia

DB: None

Simple part: 

- create a simple Snakes game using HTML5 
- the game starts when the user presses the space bar. A snake (string of attached squares) keeps moving in a big enough rectangular region in straight direction
- using the arrow keys the user can change the direction of the snake, left or right
- the challenge for the user is to not touch the boundary of the rectangular region
- if the user touches the rectangle, the game ends
- to know what a snake game is, please refer to http://www.snakegame.net/neavesnake.htm
- add music at the background and sound effects when the snake touches the rectangular region

Complex part 1: (Optional, if you complete simple part and want to take up something more challenging) 

- place food (single squares) randomly in the rectangular region
- if the snake passes through the food, add one square extra to the lenght of the snake

### Week 7 details (27 Feb - 4 Mar 2012)

Language: Scala

Problem Statement: 

App Category: Social Networking

DB: None

Simple part: 

- create a simple chat room application using scala 
- the chat room is a web app that allows multiple users to chat with each other in a conference 
- multiple users can join the chat room by providing a username. No authentication is done. The username is only required to identify the chat msg sender 
- all messages posted by a user is visible to all other users 
- Use Scala specific features to build the chat server. Use Actor class to receive messages. Explore how these are different from threads in conventional languages. Use Akka framework to create Actors. 

Complex part 1: (Optional, if you complete simple part and want to take up something more challenging) 

- Lets us start doing TDD from here on. Since it may be a relatively new concept to many, it is added as an optional portion 
- Use testing frameworks like ScalaTest to write test first for the application and then evolve the app code based on the test written 

For more detail on ScalaTest-> http://www.scalatest.org/ 

### Week 8 details (5-11 Mar 2012)

Language: Scala

Problem Statement: 

App Category: Social Networking

DB: Any (Use MongoDB in complex part)

Simple part: 

- use the chat room application created in Week 7 
- lets consider this is a char room used by a software development team to monitor project progress 
- a user posting chat message can have one of the following roles: Program Manager, Project Lead, Application Developer, Business Analyst, QA 
- Program Manager is a senior member and a non technical person 
- Project Lead is a senior member and a technical person 
- Business Analyst is a junior member and a non technical person 
- Application Developer and QA are junior members and technical persons 
- The chat server should store every chat in database. Use any db of your choice. 
- before saving the chat message the server does some post processing on the message. it should prefix the chat message by [user role] 
e.g. [Business Analysis] Mark : We need to estimate the work items for this release 
- a chat message should be post fixed by [T] if the user is a technical person 
e.g. [Application Developer] Jill: We need to upgrade Oracle drivers on all servers [T] 
- One condition. Instead of using conditional statements, try to do the post processing of messages polymorphically by using Traits 

Complex part 1: (Optional, if you complete simple part and want to take up something more challenging) 

- Use Mongo DB to store chat messages in the db. 
- Casbah is a Scala toolkit for MongoDB (http://api.mongodb.org/scala/casbah/2.0/) 

### Week 9 details (12-18 Mar 2012)

Language: Scala

Problem Statement: 

App Category: Social Networking

DB: Any

Simple part: 

- use the chat room application created in Week 7 and 8 
- any word in chat message prefixed by # is considered a key word 
- when a user clicks on "Analyize trends" button in UI, show the sorted list of most used keywords along with count of each keyword occurrence in all chat messages 
- use pattern matching feature of Scala to find the trend 

Complex part 1: (Optional, if you complete simple part and want to take up something more challenging) 

- show graph on UI for the trend 

### Week 10 details (19-25 Mar 2012)

Language: Javascript

Problem Statement: 

App Category: Financial

DB: None (Any for Complex part if needed)

Simple part: 

- create a Stock market trading site which shows real time stock quotes of listed companies 
- using any backend server technology (python, scala, etc.) create a service that keeps list of 20 dummy company stock values. Randomly keep changing the values as if these are current stock values 
- when the user opens the website, she can see all these stock values changing without refreshing the page. The application should be a one page app which shows updated values of stocks dynamically without navigating to any other page or refreshing current page 
- use javascript on client side. Use Ajax request to query the server for latest stock quotes 

Complex part 1: (Optional, if you complete simple part and want to take up something more challenging) 

- show HTML5 graph on UI to show stock trends 
- calculate % increase/decrease of stock values w.r.t the value at close of last trading day 

### Week 11 details (26 Mar - 1 Apr 2012)

Language: Javascript

Problem Statement: 

App Category: Office tools

DB: None (Local Storage in Complex part)

Simple part: 

- make a Pomodoro app. It's a time management method used by many. To know more about pomodoro please see http://www.pomodorotechnique.com 
- on the browser UI, there will be a back counter timer starting with 25min 
- the user can click on the timer to start counting backwards. On reaching time zero, an blinking message should come up. When the user responds to the message, the timer resets to 25 min 
- there will be a TO DO list sheet (like paper sheet) on the browser. The user can write activities and mark them for completion after every pomodoro 
- there will be another "Activity Inventory sheet" which will contain the total list of tasks to be completed. The user can edit this sheet 

Complex part 1: (Optional, if you complete simple part and want to take up something more challenging) 

- Ring music when the pomodoro reaches zero 
- show pomodoro timer graphically as suitable (using HTML5) 
- all the data is stored in local storage. When the user relaunches the page later, the earlier data is available. No back end server exists 

### Week 12 details (2-8 Apr 2012)

Language: Node.js (Javascript)

Problem Statement: 

App Category: Utility tools

DB: None 

Simple part: 

- make a website to upload image files 
- on upload the image should be displayed on the page 

Complex part 1: (Optional, if you complete simple part and want to take up something more challenging) 

- show other details about the image file like size, date created and camera used. You can get these info from the image file properties 

### Week 13 details (9-15 Apr 2012)

Language: Node.js (Javascript)

Problem Statement: 

App Category: Utility tools

DB: MySQL 

Simple part: 

- use the image file uploader app created in week 12, to create a photo album site 
- show a "Add New Album" button in home page. On click of that take user to a new album page 
- in new album page, the user can enter the name of the album in a textbox and click on "Upload files" button 
- on clicking of "Upload files" button, the Open file dialog comes up. The user can select multiple jpg files from hard disk 
- the selected files get uploaded to site and all photos are shown as small thumbnails in the album page 
- store all the info related to the album using MySQL db in the backend 

Complex part: (Optional, if you complete simple part and want to take up something more challenging) 

- the user can create multiple such albums and browser through each album's individual page 
- on clicking of the thumbnail, show the picture in a bigger size either in a new page or in an overlay 
- use HTML5 to do any styling\effects in the album

### Week 14 details (16-22 Apr 2012)

Language: Node.js on server and JavaScript on client side

Problem Statement: 

App Category: Utility tools

DB: MySQL 

Simple part: 

- recreate UI of photo album site of week 13, using knockout.js (see knockoutjs.com for details) 
- use databinding support of Knockout js to show photo description on the UI 
- use an MVVM pattern to create the UI using KO 
- also give facility for users to comment anonymously on the photos. When a comment is added on the UI, update the model automatically using databinding feature of knockout and propagate the data back to server to store in db

Complex part: (Optional, if you complete simple part and want to take up something more challenging) 

- give option to "Like" a photo. Implement the feature using databinding 

### Week 15 details (23-29 Apr 2012) and Week 16 details (30 Apr - 6 Apr 2012)

Language: Haskell

Problem Statement: 

App Category: Text Parsing

DB: None 

Simple part: 

- Create a Haskell module that takes a url as input 
- Read page content of the url 
- Split the content into words and find out the number of occurrences of every word in the page 
- Do not consider the following words: a, an, the, on, in, for, and, to 
- Also find out the longest and the shortest word in the page. (Longest and shortest - as per number of characters in a word) 
Try to use map, filter, foldr functions of Haskell. 

Complex part: (Optional, if you complete simple part and want to take up something more challenging) 

- implement the above solution in distributed environment using MapReduce framework (see http://holumbus.fh-wedel.de/src/doc/thesis-mapreduce.pdf) 


