# Author : Tonmoy M
# GitHub URL : https://qinetique.github.io
# Problem : Security - Message Space and Ciphertext Space
# Problem Sub-Domain : Security | Terminology and Concepts
# Problem Domain : HackerRank
# Problem URL : https://www.hackerrank.com/challenges/security-message-space-and-ciphertext-space/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

n = input()
nn = ''
for i in n:
    v = int(i)
    if v != 9:
        v += 1
        nn += str(v)
    else:
        v = 0
        nn += str(v)
print(nn)
