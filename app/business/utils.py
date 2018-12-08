import datetime

def clean_ds(data, drop_key=[]):
    """Clean a data structure for json.
    
    drop_key (list): a list of keys to recursively drop when encountered
    """
    if type(data) == dict:
        new_dict = {}
        for k,v in data.items():
            if k not in drop_key:
                new_dict[k] = clean_ds(v)
        return new_dict
    elif type(data) in [list, set]:
        return [clean_ds(v) for v in data]
    elif type(data) == datetime.datetime:
        return data.strftime("%Y%m%d-%H%M%S")
    elif type(data) in [int,float,str,bytes,bool] or data is None:
        return data
    else:
        return "Parse Error [%s]" % str(data)

def get_first_key(obj, key):
    """Return the value of the first key matching the given key.
    Recursively searches the obj.
    obj should contain at least one dict. Can be a nested dict or list of dicts
    or whatever.
    
    Returns None if not found
    """

    if type(obj) is dict and key in obj:
        return obj[key]
    elif type(obj) is dict:
        for k,v in obj.items():
            gfk = get_first_key(v, key)
            if gfk is not None:
                return gfk
    elif type(obj) is list:
        for item in obj:
            gfk = get_first_key(item, key)
            if gfk is not None:
                return gfk
    return None
