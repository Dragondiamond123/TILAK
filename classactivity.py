def find_cube_pairs(target):
    # List to store valid pairs
    solutions = []
    
    # Find the cube root of the target, rounded to the nearest integer
    max_num = round(target ** (1/3))  
    
    # Iterate over all possible values of a and b
    for a in range(1, max_num + 1):  # Fixed 'ranges' to 'range'
        for b in range(a, max_num + 1):  # Fixed 'ranges' to 'range'
            if a**3 + b**3 == target:  # Fixed '***' to '**' and 'targ' to 'target'
                solutions.append((a, b))  # Fixed 'sol' to 'solutions'
    
    return solutions  # Fixed 'sol' to 'solutions'

# Find pairs whose cube sum equals 1729
pairs = find_cube_pairs(1729)

# Print results
print("Valid cube pairs for 1729:")  # Fixed 'printf' to 'print'
for a, b in pairs:  # Fixed 'pair' to 'pairs'
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")  # Fixed '**2' to '**3'
