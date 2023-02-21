# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/20 23:36:56 by isojo-go          #+#    #+#              #
#    Updated: 2023/02/20 23:59:16 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class	Evaluator:
	def	__init__(self, words, coefs):
		self.words = words
		self.coefs = coefs

	@staticmethod
	def	input_ok(coefs, words) -> bool:
		if type(coefs) != list or type(words) != list or len(coefs) != len(words):
			return False
		return True

	@staticmethod
	def	zip_evaluate(coefs, words):
		if type(coefs) != list or type(words) != list or len(coefs) != len(words):
			return -1
		lst = list(zip(coefs, words))
		res = 0
		for i in range(0, len(lst)):
			res += lst[i][0] * len(lst[i][1])
		return res

	@staticmethod
	def	enumerate_evaluate(coefs, words):
		if type(coefs) != list or type(words) != list or len(coefs) != len(words):
			return -1
		lst = list(enumerate(words))
		res = 0
		for i in range(0, len(lst)):
			res += coefs[lst[i][0]] * len(lst[i][1])
		return res

		

if (__name__ == "__main__"):
	words = ["Le", "Lorem", "Ipsum", "est", "simple"]
	coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
	print(Evaluator.zip_evaluate(coefs, words))
	print(Evaluator.enumerate_evaluate(coefs, words))

	coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
	print(Evaluator.zip_evaluate(coefs, words))
	print(Evaluator.enumerate_evaluate(coefs, words))