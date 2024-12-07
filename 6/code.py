import numpy as np

### Read input 

data = []
with open('input', 'r') as f:
	for line in f:
		data.append(list(line.strip()))

matrix = np.array(data)

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

def step_forward(matrix, cur_pos, direction):
	new_pos = cur_pos
	new_direction = direction

	rotated = False
	peek_next_pos = get_next_pos(new_pos, new_direction)
	if is_valid_matrix_index(matrix, peek_next_pos) and matrix[peek_next_pos] == '#':
		new_direction = rotate_90_right(new_direction)
		new_pos = get_next_pos(new_pos, new_direction)
		rotated = True

	elif not rotated:
		new_pos = peek_next_pos

	return new_pos, new_direction

guard = np.where(matrix == '^')
cur_pos = (int(guard[0][0]), int(guard[1][0])) # (y,x)
direction = (-1, 0) # (y,x)
visited = np.zeros(matrix.shape)

while is_valid_matrix_index(matrix, cur_pos):
	visited[cur_pos[0]][cur_pos[1]] = 1
	cur_pos, direction = step_forward(matrix, cur_pos, direction)

print(np.sum(visited))
