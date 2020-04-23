
def find_primes(n):
	"""
	int -> list
	This function returns a list of all primes less than n
	"""
	list_of_primes = list()
	for i in range(2, n):
		if(n == 1):
			continue
		for j in range(2, i):
			if( i % j) == 0:
				break
		else:
			list_of_primes.append(i)
	print("There are {} primes. {}".format(len(list_of_primes), list_of_primes))
	return list_of_primes

def fast_powering(x, exp, mod):
	dict_of_nums = dict()
	list_of_nums = list()
	return_list = list()
	i = 1
	while i <= exp:
		list_of_nums.append(i)
		i = i * 2
	first_item = list_of_nums[0]
	list_of_nums.remove(list_of_nums[0])
	new_x = exp - first_item
	list_of_nums.reverse()
	print(list_of_nums)
	if(new_x == 0):
		return_list.append(first_item)
	else:
		return_list.append(first_item)
		for item in list_of_nums:
			if(new_x - item >= 0):
				new_x - item
				return_list.append(item)
	print(exp, return_list)
	return



def main():
	fast_powering(2, 21, 8)
	return

if __name__ == '__main__':
	main()
       
