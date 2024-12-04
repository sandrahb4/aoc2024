import numpy as np
import re

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

data = []
with open('input', 'r') as f:
	for line in f:
		data.append(list(line.strip()))

matrix = np.array(data)
word = 'XMAS'

total = 0
total += count_all_horizontal_words(matrix, word)
total += count_all_horizontal_words(matrix.transpose(), word)
total += count_all_diagonal_words(np.flip(matrix), word)
total += count_all_diagonal_words(np.flip(matrix, axis=0), word)

print(total)

### Part 2