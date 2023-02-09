# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/09 22:39:59 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/09 22:48:03 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe


test = Recipe("test1", 15, 60, ["asd", "zxc", "wer"], "xxx", "lunch")
print(str(test))
print(test.name)
print(test.cooking_lvl)
print(test.cooking_time)
print(test.ingredients)
print(test.description)
print(test.recipe_type)