from clustered import biased_clustered_profile
from bipolar_bias import bipolar
from unipolar_bias import unipolar
from fuzzing import fuzzing
import argparse
import sys

parser = argparse.ArgumentParser()
# Auxiliary arguments
parser.add_argument('--json', '-j', nargs='?', type=argparse.FileType('r'),
                    default=sys.stdin, help='Read json file as input.')

parser.add_argument('--frequency', '-bf',
                    action='store_true', help='Plot borda frequency of profile.')
parser.add_argument('--copeland-score', '-cs', action='store_true',
                    help='Generate copeland score for profile.')
parser.add_argument('--minizinc-data', '-dzn', action='store_true',
                    help='Save profile as MiniZinc datafile.')

# Template helper arguments
parser.add_argument('--fuzz', '-f', type=int, nargs='?',
                    help='Number of swaps per agent profile.')
parser.add_argument('--random', '-r', action='store_true',
                    help='Generates random profiles rather than sequential. NOTE: Can only be used with simple and clustered.')
parser.add_argument('--distribution', '-d', nargs='+', type=int,
                    help='Distribution of agents and their voting styles.')

# Template arguments, choosing one is mandatory
parser.add_argument('--unipolar', '-u', type=int,
                    help='Unipolar voting pattern. Specify the number of candidates.')

parser.add_argument('--bipolar', '-b', type=int,
                    help='Bipolar voting pattern. Specify the number of candidates.')

parser.add_argument('--cluster', '-c', type=int, nargs=2,
                    help='Clustered voting pattern. Specify the number of clusters and size of each cluster.')

parser.add_argument('--normal', '-n', type=int,
                    help='A generic voting pattern. Specify the number of candidates.')

args = parser.parse_args()

if not (args.unipolar or args.bipolar or args.cluster or args.normal):
    parser.error(
        'Specify at least one voting pattern. You can pick from --unipolar, --bipolar, --cluster and --normal')

if not args.distribution:
    parser.error('Specify distribution argument. E.g: -d 1 2 3 4')

# Imports added later for better performance
if args.unipolar:
    if len(args.distribution) != 1:
        parser.error(
            'Distribution for unipolar templates can only take 1 argument.')
    preference_profile = unipolar(args.unipolar, args.distribution[0])
elif args.bipolar:
    if len(args.distribution) != 2:
        parser.error(
            'Distribution for unipolar templates can only take 2 argument.')
    preference_profile = bipolar(
        args.bipolar, args.distribution[0], args.distribution[1])
elif args.cluster:
    # NOTE: Fix randomization for clustered template
    preference_profile = biased_clustered_profile(
        args.cluster[0], args.cluster[1], args.distribution, False, args.random)
elif args.normal:
    None

if args.fuzz:
    preference_profile = fuzzing(preference_profile, args.fuzz)

print(preference_profile)


'''
Notes
    Arguments:
        type:
            [x] --unipolar  -u  -- no_of_candidates
            [x] --bipolar   -b  -- no_of_candidates
            [x] --clustered -c  -- no_of_clusters, size_of_clusters
            [ ] --simple    -s  -- no_of_candidates
                [ ] --distribution  -d common in all.
                [ ] --fuzzing_level -f common in all.
                [ ] --random        -r only in clustered and simple, has no impact on uni and bi. 
        auxilary commands:
            [ ] --json              -j -- json file path
            [.] --borda-frequency   -bf
            [ ] --copeland          -c
            [ ] --minizinc          -mz
Checklist
    [ ] Simple template
    [ ] Copeland
    [ ] Minizinc
    [ ] JSON
    [ ] Borda-frequency
    [ ] Tie all templates together in the driver
    [ ] Implement a commandline interface
    [ ] Borda count frequencies
'''
