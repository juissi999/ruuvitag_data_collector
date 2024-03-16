import os

from ruuvitag_sensor.ruuvi import RuuviTagSensor
from tinydb import TinyDB, Query
from dotenv import load_dotenv

# load environment variables
load_dotenv()

db = TinyDB(os.getenv('DBFILE'))
Sensor = Query()

def handle_data(found_data):
  print('MAC ' + found_data[0])
  print(found_data[1])
  db.upsert({'MAC': found_data[0], 'data': found_data[1]}, Sensor.MAC == found_data[0])

if __name__ == '__main__':
  RuuviTagSensor.get_data(handle_data)
