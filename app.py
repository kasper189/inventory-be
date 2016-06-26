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
        'db': 'inventory',
        'host': 'ds019654.mlab.com',
        'port': 19654,
        'username': 'invadmin',
        'password': '>U[d63RYrc}IDAu'
    }

    db = MongoEngine(app)

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

