import time
from sympy import Matrix


def list_and_sum_primes(n):
	num_line = [True for i in range(n+1)]
	p = 2
	while (p * p <= n):
		if num_line[p] == True:

			for i in range(p * p, n+1, p):
				num_line[i] = False
		p += 1

	# prime_list = []
	prime_sum = 0
	for prime in range(2,n+1):
		if num_line[prime] == True:
			prime_sum += prime
			# prime_list.append(prime)

	return prime_sum #, prime_list


def calc_matrix():
	"""
	None -> VECTOR
	Calculate Ax = 0 (mod 2)
	"""
	#define matrices
	A = numpy.matrix(
	[[0,0,0,1,0,1,0,1,0,0],
	[0,1,0,0,1,1,1,1,1,0],
	[1,0,0,0,0,0,1,1,1,0],
	[1,0,0,0,1,1,0,0,1,0],
	[0,0,1,1,1,1,0,0,0,0],
	[1,1,0,1,0,0,0,1,1,1],
	[0,1,1,0,1,1,0,1,1,0],
	[0,0,0,0,1,0,0,1,1,0],
	[0,1,1,1,0,0,0,1,0,1],
	[0,0,1,0,1,1,1,0,1,1]])
	B = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
	A = Matrix(A) #get proper matrix format
	B = Matrix(B)
	A = A.inv_mod(2) #get inverse of A mod 2
	X = A * B # A^-1 * B = X
	print(X)
	return X


def main():
	"""
	n = (10**8)
	start_time = time.time()
	sum = list_and_sum_primes(n)
	# len_list = len(my_list)
	end_time = time.time()
	# print("There are {} primes less than {}".format( n))
	print("Their sum equals: {}".format(sum))
	print("My program took", end_time - start_time, "seconds to run")
	"""
	calc_matrix()


if __name__ == "__main__":
	main()
