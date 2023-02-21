# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/20 22:37:31 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/20 23:35:52 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randint

def shuffle(array):
	out = []
	it = len(array)
	print (it)
	i = 0
	while (i < (it - 1)):
		item = randint(0, it - 1 - i)
		out.append(array[item])
		array.pop(item)
		i += 1
	out.append(array[0])
	return out

def unique(array):
	out = []
	it = len(array)
	for i in (0, it - 1):
		item = randint(0, it - 1 - i)
		print (item)
		print (i)
		out.append(array[item])
		array.pop(item)
	out.append(array[0])
	return out

def	generator(text, sep=" ", option=None):
	'''Splits the text according to sep value and yield the substrings.'''
	if (type(text) != str):
		return "ERROR"
	valid_options = ("shuffle", "unique", "ordered")
	if (option != None and option not in valid_options):
		return "ERROR"
	array = text.split(sep)
	if (option == "shuffle"):
		array = shuffle(array)
	elif (option == "unique"):
		array = set(array)
	elif (option == "ordered"):
		array = sorted(array)
	for elem in array:
		yield elem


if (__name__ == "__main__"):
	print (generator.__doc__)
	text = "zz hola muchos amigos mios soys los zz mejores"
	for word in generator(text, sep=" ", option="unique"):
		print (word);
