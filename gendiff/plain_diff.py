from gendiff.utils.process_bool import process_bool


def form_plain(diff) -> str:
    res = []
    for k, v in diff.items():
        if v[0] is None:
            res.append(f"Property '{k}' was added with value: {process_bool(v[1])}")
        elif v[1] is None:
            res.append(f"Property '{k}' was removed")
        elif v[0] != v[1] and None not in v:
            res.append(f"Property '{k}' was updated. From {process_bool(v[0])} to {process_bool(v[1])}")
    return "\n".join(res)