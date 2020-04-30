import math
import random


def find_primes(n):
	"""
	int -> list
	This function returns a list of all primes less than n
	"""
	list_of_primes = list()
	# iterate from 2 to n since 1 is not a prime
	for i in range(2, n):
		# iterate from 2 to i
		for j in range(2, i):
			#if the i mod j is zero it is not a prime
			if(i % j) == 0:
				break
		else:
			# otherwise it is a prime
			list_of_primes.append(i)
	print("There are {} primes. {}".format(len(list_of_primes), list_of_primes))
	return list_of_primes


def fast_powering_alg(x, exp, mod):
	print([x, exp, mod])
	"""
	int, int, int -> int
	This function is supposed to replicate the fast powering algorithm.
	"""
	my_expos = list()
	return_list = list()
	return_val = 1
	i = 1
	# get all of the exponents that is less than or
	# equal to the passed in exponent
	while i <= exp:
		my_expos.append(i)
		i = i * 2
	# sort the list from largest to smallest
	my_expos.reverse()
	# grab the largest value
	largest_val = my_expos[0]
	# remove the largest value
	my_expos.remove(my_expos[0])
	#subtract the largest value from the given exponent
	if(exp == largest_val):
		exp -= my_expos[0]
		return_list.append(my_expos[0])
	else:
		exp -= largest_val
		#add the largest value to the return list
		return_list.append(largest_val)
	#if the largest value is the exponent, calculate the modular arithmetic
	j = 0
	max_index = len(return_list) - 1
	#otherwise find a combonation of numbers that add up to the exponent
	while(exp != 0):
		num = my_expos[j]
		#if the exponent - number is greater than zero
		if(exp - num >= 0):
			exp -= num #subtract from the exponent
			return_list.append(num) # add the number to the return value list
		if(num == my_expos[-1]):
			j = 0
		else:
			j = j + 1
	#iterate through the list and calculate the value 
	for num in return_list:
		return_val *= (x**num) % mod
	return return_val % mod


def gcd_ext(n, x):
	'''
    NB:  x mod(n)
	'''

	if n == 0:
		return x, 0, 1

	gcd, new_s, new_p = gcd_ext(x % n, n)
	s = new_p - (x // n) * new_s
	p = new_s

	return gcd, s, p


def calc_gcd(a, b):
	gcd, s, p = gcd_ext(a, b)
	assert ((p * b + s * a) == gcd)
	return gcd


def calc_inverse(num, mod):
	gcd, s, p = gcd_ext(mod, num)
	assert ((p * num + s * mod) == gcd)
	return p


def calc_gcd2(N):
	''' N = list of numbers
	'''

	a = N[0]
	for i in range(1, len(N)):
		b = N[i]
		a = calc_gcd(a, b)

	return a


def Miller_Rabine_test(p: int, k: int) -> str:
	"""
	:param p: prime > 3 to test
	:param k: number tests to perform to check that p is prime
	:return: string either detailing prime or composite
	"""
	# find d and r such that (2 ** r) * d = p - 1
	d = p - 1
	r = 1
	while d % 2 == 0:
		r +=1
		d = d / 2

	# number of random integers (a) we will test to check is p is prime
	for item in range(k):
		a = random.randint(1,p -1)
		while True:
			x = fast_powering_alg(a, d, p)
			if x == 1 or x == p - 1:
				break
			else:
				caller = False
				for i in range(r -1):
					x = fast_powering_alg(x, 2, p)
					if x == 1:
						caller = True
				if caller:
					break
			return "composite"
	return "probably prime"


def remainder(x, m):
  k = len(m)
  
  # Compute the product of the divisors (n1.n2.n3....nk)
  M = 1
  for i in range(k):
    M *= m[i]

  # Solution X
  X = 0
  for i in range(k):
    M_i = M / m[i]

    # Find the inverse N_i
    N_i = calc_inverse(M_i, m[i])

    X += x[i] * N_i * M_i
	#return fast_powering_alg(X,1,M)
  return X % M_i


def main():
	# question 1
	find_primes(100)
	# question 2
	#fast_powering_alg(76, 2, )

	# question 3

	# x (mod n) 197189 (mod 999979)
	x = 197189
	n = 999979
	inverse = calc_inverse(x, n)
	print("inverse of {} (mod {}) is {}".format(x, n, inverse))
	a = 2 ** 1000 - 299
	b = math.factorial(1000) + 98
	gcd = calc_gcd(a, b)
	print("gcd( 2^1000 - 299 , 1000! + 98 ): {}".format(gcd))

	#  gcd for a, b, c, d, e
	N = [887519, 146744, 388025, 880464, 189074]
	gcd = calc_gcd2(N)
	print("gcd( {} , {} , {} , {} ,  {}): {}".format(N[0], N[1], N[2], N[3], N[4], gcd))

	# question 4

	# check that 1223 is prime
	prime = 7177
	num_tests = 10
	r = Miller_Rabine_test(prime, num_tests)
	print("Miller-Rabine algorithm with {} tests states that {} is {}.".format(num_tests, prime, r))

	# check that 561 is not prime
	prime = 561
	num_tests = 10
	r = Miller_Rabine_test(prime, num_tests)
	print("Miller-Rabine algorithm with {} tests states that {} is {}.".format(num_tests, prime, r))

	# qustion 5
    # wikipedia example
	n = [3, 4, 5]

	a = [2, 3, 1]


	x = remainder(a, n)
	print("Chinese Remainder thm:\nList X = {}\nList M = {}\nOutput: {}".format(a,n,x))

if __name__ == '__main__':
	main()
