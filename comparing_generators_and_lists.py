import time

# print(sum([number for number in range(10)]))
# print(sum(number for number in range(10)))

list_start_time = time.time()
print(sum([number for number in range(100000000)]))
list_processing_time = time.time() - list_start_time


gen_start_time = time.time()
print(sum(number for number in range(100000000)))
gen_processing_time = time.time() - gen_start_time


print(f'Processing with list is {list_processing_time}')
print(f'Processing with generator is {gen_processing_time}')


# Result:
# 4999999950000000
# 4999999950000000
# Processing with list is 63.59796333312988
# Processing with generator is 11.566556692123413