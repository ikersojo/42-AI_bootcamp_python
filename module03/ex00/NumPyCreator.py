# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NumPyCreator.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/02 21:47:34 by codespace         #+#    #+#              #
#    Updated: 2023/03/03 12:59:01 by isojo-go         ###   ########.fr        #
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
	npc = NumpyCreator()

	print(npc.from_list([[1,2,3],[6,3,4]]))
	print("      --> Expected result: array([[1, 2, 3],")
	print("                                  [6, 3, 4]])")
	

	# print(npc.from_list([[1,2,3],[6,4]]))
	# print("      --> Expected result: None")


	# print(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]))
	# print("      --> Expected result: array([['1','2','3'],")
	# print("                                  ['a','b','c'],")
	# print("                                  ['6','4','7'], dtype='<U21'])")

	# print(npc.from_list(((1,2),(3,4))))
	# print("      --> Expected result: None")

	
	# print(npc.from_tuple(["a", "b", "c"]))
	# print("      --> Expected result: array(['a', 'b', 'c'])")


	# print(npc.from_iterable(range(5)))
	# print("      --> Expected result: array([0, 1, 2, 3, 4])")


	# shape=(3,5)
	# print(npc.from_shape(shape))
	# print("      --> Expected result: array([[0, 0, 0, 0, 0],")
	# print("                                  [0, 0, 0, 0, 0],")
	# print("                                  [0, 0, 0, 0, 0]])")
	

	# print(npc.random(shape))
	# print("      --> Expected result: array([[0.57055863, 0.23519999, 0.56209311, 0.79231567, 0.213768 ],")
	# print("                                  [0.39608366, 0.18632147, 0.80054602, 0.44905766, 0.81313615],")
	# print("                                  [0.79585328, 0.00660962, 0.92910958, 0.9905421 , 0.05244791]])")
	
	
	# print(npc.identity(4))
	# # Output :
	# print("      --> Expected result: array([[1., 0., 0., 0.],")
	# print("                                  [0., 1., 0., 0.],")
	# print("                                  [0., 0., 1., 0.],")
	# print("                                  [0., 0., 0., 1.]])")
