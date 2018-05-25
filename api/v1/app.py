#!/usr/bin/python3
'''
Flask RESTful API App that integrates with web static content.
'''
from api.v1.views import app_views
from flask import Flask, jsonify, make_response, render_template, url_for
from flask_cors import CORS, cross_origin
from models import storage
import os

app = Flask(__name__)
app.url_map.strict_slashes = False
host = os.getenv('RENTABIKE_API_HOST', '0.0.0.0')
port = os.getenv('RENTABIKE_API_PORT', 5001)

# Cross-Origin Resource Sharing
cors = CORS(app, resources={r'/api/v1/*': {'origins': '*'}})

# app_views BluePrint defined in api.v1.views
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    '''
    After each request, this method closes the current SQLAlchemy Session.
    '''
    storage.close()


@app.errorhandler(404)
def handle_404(exception):
    '''
    Handles 404 errors in the event that global error handler fails.
    '''
    code = exception.__str__().split()[0]
    description = exception.description
    message = {'error': description}
    return make_response(jsonify(message), code)


if __name__ == '__main__':
    '''
    RESTful API entry point
    '''
    app.run(host=host, port=port)
