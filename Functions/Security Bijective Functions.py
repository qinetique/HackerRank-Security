# Author : Tonmoy M
# GitHub URL : https://qinetique.github.io
# Problem : Security Bijective Functions
# Problem Sub-Domain : Security | Functions
# Problem Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/security-bijective-functions/problem?isFullScreen=true

def func(v, l):
    for i in range(0, v):
        for j in range(0, i):
            if (j + 1) in l:
                continue
            else:
                return 'NO'
    return 'YES'


v = int(input())
l = list(map(int, input().split()))
print(func(v, l))
