class RESTObject(object):
    _defaults = {
        "operation": "get",
        "endpoint": None,
        "params": {},
        "headers": "",
        "payload": ""
    }
    def __init__(self, **kwargs):
        self.__dict__.update(self._defaults)
        self.__dict__.update(kwargs)    