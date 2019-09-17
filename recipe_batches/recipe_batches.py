#!/usr/bin/python
#recipes arrive in the form of a dictionary
#ingredients arrive in the form of a dictionary
#both have same form 
# need to return the number of batches that can be made with the supplied ingredienst
import math

def recipe_batches(recipe, ingredients):
  batches = None         #tried initializing batches to zero, it stayed 0 and returned 0 regardless.
  #do we have all the ingredients?
  if len(recipe) > len(ingredients):
      return 0
  #if recipe amount > ingredient amount, return 0
  #loop through both arrays
  for amount in recipe and ingredients:
      #if any ingredient in recipe amount is larger than in ingredients, return 0
      if ingredients[amount] < recipe[amount]:
        return 0
      else:
        temp = ingredients[amount] // recipe[amount]   #flooring division aka integer division (round down to whole number - without remainders)
        if batches is None:       #solves the int None value issue
          batches = temp
        if temp < batches:
          batches = temp
        
      
  return batches
  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 432, 'butter': 248, 'flour': 251 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))