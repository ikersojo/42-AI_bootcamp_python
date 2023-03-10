# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/09 22:39:55 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/12 20:44:48 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# With input error control:
# class Recipe:
# 	'''Recipe Class. Recipe(name, lvl, time, ingredients, type, description)'''
# 	def __init__(self, name, lvl, time, ingr, type, descr = 'Not available.'):
# 		self.name = name
# 		try:
# 			int(lvl)
# 			if(lvl >= 1 and lvl <= 5):
# 				self.lvl = lvl
# 			else:
# 				self.lvl = 1
# 				print(f"\033[31mLevel out of range in {name}. Defaulted to 1.\033[0m")
# 		except:
# 			self.lvl = 1
# 			print(f"\033[31mLevel out of range in {name}. Defaulted to 1.\033[0m")
# 		self.time = time
# 		self.ingr = ingr
# 		if (type == "starter" or type == "lunch" or type == "dessert"):
# 			self.type = type
# 		else:
# 			print("\033[31mType not valid. Defaulted to 'lunch'.\033[0m")
# 			self.type = "lunch"
# 		self.descr = descr

class Recipe:
	'''Recipe Class. Recipe(name, lvl, time, ingredients, type, description)'''
	name = str
	lvl = int
	time = int
	ingr = [str]
	type = str
	descr = str

	def __init__(self, name, lvl, time, ingr, type, descr = 'Not available.'):
		self.name = name
		self.lvl = lvl
		self.time = time
		self.ingr = ingr
		self.type = type
		self.descr = descr

	def __str__(self):
		txt = "This is the Recipe Class"
		return txt
	
	def print_recipe(self):
		print("\033[90m")
		print(f"\nRecipe name: {self.name}")
		print(f"    Level: {self.lvl}")
		print(f"    Time: {self.time}")
		print(f"    Ingredients: {self.ingr}")
		print(f"    Type: {self.type}")
		print(f"    Description: {self.descr}\n")
		print("\033[0m")

if (__name__ == '__main__'):
	print("\033[33mbuilt-in test...\033[0m")
	test1 = Recipe("test1", 5, 60, ["asd", "zxc", "wer"], "lunch", "hi!")
	test1.print_recipe()
	print(str(test1))
	print(test1.__doc__)
	test2 = Recipe("test2", 1, 60, ["asd", "zxc", "wer"], "lunch")
	test2.print_recipe()
	test3 = Recipe("test3", 2, 60, ["asd", "zxc", "wer"], "dessert")
	test3.print_recipe()
	test4 = Recipe("test4", 3, 60, ["asd", "zxc", "wer"], "starter")
	test4.print_recipe()
