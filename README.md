# Top5-Reddit-RestAPI

Description: restAPI that returns (as a JSON object) the top 5 reddit article titles given a subreddit. Written in Python utilizing Flask framework.

How it works:

  Creates a Flask resource with a GET command to utilize python's urllib to retrieve the JSON data from the Reddit API. Accesses the children key in this JSON data to then create a list of the article titles for the top 5 articles in a subreddit. Utilizes reddit API 'hot' and 'limit = 5' to achieve this

To run locally: 
  1) From the command line, run RedditRestAPI.py
  2) From a 2nd command line window, run testAPI.py (this sends an example command using the 'news' subreddit header)
 
To run online:
  1) Go to the link: http://sfine.pythonanywhere.com/reddit/
  2) Add to this URL the name of the subreddit header (Ex. http://sfine.pythonanywhere.com/reddit/news) retrieves top article titles from the news subreddit thread.
  
 
