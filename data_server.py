from flask import Flask
from tinydb import TinyDB, Query
from dotenv import load_dotenv

import os

# load environment variables
load_dotenv()

db = TinyDB(os.getenv('DBFILE'))
Sensor = Query()


app = Flask(__name__)


@app.route('/')
def send_index():
    return app.send_static_file('index.html')

@app.route('/data')
def summary():
    return {'temperature':1}

if __name__ == '__main__':  # pragma: no cover
    app.run(port=5050)