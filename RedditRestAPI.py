#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 20:31:54 2021

@author: Seth Fine
"""

from flask import Flask
from flask_restful import Api, Resource
import json
import urllib.request

app = Flask(__name__)
api = Api(app)


class Reddit(Resource):
    def get(self, subReddit):
        url = "http://www.reddit.com/r/" + subReddit + "/hot/.json?limit=5"
        try:
            response = urllib.request.urlopen(url).read().decode()
            data = json.loads(response)
            #The returned JSON object is simplified from what we recieve from Reddit to the subreddit description
            # and the titles of the top 5 articles and their authors
            #top 5 titles in the SubReddit
            description = data["data"]["children"][0]["data"]["selftext"]
            first_line = description.split('\n')[0]
            
            authors = []
            a = data["data"]["children"]
            for b in a:
                authors.append(b["data"]["author_fullname"])
            
            titles = []
            for child in a:
                titles.append(child["data"]["title"])
            
            return json.dumps({"Description": first_line, "titles": titles, "authors" : authors})
        
        except:
            return("Invalid subreddit title or title formatting")
        
    
    
api.add_resource(Reddit, "/reddit/<string:subReddit>")


if __name__ == "__main__":
    app.run(debug = False)

