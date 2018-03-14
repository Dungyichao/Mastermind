import random
from itertools import permutations


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


def ini_population():
    population = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
    return list(population)


total_num = 0
for i in range(1000):
    code = givenum()
    code_set = ini_population()
    guess = tuple(random.sample(range(0, 9), 4))
    A, B = playresult(code, guess)
    play_count = 1
    while (A < 4):
        play_count = play_count + 1
        for idx, val in enumerate(code_set):
            a, b = playresult(val, guess)
            if (A != a or B != b):
                code_set.remove(val)
        guess = random.choice(code_set)
        A, B = playresult(code, guess)
    total_num = total_num + play_count

print("Average number of count: ", total_num / 1000)

