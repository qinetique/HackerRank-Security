# Author : Tonmoy M
# GitHub URL : https://qinetique.github.io
# Problem : Security Permutations
# Problem Sub-Domain : Security | Functions
# Problem Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/security-tutorial-permutations/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

n = int(input())
l = list(map(int, input().split()))
for i in range(n):
    print(l[l[i] - 1])