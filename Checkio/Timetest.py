import timeit

code_to_test = """
temp = [73, 74, 75, 71, 69, 72, 76, 73]


def daily_temperatures(t):
    days = []
    for ind, temp in enumerate(t):
        temp_greater = [(i, val) for i, val in enumerate(t[ind+1:], ind+1) if val > temp]
        day = temp_greater[0][0]-ind if temp_greater else 0
        days.append(day)
    return days

daily_temperatures(temp)
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)
