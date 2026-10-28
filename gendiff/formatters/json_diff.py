import json


def form_json(diff):
    res = []
    for k, v in diff.items():
        if v[0] is None:
            res.append({
                "key": k,
                "type": "added",
                "value": v[1],
            })
        elif v[1] is None:
            res.append({
                "key": k,
                "type": "removed",
                "value": v[0],
            })
        elif v[1] != v[0] and None not in v:
            res.append({
                "key": k,
                "type": "changed",
                "old_value": v[0],
                "new_value": v[1],
            })
        elif v[0] == v[1] and None not in v:
            res.append({
                "key": k,
                "type": "unchanged",
                "value": v[0],
            })
    res = json.dumps(res, indent=2)
    return res