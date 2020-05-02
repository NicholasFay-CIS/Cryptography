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
		for j in list_of_primes:
			# if the i mod j is zero it is not a prime
			if(i % j) == 0:
				break
		else:
			# otherwise it is a prime
			list_of_primes.append(i)
			# print(list_of_primes)
	print("There are {} primes. {}".format(len(list_of_primes), list_of_primes))
	return list_of_primes


def fast_powering_alg(x, exp, mod):
	"""
	int, int, int -> int
	This function is supposed to replicate the fast powering algorithm.
	"""
	my_expos = list()
	calculated_list = list()
	return_list = list()
	calculated_dict = dict()
	return_val = 1
	i = 1
	j = 0
	while i <= exp:
		if(i == 1):
			val = x
		else:
			val = ((calculated_list[-1] * calculated_list[-1]) % mod)
		calculated_dict[i] = val
		calculated_list.append(val)
		my_expos.append(i)
		i *=  2
	my_expos.reverse()
	largest_val = my_expos[0]
	my_expos.remove(my_expos[0])
	if(exp == largest_val):
		exp -= my_expos[0]
		return_list.append(my_expos[0])
	else:
		exp -= largest_val
		return_list.append(largest_val)
	while(exp != 0):
		num = my_expos[j]
		if(exp - num >= 0):
			exp -= num
			return_list.append(num)
		if(num == my_expos[-1]):
			j = 0
			continue
		j = j + 1
	for power in calculated_dict.keys():
		if(power in return_list):
			return_val *= (calculated_dict[power])
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


def Miller_Rabin_test(n, k):
	"""
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
	# find r, d such that n-1 = 2**r*d
	r = 0
	d = n - 1
	while d % 2 == 0:
		d >>= 1
		r += 1
	# check they're equal
	assert (2 ** r * d == n - 1)

	# function testing if a**d, a**2d, ... , a**rd is equal to 1 (mod n) or n-1(mod n)
	def test_composite(a):
		if pow(a, d, n) == 1:
			return False
		for i in range(r):
			if pow(a, 2 ** i * d, n) == n - 1:
				return False
		return True

	# runs through the test_composite function k times to check
	# different bases. The greater k is the more likely n
	# is to be prime
	for i in range(k):  # number of trials
		a = random.randrange(2, n)
		is_composite = test_composite(a)
		if is_composite:
			return False

	return True


def generate_prime(b, k):
	while True:
		bottom_range, top_range = 2**(b-1), (2**b)-1
		n = random.randrange(bottom_range + 1, top_range, 2)
		if Miller_Rabin_test(n, k):
			break
	return n


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


def prime_factors(s, n):
	while (n % 2 == 0):
		s.add(2)
		n = n // 2
	# n must be odd at this point. So we can
	# skip one element (Note i = i +2)
	square_root = int(math.sqrt(n))
	list_primes = find_primes(square_root)
	for i in list_primes:
		while (n % i == 0):
			s.add(i)
			n = n // i
		# This condition is to handle the case
	# when n is a prime number greater than 2
	if (n > 2):
		s.add(n)


def primitive_root(n):
	s = set()
	phi = n - 1
	prime_factors(s, phi)
	for r in range(2, phi + 1):
		flag = False
		for it in s:
			# Check if r^((phi)/primefactors)
			# mod n is 1 or not
			if (pow(r, phi // it, n) == 1):
				flag = True
				break
		# If there was no power with value 1.
		if (flag == False):
			return r


def main():
	# question 1
	print("Question 1")
	find_primes(100)
	find_primes(367400)
	print()



	# question 2
	print("Question 2:")
	base = 2
	exp = 10
	exp2 = 15
	mod = 100000
	fp = (10 ** 15)
	fp2 = fast_powering_alg(base, fp, mod)
	print("{}^({}^{}) (mod {}) = {}".format(base, exp, exp2, mod, fp2))
	print()



	# question 3
	print("Question 3:")

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
	print()



	# question 4
	print("Question 4:")
	# check that 5915587277 is prime
	prime = 5915587277
	num_tests = 10
	r = Miller_Rabin_test(prime, num_tests)
	print("Miller-Rabin with {} tests. Is {} prime? {}".format(num_tests, prime, r))
	# check that 561 is not prime
	prime = 561
	num_tests = 10
	r = Miller_Rabin_test(prime, num_tests)
	print("Miller-Rabin with {} tests. Is {} prime? {}".format(num_tests, prime, r))
	# generate prime over 1000 bits (302 digits)
	bits = 1000
	probable_prime = generate_prime(bits, 10)
	print("A probable prime over {} bits = {}".format(bits, probable_prime))
	print()



	# qustion 5
	print("Question 5:")
    # wikipedia example
	n = [3, 4, 5]
	a = [2, 3, 1]
	x = remainder(a, n)
	print("Chinese Remainder thm:\nList X = {}\nList M = {}\nOutput: {}".format(a,n,x))
	print()



	# question 6
	print("Question 6a:")
	prime = 37055228012567588205472561716198899109643
	num_tests = 10
	r = Miller_Rabin_test(prime, num_tests)
	print("Miller-Rabin with {} tests. Is {} prime? {}".format(num_tests, prime, r))
	print()
	print("Question 6b:")
	prime = 37055228012567588205472561716198899109643
	g = primitive_root(prime)
	print("The smallest primitive root of {} = {}".format(prime, g))

if __name__ == '__main__':
	main()
