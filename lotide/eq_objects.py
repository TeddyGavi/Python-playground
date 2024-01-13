def eq_objects(obj1, obj2):
    if len(obj1) != len(obj2) or obj1.keys() != obj2.keys():
        return False
    else:
        for key, value in obj1.items():
            if isinstance(value, dict) and isinstance(obj2[key], dict):
                return eq_objects(value, obj2[key])
            elif value != obj2[key]:
                return False

    return True
