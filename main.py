def fibonacci(arr, steps):
    if len(arr) >= steps:
        return arr
    next_el = arr[-1]+arr[-2]
    result = arr+[next_el]
    return fibonacci(result, steps)

def fibonacciLimit(arr, limit):
    if len(arr) < 2:
        return arr
    result = arr[-1] + arr[-2]
    if result > limit:
        return arr
    if result <= limit:
        result = arr + [result]
    return fibonacciLimit(result, limit)

file1 = open('steps.txt', 'r')
steps = int(file1.readline())
file1.close()

file2 = open('limit.txt', 'r')
limit = float(file2.readline())
file2.close()

file3 = open('input.txt', 'r')
line = file3.readline()
first, second = map(float, line.split())
file3.close()

arr = [first, second]

file4 = open('result.txt', 'w')
file4.write(fibonacci(arr, steps - 2))
file4.write(fibonacciLimit(arr, limit))
file4.close()
