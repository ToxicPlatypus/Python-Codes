def average_mark(*args):
    result = 0
    x = 0
    for n in args:
        result += n
        x += 1
    result = result / x
    return round(result, 1)
