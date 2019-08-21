import json
import collections


def readfile(barrackfile):
    with open(barrackfile) as jsonfile:
        for row in jsonfile:
            obj = json.loads(row)
            yield(collections.namedtuple("Grunt", obj.keys())(*obj.values()))
