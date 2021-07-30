from templates.clustered import biased_clustered_profile
from templates.bipolar_bias import bipolar
from templates.unipolar_bias import unipolar
from templates.normal import normal_pref_profile

from helpers.fuzzing import fuzzing
from helpers.plots import borda_count_frequency
from helpers.iterative_copeland.iterative_copeland import pairwiseScoreCalcListFull, copelandScoreFull

import argparse
import json


parser = argparse.ArgumentParser()
# Auxiliary arguments
parser.add_argument('--json', '-j', nargs='?', help='Read json file as input.')

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
preference_profile = None

if args.json:
    with open(args.json, 'rt') as f:
        t_args = argparse.Namespace()
        t_args.__dict__.update(json.load(f))
        args = parser.parse_args(namespace=t_args)

if not (args.unipolar or args.bipolar or args.cluster or args.normal):
    parser.error(
        'Specify at least one voting pattern. You can pick from --unipolar, --bipolar, --cluster and --normal')

if not args.distribution:
    parser.error('Specify distribution argument. E.g: -d 1 2 3 4')

if [args.unipolar, args.bipolar, args.cluster, args.normal].count(None) < 3:
    parser.error('Specify exactly one of --unipolar, --bipolar, --cluster and --normal')

print(args)

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
    preference_profile = normal_pref_profile(args.normal, args.distribution, args.random)

if args.fuzz:
    preference_profile = fuzzing(preference_profile, args.fuzz)

print(preference_profile)

if args.copeland_score:
    score_list = pairwiseScoreCalcListFull(preference_profile, preference_profile.shape[0],preference_profile.shape[1])
    copeland_score = copelandScoreFull(score_list, preference_profile.shape[0],preference_profile.shape[1])
    print(copeland_score)

if args.frequency:
    borda_count_frequency(preference_profile, True)
if args.minizinc_data:
    dzn_lines = []
    dzn_lines.append("CANDIDATES = "+str(preference_profile.shape[0])+";\n")
    dzn_lines.append("AGENTS = "+str(preference_profile.shape[1])+";\n")
    dzn_pref_profile = str(list(map(int, preference_profile.flatten())))
    dzn_pref_profile = 'rankings = array2d(CANDIDATES, AGENTS,'+dzn_pref_profile+');\n'
    dzn_lines.append(dzn_pref_profile)
    if args.copeland_score:
        dzn_lines.append("copeland = "+str(copeland_score)+"\n")
    with open('profile.dzn', 'w') as f:
        f.writelines(dzn_lines)

'''
Notes
    Arguments:
        type:
            --unipolar  -u  -- no_of_candidates
            --bipolar   -b  -- no_of_candidates
            --clustered -c  -- no_of_clusters, size_of_clusters
            --simple    -s  -- no_of_candidates
                --distribution  -d common in all.
                --fuzzing_level -f common in all.
                --random        -r only in clustered and simple, has no impact on uni and bi. 
        auxilary commands:
            [x] --json              -j -- json file path
            [.] --borda-frequency   -bf
            [x] --copeland          -c
            [x] --minizinc          -mz
Checklist
    [x] Simple template
    [x] JSON
    [x] Copeland
    [x] Minizinc
    [ ] Borda-frequency
    [x] More JSON tests
'''
