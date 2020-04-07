import json
from collections import defaultdict


def list_duplicates(seq):
    tally = defaultdict(list)
    for i, item in enumerate(seq):
        tally[item].append(i)
    return ((key, locs) for key, locs in tally.items() if len(locs) > 1)


def extract(file):
    json_file = open(file)
    data = json.load(json_file)
    dow = []
    time = []
    conf = []
    for p, q, r in data:
        for k, v in p.items():
            dow.append(v)
        for t, h in q.items():
            time.append(h)
        for a, b in r.items():
            for c in b.items():
                conf.append(b["Large"])
    x = {}
    y = {}
    for c in (list_duplicates(dow)):
        # print(c)
        x.update({c[0]: c[1]})

    for k, v in x.items():
        t_room = {}
        for p in v:
            t_room.update({time[p]: conf[p]})
        y.update({k: t_room})

    m = {'Monday': {}, 'Tuesday': {}, 'Wednesday': {}, 'Thursday': {}, 'Friday': {}}
    for k, v in m.items():
        m.update({k: y[k]})
    for k, v in m.items():
        s = {i: v[i] for i in sorted(v)}
        m.update({k: s})

    return m


ext = extract("F5_Week1.txt")
print(ext)