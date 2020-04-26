#!/usr/bin/env python3

import csv
import json
import sys
import requests
import os

verbose = os.getenv('VERBOSE', False)
url = os.getenv('URL')

if len(sys.argv) != 2:
    print("Usage: [URL=...] ./upload-csv.py file.csv")
    sys.exit(1)

csv_path = sys.argv[1]


class Dumper:
    MAX_RECORDS_IN_POST = os.getenv('MAX_RECORDS_IN_POST', 50)

    def __init__(self, url, verbose):
        self.url = url
        self.verbose = verbose
        self.data = []

    def sumo_json(self, data):
        rows = []
        for record in data:
            rows.append(json.dumps(record))
        return "\n".join(rows)

    def dump_maybe(self, force=False):
        if len(self.data) >= Dumper.MAX_RECORDS_IN_POST or force:
            payload = self.sumo_json(self.data)
            if verbose:
                print(payload)

            if self.url:
                print("Sending a payload of %d records to %s" % (len(self.data), self.url))
                response = requests.post(url=self.url, data=payload)
                print(response)
            self.data = []

    def process(self, path):
        with open(path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.data.append(row)
                self.dump_maybe()

            self.dump_maybe(True)


Dumper(url, verbose).process(csv_path)
