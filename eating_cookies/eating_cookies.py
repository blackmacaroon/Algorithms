#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
#how many ways can cookie monster eat n cookies, if he can eat no more than three at a time
#look at the ways to eat n-1 cookies, then eat 1 more
# look at the ways to eat n-2 cookies, then eat 2 more
#  look at the ways to eat n-3 cookies, then eat 3 more
# e_l_fudge = 35
# def eating_cookies(n, cache=None):
#   # fibonacci
#   if cache is None:
#     cache = {}
#   if n == 0:
#     return 1
#   if n < 3:
#     return n
#   if cache and n in cache >0:
#     return cache[n] 
#   else:
#     cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
#     return cache[n]
    

# print("mmmmm", eating_cookies(e_l_fudge))

e_l_fudge = 38
# cookie_cache = {}
def eating_cookies(n, cookie_cache={}):
  #couldnt find a way to make cache=None work
  # fibonacci
  if n == 0:
    return 1
  if n < 3:
    return n
  if cookie_cache and cookie_cache[n] >=3:
    return cookie_cache[n] 
  else:
    cookie_cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    return cookie_cache[n]
  
# tried with empty cache and one argument in the function, but that causes TypeError File "test_eating_cookies.py", line 14, in test_eating_cookies_large_n
#     self.assertEqual(eating_cookies(50, [0 for i in range(51)]), 10562230626642)
# TypeError: eating_cookies() takes exactly 1 argument (2 given)
    

print("mmmmm", eating_cookies(e_l_fudge))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')