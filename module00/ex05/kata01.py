# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 16:27:41 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/03 16:37:04 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata01.py file
kata = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
	}

for key, value in kata.items():
	print(f"{key} was created by {value}" )
	