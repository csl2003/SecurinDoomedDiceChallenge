total_combinations = 6 * 6
print("Total number of Combinations:", total_combinations)

print()


print("Combination Matrix:")
for i in range(1,7):
    for j in range(1,7):
        print((i,j),end=' ')
    print()
print("Distribution Matrix:")
for i in range(1,7):
    for j in range(1,7):
        print((i+j),end='  ')
    print()
    
print()    

combinations = [(i + j) for i in range(1, 7) for j in range(1, 7)]
sum_count = {}
for c in combinations:
    if c in sum_count:
        sum_count[c] += 1
    else:
        sum_count[c] = 1

total_combinations = 6 * 6
probability = {k: v / total_combinations for k, v in sum_count.items()}
print("Probability of Sums:")
for k, v in probability.items():
    print(f"P(Sum = {k}) = {v:.4f}")
