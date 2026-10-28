from gendiff.utils.process_bool import process_bool


def form_stylish(diff):
    comp = "{\n"
    for k, v in diff.items():
        if v[0] is None:
            comp += f"  + {k}: {process_bool(v[1])}\n"
        elif v[1] is None:
            comp += f"  - {k}: {process_bool(v[0])}\n"
        elif v[0] == v[1]:
            comp += f"    {k}: {process_bool(v[0])}\n"
        elif v[0] != v[1] and None not in v:
            comp += f"  - {k}: {process_bool(v[0])}\n"
            comp += f"  + {k}: {process_bool(v[1])}\n"
    comp += "}"
    return comp