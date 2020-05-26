import math

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


def factor_list(list,p):
	"""
	Updates the list's values where it's divisible

	"""

	isDivisible = False
	for i in range(len(list)):
		if list[i] % p == 0:
			isDivisible = True
			list[i] = int(list[i] / p)
	if isDivisible:
		factor_list(list,p)

	return


def quad_sieve(N):
	"""
	F(T) = T^2 - N
	a = [√N] + 1
	#F(a), F(a+1), F(a+2),...,F(b)
	still needs work....
	"""

	#prime basis from 2 to 11
	#TODO: 2 to B?
	primes = (2,3,5,7,11)
	print("N =",N)
	print("B =",primes[-1])
	a = math.floor(math.sqrt(N)) + 1
	#F(a), F(a+1), F(a+2),...,F(b)

	F_list = []

	#example
	for a_i in range(0,a+1):
		F_list.append(int(F_t(a + a_i,N)))
	print(F_list)
	for prime in primes:
		factor_list(F_list,prime)
	print(F_list)

	#some steps

def main():
	problem2 = True
	while(problem2 == True):
		input1 = int(input("Enter an a (possible square mod N):\n"))
		input2 = int(input("Enter a N (modulus):\n"))
		squares(input1, input2)
		next_input = input("Do you want to continue yes or no?:\n")
		if(next_input == "yes" or next_input == "Yes"):
			continue
		problem2 = False

	#find_B(221)
	quad_sieve(221)
	return

main()




