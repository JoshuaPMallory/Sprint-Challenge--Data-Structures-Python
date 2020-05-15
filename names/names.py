import time


def dup_baseline():
	f = open('names_1.txt', 'r')
	names_1 = f.read().split("\n")  # List containing 10000 names
	f.close()

	f = open('names_2.txt', 'r')
	names_2 = f.read().split("\n")  # List containing 10000 names
	f.close()

	duplicates = []  # Return the list of duplicates in this data structure

	# Replace the nested for loops below with your improvements
	for name_1 in names_1:
	    for name_2 in names_2:
	        if name_1 == name_2:
	            duplicates.append(name_1)
	return duplicates

def dup_tuple():
	f = open('names_1.txt', 'r')
	names_1 = tuple(f.read().split("\n") ) # ~List~ Tuple containing 10000 names
	f.close()

	f = open('names_2.txt', 'r')
	names_2 = tuple(f.read().split("\n"))  # ~List~ Tuple containing 10000 names
	f.close()

	duplicates = []  # Return the list of duplicates in this data structure

	# Replace the nested for loops below with your improvements
	for name_1 in names_1:
	    for name_2 in names_2:
	        if name_1 == name_2:
	            duplicates.append(name_1)
	return duplicates

def dup_pd():
	'''Pandas (Uses C)'''
	import pandas as pd


	s1 = pd.read_csv('names_1.txt', names = ['1'])
	s2 = pd.read_csv('names_2.txt', names = ['1'])

	df = pd.concat([s1, s2], ignore_index = True)

	duplicates = df[df.duplicated()]['1'].values.tolist()

	return duplicates

def endit(duplicates):
	end_time = time.time()
	print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
	print (f"runtime: {end_time - start_time} seconds")


print('Baseline Test')
start_time = time.time()
endit(dup_baseline())
print()


print('Tuple Test')
start_time = time.time()
endit(dup_tuple())
print()


print('Pandas Test')
start_time = time.time()
endit(dup_pd())
print()


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


