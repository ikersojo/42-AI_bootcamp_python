# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NumPyCreator.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/02 21:47:34 by codespace         #+#    #+#              #
#    Updated: 2023/03/04 12:20:06 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class NumpyCreator():
	def try_func(func):
		def decorator(*args, **kwargs):
			try:
				return func(*args, **kwargs)
			except:
				return None
		return decorator

	@try_func
	def from_list(self, lst):
		if type(lst) is not list:
			return None
		return np.array(lst).__repr__() #not identical ] vs. ]]

	@try_func
	def from_tuple(self, tpl):
		if type(tpl) is not tuple:
			return None
		return np.array(tpl).__repr__() #not identical with or without .__repr__()

	@try_func
	def from_iterable(self, itr):
		if not hasattr(itr, '__iter__'):
			return None
		return np.array(itr).__repr__()

	@try_func
	def from_shape(self, shape, value=None):
		if value == None:
			return np.zeros(shape)
		else:
			return np.array(value).reshape(shape).__repr__()

	@try_func
	def random(self, shape):
		pass

	@try_func
	def identity(self, n):
		pass

if __name__ == '__main__':
	npc = NumpyCreator()

	print(npc.from_list([[1,2,3],[6,3,4]]))
	print("      --> Expected result: array([[1, 2, 3],")
	print("                                  [6, 3, 4]])")
	

	print(npc.from_list([[1,2,3],[6,4]]))
	print("      --> Expected result: None")


	print(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]))
	print("      --> Expected result: array([['1','2','3'],")
	print("                                  ['a','b','c'],")
	print("                                  ['6','4','7'], dtype='<U21'])")


	print(npc.from_list(((1,2),(3,4))))
	print("      --> Expected result: None")

	
	print(npc.from_tuple(("a", "b", "c")))
	print("      --> Expected result: array(['a', 'b', 'c'])")


	print(npc.from_iterable(range(5)))
	print("      --> Expected result: array([0, 1, 2, 3, 4])")


	shape=(3,5)
	print(npc.from_shape(shape))
	print("      --> Expected result: array([[0, 0, 0, 0, 0],")
	print("                                  [0, 0, 0, 0, 0],")
	print("                                  [0, 0, 0, 0, 0]])")
	

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
