import csv
import collections


def readfile(barrackfile):
    with open(barrackfile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield(collections.namedtuple("Grunt", row.keys())(*row.values()))
