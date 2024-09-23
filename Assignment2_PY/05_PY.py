#5 Filters and Lambdas:
def filter_odd_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))
result = filter_odd_numbers([1, 2, 3, 4, 5])
print(result)