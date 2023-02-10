# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/10 16:05:46 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/10 16:05:49 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
	def __init__(self, values):
		self.values = values
		if (len(values) == 1):
			self.shape = (1, len(values[0])) # row: list of a list of several floats: [[1., 2., 3.]]
		else:
			self.shape = (len(values), 1) # col: list of lists of single float: [[1.], [2.], [3.]]
	
	# def dot(self, other):
	# 	if (self.shape == other.shape):

	# def T(self):
		



if(__name__ == "__main__"):
	print("\033[33mtesting...\033[0m")
	v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
	v2 = Vector([[0.0], [1.0], [2.0], [3.0]])
	print(v1.shape)
	print(v2.shape)