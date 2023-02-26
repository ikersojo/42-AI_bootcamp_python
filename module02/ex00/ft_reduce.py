# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/22 11:57:30 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/22 12:05:23 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_reduce(function_to_apply, iterable):
"""Apply function of two arguments cumulatively.
Args:
function_to_apply: a function taking an iterable.
iterable: an iterable object (list, tuple, iterator).
Return:
A value, of same type of elements in the iterable parameter.
None if the iterable can not be used by the function.
"""
# ... Your code here ..