
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
			if(i % j) == 0:
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
	if(exp == largest_val):
		my_expos.remove(my_expos[0])
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
	print(return_list)
	print("Fast powering found the last 5 digits as {}".format(return_val % mod))
	return return_val % mod


def main():
	print("Problem 1")
	find_primes(100)
	print("\nProblem 2")
	fast_powering_alg(2, 600, 100000)
	return

if __name__ == '__main__':
	main()
       
