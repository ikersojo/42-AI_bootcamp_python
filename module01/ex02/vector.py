# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/10 16:05:46 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/20 22:35:09 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
	def __init__(self, values):
		if (type(values) == list):
			self.values = values
			if (len(values) == 1):
				self.shape = (1, len(values[0])) # row: list of a list of several floats: [[1., 2., 3.]]
				self.size = len(values[0])
			else:
				self.shape = (len(values), 1) # col: list of lists of single float: [[1.], [2.], [3.]]
				self.size = len(values)
		elif (type(values) == int):
			self.size = values
			self.values = []
			for i in range (0, 3):
				self.values.append([float(i)])
			self.shape = (values, 1)
		elif (type(values) == tuple):
			if (values[0] >= values[1]):
				print ("Error: Range not in ascending order.")
			else:
				self.size = values[1] - values[0]
				self.shape = (self.size, 1)
				self.values = []
				for i in range (values[0], values[1]):
					self.values.append([float(i)])
				
	def __str__(self):
		return "This is a Vector."
	
	def dot(self, other):
		res = 0
		if (self.shape == other.shape):
			if (len(self.values) == 1):
				i = 0
				while (i < self.size):
					res += self.values[0][i] * other.values[0][i]
					i += 1
			else:
				i = 0
				while (i < self.size):
					res += self.values[i][0] * other.values[i][0]
					i += 1
		else:
			print("Not the same shape. Returning 0.")
		return res

	def T(self):
		res = []
		if (len(self.values) == 1):
			for val in self.values[0]:
				res.append([val])
			res = Vector(res)
		else:
			for val in self.values:
				res.append(val[0])
			res = [res]
			res = Vector(res)
		return res
	
	def	__add__(self, other):
		if (self.shape == other.shape):
			res = []
			if (len(self.values) == 1):
				for i in range (0, self.size):
					res.append([self.values[0][i] + other.values[0][i]])
				res = Vector(res).T()
			else:
				for i in range (0, self.size):
					res.append([self.values[i][0] + other.values[i][0]])
				res = Vector(res)
			return res
		else:
			print("Not the same shape. Returning 0.")

	def	__sub__(self, other):
		if (self.shape == other.shape):
			res = []
			if (len(self.values) == 1):
				for i in range (0, self.size):
					res.append([self.values[0][i] - other.values[0][i]])
				res = Vector(res).T()
			else:
				for i in range (0, self.size):
					res.append([self.values[i][0] - other.values[i][0]])
				res = Vector(res)
			return res
		else:
			print("Not the same shape. Returning 0.")

	def	__mul__(self, other):
		if (type(other) == int or type(other) == float):
			res = []
			if (len(self.values) == 1):
				for i in range (0, self.size):
					res.append([self.values[0][i] * other])
				res = Vector(res).T()
			else:
				for i in range (0, self.size):
					res.append([self.values[i][0] * other])
				res = Vector(res)
			return res
		else:
			raise NotImplementedError

	def	__truediv__(self, other):
		if (type(other) == int or type(other) == float):
			res = []
			if (len(self.values) == 1):
				for i in range (0, self.size):
					res.append([self.values[0][i] / other])
				res = Vector(res).T()
			else:
				for i in range (0, self.size):
					res.append([self.values[i][0] / other])
				res = Vector(res)
			return res
		else:
			raise NotImplementedError

# 	def	__mul__(self, scalar):
# 		new_vector = []
# 		if len(self.values) == 1:
# 			for i in range(len(self.values[0])):
# 				new_vector.append(self.values[0][i]*scalar)
# 			mul_res = instantiate([new_vector])
# 		else:
# 			for i in range(len(self.values)):
# 				new_vector.append([self.values[i][0]*scalar])
# 			mul_res = instantiate(new_vector)
# 		return mul_res

# 	def	__truediv__(self, scalar):
# 		new_vector = []
# 		if len(self.values) == 1:
# 			for i in range(len(self.values[0])):
# 				new_vector.append(round(self.values[0][i]/scalar, 2))
# 			mul_res = instantiate([new_vector])
# 		else:
# 			for i in range(len(self.values)):
# 				new_vector.append([round(self.values[i][0]/scalar, 2)])
# 			mul_res = instantiate(new_vector)
# 		return mul_res


if(__name__ == "__main__"):
	print("\033[33mStarting test:\033[0m")

	# Checking Vector class assignation:
	print("\n\033[33m    - Checking Vector class assignation:\033[0m")
	v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
	v2 = Vector([[1.0], [1.0], [1.0], [1.0]])
	print (v1.values, v1.shape)
	print (v2.values, v2.shape)
	v10 = Vector(3)
	v11 = Vector((10, 16))
	print (v10.values, v10.shape)
	print (v11.values, v11.shape)

	# Checking dot method:
	print("\n\033[33m    - Checking dot method:\033[0m")
	v3 = Vector([[0.0, 1.0, 2.0, 3.0]])
	v4 = Vector([[1.0], [1.0], [1.0], [1.0]])
	print(v1.dot(v3))
	print(v2.dot(v4))

	# Checking Transpose method:
	print("\n\033[33m    - Checking Transpose method:\033[0m")
	print (v1.values, v1.shape)
	vx = v1.T()
	print (vx.values, vx.shape)
	print("-----------")
	print (v2.values, v2.shape)
	vz = v2.T()
	print (vz.values, vz.shape)

	# Checking addition method:
	print("\n\033[33m    - Checking addition method:\033[0m")
	print (v1.values, v1.shape)
	print (v3.values, v3.shape)
	vy = v1 + v3
	print (vy.values, vy.shape)
	print("-----------")
	print (v2.values, v2.shape)
	print (v4.values, v4.shape)
	va = v2 + v4
	print (va.values, va.shape)
	print("-----------")
	vb = v1 + v2

	# Checking substraction method:
	print("\n\033[33m    - Checking substraction method:\033[0m")
	print (v1.values, v1.shape)
	print (v3.values, v3.shape)
	vys = v1 - v3
	print (vys.values, vys.shape)
	print("-----------")
	print (v2.values, v2.shape)
	print (v4.values, v4.shape)
	vas = v2 - v4
	print (vas.values, vas.shape)
	print("-----------")
	vbs = v1 - v2

	# Checking multiplication method:
	print("\n\033[33m    - Checking multiplication method:\033[0m")
	print (v1.values, v1.shape)
	vym = v1 * 5
	print (vym.values, vym.shape)
	print("-----------")
	print (v2.values, v2.shape)
	vam = v2 * 3
	print (vam.values, vam.shape)
	print("-----------")
	print (v1.values, v1.shape)
	print (v3.values, v3.shape)
	try:
		vbm = v1 * v3
	except:
		print("Error")

	# Checking division method:
	print("\n\033[33m    - Checking division method:\033[0m")
	print (v1.values, v1.shape)
	vym = v1 / 5
	print (vym.values, vym.shape)
	print("-----------")
	print (v2.values, v2.shape)
	vam = v2 / 2
	print (vam.values, vam.shape)
	print("-----------")
	print (v1.values, v1.shape)
	print (v3.values, v3.shape)
	try:
		vbm = v1 / v3
	except:
		print("Error")
