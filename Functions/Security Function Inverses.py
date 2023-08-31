# Author : Tonmoy M
# GitHub URL : https://qinetique.github.io
# Problem : Security Function Inverses
# Problem Sub-Domain : Security | Functions
# Problem Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/security-inverse-of-a-function/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

n = int(input())
l = list(map(int, input().split()))
position = []
for i in range(1, n + 1):
    position.append(i)
v = zip(position, l)
v = sorted(v, key=lambda k: k[1])
for sex in v:
    print(sex[0])
