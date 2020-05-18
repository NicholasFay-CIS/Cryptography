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
	A = [[0,0,0,1,0,1,0,1,0,0],
	[0,1,0,0,1,1,1,1,1,0],
	[1,0,0,0,0,0,1,1,1,0],
	[1,0,0,0,1,1,0,0,1,0],
	[0,0,1,1,1,1,0,0,0,0],
	[1,1,0,1,0,0,0,1,1,1],
	[0,1,1,0,1,1,0,1,1,0],
	[0,0,0,0,1,0,0,1,1,0],
	[0,1,1,1,0,0,0,1,0,1],
	[0,0,1,0,1,1,1,0,1,1]]
	B = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
	A_M = Matrix(A) #get proper matrix format
	B_M = Matrix(B)
	is_inv = False
	my_l = []
	j = 0
	try:
		#make sure the matrix is not singular mod A
		A = A_M.inv_mod(5) #get inverse of A mod 2
		is_inv = True
	except:
		pass
	if(is_inv):
		X = A * B # A^-1 * B = X
		return X
	echelon_form = Matrix.rref(A_M) # get the row reduced echelon form
	X = echelon_form[-1] #get the resultant vector
	while j < len(X): #apply the vector to the appropriate columns
		for row in A:
			row[j] *= X[j]
		j += 1 
	A_X = A #update A to be Ax
	print(A_X)
	for item in A_X: #calculate AX mod 2
		sum_= 0
		for val in item:
			sum_ += val
		sum_ = sum_ % 2
		my_l.append(sum_)
	print("Ax mod 2 is  {}".format(my_l))
	return X


def main():
	# Problem 1
	n = (10**8)
	start_time = time.time()
	sum = list_and_sum_primes(n)
	# len_list = len(my_list)
	end_time = time.time()
	# print("There are {} primes less than {}".format( n))
	print("Their sum equals: {}".format(sum))
	print("My program took", end_time - start_time, "seconds to run")
	#Problem 2
	# From tests online it seemed that the only answer was trivial (meaning 0)
	# This is the code that we used to find the non trivial solution but could not get Ax = 0 mod 2
	calc_matrix()


if __name__ == "__main__":
	main()
