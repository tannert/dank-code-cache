import random

N = 10


def roll():
    return random.randint(1, 6)


ladders = {1: 38,
           4: 14,
           9: 31,
           21: 42,
           28: 84,
           36: 44,
           51: 67,
           71: 91,
           80: 100}

chutes = {16: 6,
          47: 26,
          49: 11,
          56: 53,
          62: 19,
          64: 60,
          87: 24,
          93: 73,
          95: 75,
          98: 78}

ladders.update(chutes)
routes = ladders


def land_on(sq):
    print sq,
    hits[sq] += 1


for i in xrange(N):
    square = 0
    hits = [0] * 101
    while True:
        this_roll = roll()
        if this_roll + square > 100:
            # does staying on the same space count twice?
            continue
        square += this_roll

        land_on(square)

        if square in routes:
            square = routes[square]
            land_on(square)

        if square == 100:
            print
            break  # won the game
