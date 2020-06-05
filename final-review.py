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


def DiffieHellman(a, b, p, g):
	alice = (g**a) % p
	bob = (g**b) % p
	alice_2 = (alice**b) % p
	bob_2 = (bob**a) % p
	print(alice, bob)
	print("Bob's Secret key: {}, Alice's Secret key: {}".format(bob_2, alice_2))
	return

def Eratosthenes_Seive(m):
	my_list = [i for i in range(2, m+1)]
	while(True):
		removed = my_list[0]
		if(removed >= math.floor(math.sqrt(m))):
			break
		my_list.remove(removed)
		for item in my_list:
			if(item % removed == 0):
				my_list.remove(item)
	print(my_list)
	return

def Eratosthenes_Seive_M_Smooth(m):
	pointer = 0
	my_list = [i for i in range(2, m+1)]
	print("List starting as:\n {}".format(my_list))
	while(pointer <= len(my_list)-1):
		div_val = my_list[pointer]
		print("Dividing by {}".format(div_val))
		for i in range(pointer, len(my_list)):
			if(my_list[i] % div_val == 0):
				my_list[i] = my_list[i] / div_val
		print("List After Division {}".format(my_list))
		pointer += 1
	return
def DiffieHellman(a, b, p, g):
	alice = (g**a) % p
	bob = (g**b) % p
	alice_2 = (alice**b) % p
	bob_2 = (bob**a) % p
	print(alice, bob)
	print("Bob's Secret key: {}, Alice's Secret key: {}".format(bob_2, alice_2))
	return

def Eratosthenes_Seive(m):
	my_list = [i for i in range(2, m+1)]
	while(True):
		removed = my_list[0]
		if(removed >= math.floor(math.sqrt(m))):
			break
		my_list.remove(removed)
		for item in my_list:
			if(item % removed == 0):
				my_list.remove(item)
	print(my_list)
	return

def Eratosthenes_Seive_M_Smooth(m):
	pointer = 0
	my_list = [i for i in range(2, m+1)]
	print("List starting as:\n {}".format(my_list))
	while(pointer <= len(my_list)-1):
		div_val = my_list[pointer]
		print("Dividing by {}".format(div_val))
		for i in range(pointer, len(my_list)):
			if(my_list[i] % div_val == 0):
				my_list[i] = my_list[i] / div_val
		print("List After Division {}".format(my_list))
		pointer += 1
	return
def find_primes(n):
    i = 2
    d = {}
    list_of_primes = []
    while(i < n):
        while (d.get(i) == None):
            list_of_primes.append(i)
            total = i
            while (total < n):
                d[total] = 1
                total += i
            i += 1
        i += 1
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
	for power in return_list:
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


def is_divisible(n, small_primes: list):
	for number in small_primes:
		if (n % number) == 0:
			return True
	return False


def prime_factors(s, n):
	# while (n % 2 == 0):
	# 	s.add(2)
	# 	n = n // 2

	list_of_n = [n]
	small_prime_list = find_primes(100000)
	check_small_primes = small_prime_list

	while is_divisible(min(list_of_n), check_small_primes):
		n1 = min(list_of_n)
		for small_prime in check_small_primes:
			n2 = n1
			while (n2 % small_prime == 0):
				s.add(small_prime)
				n2 = n2//small_prime
			else:
				if n2 not in list_of_n:
					list_of_n.append(n2)
				n2 = n1


	square_root = int(math.sqrt(min(list_of_n)))
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

def Polard_P_Minus_one_factoring(num):
	a = 2
	square = 1
	while(True):
		val = math.gcd(a-1, num)
		if(val == 1):
			square += 1
			a = fast_powering_alg(a, square, num)
			continue
		break
	print(val, num/val)
	return

def my_squares_brute_force(a, N):
	roots = []
	#has roots
	for i in range(N):
		if((i*i) % N == a):
			roots.append(i)
	if(len(roots) > 0):
		print("The roots of {} mod {} are {}".format(a, N,roots))
		return
	#does not have roots, find the smallest ~a
	a = a + 1
	while(len(roots) == 0):
		for i in range(N):
			if((i*i) % N == a):
				roots.append(i)
		a =  (a + 1) % N
	print("The roots of {} (~a: ~a > a) mod {} are {}".format(a, N, roots))
	return


def main():
	num = shanks_alg(3, 19, 59, 5)
	print(num)
	Eratosthenes_Seive(20)
	Eratosthenes_Seive_M_Smooth(13)
	print(fast_powering_alg(2, 2, 5429))
main()
