import getRestData
import hashlib
from RESTObject import RESTObject as ro

print('Tests Starting')

'''
restObj = {}
config = {}

restObj['operation'] = 'get'
restObj['endpoint'] = 'https://api.scryfall.com/cards/named'
restObj['params'] = {'exact':'Overgrown Tomb'}
restObj['headers'] = {}
restObj['payload'] = {}

config['output'] = hashlib.md5('Overgrown Tomb'.encode()).hexdigest() + '.json'
config['cache'] = 'cache/cards'
config['time'] = 21600
config['sleep'] = 200
config['rest'] = restObj

print(config)
'''
#print(getRestData.execute(config))

#test min
def test1():
	restObj = {}
	config = {}
	restObj['operation'] = 'get'
	restObj['endpoint'] = 'https://api.scryfall.com/cards/named'
	restObj['params'] = {'exact':'Overgrown Tomb'}
	restObj['headers'] = {}
	restObj['payload'] = {}
	config['rest'] = restObj
	print(getRestData.execute(config))
#test1()
#test false
def test2():
	#restObj = {}
	config = {}
	#restObj['operation'] = 'get'
	#restObj['endpoint'] = 'https://api.scryfall.com/cards/named'
	#restObj['params'] = {'exact':'Overgrown Tomb'}
	#restObj['headers'] = {}
	#restObj['payload'] = {}
	restObj = ro(operation='get', endpoint='https://api.scryfall.com/cards/named',params={'exact':'Sacred Foundry'},headers={},payload={})
	config['rest'] = restObj

	config['output'] = hashlib.md5('Sacred Foundry'.encode()).hexdigest() + '.json'
	config['cache'] = 'cache/cards'
	config['time'] = 21600
	config['sleep'] = 200

	print(getRestData.execute(config))
test2()