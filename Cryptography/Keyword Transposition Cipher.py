# Author : Tonmoy M
# GitHub URL : https://qinetique.github.io
# Problem : Keyword Transposition Cipher
# Problem Sub-Domain : Security | Cryptography
# Problem Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/keyword-transposition-cipher/problem?isFullScreen=true

# attempt 24

from string import ascii_uppercase as asciiup


def decode_function(k, m):
    key = ''.join([x for i, x in enumerate(k) if k.index(x) == i])
    letter = ''.join([x for x in asciiup if x not in key])
    decode = key + letter
    col = sorted([''.join([decode[x] for x in range(n, len(decode), len(key))]) for n in range(len(key))])
    d = {a: b for b, a in zip(asciiup, ''.join(col))}
    return ''.join(d[x] if x in d else ' ' for x in m)


t = int(input())
for _ in range(t):
    key = input()
    v = input()
    print(decode_function(key, v))
