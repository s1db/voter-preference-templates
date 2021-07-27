import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--json', '-j', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='Read json file as input.')

parser.add_argument('--borda-frequency', '-bf', action='store_true', help='Plot borda frequency of profile.')
parser.add_argument('--copeland', '-c', action='store_true', help='Generate copeland score for profile.')
parser.add_argument('--minizinc-data', '-dzn', action='store_true', help='Save profile as MiniZinc datafile.')
parser.add_argument('--fuzz', '-f', type=int, nargs='?', help='Number of swaps per agent profile.')

args = parser.parse_args()

import sys

'''
Notes
    Arguments:
        type:
            --unipolar  -u  -- candidates, distribution
            --bipolar   -b  -- candidates, distribution
            --clustered -c  -- no_of_clusters, size_of_clusters, distribution, random?
            --simple    -s  -- candidates, distribution, random?
        auxilary commands:
            x--json              -j -- json file path
            x--fuzzing_level     -f
            x--borda-frequency   -bf
            x--copeland          -c
            x--minizinc          -mz
Checklist
    [ ] Tie all templates together in the driver
    [ ] Implement a commandline interface
    [ ] Borda count frequencies
'''