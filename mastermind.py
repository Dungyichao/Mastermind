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

    play_count = 0  # store the value of the number of guessing in this play

    ini_process = 0  # To enter the while loop
    A = 0  # To enter the while loop
    ini_play_set = [(1, 2, 3, 4), (5, 6, 7, 8), (9, 0, 1, 5)]  # The fix code we play for the first 3 play
    while (ini_process < 3 and A < 4):  # while in first three play and the answer not yet obtained
        play_count = play_count + 1  # keep recording the time we play
        guess = ini_play_set[ini_process]  # using the fix code to play
        A, B = playresult(code, guess)  # Get the A, B value with guess and code
        for idx, val in enumerate(code_set):  # Check all the element in the code_set
            a, b = playresult(val, guess)  # we assume val were the answer and compare with the guess
            if (A != a or B != b):  # if a, b is not the same as A, B --> val is not answer
                code_set.remove(val)  # remove the val from the code_set
        ini_process = ini_process + 1  # move to the next fix code set

    while (A < 4):  # Still cleaning the code_set until we find the real answer
        play_count = play_count + 1
        for idx, val in enumerate(code_set):
            a, b = playresult(val, guess)
            if (A != a or B != b):
                code_set.remove(val)
        guess = chooseone(code_set)  # We use the chooseone function to pick the element in the code set for next play
        A, B = playresult(code, guess)
        # Store the data to csv
    with open('./mastermind/mastermind_new1.csv', 'a') as f:
        df = pd.DataFrame([play_count])
        df.to_csv(f, header=False)

    total_num = total_num + play_count  # add the total number of playing to total_num

print("Average number of count: ", total_num / play_number)  # show the average number of guessing