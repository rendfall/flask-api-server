from flask import Flask, json, jsonify

server = Flask(__name__)

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

if __name__ == '__main__':
    server.run(host = '0.0.0.0', debug = True)
    # server.run(host = '0.0.0.0')
