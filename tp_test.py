import numpy as np

lengths = [1000, 10000, 100000, 1000000, 10000000]
np.random.seed(42)


def sequential_search(val, target):
    for i in range(len(val)):
        if target == val[i]:  
            return i + 1
    return len(val)

def advanced_sequential_search(val, target):
    comparison = 0
    for i in range(len(val)):
        comparison += 2
        if target == val[i]:  
            comparison -= 1
            break
        elif target < val[i]:
            break
    return comparison

def binary_search(val, target):
    start = 0
    end = len(val) - 1
    comparison = 1
    while start <= end:
        half = (start + end) // 2
        comparison += 2
        if target == val[half]:
            comparison -= 1
            break
        elif target < val[half]:
            end = half - 1
        else:
            start = half + 1
        comparison += 1
    return comparison

num_tests_per_size = 6

for n in lengths:
    print(f"\n Array length = {n:,}")
    val = np.sort(np.random.randint(1, 10_000_000, size=n))
    
    for t in range(num_tests_per_size):
        target = np.random.randint(1, 10_000_000)
        seq = sequential_search(val, target)
        adv = advanced_sequential_search(val, target)
        bin = binary_search(val, target)
        print(f"Test {t+1}: Seq={seq}, Adv={adv}, Bin={bin}")
