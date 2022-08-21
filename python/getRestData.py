import pwd
import sys
import os
import time
import requests
import json


import argparse


def init_argparse() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [FILE]...",
        description="<program_description>"
    )

    parser.add_argument(
        "-v", "--version", action="version",
        version = f"{parser.prog} version 0.01"
    )
    ###
    #Add Custom arguments here with add_argument
    ###
    #the file to write to, 1 positional argument after
    parser.add_argument('-o','--output',nargs=1,default=False,
                    help='file to store result in - defaults to none')
    #location of cache file to write or check, 1 positional argument after
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

def getTime(float):
    return int(str(float).split('.')[0])
    pass

#004 - Read File
def readCache(file, path=os.getcwd(), age=5):
    fileToOpen = path + '/' + file
    if os.path.exists(fileToOpen):
        fileAge = getTime(time.time()) - getTime(os.path.getmtime(fileToOpen))
        if fileAge/60 > age:
            return False 
        
        with open(fileToOpen) as f:
            for line in f:
                jsonObj = line.strip(' \t\n\r')
                return jsonObj
    return False

def execute(config):
    returnJSON = False
    time.sleep(config.cache / 1000)
    #003 - Check Cache
    #are we using cache
    if 'output' in config:
        returnJSON = readCache(config['output'], config['cache'] or os.getcwd())
        pass

    #005 - Rest Call
    if returnJSON is False or config['no_cache']:
        pass
    #006 - Write to cache

    #007 - Return JSON Data
    return returnJSON

def main():
    args = init_argparse()
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

#print(parser)