import random
from itertools import permutations
import numpy as np
import pandas as pd


def givenum():
    num = random.sample(range(0, 9), 4)
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
        S = random.sample(code_idx, int(len(code_set) / 3))
        remain = 0
        for idxx in S:  # each idxx acts like answer
            rema = code_idx.copy()
            rema.remove(idxx)
            A, B = playresult(code_set[idxx], code_set[idx])
            for k in rema:
                a, b = playresult(code_set[k], code_set[idx])
                if (a == A and b == B):
                    remain = remain + 1
        remain_table[idx] = remain
    mindex = np.argmin(remain_table)
    return code_set[mindex]


def ini_population():
    population = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
    return list(population)


play_number = 10000
total_num = 0
for i in range(play_number):
    code = givenum()
    code_set = ini_population()

    play_count = 0

    ini_process = 0
    A = 0
    ini_play_set = [(1, 2, 3, 4), (5, 6, 7, 8), (9, 0, 1, 5)]
    while (ini_process < 3 and A < 4):
        play_count = play_count + 1
        guess = ini_play_set[ini_process]
        A, B = playresult(code, guess)
        # code_set.remove(guess)
        for idx, val in enumerate(code_set):
            a, b = playresult(val, guess)
            if (A != a or B != b):
                code_set.remove(val)
        ini_process = ini_process + 1

    while (A < 4):
        play_count = play_count + 1
        # code_set.remove(guess)
        for idx, val in enumerate(code_set):
            a, b = playresult(val, guess)
            if (A != a or B != b):
                code_set.remove(val)
        guess = chooseone(code_set)
        A, B = playresult(code, guess)
    # Store the data to csv
    with open('./mastermind/result.csv', 'a') as f:
        df = pd.DataFrame([play_count])
        df.to_csv(f, header=False)

    total_num = total_num + play_count

print("Average number of count: ", total_num / play_number)
