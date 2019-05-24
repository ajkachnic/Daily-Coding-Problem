"""
This problem was asked by Bloomberg.

There are N prisoners standing in a circle, waiting to be executed. The executions are carried 
out starting with the kth person, and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a 
prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.
"""

def prisonercircle(N, k):
    prisonerlist = list()
    overN = 1
    kth = 0
    for _ in range(0, N * k):
      if kth == 0:
        if k + _ <= N:
          prisonerlist.append(k + _)
        else:
          prisonerlist.append(overN)
          overN += 1
        kth += 1
      else:
        if kth  + 1 == k:
          kth = 0
    return prisonerlist[len(prisonerlist) - 1]
