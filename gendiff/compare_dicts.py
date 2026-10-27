from gendiff.utils.process_bool import process_bool


def compare(d1, d2):
    comp = "{\n"
    all_keys = set(d1.keys()).union(set(d2.keys()))
    all_keys = sorted(all_keys)
    for k in all_keys:
        if k in d2.keys() and k not in d1.keys():
            comp += f"  + {k}: {process_bool(d2[k])}\n"
        elif k in d1.keys() and k not in d2.keys():
            comp += f"  - {k}: {process_bool(d1[k])}\n"
        elif k in d2.keys() and d1[k] == d2[k]:
            comp += f"    {k}: {process_bool(d1[k])}\n"
        elif k in d2.keys() and d1[k] != d2[k]:
            comp += f"  - {k}: {process_bool(d1[k])}\n"
            comp += f"  + {k}: {process_bool(d2[k])}\n"
    comp += "}"
    return comp