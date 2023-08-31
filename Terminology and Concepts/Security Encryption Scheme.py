# Author : Tonmoy M
# GitHub URL : https://qinetique.github.io
# Problem : Security Encryption Scheme
# Problem Sub-Domain : Security | Terminology and Concepts
# Problem Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/security-encryption-scheme/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def w_funct(n):
    if n == 1:
        return 1
    return n * w_funct(n - 1)
n = int(input())
print(w_funct(n))

