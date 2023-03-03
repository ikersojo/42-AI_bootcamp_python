# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NumPyCreator.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: codespace <codespace@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/02 21:47:34 by codespace         #+#    #+#              #
#    Updated: 2023/03/03 09:40:17 by codespace        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class NumPyCreator():
	def from_list(self, lst):
		return np.array(lst)

	def from_tuple(self, lst):
		pass

	def from_iterable(self, lst):
		pass

	def from_shape(self, lst):
		pass

	def random(self, n):
		pass

	def identity(self, shape):
		pass

if __name__ == '__main__':
	print('hola mundo')