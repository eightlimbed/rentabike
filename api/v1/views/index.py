#!/usr/bin/python3
'''
Main Flask routes.
'''
from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    '''
    Returns the status of the API.
    '''
    if request.method == 'GET':
        resp = {'status': 'OK'}
        return jsonify(resp)


@app_views.route('/stats', methods=['GET'])
def stats():
    '''
    Returns the count of all objects in storage.
    '''
    if request.method == 'GET':
        response = {}
        PLURALS = {
            'Category': 'categories',
            'City': 'cities',
            'Bike': 'bikes',
            'Review': 'reviews',
            'State': 'states',
            'User': 'users'
        }
        for key, value in PLURALS.items():
            response[value] = storage.count(key)
        return jsonify(response)
