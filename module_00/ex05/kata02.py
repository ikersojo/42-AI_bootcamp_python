# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 20:34:14 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/14 22:35:35 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

yyyy, mm, dd, h, m = kata
print(f"{dd:02d}/{mm:02d}/{yyyy:04d} {h:02d}:{m:02d}")