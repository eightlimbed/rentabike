#!/usr/bin/python3
'''
Flask route that returns json status response
'''
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage, CNC
from os import environ


STORAGE_TYPE = environ.get('RENTABIKE_TYPE_STORAGE')


@app_views.route('/cities/<city_id>/bikes', methods=['GET', 'POST'])
def bikes_per_city(city_id=None):
    '''
    Bikes route to handle http method for requested bikes by city
    '''
    city_obj = storage.get('City', city_id)
    if city_obj is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        all_bikes = storage.all('Bike')
        city_bikes = [obj.to_dict() for obj in all_bikes.values()
                       if obj.city_id == city_id]
        return jsonify(city_bikes)

    if request.method == 'POST':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        user_id = req_json.get('user_id')
        if user_id is None:
            abort(400, 'Missing user_id')
        user_obj = storage.get('User', user_id)
        if user_obj is None:
            abort(404, 'Not found')
        if req_json.get('name') is None:
            abort(400, 'Missing name')
        Bike = CNC.get('Bike')
        req_json['city_id'] = city_id
        new_object = Bike(**req_json)
        new_object.save()
        return jsonify(new_object.to_json()), 201


@app_views.route('/bikes/<bike_id>', methods=['GET', 'DELETE', 'PUT'])
def bikes_with_id(bike_id=None):
    '''
    Bikes route to handle http methods for given bike.
    '''
    bike_obj = storage.get('Bike', bike_id)
    if bike_obj is None:
        abort(404, 'Not found')
    if request.method == 'GET':
        return jsonify(bike_obj.to_json())
    if request.method == 'DELETE':
        bike_obj.delete()
        del bike_obj
        return jsonify({}), 200
    if request.method == 'PUT':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        bike_obj.bm_update(req_json)
        return jsonify(bike_obj.to_json()), 200


@app_views.route('/bikes_by_categories/<ids>', methods=['POST'])
def bikes_by_categories(ids=None):
    '''
    Bikes route to handle POST request for bikes by amenity ids
    '''
    result = []
    all_ids = ids.split(',')
    all_bikes = [b for b in storage.all('Bike').values()]
    for bike in all_bikes:
        count = 0
        for c_id in all_ids:
            c_ids = [cat.id for cat in bike.categories]
            if c_id in c_ids:
                count += 1
        if count == len(all_ids):
            result.append(bike)
    return jsonify([bike.to_json() for bike in result])

@app_views.route('/bikes_by_categories', methods=['POST'])
def bikes_by_categories_empty():
    '''
    Bikes route to handle POST request for all bikes. handles the
    case for when a user clicks on 'search' without selecting any
    categories. Just returns all bikes.
    '''
    all_bikes = [b for b in storage.all('Bike').values()]
    return jsonify([b.to_json() for b in all_bikes])

@app_views.route('/bikes_search', methods=['POST'])
def bikes_search():
    '''
    Bikes route to handle http method for request to search bikes.
    '''
    all_bikes = [p for p in storage.all('Bike').values()]
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    states = req_json.get('states')
    if states and len(states) > 0:
        all_cities = storage.all('City')
        state_cities = set([city.id for city in all_cities.values()
                            if city.state_id in states])
    else:
        state_cities = set()
    cities = req_json.get('cities')
    if cities and len(cities) > 0:
        cities = set([
            c_id for c_id in cities if storage.get('City', c_id)])
        state_cities = state_cities.union(cities)
    categories = req_json.get('categories')
    if len(state_cities) > 0:
        all_bikes = [b for b in all_bikes if b.city_id in state_cities]
    elif categories is None or len(categories) == 0:
        result = [bike.to_json() for bike in all_bikes]
        return jsonify(result)
    bikes_categories = []
    if categories and len(categories) > 0:
        categories = set([
            c_id for c_id in categories if storage.get('Category', c_id)])
        for b in all_bikes:
            b_categories = None
            if STORAGE_TYPE == 'db' and b.categories:
                b_categories = [c.id for c in b.categories]
            elif len(b.categories) > 0:
                b_categories = b.categories
            if b_categories and all([c in b_categories for c in categories]):
                bikes_categories.append(p)
    else:
        bikes_categories = all_bikes
    result = [bike.to_dict() for bike in bikes_categories]
    return jsonify(result)
