### Part 1

l1 = []
l2 = []

with open('input', 'r') as f:
    for l in f:
        nums = l.strip().split('   ')
        l1.append(int(nums[0]))
        l2.append(int(nums[1]))

l1.sort()
l2.sort()

diffs = [abs(i1 - i2) for i1, i2 in zip(l1, l2)]

print(sum(diffs)) 

### Part 2 

l1 = []
l2 = []

with open('input', 'r') as f:
    for l in f:
        nums = l.strip().split('   ')
        l1.append(int(nums[0]))
        l2.append(int(nums[1]))

score = 0
for n in l1: 
    score += n * l2.count(n)

print(score)
