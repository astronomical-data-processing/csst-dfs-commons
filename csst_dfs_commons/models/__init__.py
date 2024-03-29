# coding: utf-8
class Result(dict):
    def __init__(self):
        super(Result, self).__init__()
        self["code"] = 0
        self["message"] = ""
        self["data"] = None
    
    @property
    def success(self):
        return self["code"] == 0

    @property
    def data(self):
        return self["data"]

    @property
    def message(self):
        return self["message"]
        
    @staticmethod
    def error(code = -1, message = ""):
        r = Result()
        r["code"] = code
        r["message"] = message
        return r

    @staticmethod
    def ok_data(data=None):
        r = Result()
        r["data"] = data
        return r
        
    @staticmethod
    def ok_msg(message):
        r = Result()
        r["message"] = message
        return r

    def append(self, k: str, v):
        self[k] = v
        return self

class Request(object):
    def __init__(self, **kvargs):
        super(Request, self).__init__()
        for k, v in kvargs.items():
            self.append(k, v)

    @staticmethod
    def from_dict(d: dict):
        r = Request()
        for k, v in d.items():
            r.append(k, v)
        return r

    def append(self, k: str, v):
        self.__setattr__(k, v)
        return self

    def __getattr__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except:
            return ''
