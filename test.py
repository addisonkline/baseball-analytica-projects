import random
import numpy as np

results = []

for i in range(100):
    escaped = False
    days = 0

    while (not escaped):
        rand = random.random()

        if (rand >= 0.5): # door 1
            days += 2
        elif (rand >= 0.2): # door 2
            days += 4
        else: # door 3
            days += 1
            escaped = True
    
    print(f'Iteration: {i+1}: {days} days')
    results.append(days)

print(f'Mean: {np.mean(results)}')
