nums = [1, 11, 4, 10, 3]

output = []

soma = 0

for i in nums:
    soma += i
    output += [soma]
    
print(output)