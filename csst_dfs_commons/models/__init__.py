# coding: utf-8
class Result(dict):
    def __init__(self):
        super(Result, self).__init__()
        self.code = 0
        self.message = ""
        self.data = None
    
    def success(self):
        return self.code >= 0

    @staticmethod
    def error(code = -1, message = ""):
        r = Result()
        r.code = code
        r.message = message
        return r

    @staticmethod
    def ok_data(data):
        r = Result()
        r.data = data
        return r
        
    @staticmethod
    def ok_msg(message):
        r = Result()
        r.message = message
        return r