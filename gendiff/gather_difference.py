

def form_difference_dict(d1, d2) -> dict:
    all_keys = set(d1.keys()).union(set(d2.keys()))
    all_keys = sorted(all_keys)
    diff = {}
    for k in all_keys:
        if k in d1.keys() and k in d2.keys():
            diff[k] = [d1[k], d2[k]]
        elif k in d1.keys():
            if k not in d2.keys():
                diff[k] = [d1[k], None]
            elif d2[k] != d1[k]:
                diff[k] = [d1[k], d2[k]]
        elif k in d2.keys() and k not in d1.keys():
            diff[k] = [None, d2[k]]
    return diff