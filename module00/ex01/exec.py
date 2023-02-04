# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 13:32:50 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/04 09:17:59 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (len(sys.argv) >= 2):
	# string = sys.argv[1]
	# i = 2
	# while (i < len(sys.argv)):
	# 	string += ' '
	# 	string += sys.argv[i]
	# 	i += 1

	string = " ".join(sys.argv[1::])

	# rev = ''
	# i = len(string) - 1
	# while (i >= 0):
	# 	if (string[i].islower()):
	# 		rev += string[i].upper()
	# 	else:
	# 		rev += string[i].lower()
	# 	i -= 1

	rev = string[::-1].swapcase()

	print(rev)
	
