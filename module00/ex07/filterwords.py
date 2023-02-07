# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/06 19:11:03 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/07 18:26:10 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (__name__ == "__main__"):
	if (len(sys.argv) == 3):
		try:
			s = sys.argv[1]
			n = int(sys.argv[2])
		except:
			print("ERROR")
		s = s.replace(',', '')
		s = s.replace('.', '')
		s = s.replace(';', '')
		s = s.replace(':', '')
		s = s.replace('!', '')
		s = s.replace('?', '')
		words = s.split()
		i = 0
		for word in words:
			if (len(word) <= n):
				words.pop(i)
			i += 1
		print(words)
	else:
		print("ERROR")
