# GetRESTData
Repository of scripts that acquire resources from a REST endpoint

# Inputs

output - o - file to store result in - defaults to none

no-cache - nc - forces a rest call - defaults to false

cache - c - cache directory - defaults to forced call and stores result in cwd if output provided

time - t - age of cache file in mins to force call - defaults to 5 

sleep - s -time to sleep in ms for the request - default 200

rest - r - REST object - if not provided will return a False

* operation
* endpoint
* params
* header
* payload

e.g

runs a Magic the Gathering card search against the exact name 'Overgrown Tomb' and stores the result in a cache file 'dfb86d6f05e9f54e9dde11f6ad052660.json', which is the md5 version of the name, in the cache/ directory the program is run from, this file will be used, since -nc was not given, if the file is less than 15days old. The program will wait 200ms before returning the result

program -o "dfb86d6f05e9f54e9dde11f6ad052660" -c "cache/cards" -t 21600 -s 200 -r "{'operation':'get','endpoint':'https://api.scryfall.com/cards/named','params':{'exact':'Overgrown Tomb'},'headers':{},'payload':{}}"

the program will return the json string representation of the result of the command or an Error object:

```json
{"object":"card","id":"eff1f52c-5c43-4260-aaa0-6920846a191c","oracle_id":"975ec9a3-6f20-4177-8211-82526e092538","multiverse_ids":[453003],"mtgo_id":69919,"arena_id":68734,"tcgplayer_id":175196,"cardmarket_id":363554,"name":"Overgrown Tomb",.....ll"}}

{"errorCode":"404","errorDescription":"Resource not found"}

{"errorCode":"json.decoder.JSONDecodeError","errorDescription":"Unterminated string starting at: line 1 column 14 (char 13)"}
```

can also be invoked as a python module via getRestData().execute(config)

where the config object follows a similar structure:

```python
config = {
    'output': 'dfb86d6f05e9f54e9dde11f6ad052660.json',
    'cache': 'cache/cards',
    'time': 21600,
    'sleep': 200,
    'rest': {
        'operation': 'get',
        'endpoint': 'https://api.scryfall.com/cards/named',
        'params': {'exact': 'Overgrown Tomb'},
        'headers': {},
        'payload': {}
    }
}
response = getRestData.execute(config)
```

![Process Flow](https://github.com/samuelshiels/GetRESTData/blob/main/Get-Rest-Data.drawio.png "Process Flow")
