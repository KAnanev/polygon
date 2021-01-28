def chunked(num, data):
    return [data[i:i + num] for i in range(0, len(data), num)]


print(chunked(2, ('A', 'B', 'C', 'D')))


