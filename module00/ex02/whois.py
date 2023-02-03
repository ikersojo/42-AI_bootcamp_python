# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 09:24:35 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/03 10:05:15 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if(len(sys.argv) > 2):
	print("AssertionError: more than one argument are provided")
elif (len(sys.argv) == 2):
	try:
		n = int(sys.argv[1])
	except:
		print("AssertionError: argument is not an integer")
	else:
		if (n == 0):
			print("I'm Zero.")
		elif (n % 2 == 0):
			print("I'm Even.")
		else:
			print("I'm Odd.")
