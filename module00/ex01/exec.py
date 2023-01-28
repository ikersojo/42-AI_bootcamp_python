# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/28 17:47:14 by isojo-go          #+#    #+#              #
#    Updated: 2023/01/28 22:58:04 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (len(sys.argv) >= 2):
	string = sys.argv[1]
	i = 2
	while (i < len(sys.argv)):
		string += ' '
		string += sys.argv[i]
		i += 1

	rev = ''
	i = len(string) - 1
	while (i >= 0):
		if (string[i].islower()):
			rev += string[i].upper()
		else:
			rev += string[i].lower()
		i -= 1

	print(rev)
