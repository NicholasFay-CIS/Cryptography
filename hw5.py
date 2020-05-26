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
	x = N + 1
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

def main():
	while(True):
		input1 = input("Enter an a (possible square mod N):\n")
		input2 = input("Enter a N (modulus): ")



