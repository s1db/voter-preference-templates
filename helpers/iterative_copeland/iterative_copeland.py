'''
Iterative Copeland:
    - VOTERS/AGENTS -> the agents that rank/score the different candidates.
    - CANDIDATES -> the set of solutions that the different agents rank/score.
    - Cadidates are added in each iteration.
    - Our aim is do better than recomputing the whole matrix at each iteration.
    - Numpy is avoided to study the computational complexity of the whole program.
    - Once done, check if it gives the same output when the candidates are shuffled.
    - Present literature claims that Copeland Method is NP.
    - We want to check if adding a new candidate iteratively is also NP with a constant number of agents.
        - It's computationally cheaper than I thought! 
    - We also want to check if its better than recomputing the whole matrix.
'''
'''
PROJECT NOTE:
    - the rankings will either need to be recomputed at each iteration, or we'll need to use an ordinal approach.
        - Iteratively adding candidates would technically require a recompute of all rankings.
    - Incase of the ordinal approach, utility of each voter needs to be normalized.
    - ML literature has many ways scores can be computed and normalized to mitigate bias.
    - This can also be defied as a reasonable constraint on the problem at hand.
'''
'''
OPEN QUESTIONS NOTE:
    # Could rankings be replaced with utility scores?
    # How does that affect the copeland method?
    # Refer to chapter 10 of comsoc.
'''

VOTERS = 5
CANDIDATES = 4

# Global value to remember the index location of each iteration.
OFFSET = 0

#                    V_0 V_1 V_2 V_3 V_4   <-- voters/agents
original_rankings = [[0,  0,  3,  3,  1],   # C_0
                     [1,  1,  0,  0,  2],   # C_1
                     [2,  2,  1,  1,  3],   # C_2
                     [3,  3,  2,  2,  0]]   # C_3 <-- candidates
                                            # ...

example_rankings = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2], # A
                    [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], # B
                    [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3], # C
                    [0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]] # D

video = [[0, 0, 0, 0, 2, 2, 2, 1, 1, 1],
         [2, 1, 1, 1, 1, 1, 1, 0, 0, 0],
         [1, 2, 2, 2, 0, 0, 0, 2, 2, 2]]

def matrix2list(r, c, scores_list, no_of_voters):
    if r < c: return no_of_voters - scores_list[int(c*(c-1)//2 + r)]
    elif r == c: return 0
    else: return scores_list[(r*(r-1)//2 + c)]

def list2matrix(k):
    # NOTE: Very bad implementation, could possibly just be an equation.
    # It works though!!
    r = 1
    while r*(r-1)/2 <= k:
        r += 1
    r = r - 1
    c = k - (r*(r-1)//2)
    return (r,c)



'''
    - Computes the complete matrix
    - Only performs half the comparisions.
    - Returns an array which grows as an arithmetic progression with the no candidates.
    - A visual proof for how this works and why it can be done iteratively with the addition of a new candidate: 
        https://docs.google.com/presentation/d/1QSrd2i72x5r1nJ_GzHoGXJsJYefKVytp2YtCwlCuWYo/edit?usp=sharing
'''
def pairwiseScoreCalcListFull(pref_profile, no_of_candidates, no_of_agents):
    scores = []
    for i in range(no_of_candidates):
        for j in range(i):
            comparison_bool_list = [pref_profile[i][k] < pref_profile[j][k] for k in range(no_of_agents)]
            pairwise_comparison_score = sum(comparison_bool_list)
            scores.append(pairwise_comparison_score)
    return scores

# print("-----🌟-----")
# print(pairwiseScoreCalcListFull(example_rankings, len(example_rankings)))
# print("-----🌟-----")

'''
    - Similar to the code above.
    - Difference being that it doesn't recompute all scores, just appends to the 'scores list'.
    - NOTE: Needs to be changed to use the global scores array rather than a local copy.
'''
def pairwiseScoreCalcListNew(pref_profile, no_of_candidates):
    new_scores = []
    for j in range(no_of_candidates):
        new_scores.append(sum([pref_profile[no_of_candidates][k] < pref_profile[j][k] for k in range(VOTERS)]))
    return new_scores

# print("-----🌟-----")
# print(pairwiseScoreCalcListNew(original_rankings, 2))
# print("-----🌟-----")


def copelandScoreFull(scores, no_of_candidates, no_of_agents):
    final_score = [0]*no_of_candidates
    for x, i in enumerate(scores):
        r, c = list2matrix(x)
        if i > no_of_agents/2:
            final_score[r] += 1
        elif i == no_of_agents/2:
            final_score[r] += 0.5
            final_score[c] += 0.5
        else:
            final_score[c] += 1

    return final_score

# print("-----🌟-----")
# print(copelandScoreFull(pairwiseScoreCalcListFull(example_rankings, len(example_rankings)), len(example_rankings[0]), len(example_rankings)))
# print("-----🌟-----")


'''
    - new_scores are the scores of the addition of a new candidate(the pairwise scores).
    - final_score are the final copeland scores.
    - no_of_agents is the number of agents that rank the candidates.
    - offset is the 'virtual' pointer of the array position.
'''
def copelandScoreNew(new_scores, final_score, no_of_agents):
    i_final_scores.append(0)
    # imitating a pointer
    global OFFSET
    for i in new_scores:
        r, c = list2matrix(OFFSET)
        OFFSET += 1
        if i > no_of_agents/2:
            final_score[r] += 1
        elif i == no_of_agents/2:
            final_score[r] += 0.5
            final_score[c] += 0.5
        else:
            final_score[c] += 1
    return final_score

'''
- Reads list of scores and presents the scores[r][c] value
'''


# scores = pairwiseScoreCalcListFull(original_rankings, CANDIDATES)
# final_scores = copelandScoreFull(scores, VOTERS, CANDIDATES)
# print(scores)
# print(final_scores)

'''
    - Prints complete pairwise score matrix
'''

def fullScoreMatrixOutput(scores_list, candidates, no_of_voters):
    for i in range(candidates):
        s = ""
        for j in range(candidates):
            s = s + str(matrix2list(i, j, scores_list, no_of_voters)) + " "
        print(s)

# score_list = pairwiseScoreCalcListFull(example_rankings, len(example_rankings), len(example_rankings[0]))
# print(score_list)
# fullScoreMatrixOutput(score_list, len(example_rankings), len(example_rankings[0]))
# print(copelandScoreFull(score_list, len(example_rankings), len(example_rankings[0])))

'''
- Compares all preference profiles with each other.
- Returns a CANDIDATE X CANDIDATE matrix.
- Uses matrices and not lists.
'''
@DeprecationWarning
def scoreCalc(pref_profile):
    scores = []
    for x in pref_profile:
        l = []
        for y in pref_profile:
            l.append(sum([x[k] < y[k] for k in range(len(x))]))
        scores.append(l)
    return scores

@DeprecationWarning
def copelandScore(pref_profile, agents, voters):
    copeland_score = []
    for i in range(agents):
        copeland_score.append(scoreCalc(i))
    return copeland_score

# # Grows with each addition to the candidates, samples from the original profile.
# i_rankings = []
# i_scores = []
# i_final_scores = []
# # Adds new agents, one at a time.
# for x, i in enumerate(original_rankings):
#     i_rankings.append(i) # Addition of a new candidate from the original profile.
#     i_scores = pairwiseScoreCalcListNew(i_rankings, x)
#     i_final_scores = copelandScoreNew(i_scores, i_final_scores, VOTERS)
#     # print("Pairwise Scores: " + str(i_scores))
#     print("Final Score: " + str(i_final_scores))
