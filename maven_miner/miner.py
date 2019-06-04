#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
from pathlib import Path


class DataStore:

    def __init__(self):
        self.adjacency_list = {}

    def add(self, name, dependencies):
        # Expect uniqueness
        assert name not in self.adjacency_list.keys(), name

        # Add the item to the adjacency list.
        self.adjacency_list[name] = dependencies


class Miner:

    def __init__(self, directories):
        self.directories = directories
        self.datastore = DataStore()
        self.propfile_locations = itertools.chain(*(
            Path(i).glob('**/build.properties') for i in self.directories))

    def run(self):
        # Parse all of the new files.
        for propfile in self.propfile_locations:
            self.parse(propfile)

        return self.datastore

    def process(self, name, dependencies):
        self.datastore.add(name, dependencies)

    def parse(self, propfile):
        data = propfile.open().read()
        lines = data.split('\n')
        name = None
        deps = None
        for line in lines:
            if '=' not in line or line[:1] == '#' or '${' in line:
                continue

            # Extract the key and value.
            key, value = map(str.strip, line.strip().split('='))
            if 'application.name' in key or 'framework.name' in key:
                name = value
            elif 'dependencies' in key:
                deps = list(map(str.strip, value.split(',')))

        if name is not None and deps is not None:
            self.process(name, deps)
