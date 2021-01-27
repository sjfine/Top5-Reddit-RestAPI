#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 02:48:02 2021

@author: Seth Fine
"""
import os
import tempfile
import pytest
from flaskr import flaskr
from flask import request, jsonify

@pytest.fixture
def client():
    db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    flaskr.app.config['TESTING'] = True

    with flaskr.app.test_client() as client:
        with flaskr.app.app_context():
            flaskr.init_db()
        yield client

    os.close(db_fd)
    os.unlink(flaskr.app.config['DATABASE'])


@app.route('/RedditRestAPI')
def auth():
    json_data = request.get_json()
    description = json_data['description']
    titles = json_data['title']
    authors = json_data['authors']
    return jsonify(token = generate_token(description, titles, authors))

with app.test_client() as c:
    rv = c.post('/RedditRestAPI', json={'description': "", 'titles': "", 'authors' : ""})
    json_data = rv.get_json()
    assert verify_token(titles, json_data['token'])
