import bottle
import pymongo

@bottle.route('/')
def index():
  from pymongo import MongoClient
  connection = MongoClient("mongodb://192.168.99.100")
  db = connection.test

  names = db.names

  item = names.find_one()

  return '<b>Hello %s!</b>' %item['name']


bottle.debug(True)
bottle.run(host='localhost', port = 8082)