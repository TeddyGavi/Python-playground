def find_key_by_value(obj, val):
    for key, value in obj:
        if value == val:
            return key
