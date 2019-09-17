#!/usr/bin/python
# "all possible permutations" means we need RECURSION
import sys

def rock_paper_scissors(n):
  #list my choices, strings 
  #new empty list for lists of strings
  draw = ["rock", "paper", "scissors"]
  sequence = []


  #recursive funtction calls itself until base case is met
  def rps_recursion(n, arr)  #what does it take in?
    if n == 0:   #base case, define the moment we want it to stop
      return sequence



  return sequence
  #return list of lists (with a length of n) containing strings


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')