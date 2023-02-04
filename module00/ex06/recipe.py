# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/04 09:15:13 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/04 11:11:29 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

sandwich = {
	"ingredients": ["ham", "bread", "cheese", "tomatoes"],
	"meal": "lunch",
	"prep_time": 10
}

cake = {
	"ingredients": ["flour", "sugar", "eggs"],
	"meal": "dessert",
	"prep_time": 60
}

salad = {
	"ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
	"meal": "lunch",
	"prep_time": 15
}

cookbook = {
	"sandwich": sandwich,
	"cake": cake,
	"salad": salad
}

def add(cookbook):
	name = input(">>> Enter a name:\n")
	ingr = input(">>> Enter ingredients:\n")

def print_recipe(name):
	print(f"Recipe for {name}:")
	i = cookbook[name]["ingredients"]
	m = cookbook[name]["meal"]
	p = cookbook[name]["prep_time"]
	print(f"    Ingredients list: {i}")
	print(f"    To be eaten for {m}.")
	print(f"    Takes {p} minutes of cooking.")

def print_all(cookbook):
	for key, value in cookbook.items():
		print_recipe(key)
		print("\n------------------\n")

if (__name__ == "__main__"):
	# print_recipe(sys.argv[1])
	print_all(cookbook)
