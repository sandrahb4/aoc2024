import numpy as np

### Read input 

data = []
with open('input', 'r') as f:
	for line in f:
		data.append(list(line.strip()))

matrix = np.array(data)
guard = np.where(matrix == '^')
start_pos = (int(guard[0][0]), int(guard[1][0])) # (y,x)
start_dir = (-1, 0) # (y,x)

### Part 1

def rotate_90_right(direction):
	rotations = {}
	rotations[(-1,0)] = (0,1) # Up to right
	rotations[(0,1)] = (1,0) # Right to down
	rotations[(1,0)] = (0,-1) # Down to left
	rotations[(0,-1)] = (-1,0) # Left to up
	return rotations[direction]

def get_next_pos(cur_pos, direction): 
	return (cur_pos[0] + direction[0], cur_pos[1] + direction[1])

def is_valid_matrix_index(matrix, cur_pos):
	return cur_pos[0] >= 0 and cur_pos[0] < matrix.shape[0] and cur_pos[1] >= 0 and cur_pos[1] < matrix.shape[1]

def step_forward(matrix, cur_pos, cur_dir):
	new_pos = cur_pos
	new_dir = cur_dir

	peek_next_pos = get_next_pos(new_pos, new_dir)
	rotated = False
	while is_valid_matrix_index(matrix, peek_next_pos) and matrix[peek_next_pos] == '#':
		new_dir = rotate_90_right(new_dir)
		peek_next_pos = get_next_pos(new_pos, new_dir)
		if matrix[peek_next_pos] == '#':
			continue
		else:
			new_pos = peek_next_pos
		rotated = True

	if not rotated:
		new_pos = peek_next_pos

	return new_pos, new_dir

visited = np.zeros(matrix.shape)
cur_pos = start_pos
cur_dir = start_dir
while is_valid_matrix_index(matrix, cur_pos):
	visited[cur_pos[0]][cur_pos[1]] = 1
	cur_pos, cur_dir = step_forward(matrix, cur_pos, cur_dir)

print(np.sum(visited))

### Part 2

def matrix_contains_guard_loop(matrix, start_pos, start_dir):
	visited_pos_dirs = set()
	cur_pos = start_pos
	cur_dir = start_dir

	while is_valid_matrix_index(matrix, cur_pos):
		if (cur_pos, cur_dir) in visited_pos_dirs:
			return True
		visited_pos_dirs.add((cur_pos, cur_dir))
		cur_pos, cur_dir = step_forward(matrix, cur_pos, cur_dir)

	return False

count = 0
for index,item in np.ndenumerate(matrix):
	if item == '#' or index == start_pos:
		continue
	obstr_matrix = matrix.copy()
	obstr_matrix[index] = '#'
	if matrix_contains_guard_loop(obstr_matrix, start_pos, start_dir):
		count += 1

print(count)