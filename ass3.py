import math

def find_primes(n):
	"""
	int -> list
	This function returns a list of all primes less than n
	"""
	list_of_primes = list()
	#iterate from 2 to n since 1 is not a prime
	for i in range(2, n):
		#iterate from 2 to i
		for j in range(2, i):
			#if the i mod j is zero it is not a prime
			if( i % j) == 0:
				break
		else:
			#otherwise it is a prime
			list_of_primes.append(i)
	print("There are {} primes. {}".format(len(list_of_primes), list_of_primes))
	return list_of_primes

def fast_powering_alg(x, exp, mod):
	"""
	int, int, int -> int
	This function is supposed to replicate the fast powering algorithm.
	"""
	my_expos = list()
	return_list = list()
	return_val = 1
	i = 1
	#get all of the exponents that is less than or
	#equal to the passed in exponent
	while i <= exp:
		my_expos.append(i)
		i = i * 2
	#sort the list from largest to smallest
	my_expos.reverse()
	#grab the largest value
	largest_val = my_expos[0]
	#remove the largest value
	my_expos.remove(my_expos[0])
	#subtract the largest value from the given exponent
	exp -= largest_val
	#add the largest value to the return list
	return_list.append(largest_val)
	#if the largest value is the exponent, calculate the modular arithmetic
	if(exp == 0):
		return (x**largest_val) % mod
	#otherwise find a combonation of numbers that add up to the exponent
	for num in my_expos:
		#if the exponent - number is greater than zero
		if(exp - num >= 0):
			exp -= num #subtract from the exponent
			return_list.append(num) # add the number to the return value list
	#iterate through the list and calculate the value 
	for num in return_list:
		return_val *= (x**num) % mod
	print("Fast powering found the last 2 digits as {}".format(return_val % mod))
	return return_val % mod


def gcd_ext(n, x):
	'''
    NB:  x mod(n)
	'''

	if n == 0:
		return x, 0, 1

	gcd, new_s, new_p = gcd_ext(x%n, n)
	s = new_p - (x//n) * new_s
	p = new_s

	return gcd, s, p

def calc_gcd(a, b):
	gcd, s, p = gcd_ext(a, b)
	assert( (p*b + s*a) == gcd )
	return gcd

def calc_inverse(num, mod):
	gcd, s, p = gcd_ext(mod, num)
	assert( (p*num + s*mod) == gcd )
	return p

def calc_gcd2(N):
	''' N = list of numbers
	'''

	a = N[0]
	for i in range(1, len(N)):
		b = N[i]
		a = calc_gcd(a, b)


	return a



def main():

    #question 1
	find_primes(100)
    #question 2
	fast_powering_alg(2, 521, 100)

	#question 3

	# x (mod n) 197189 (mod 999979)
	x = 197189
	n = 999979
	inverse = calc_inverse(x, n)
	print("inverse of {} (mod {}) is {}".format(x,n,inverse))
	a = 2**1000 - 299
	b = math.factorial(1000) + 98
	gcd = calc_gcd(a, b)
	print("gcd( 2^1000 - 299 , 1000! + 98 ): {}".format(gcd))

	#  gcd for a, b, c, d, e
	N = [887519, 146744, 388025, 880464, 189074]
	gcd = calc_gcd2(N)
	print("gcd( {} , {} , {} , {} ,  {}): {}".format(N[0],N[1],N[2],N[3],N[4],gcd))


    
	return

if __name__ == '__main__':
	main()
       
