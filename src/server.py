from flask import Flask, json, jsonify, request
from flask_pymongo import PyMongo

server = Flask(__name__)

mongo = PyMongo(server, uri = 'mongodb://localhost:27017/flask-api')

@server.route('/')
def index():
    return jsonify(
        Hello = 'World',
        Lorem = 'Ipsum'
    )

@server.route('/solar-system', methods = ['GET'])
def get_solar_system():
    # Source: https://raw.githubusercontent.com/duckduckgo/zeroclickinfo-goodies/master/share/goodie/cheat_sheets/json/solar-system.json
    file = open('data/solar-system.json')
    content = json.load(file)
    return jsonify(content)

@server.route('/planet/<name>', methods = ['GET'])
def get_planet(name):
    data = mongo.db.planets.find_one_or_404({ 'name': name })
    return jsonify({ 'name': data['name'] })

@server.route('/planet', methods = ['POST'])
def add_planet():
    name = request.json['name']
    planet_id = mongo.db.planets.insert({ 'name': name })
    new_planet = mongo.db.planets.find_one({ '_id': planet_id })
    return jsonify({ 'name' : new_planet['name'] })

@server.route('/planet/<name>', methods = ['PUT'])
def update_planet(name):
    new_name = request.json['name']
    planet_id = mongo.db.planets.update({ 'name': name }, { 'name': new_name })
    updated_planet = mongo.db.planets.find_one({ 'name': new_name })
    return jsonify({ 'name' : updated_planet['name'] })

if __name__ == '__main__':
    server.run(host = '0.0.0.0', debug = True)
    # server.run(host = '0.0.0.0')
