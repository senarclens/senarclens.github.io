#!/usr/bin/python3

import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('infile', nargs='+',
                    help='one or more input files')
parser.add_argument('--generate', action='store_true',
                    help='generate new instance and exit')
parser.add_argument('--heuristic',
                    choices=('option_1', 'option_2', 'option_3'),
                    help='select the clustering heuristic to use')
parser.add_argument('--no-color', action='store_true',
                    help='optimize visualization for gray scale printouts')
parser.add_argument('--no-writeback', dest="no_writeback",
                    action='store_true',
                    help='disable updating problems with new best results')
parser.add_argument('--outdir', default=os.curdir+os.sep,
                    metavar='dir',
                    help=('write all output files in this directory; '
                          'the given directory must exist and be writable '
                          '(default: {})'.format(os.curdir+os.sep)))
parser.add_argument('--parkings', type=int, default=3,
                    metavar='n',
                    help=('every Nth input line is a parking '
                          '(only relevant for non-JSON input) '
                          '(default: 3)'))
parser.add_argument('-p', '--penalty', type=float,
                    default=0.0,
                    metavar='value',
                    help=('penalty for cluster attractiveness when adding '
                          'a customer requires more workers; '
                          'should be >= 1 '
                          '(default: 0.0)'))

args = parser.parse_args()
print(args.infile)
print(args.outfile)
print(args.flag)

