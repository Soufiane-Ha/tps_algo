 # tps_algo
 ## tasks : 
 ceate the following algorithms : 
1. sequantial_search
2. advanced_sequantial_search
3. binary_search

 ## Solution : 
 1. Create file ex name my_tp
 2. Open file 
 3. First go to terminal and copy :
```bash
pip install numpy
```
Or
```bash
python -m pip install numpy
```
Or
```bash
py -m pip install numpy
```
4. After downloading NUMPY
5. copy this code 
```head
import numpy as np
lengths = [1000, 10000, 100000, 1000000, 10000000]
np.random.seed(42)
```
5.1. sequantial_search

```sequantial_search
def sequantial_search(val,target):
    for i in range(len(val)):
        if target == val[i]: 
            return i+1
    
    return len(val)
```
5.2. advanced_sequantial_search

```advanced_sequantial_search
def advanced_sequantial_search(val,target):
    comparison = 0
    for i in range(len(val)):
        comparison+=2
        if target == val[i]: # comparision
            comparison-=1
            break
        # add the part to stop searching when target small to the element
        elif target < val[i]:
            break
    return comparison
```
5.3. binary_search

```binary_search
def binary_search(val,target):
	
    start = 0
    end = len(val)-1
    comparison = 1

    while start < end:
        half = (end + start)//2
        comparison+=2
        if target == val[half]:
            comparison-=1
            break
        elif target < val[half]:
            end = half -1
        else:
            start = half + 1 
        comparison+=1
    return comparison 
```
5.4. end
```end
num_tests_per_size = 6

for n in lengths:
    print(f"\n🔹 Array length = {n:,}")
    val = np.sort(np.random.randint(1, 10_000_000, size=n))
    
    for t in range(num_tests_per_size):
        target = np.random.randint(1, 10_000_000)
        seq = sequential_search(val, target)
        adv = advanced_sequential_search(val, target)
        bin = binary_search(val, target)
        print(f"Test {t+1}: Seq={seq}, Adv={adv}, Bin={bin}")
```
6. RUN

```error
  File "tp_test.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
```
> [!CAUTION]
> his simply means that the NumPy library is not installed in your Python environment.
To resolve the issue, install the library in the appropriate manner for your environment.
