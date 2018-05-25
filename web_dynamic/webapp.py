#!/usr/bin/python3
'''
Flask Application that integrates with the HTML/Jinja template in web_static.
'''
from flask import Flask, render_template, url_for
from models import storage


# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


@app.teardown_appcontext
def teardown_db(exception):
    '''
    After each request, this method closes the current SQLAlchemy Session
    '''
    storage.close()


@app.route('/rentabike')
def category_filters(the_id=None):
    '''
    Handles request to custom template with states, cities & categories
    '''
    cities = storage.all('City').values()
    cats = storage.all('Category').values()
    bikes = storage.all('Bike').values()
    users = dict([user.id, '{} {}'.format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    return render_template('index.html',
                           cities=cities,
                           cats=cats,
                           bikes=bikes,
                           users=users)

if __name__ == '__main__':
    '''
    Application entry point.
    '''
    app.run(host=host, port=port)
