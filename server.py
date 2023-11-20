from flask import Flask
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin

server_app = Flask(__name__, static_folder='colour-palette-frontend/build', static_url_path='')
cors = CORS(server_app)

@server_app.route('/test', methods=['GET'])
@cross_origin()
def index():
    return{
        "test": "Flask test"
    }

@server_app.route('/')
def serve():
    return send_from_directory(server_app.static_folder, 'index.html')

if __name__ == '__main__':
    server_app.run()