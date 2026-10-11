import time
import numpy as np

def exchange_sort_with_metrics(arr):
    operation_count = 0
    
    start_tick = time.perf_counter_ns()
    
    n = len(arr)
    operation_count += 1 
    
    for i in range(n):
        operation_count += 2 
        
        operation_count += 1 
        for j in range(i + 1, n):
            operation_count += 2 
            
            operation_count += 1 
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                operation_count += 3

    end_tick = time.perf_counter_ns()
    elapsed_time_ms = (end_tick - start_tick) / 1_000_000
    
    return arr, operation_count, elapsed_time_ms

#------------------------------------random array------------------------------------
random_array = np.random.randint(0, 1000, size=1000)
print(f"Original List: {random_array}\n")

#------------------------------------ascending array------------------------------------\
# ascending_array = np.arange(1000)               #0-999
ascending_array = np.sort(random_array)
print(f"Original List: {ascending_array}\n")
#------------------------------------descending array------------------------------------
# descending_array = np.arange(999, -1, -1)
descending_array = np.sort(random_array)[::-1].copy()
print(f"Original List: {descending_array}\n")



print('-------------------------------------sorting random array------------------------------------')
sorted_list, total_ops, duration = exchange_sort_with_metrics(random_array)
print(f"Sorted List:   {sorted_list}")
print(f"⚙️ Total Operations Tracked: {total_ops}")
print(f"⏱️ Elapsed Time: {duration:.4f} ms")

print('-------------------------------------sorting ascending array------------------------------------')
sorted_list, total_ops, duration = exchange_sort_with_metrics(ascending_array)
print(f"Sorted List:   {sorted_list}")
print(f"⚙️ Total Operations Tracked: {total_ops}")
print(f"⏱️ Elapsed Time: {duration:.4f} ms")

print('-------------------------------------sorting descending array------------------------------------')
sorted_list, total_ops, duration = exchange_sort_with_metrics(descending_array)
print(f"Sorted List:   {sorted_list}")
print(f"⚙️ Total Operations Tracked: {total_ops}")
print(f"⏱️ Elapsed Time: {duration:.4f} ms")

