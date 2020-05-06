import math
import random

def find_inverse(a, N):
	"""
	int, int -> int
	find the inverse of some a modulo N
	"""
	i = 1
	while(True):
		if((a*i) % N == 1):
			return i
		i += 1

def shanks_alg(a, b, N, k):
	"""
	int, int ,int, int -> int
	This function is meant to solve the discrete
	logarithm problem using shanks algorithm.
	"""
	a_dict = dict()
	a_list = list()
	b_dict = dict()
	num_to_check = -1
	i = 1
	r = 1
	#find the inverse of a
	a_inverse = find_inverse(a, N)
	#calculate a^-k modulo N
	a_k_inverse = (a_inverse ** k) % N
	#find all the powers of a to the i mod N while i
	#is less than the random number k
	while(i < k):
		a_dict[i] = ((a**i)%N)
		#add to the list
		a_list.append((a**i)%N)
		i += 1
	#while rk is not greater than N
	#we want to compute a^(-rk)
	while(r*k <= N):
		#since we know a^-1
		#solve for a^-rk mod N
		k_inv = (a_k_inverse ** r) % N
		#we calculate b(a)^-rk mod N
		num_to_check = (b * k_inv) % N
		#create a key rk for a unique r
		#have the value be b(a)^-rk mod N
		b_dict[r*k] = num_to_check
		#if this number is in the list of a^i mod N
		#break out of the loop and check the powers
		if(num_to_check in a_list):
			break
		r += 1
	#check
	#iterate through all the keys in the a^i mod N dict
	#if the value of that key is the value of the number we are checking
	for key in a_dict:
		if(a_dict[key] == num_to_check):
			#calculate the power by adding exponents
			power = ((key + (r*k)))
			#check if a^x is congruent to b mod N
			if(a**power % N == b):
				#if so return the power and print the answer
				print("Answer: {} ^ {} % {} = {} ".format(a, power, N, b))
				return power
	#no answer
	return -1

def main():
	num = shanks_alg(2, 1, 5, 1)
	print(num)

main()
