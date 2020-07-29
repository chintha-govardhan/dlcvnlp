"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated
sequence on a single line.
"""
start = 2000
end = 3200

def filter_numbers():

    result = filter(lambda x: x%7 == 0 and x%5 != 0, range(start, end+1))
    return list(result)

for i in filter_numbers():
    print(i, end=' ')