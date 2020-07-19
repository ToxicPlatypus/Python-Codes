def range_sum(numbers, start, end):
    result = 0
    for x in numbers:
        if start <= x <= end:
            result += x
    return result


input_numbers = list(map(int, input().split()))
a, b = map(int, input().split())
print(range_sum(input_numbers, a, b))