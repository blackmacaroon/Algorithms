#!/usr/bin/python
# receives a list of stock prices
# returns the max profitt from a single day
# must buy before selling
import argparse


def find_max_profit(prices):
    # the first number in the list, must BUY before SELLing
    min_price = prices[0]
    max_profit = prices[1] - min_price
    # loop through the array
    # enumerate() starts at 0 and attaches an automatic counter while it iterated through a loop!!!
    for i, price in enumerate(prices):
        # print(i, price)
        # skip i = 0 (the first index), must buy before selling. start with a negative number
        # if the price minus the min price (first number after BUY) is greater than profit, it becomes the max_profit, if the price is less than the min_price, it becomes the min_price
        if i != 0:
            if price - min_price > max_profit:
                max_profit = price - min_price
            if price < min_price:
                min_price = price
    return max_profit

# find_max_profit([1050, 270, 1540, 3800, 2])

if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an integer price"
    )
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers), prices=args.integers
        )
    )

