import getRestData
import hashlib

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

#test false
def test2():
    restObj = {}
    config = {}
    restObj['operation'] = 'get'
    restObj['endpoint'] = 'https://api.scryfall.com/cards/named'
    restObj['params'] = {'exact':'Overgrown Tomb'}
    restObj['headers'] = {}
    restObj['payload'] = {}
    #config['rest'] = restObj
    print(getRestData.execute(config))
test2()