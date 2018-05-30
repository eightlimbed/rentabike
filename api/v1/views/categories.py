#!/usr/bin/python3
'''
Flask routes related to Categories.
'''
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage, CNC


@app_views.route('/categories/', methods=['GET', 'POST'])
def categories_no_id(category_id=None):
    '''
    Categories route that handles http requests no ID given
    '''
    if request.method == 'GET':
        all_categories = storage.all('Category')
        all_categories = [obj.to_dict() for obj in all_categories.values()]
        return jsonify(all_categories)
    if request.method == 'POST':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        if req_json.get('name') is None:
            abort(400, 'Missing name')
        Category = CNC.get('Category')
        new_object = Category(**req_json)
        new_object.save()
        return jsonify(new_object.to_json()), 201


@app_views.route('/categories/<category_id>', methods=['GET', 'DELETE', 'PUT'])
def categories_with_id(category_id=None):
    '''
    Categories route that handles http requests with ID given
    '''
    category_obj = storage.get('Category', category_id)
    if category_obj is None:
        abort(404, 'Not found')
    if request.method == 'GET':
        return jsonify(category_obj.to_json())
    if request.method == 'DELETE':
        category_obj.delete()
        del category_obj
        return jsonify({}), 200
    if request.method == 'PUT':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        category_obj.bm_update(req_json)
        return jsonify(category_obj.to_json()), 200
