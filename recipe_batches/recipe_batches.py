#!/usr/bin/python
#recipes arrive in the form of a dictionary
#ingredients arrive in the form of a dictionary
#both have same form 
# need to return the number of batches that can be made with the supplied ingredienst
import math

def recipe_batches(recipe, ingredients):
  batches = None
  #do we have all the ingredients?
  if len(recipe) > len(ingredients):
      return 0
  #if recipe amount > ingredient amount, return 0
  #loop through both arrays
  for amount in recipe and ingredients:
      #if any ingredient in recipe amount is larger than in ingredients, return 0
      if batches == None or ingredients[amount] // recipe[amount] < batches:
        batches = ingredients[amount] // recipe[amount]
      else:
        return 0
      
  return batches
  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))