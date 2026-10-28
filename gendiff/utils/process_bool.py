

def process_bool(val):
    if val is True:
        return "true"
    elif val is False:
        return "false"
    elif val is None:
        return "null"
    else:
        return val