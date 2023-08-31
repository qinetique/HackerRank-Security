# Author : Tonmoy M
# GitHub URL : https://qinetique.github.io
# Problem : PRNG Sequence Guessing
# Problem Sub-Domain : Security | Cryptography
# Problem Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/prng-sequence-guessing/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

def tonmoy_update(seed):
    return (seed * 0x5DEECE66D + 0xB) & ((1 << 48) - 1)


def tonmoy_shift(seed):
    return seed >> 17


def nextInt(seed, n):
    return tonmoy_shift(seed) % n


def tonmoy_search(v):
    global seed
    for lb in range(2 ** 20):
        seed = lb
        for i in v:
            seed = tonmoy_update(seed)
            if (tonmoy_shift(seed) & 7) - (i & 7):
                break
        else:
            for hb in range(2 ** 64):
                seed = lb | (hb << 20)
                for i in v:
                    seed = tonmoy_update(seed)
                    if nextInt(seed, 1000) != i:
                        break
                else:
                    return seed


t = int(input())
for _ in range(t):
    v = list(map(int, input().split()))
    seed = tonmoy_search(v)
    solution = list()
    for _ in range(10):
        seed = tonmoy_update(seed)
        solution.append(nextInt(seed, 1000))
    print(' '.join(map(str, solution)))
