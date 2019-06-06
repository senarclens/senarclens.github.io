#!/usr/bin/env python3

import argparse
import getpass
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--update-password', dest='password',
                        action='store_true',
                        help='ask for password to update keyring')
    parser.add_argument('-u', '--user', default=getpass.getuser(),
                        help='timetac API instance username')
    parser.add_argument('-v', '--verbose', action='count')
    args = parser.parse_args()
    # ...
    print(f'logging in {args.user}')

if __name__ == '__main__':
    sys.exit(main())
