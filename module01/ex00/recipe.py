# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/09 22:39:55 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/09 22:54:33 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe:
	'''Recipe Class. Recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)'''
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

	def __str__(self):
		txt = "Recipe Class"
		return txt
	
	def print_recipe(self):
		print(f"Recipe name: {test.name}")
		print(f"    Level: {test.cooking_lvl}")
		print(f"    Time: {test.cooking_time}")
		print(f"    Ingredients: {test.ingredients}")
		print(f"    Description: {test.description}")
		print(f"    Type: {test.recipe_type}")


if (__name__ == '__main__'):
	test = Recipe("test1", 15, 60, ["asd", "zxc", "wer"], "xxx", "lunch")
	test.print_recipe()