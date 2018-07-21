from flask import Flask
from flask import jsonify

server = Flask(__name__)

@server.route("/")
def index():
    return jsonify(
        Hello="World",
        Lorem="Ipsum"
    )

if __name__ == '__main__':
    #server.run(host='0.0.0.0', debug=True)
    server.run(host='0.0.0.0')
