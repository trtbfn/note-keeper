from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

import api


if __name__ == '__main__':
  app.debug = True
  app.run()
