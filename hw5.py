import math
try:
    from sympy import Matrix, pprint
except:
    print("you need to download 'SymPy' library\n")
    exit(-1)

def check_square_mod(a):
	"""
	int -> bool
	"""
	is_sqr = math.sqrt(a)
	if((is_sqr - math.floor(is_sqr)) == 0):
		return True
	return False


def squares(a, N):
	"""
	a (int), N (int) -> None
	"""
	x = a + 1
	val = a % N
	if(val != 0 and check_square_mod(val)):
		root = math.floor(math.sqrt(val))
		print("{} = {}^2 (mod {})".format(a, root, N))
		return root

	while(True):
		if(check_square_mod((x%N))):
			root = math.floor(math.sqrt((x%N)))
			print("Some a ({}) % {} is not a square of some b. The smallest a that satisfies such is ~a = {} = {}^2 (mod {})".format(a, N, x, root, N))
			return root
		x += 1

def list_primes(n):
	"""
	From assignment 4
	"""
	num_line = [True for i in range(n+1)]
	primes = []
	p = 2
	while (p * p <= n):
		if num_line[p] == True:

			for i in range(p * p, n+1, p):
				num_line[i] = False

		p += 1
	for prime in range(2,n+1):
		if num_line[prime] == True:
			primes.append(prime)

	return primes


def find_B(X):
	"""
    L(X) = e^(√(lnX)(ln lnX))
    B = L(N)^(1/√2)
    """
	L_x = (math.e ** math.sqrt(math.log(X) * math.log(math.log(X))))

	L_n = L_x ** (1 / math.sqrt(2))

	return L_n

def F_t(T,N):
	return T**2 - N

matrix_Ax = []
def factor_list(list,p):
	"""
	Updates the list's values where it's divisible

	"""
	global matrix_Ax
	isDivisible = False
	for i in range(len(list)):
		if list[i] % p == 0:
			isDivisible = True
			list[i] = int(list[i] / p)
	if isDivisible:
		matrix_Ax.append(list.copy())
		factor_list(list,p)


	return


def quad_sieve(N):
	"""
	Following text book steps
	F(T) = T^2 - N
	a = [√N] + 1
	#F(a), F(a+1), F(a+2),...,F(b)
	"""
	global matrix_Ax
	#prime basis from 2 to B
	primes = list_primes(int(find_B(N)))
	print("factor base:",primes)
	print("N = {} : B = {}".format(N,int(find_B(N))))
	a = math.floor(math.sqrt(N)) + 1
	#F(a), F(a+1), F(a+2),...,F(b)
	F_list = []
	F_pos = [] #positions
	F_init = [] #initial list

	for a_i in range(0,a+1):
		F_pos.append(a + a_i)
		F_list.append(int(F_t(a + a_i,N)))

	for item in F_list:
		F_init.append(item)

	matrix_Ax.append(F_list.copy())

	for prime in primes:
		factor_list(F_list,prime)


	print()
	for i in matrix_Ax:
		print(i)
	F_matrix = []
	for i in range(len(F_list)):
		if F_list[i] == 1:
			print("| F({}) = {}  ".format(F_pos[i],F_init[i]), end="")
			F_matrix.append(i)
	print()

	matrix_2d = []
	matrix_row = []

	for i in range(len(matrix_Ax)):
		for j in range(len(matrix_Ax[0])):
			if j in F_matrix:
				matrix_row.append(matrix_Ax[i][j])
		if len(matrix_row) != 0:
			matrix_2d.append(matrix_row.copy())
			matrix_row = []
	M = Matrix(matrix_2d)
	print()
	pprint(M)
	print()
	pprint(M % 2)
def main():
	print("Probelm 2------\n")
	problem2 = True
	while(problem2 == True):
		input1 = int(input("Enter an a (possible square mod N):\n"))
		input2 = int(input("Enter a N (modulus):\n"))
		squares(input1, input2)
		next_input = input("Do you want to continue yes or no?:\n")
		if(next_input == "yes" or next_input == "Yes"):
			continue
		problem2 = False
	print("Probelm 3------\n")
	input3 = int(input("Choose a value for N:"))
	quad_sieve(input3)
	return

main()