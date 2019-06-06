# Argparse

Easy to use, very powerful replacment for manually parsing commandline
arguments with `sys.argv`.

```python
#!/usr/bin/env python3

import sys
print(sys.argv)
```

The commandline help is automatically generated.

```python
#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()
args = parser.parse_args()
```

The following shows a selection of what can be done with it. Comprehensive
documentation can be found in the
[Python Documentation](https://docs.python.org/3/howto/argparse.html).

```python
#!/usr/bin/python3

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('infile', nargs='+',
                    help='one or more input files')
parser.add_argument('--generate', action='store_true',
                    help='generate new instance and exit')
parser.add_argument('--heuristic',
                    choices=sorted(heuristic.heuristic.keys()),
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
parser.add_argument('--parkings', type=int, default=cfg.PARKINGS,
                    metavar='n',
                    help=('every Nth input line is a parking '
                          '(only relevant for non-JSON input) '
                          '(default: {})'.format(cfg.PARKINGS)))
parser.add_argument('-p', '--penalty', type=float,
                    default=cfg.ATTRACTIVITY_PENALTY,
                    metavar='value',
                    help=('penalty for cluster attractiveness when adding '
                          'a customer requires more workers; '
                          'should be >= 1 '
                          '(default: {})'.format(cfg.ATTRACTIVITY_PENALTY)))

args = parser.parse_args()
print(args.infile)
print(args.outfile)
print(args.flag)
```

Usually, you'd either parse the arguments from within the main function or
a function called from there.

```python
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
```

