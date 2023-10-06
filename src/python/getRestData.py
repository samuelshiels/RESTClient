import os
import time
import requests
import argparse
from pathlib import Path

from diskcache import Cache as C
cache = C()
import LogHelper as log
from RESTObject import RESTObject



ae = {}
ae['app_name'] = appName = 'getRestData'
ae['version'] = '0.1.0'
ae['root_dir'] = os.path.join(
str(Path.home()), ".config/", ae['app_name'])
ae['cache_dir'] = cache_dir = ''
ae['log_file'] = logFileName = 'getRestData.log'
ae['log_file_dir'] = logFilePath = os.path.join(str(Path.home()), '.cache', appName)
ae['debug'] = False

import logging
logging.basicConfig(
format='%(asctime)s | %(levelname)s | %(message)s', level=logging.DEBUG)
debug = True
def __debugMessage(message):
	global debug
	if debug:
		logging.debug(str(message))

def debug(content):
	if not logging:
		return
	log.writeLog(logFileName, logFilePath, log.formatLog(str(content)))


def get_short_string(content):
	if str(content).__len__() < 110:
		return content
	else:
		return f"{str(content)[:100]}...{str(content)[-10:]}"

def __init_argparse() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser(
		usage="%(prog)s [OPTION] [FILE]...",
		description="<program_description>"
	)
	parser.add_argument(
		"-v", "--version", action="version",
		version = f"{parser.prog} version 0.01"
	)
	parser.add_argument('-o','--output',nargs=1,default=False,
					help='file to store result in - defaults to none')
	parser.add_argument('-c','--cache',nargs=1,default=False,
					help='cache directory - defaults to forced call and stores result in cwd if output provided')
	parser.add_argument('-t','--time',nargs=1,type=int,default=5,
					help='age of cache file in mins to force call - defaults to 5 ')
	parser.add_argument('-s','--sleep',nargs=1,type=int,default=200,
					help='time to sleep in ms for the request - default 200')
	parser.add_argument('-nc','--no-cache',default=False,action='store_true',
					help='force a rest call')
	parser.add_argument('-r','--rest',nargs=1,default=False,
					help='REST object - if not provided will return an error object')
	args = parser.parse_args()
	#print(args)
	if args.cache is False:
		args.cache = os.getcwd()
	return args
	
def __readCache(file, path=os.getcwd(), age=5):
	try:
		return cache.get(file, default=False)
	except Exception as e:
		return {
			'errorCode':'ReadFile',
			'errorDescription':str(e)
		} 

def __executeCall(restObj: RESTObject, sleep: int) -> str | dict:
	sleep_time = sleep / 1000
	__debugMessage(f'Starting Sleep for {sleep_time}s {time.time()}')
	time.sleep(sleep_time)
	__debugMessage(f'Finished for {sleep_time}s {time.time()}')
	try:
		operation = restObj.operation 
		endpoint = restObj.endpoint
		params = restObj.params
		payload = restObj.payload
		headers = restObj.headers
		if operation == 'get':
			__debugMessage(['Running REST Call', operation, endpoint, params, headers, get_short_string(payload)])
			response = requests.get(
				url=endpoint,
				params=params,
				headers=headers,
				data=payload
			)
			return response.text
	except Exception as e:
		return {
			'errorCode':'RESTCall',
			'errorDescription':str(e)
		}

def __writeCache(file, content, path=os.getcwd()):
	try:
		key, value = file, content
		__debugMessage(f'Setting key {key} {value} {0}')
		return C.set(key, value, expire=None)
	except Exception as e:
		return {
			'errorCode':'WriteFile',
			'errorDescription':str(e)
		}
	
def __validateConfig(config):
	if 'no_cache' not in config:
		config['no_cache'] = False
	if 'output' not in config:
		config['output'] = None
	if 'cache' not in config:
		config['cache'] = None
	if 'time' not in config:
		config['time'] = 5
	if 'sleep' not in config:
		config['sleep'] = 200
	if 'rest' not in config:
		return False
	return config

def retrieveFile(url, cache, fileName, age, log=False):
	"""Retrieves the file from the given url and writes it to the provided cache and filename under the conditions the cache is not older than the age"""
	if not __readCache(fileName, cache, age):
		# print(f'retrieving file from {url} into {cache}/{fileName}')
		r = requests.get(url)
		__writeCache(fileName, r.content, cache)
		# urllib.request.urlretrieve(url, f'{cache}/{fileName}')
	return f'{cache}/{fileName}'

def execute(config, log=False):
	global debug
	debug = log

	config = __validateConfig(config)

	global cache_dir, cache
	cache_dir = config['cache']
	cache = C(cache_dir)

	if not config:
		return False
	
	runCall = False
	returnJSON = False
	#003 - Check Cache
	if config['output'] is not None and config['no_cache'] is not True:
		#004 - Read File
		returnJSON = __readCache(config['output'], config['cache'] or os.getcwd(), config['time'])
	#005 - Rest Call
	if returnJSON is False or config['no_cache']:
		returnJSON = __executeCall(config['rest'], config['sleep'])
		runCall = True
	#006 - Write to cache
	if returnJSON is not False and config['output'] and runCall:
		if 'errorCode' not in returnJSON:
			errorObj = __writeCache(config['output'], returnJSON, config['cache'])
	#007 - Return JSON Data
	return returnJSON

def main():
	args = __init_argparse()
	config = {
		'cache': args.cache,
		'output': args.output,
		'time': args.time,
		'sleep': args.sleep,
		'no_cache': args.no_cache,
		'rest': args.rest
	}
	returnJSON = execute(config)
	print(returnJSON)

if __name__ == "__main__":
	main()