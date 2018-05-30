#!/usr/bin/python3
'''
Flask route that returns json status response
'''
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage


@app_views.route('/bikes/<bike_id>/reviews', methods=['GET', 'POST'])
def reviews_per_bike(bike_id=None):
    '''
    Reviews route to handle http method for requested reviews by bike id.
    '''
    bike_obj = storage.get('Bike', bike_id)
    if request.method == 'GET':
        if bike_obj is None:
            abort(404, 'Not found')
        all_reviews = storage.all('Review')
        bike_reviews = [obj.to_dict() for obj in all_reviews.values()
                         if obj.bike_id == bike_id]
        return jsonify(bike_reviews)
    if request.method == 'POST':
        if bike_obj is None:
            abort(404, 'Not found')
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        user_id = req_json.get('user_id')
        if user_id is None:
            abort(400, 'Missing user_id')
        user_obj = storage.get('User', user_id)
        if user_obj is None:
            abort(404, 'Not found')
        if req_json.get('text') is None:
            abort(400, 'Missing text')
        Review = models.classes.get('Review')
        req_json['bike_id'] = bike_id
        new_object = Review(**req_json)
        new_object.save()
        return jsonify(new_object.to_json()), 201


@app_views.route('/reviews/<review_id>', methods=['GET', 'DELETE', 'PUT'])
def reviews_with_id(review_id=None):
    '''
    Reviews route to handle http methods for given review by ID
    '''
    review_obj = storage.get('Review', review_id)
    if request.method == 'GET':
        if review_obj is None:
            abort(404, 'Not found')
        return jsonify(review_obj.to_json())
    if request.method == 'DELETE':
        if review_obj is None:
            abort(404, 'Not found')
        review_obj.delete()
        del review_obj
        return jsonify({}), 200
    if request.method == 'PUT':
        if review_obj is None:
            abort(404, 'Not found')
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        review_obj.bm_update(req_json)
        return jsonify(review_obj.to_json()), 200
