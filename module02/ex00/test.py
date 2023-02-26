# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/22 11:59:32 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/22 12:05:23 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Example 1:
print("\033[33m- Example 1:\033[0m")
print("\033[33m    x = [1, 2, 3, 4, 5]\033[0m")
print("\033[33m    ft_map(lambda dum: dum + 1, x)\n\033[0m")
print("\033[33m    Expected Output:\033[0m")
print("\033[33m    <generator object ft_map at 0x7f708faab7b0> # The adress will be different\033[0m")

x = [1, 2, 3, 4, 5]
ft_map(lambda dum: dum + 1, x)


# Example 2:
list(ft_map(lambda t: t + 1, x))
# Output:
[2, 3, 4, 5, 6]
# Example 2:
ft_filter(lambda dum: not (dum % 2), x)
# Output:
<generator object ft_filter at 0x7f709c777d00> # The adress will be different




list(ft_filter(lambda dum: not (dum % 2), x))
# Output:
[2, 4]
# Example 3:
lst = [’H’, ’e’, ’l’, ’l’, ’o’, ’ ’, ’w’, ’o’, ’r’, ’l’, ’d’]
ft_reduce(lambda u, v: u + v, lst)
# Output:
"Hello world