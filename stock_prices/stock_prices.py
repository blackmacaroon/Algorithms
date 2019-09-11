#!/usr/bin/python
#receives a list of stock prices
#returns the max profitt from a single day
#must buy before selling
import argparse

def find_max_profit(prices):
    #the first number in the list, must BUY before SELLing
    current_min_price_so_far = prices[0]
    max_profit_so_far = prices[1] - current_min_price_so_far
    #loop through the array
    #enumerate 
    for i, price in enumerate(prices):
        print(i, price)

    return max_profit_so_far

find_max_profit([1050, 270, 1540, 3800, 2])

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

