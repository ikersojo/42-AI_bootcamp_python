# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 16:48:24 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/03 16:52:13 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

print(f"module_{kata[0]:02d}, ex_{kata[1]:02d} : {kata[2]:.2f}, {kata[3]:.2e}, {kata[4]:.2e}")