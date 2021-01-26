import timeit

code_to_test = """
def is_power_of_three(number):
    counter = 1  # 3 ** 0
    while counter < number:
        counter *= 3
    return counter == number
"""

elapsed_time = timeit.timeit(code_to_test, number=1000)/100
print(elapsed_time)