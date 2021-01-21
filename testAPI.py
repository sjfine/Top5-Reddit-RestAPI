#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 20:39:17 2021

@author: Seth
"""
import requests

BASE = "http://127.0.0.1:5000/" #The URL beginning for LocalHost

response = requests.get(BASE + "/reddit/soccer")
print(response.json())