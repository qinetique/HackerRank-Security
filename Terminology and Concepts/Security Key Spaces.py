# Author : Tonmoy M
# GitHub URL : https://qinetique.github.io
# Problem : Security Key Spaces
# Problem Sub-Domain : Security | Terminology and Concepts
# Problem Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/security-message-space-and-ciphertext-space/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

n = input()
m = int(input())
nn = ''
for i in n:
    v = int(i)
    nn += str((v + m) % 10)
print(nn)