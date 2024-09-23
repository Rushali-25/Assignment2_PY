#4 Lambdas and map:
def square_list(numbers):
    return list(map(lambda x: x ** 2, numbers))
result = square_list([1, 2, 3, 4])
print(result)