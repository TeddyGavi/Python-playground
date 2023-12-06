def findKey(obj, cb):
    for key, value in obj:
        if cb(value):
            return key
