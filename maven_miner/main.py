#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from miner import Miner


def main():
    parser = argparse.ArgumentParser(description='Generate a dependency map from multiple Maven'
                                     'projects.')
    parser.add_argument('directory', nargs='+',
                        help='Directory to recursively search for build.properties files in.')

    args = parser.parse_args()
    miner = Miner(args.directory)
    miner.run()


if __name__ == '__main__':
    main()
