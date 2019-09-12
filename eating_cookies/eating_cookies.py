#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
#look at the ways to eat n-1 cookies, then eat 1 more
# look at the ways to eat n-2 cookies, then eat 2 more
#  look at the ways to eat n-3 cookies, then eat 3 more
e_l_fudge = 8
cache = {0: 0, 1: 1, 2: 2}

def eating_cookies(n, cache=None):
  # fibonacci
  if cache is not None and n in cache:
    return cache[n]
  if n == 0:
    return 1
  elif n < 3:
    return n
  else: 
    value = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    
    return value[n]

print("mmmmm", eating_cookies(e_l_fudge))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')