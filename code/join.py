#!/usr/bin/env python

import argparse
import json
import os
from os.path import dirname, realpath

from pyspark import SparkContext


def parse_args():
    parser = argparse.ArgumentParser(description='MapReduce join (Problem 2)')
    parser.add_argument('-d', help='path to data file', default='./../data/records.json')
    parser.add_argument('-n', help='number of data slices', default=128)
    parser.add_argument('-o', help='path to output JSON', default='output')
    return parser.parse_args()


# Feel free to create more mappers and reducers.
def mapper():
    # TODO
    pass

def reducer1():
    # TODO
    pass

def reducer2():
    # TODO
    pass



def main():
    args = parse_args()
    sc = SparkContext()

    with open(args.d, 'r') as infile:
        data = [json.loads(line) for line in infile]
    
    # TODO: build your pipeline
    # join_result =

    sc.stop()

    if not os.path.exists(args.o):
        os.makedirs(args.o)

    with open(args.o + '/output_join.json', 'w') as outfile:
        json.dump(join_result, outfile, indent=4)


if __name__ == '__main__':
    main()
