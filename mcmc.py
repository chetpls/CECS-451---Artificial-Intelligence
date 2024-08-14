import sorobn as hh
import pandas as pd
import random

#part A
bn = hh.BayesNet(('C', ['S','R']),('S', 'W'), ('R','W'))

bn.P['C'] = pd.Series({True: 0.5, False:0.5})
bn.P['S'] = pd.Series({
     (True, True): 0.1, (True, False): 0.9,
     (False, True): 0.5, (False, False): 0.5})
bn.P['R'] = pd.Series({
     (True, True): 0.8, (True, False): 0.2,
     (False, True): 0.2, (False, False): 0.8})
bn.P['W'] = pd.Series({
     (True, True, True): 0.99, (True, True, False): 0.01,
     (True, False, True): 0.9, (True, False, False): 0.1,
     (False, True, True): 0.95, (False, True, False): 0.05,
     (False, False, True): 0.05, (False, False, False): 0.95})
bn.prepare()
bn.query('C', event={'S': False, 'W': True})

#part B
#P-> (C|¬s, r)
p_c_given_not_s_r = bn.query('C', event = {'S':False, 'R':True})

#P-> (C|¬s, ¬r)
p_c_given_not_s_not_r = bn.query('C', event = {'S':False, 'R':False})

#P->(R|c,¬s,w)
p_r_given_c_not_s_w = bn.query('R', event={'C':True,'S':False,'W':True})

#P->(R|¬c,¬s,w)
p_r_given_not_c_not_s_w = bn.query('R', event={'C':False,'S':False,'W':True})

#part C
#Transition matrix for s1
s1_s1 = (.5 * p_c_given_not_s_r[True]) + (.5 * p_r_given_c_not_s_w[True])
s1_s2 = .5 * p_r_given_c_not_s_w[False]
s1_s3 = .5 * p_c_given_not_s_r[False]
s1_s4 = 0

#Transition matrix for s2
s2_s1 = .5 * p_r_given_c_not_s_w[True]
s2_s2 = (.5 * p_r_given_c_not_s_w[False]) + (.5 * p_c_given_not_s_not_r[True])
s2_s3 = 0
s2_s4 = .5 * p_c_given_not_s_not_r[False]

#Transition matrix for s3
s3_s1 = .5 * p_c_given_not_s_r[True]
s3_s2 = 0
s3_s3 = (.5 * p_r_given_not_c_not_s_w[True]) + (.5 * p_c_given_not_s_r[False])
s3_s4 = .5 * p_r_given_not_c_not_s_w[False]

#Transition matrix for s4
s4_s1 = 0
s4_s2 = .5 * p_c_given_not_s_not_r[True]
s4_s3 = .5 * p_r_given_not_c_not_s_w[True]
s4_s4 = (.5 * p_r_given_not_c_not_s_w[False]) + (.5 * p_c_given_not_s_not_r[False])

#Transition matrix
transitionMatrix = [
    [s1_s1, s1_s2, s1_s3, s1_s4],
    [s2_s1, s2_s2, s2_s3, s2_s4],
    [s3_s1, s3_s2, s3_s3, s3_s4],
    [s4_s1, s4_s2, s4_s3, s4_s4]
]

#part D
#mcmc sampling
def estimate(n, transition_matrix):
    #states
    states = [1,2,3,4]

    #initialize state
    currentState = random.choice(states)

    #number of c=true,s=false,w=true
    counter = 0

    #mcmc sampling
    for i in range(n):
          #choose next state based on transition matrix
          nextIndex = random.choices(range(4), weights = transitionMatrix[states.index(currentState)])[0]
          nextState = states[nextIndex]
          #update count of when c=true,s=false,w=true
          if nextState == 1 or nextState == 2:
               counter += 1

        # Move to the next state
          currentState= nextState

    #calculate estimated
    estimated = counter / n

    return estimated

#part E, print part A
partA = "Part A. The sampling probabilities\n"
partA += "P(C|-s,r) = <{:.4f}, {:.4f}>".format(p_c_given_not_s_r[True], p_c_given_not_s_r[False]) + "\n"
partA += "P(C|-s,-r) = <{:.4f}, {:.4f}>".format(p_c_given_not_s_not_r[True],p_c_given_not_s_not_r[False]) + "\n"
partA += "P(R|c,-s,w) = <{:.4f}, {:.4f}>".format(p_r_given_c_not_s_w[True],p_r_given_c_not_s_w[False]) + "\n"
partA += "P(R|-c,-s,w) = <{:.4f}, {:.4f}>".format(p_r_given_not_c_not_s_w[True],p_r_given_not_c_not_s_w[False]) + "\n"
print(partA)

#part E, print part B
print("Part B. The transition probability matrix")
print("       S1     S2     S3     S4")
for i, row in enumerate(transitionMatrix):
     print(f"S{i+1}", " ".join(["{:.4f}".format(x) for x in row]))

#calculate exact probability
exact = bn.query('C', event={'S': False, 'W': True})

#part e, print C
print("\nPart C. The probability for the query P(C|-s,w)")
print(f"Exact probability: <{exact[True]:.4f}, {exact[False]:.4f}>")
#show estimated probability for given n
n = [10**3, 10**4, 10**5, 10**6]
for i in n:
    estimated = estimate(i, transitionMatrix)
    error = abs(estimated - exact[True]) / exact[True] * 100
    print(f"n = 10 ^ {len(str(i))-1}: <{estimated:.4f}, {1-estimated:.4f}>, error = {error:.2f}%")

