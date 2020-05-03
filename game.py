import sys
import random
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_simple_geoip import SimpleGeoIP
import json
from flask import request


import threading

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_test.db'

db = SQLAlchemy(app)



BASECOORDS = [48, 11]


class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    player_name = db.Column(db.String)
    marked = db.Column(db.String)



    def __init__(self, id, name, lat, lng):
        self.id = id
        self.player_name = name
        self.lat = lat
        self.lon = lng
        self.marked = "no"


    def __repr__(self):

        return '{"id" : self.id , "player_name": self.player_name, "lat": self.lat, "lon":self.lon, "marked":self.marked}'
        #return "<Point %d: Lat %s Lng %s Mared %s>" % (self.id, self.latitude, self.longitude, self.marked)

    @property
    def latitude(self):
        return self.lat
    @property
    def longitude(self):
        return self.lon


@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
        """return the information for <user_id>"""
        return json.loads(user_id)[0]

    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        # you can use <user_id>, which is a str but could
        # changed to be int or whatever you want, along
        # with your lxml knowledge to make the required
        # changes
        data = request.form # a multidict containing POST data

    if request.method == 'DELETE':
        """delete user with ID <user_id>"""


        





@app.route('/')
def index():

    return render_template('index.html')

@app.route('/points')
def points():
    points = Point.query.all()
    coords = [[point.latitude, point.longitude] for point in points]
    return jsonify({"data": coords})


def make_player(db):

    pid = random.randint(0,100)
    lat = 48 + random.random()
    lng = 11 +random.random()
    row = Point(pid, "harry", lat, lng)
    db.session.add(row)
    db.session.commit()







if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'mkdb':
            db.create_all()
            make_player(db)
    else:
        app.run(debug=True)
