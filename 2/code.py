### Part 1

def is_ordered(levels):
	return levels == sorted(levels) or levels == sorted(levels, reverse = True)

def is_safe_stepsize(levels):
    for i, level in enumerate(levels): 
        if i == 0: 
        	continue
        stepsize = abs(levels[i] - levels[i - 1])
        if stepsize < 1 or stepsize > 3: 
            return False

    return True 

safe_count = 0
with open('input', 'r') as f:
    for report in f:
        levels = list(map(int, report.strip().split(' ')))
        if not is_ordered(levels) or not is_safe_stepsize(levels):	
        	continue 
        safe_count += 1

print(safe_count)
      
### Part 2

safe_count = 0
with open('input', 'r') as f:
    for report in f:
        levels = list(map(int, report.strip().split(' ')))
        # TODO
