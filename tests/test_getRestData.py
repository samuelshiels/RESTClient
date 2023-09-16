'''import json
import hashlib
import os
from pathlib import Path
from src.python.RESTObject import RESTObject as ro

import src.python.getRestData as grd'''

def test_active():
	assert(1 == 1)
	assert(True is not False)
'''
def test_minimal_config():
	config = {}
	restObj = ro(operation='get', endpoint='https://api.scryfall.com/cards/named',params={'exact':'Overgrown Tomb'},headers={},payload={})
	config['rest'] = restObj
	return_json = grd.execute(config, True)
	return_obj = json.loads(return_json)
	assert(return_obj['name'] == 'Overgrown Tomb')

def test_cache():
	config = {}
	restObj = ro(operation='get', endpoint='https://api.scryfall.com/cards/named',params={'exact':'Sacred Foundry'},headers={},payload={})
	config['rest'] = restObj
	config['output'] = hashlib.md5('Sacred Foundry'.encode()).hexdigest() + '.json'
	config['cache'] = os.path.join(Path.home(),'.cache/cards')
	config['time'] = 21600
	config['sleep'] = 200
	#return_json = grd.execute(config, True)
	assert(1 == 1)'''
