# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/10 15:33:21 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/10 16:06:26 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

print("\033[0m Column vector of shape n * 1\033[0m\033[0m")

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1 * 5
print(v2)

print("\033[0m Expected output:\033[0m\033[0m")
print("\033[0m Vector([[0.0], [5.0], [10.0], [15.0]])\033[0m")
print("\033[0m Row vector of shape 1 * n\033[0m")

v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = v1 * 5
print(v2)


print("\033[0m Expected output\033[0m")
print("\033[0m Vector([[0.0, 5.0, 10.0, 15.0]])\033[0m")

v2 = v1 / 2.0
print(v2)

print("\033[0m Expected output\033[0m")
print("\033[0m Vector([[0.0], [0.5], [1.0], [1.5]])\033[0m")

v1 / 0.0

print("\033[0m Expected ouput\033[0m")
print("\033[0m ZeroDivisionError: division by zero.\033[0m")

2.0 / v1

print("\033[0m Expected output:\033[0m")
print("\033[0m NotImplementedError: Division of a scalar by a Vector is not defined here.\033[0m")
print("\033[0m Column vector of shape (n, 1)\033[0m")
print("Vector([[0.0], [1.0], [2.0], [3.0]]).shape")
print("\033[0m Expected output\033[0m")
print("\033[0m (4,1)\033[0m")
print("Vector([[0.0], [1.0], [2.0], [3.0]]).values")
print("\033[0m Expected output\033[0m")
print("\033[0m [[0.0], [1.0], [2.0], [3.0]]\033[0m")
print("\033[0m Row vector of shape (1, n)\033[0m")
print("Vector([[0.0, 1.0, 2.0, 3.0]]).shape")
print("\033[0m Expected output\033[0m")
print("\033[0m (1,4)\033[0m")
print("Vector([[0.0, 1.0, 2.0, 3.0]]).values")
print("\033[0m Expected output\033[0m")
print("\033[0m [[0.0, 1.0, 2.0, 3.0]]\033[0m")
print("\033[0m Example 1:\033[0m")

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1.shape)
print("\033[0m Expected output:\033[0m")
(4,1)
print(v1.T())
print("\033[0m Expected output:\033[0m")
print("\033[0m Vector([[0.0, 1.0, 2.0, 3.0]])\033[0m")
print(v1.T().shape)
print("\033[0m Expected output:\033[0m")
print("\033[0m (1,4)\033[0m")
print("\033[0m Example 2:\033[0m")
v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v2.shape)
print("\033[0m Expected output:\033[0m")
print("\033[0m (1,4)\033[0m")
print(v2.T())
print("\033[0m Expected output:\033[0m")
print("\033[0m Vector([[0.0], [1.0], [2.0], [3.0]])\033[0m")
print(v2.T().shape)
print("\033[0m Expected output:\033[0m")
print("\033[0m (4,1)\033[0m")
print("\033[0m Example 1:\033[0m")
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
print(v1.dot(v2))
print("\033[0m Expected output:\033[0m")
print("\033[0m 18.0\033[0m")
v3 = Vector([[1.0, 3.0]])
v4 = Vector([[2.0, 4.0]])
print(v3.dot(v4))
print("\033[0m Expected output:\033[0m")
print("\033[0m 13.0\033[0m")
v1
print("\033[0m Expected output: to see what __repr__() should do\033[0m")
print("\033[0m [[0.0, 1.0, 2.0, 3.0]]\033[0m")
print(v1)
print("\033[0m Expected output: to see what __str__() should do\033[0m")
print("\033[0m [[0.0, 1.0, 2.0, 3.0]]\033[0m")