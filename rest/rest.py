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


@bottle.route('/teste')
def home_page():
  mythings = ['apple', 'orange', 'banana', 'peach']
  return bottle.template('hello_world', {'username':'Jessica', 'things':mythings})

@bottle.route('/teste2')
def home_page():
  mythings = ['apple', 'orange', 'banana', 'peach']
  return bottle.template('hello_world2', {'username':'Jessica','things':mythings})

@bottle.post('/favorite_fruit')
def favorite_fruit():
  fruit = bottle.request.forms.get('fruit')
  if fruit == None or fruit == '':
    fruit = 'No Fruit Selected'
  return bottle.template('fruit_selection', {'fruit':fruit})


bottle.debug(True)
bottle.run(host='localhost', port = 8082)
