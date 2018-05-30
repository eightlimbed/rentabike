#!/usr/bin/python3
'''
Flask routes related to Bikes and Categories.
'''
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from os import environ


STORAGE_TYPE = environ.get('RENTABIKE_TYPE_STORAGE')


@app_views.route('/bikes/<bike_id>/categories', methods=['GET'])
def categories_per_bike(bike_id=None):
    '''
    Bike route to handle http method for requested categories of a Bike
    instance.
    '''
    bike_obj = storage.get('Place', bike_id)
    if request.method == 'GET':
        if bike_obj is None:
            abort(404, 'Not found')
        all_categories = storage.all('Category')
        if STORAGE_TYPE == 'db':
            bike_categories = bike_obj.categories
        else:
            bike_amen_ids = bike_obj.categories
            bike_categories = []
            for amen in bike_amen_ids:
                response.append(storage.get('Category', amen))
        bike_categories = [
            obj.to_dict() for obj in bike_categories
            ]
        return jsonify(bike_categories)


@app_views.route('/bikes/<bike_id>/categories/<category_id>',
                 methods=['DELETE', 'POST'])
def category_to_bike(bike_id=None, category_id=None):
    '''
    Bike route to handle http methods for given category and bike by id.
    '''
    bike_obj = storage.get('Place', bike_id)
    category_obj = storage.get('Category', category_id)
    if bike_obj is None:
        abort(404, 'Not found')
    if category_obj is None:
        abort(404, 'Not found')
    if request.method == 'DELETE':
        if (category_obj not in bike_obj.categories and
                category_obj.id not in bike_obj.categories):
            abort(404, 'Not found')
        if STORAGE_TYPE == 'db':
            bike_obj.categories.remove(category_obj)
        else:
            bike_obj.category_ids.pop(category_obj.id, None)
        bike_obj.save()
        return jsonify({}), 200
    if request.method == 'POST':
        if (category_obj in bike_obj.categories or
                category_obj.id in bike_obj.categories):
            return jsonify(category_obj.to_json()), 200
        if STORAGE_TYPE == 'db':
            bike_obj.categories.append(category_obj)
        else:
            bike_obj.categories = category_obj
        return jsonify(category_obj.to_json()), 201
