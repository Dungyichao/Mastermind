import random
from itertools import permutations
import numpy as np
import pandas as pd

def givenum():
    num = random.sample(range(0,9), 4)
    return tuple(num)

def playresult(notknow, guess):
    A = 0
    B = 0
    for idx, val in enumerate(notknow):
        for idx2, val2 in enumerate(guess):
            if (idx == idx2 and val == val2):  # position & value are correct
                A = A + 1
            elif (val == val2):
                B = B + 1
    return A, B


def chooseone(code_set):
    remain_table = np.zeros(len(code_set))
    for idx, val in enumerate(code_set):
        code_idx = [j for j in range(len(code_set))]
        code_idx.remove(idx)
        if (len(code_idx) > 100):
            S = random.sample(code_idx, 100)
        else:
            S = random.sample(code_idx, len(code_idx))
        remain = 0
        for idxx in S:   #  each idxx acts like answer
            A, B = playresult(code_set[idxx], code_set[idx])
            for k in S:
                a, b = playresult(code_set[k], code_set[idx])
                if (a == A and b == B):
                    remain = remain + 1
        remain_table[idx] = remain
    mindex = np.argmin(remain_table)
    return code_set[mindex]

def ini_population():
    population = permutations([0,1,2,3,4,5,6,7,8,9], 4)
    return list(population)


play_number = 10000  # how many time we want to play
total_num = 0  # store the value of the total number of guessing through all the play
for i in range(play_number):  # start playing each game
    code = givenum()  # Create a code
    code_set = ini_population()  # Initialize a set of code set containing possible answer

    # Create a first guess randomly
    guess = tuple(random.sample(range(0, 9), 4))
    # Get the A, B value with guess and code
    A, B = playresult(code, guess)
    play_count = 1  # store the value of the number of guessing in this play

    while (A < 4):  # Still cleaning the code_set until we find the real answer
        play_count = play_count + 1
        code_set = [t for t in code_set if playresult(t, guess) == (A, B)]
        guess = chooseone(code_set)  # We use the chooseone function to pick the element in the code set for next play
        A, B = playresult(code, guess)
        # Store the data to csv
    with open('./mastermind/mastermind_final.csv', 'a') as f:
        df = pd.DataFrame([play_count])
        df.to_csv(f, header=False)

    total_num = total_num + play_count  # add the total number of playing to total_num

print("Average number of count: ", total_num / play_number)  # show the average number of guessing