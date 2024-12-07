### Read data

rules = {}
updates = []
section1 = True

with open('input', 'r') as f:
	for line in f:
		if not line.strip():
			section1 = False
			continue

		if section1: 
			rule = line.strip()
			nums = rule.split('|')
			if nums[0] not in rules:
				rules[nums[0]] = []
			rules[nums[0]].append(nums[1])
		else:
			updates.append(line.strip().split(','))

### Part 1 

def is_valid_update(update, rules):
	for i, num in enumerate(update): 
		if num not in rules:
			continue
		
		for rule_num in rules[num]:
			if rule_num in update[:i]:
			 	return False

	return True

sum_corr_mids = 0
for update in updates: 
	if is_valid_update(update, rules):	
		sum_corr_mids += int(update[int(len(update) / 2)])

print(sum_corr_mids)

### Part 2

def correct_invalid_update(update, rules):
	corrected_update = update[:]

	while not is_valid_update(corrected_update, rules):
		for i, num in enumerate(corrected_update): 
			if num not in rules:
				continue
			
			for rule_num in rules[num]:
				if rule_num in corrected_update[:i]:
					cur_pos = corrected_update.index(rule_num) 
					corrected_update.insert(i, corrected_update.pop(cur_pos))

	return corrected_update

sum_corrected_mids = 0
for update in updates: 
	if not is_valid_update(update, rules):
		corrected_update = correct_invalid_update(update, rules)
		sum_corrected_mids += int(corrected_update[int(len(corrected_update) / 2)])
		
print(sum_corrected_mids)