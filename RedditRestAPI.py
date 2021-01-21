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
            #The returned JSON object is simplified from what we recieve from Reddit to just the titles of the
            #top 5 titles in the SubReddit
            titles = []
            c = data["data"]["children"]
            for child in c:
                titles.append(child["data"]["title"])
            
            return json.dumps({"titles": titles})
        
        except:
            return("Invalid subreddit title or title formatting")
        
    
    
api.add_resource(Reddit, "/reddit/<string:subReddit>")


if __name__ == "__main__":
    app.run(debug = False)

