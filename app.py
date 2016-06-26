from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api
from flask_cors import CORS

from api import manager

import logging
import os
import sys


app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(manager.InventoryManager, '/inventory')

if __name__ == '__main__':

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

    app.config['MONGODB_SETTINGS'] = {
        'db': os.environ['DB_NAME'],
        'host': os.environ['DB_HOSTNAME'],
        'port': int(os.environ['DB_PORT']),
        'username': os.environ['DB_USERNAME'],
        'password': os.environ['DB_PASSWORD']
    }

    db = MongoEngine(app)

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

