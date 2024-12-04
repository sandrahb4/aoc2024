import re 

### Part 1

total = 0
with open('input', 'r') as f:
	for line in f:
		muls = re.findall('mul\(\d+,\d+\)', line)
		for mul in muls:
			nums = mul.split('(')[1].split(')')[0].split(',')
			total += int(nums[0]) * int(nums[1])

print(total)
		
### Part 2

total = 0
activated_instructions = True
with open('input', 'r') as f:
	for line in f:
		instrs = re.findall('(mul\(\d+,\d+\))|(do\(\))|(don\'t\(\))', line)
		for instr_list in instrs:
			instr = list(filter(None, instr_list))[0]
			if instr.startswith('do()'):
				activated_instructions = True
			elif instr.startswith('don\'t()'):
				activated_instructions = False 
			elif instr.startswith('mul') and activated_instructions: 
				nums = instr.split('(')[1].split(')')[0].split(',')
				total += int(nums[0]) * int(nums[1])

print(total)