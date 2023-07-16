import time
from bard import bard_algorithm
from chatgpt import chatgpt_algorithm
# from copilot import copilot_algorithm

def benchmark_algorithm(algorithm, test_data):
    start_time = time.time()
    for data in test_data:
        algorithm(*data)  # Unpack the tuple into separate arguments
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Generate test data
test_data = [("aba", 10), ("abcac", 10), ("abacaba", 100), ("a", 1000000000001), ("aab", 882787), ("abcac", 20),
             ("aba", 10), ("abcac", 10), ("abacaba", 100), ("a", 1000000000001), ("aab", 882787), ("abcac", 20)]

# Run benchmarking for each algorithm
# copilot_execution_time = benchmark_algorithm(copilot_algorithm, test_data) ## Timeout
chatgpt_execution_time = benchmark_algorithm(chatgpt_algorithm, test_data)
bard_execution_time = benchmark_algorithm(bard_algorithm, test_data)

# Compare the execution times

# print("COPILOT execution time:", copilot_execution_time) ## Timeout
print("CHATGPT execution time:", chatgpt_execution_time) ## CHATGPT execution time: 1.5974044799804688e-05
print("BARD execution time:", bard_execution_time) ## BARD execution time: 8.821487426757812e-06
