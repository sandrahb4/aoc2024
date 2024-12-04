import numpy as np
import re

### Read input 

data = []
with open('input', 'r') as f:
	for line in f:
		data.append(list(line.strip()))

matrix = np.array(data)

# Part 1

def count_all_possible_words_in_array(array, word): 
	array_str = "".join(array).strip()
	return len(re.findall('XMAS', array_str))

def count_all_horizontal_words(matrix, word):
	count = 0

	for array in matrix: 
		count += count_all_possible_words_in_array(array, word)
		count += count_all_possible_words_in_array(list(reversed(array)), word)

	return count

def count_all_diagonal_words(matrix, word):
	count = 0

	for i in range(0, matrix.shape[0]):
		diag = matrix.diagonal(i)
		if len(diag) < len(word):
			break
		count += count_all_possible_words_in_array(diag, word)
		count += count_all_possible_words_in_array(list(reversed(diag)), word)

	for i in range(-1, -1 * matrix.shape[0], -1):
		diag = matrix.diagonal(i)
		if len(diag) < len(word):
			break
		count += count_all_possible_words_in_array(diag, word)
		count += count_all_possible_words_in_array(list(reversed(diag)), word)

	return count

word = 'XMAS'
total = 0

total += count_all_horizontal_words(matrix, word)
total += count_all_horizontal_words(matrix.transpose(), word)
total += count_all_diagonal_words(matrix, word)
total += count_all_diagonal_words(np.flip(matrix, axis=0), word)

print(total)

### Part 2

def is_valid_xmas_diagonal(item1, item2):
	return (item1 == 'M' and item2 == 'S') or (item1 == 'S' and item2 == 'M')

def is_valid_xmas(matrix, index): 
	if index[0] < 1 or index[0] >= matrix.shape[0]-1 or index[1] < 1 or index[1] >= matrix.shape[1]-1:
		return False

	item1_diag1 = matrix[(index[0]-1, index[1]-1)]
	item2_diag1 = matrix[(index[0]+1, index[1]+1)]

	item1_diag2 = matrix[(index[0]-1, index[1]+1)]
	item2_diag2 = matrix[(index[0]+1, index[1]-1)]
	
	return is_valid_xmas_diagonal(item1_diag1, item2_diag1) and is_valid_xmas_diagonal(item1_diag2, item2_diag2)

count = 0 
for index,item in np.ndenumerate(matrix):
	if item == 'A' and is_valid_xmas(matrix, index): 
		count += 1

print(count)

