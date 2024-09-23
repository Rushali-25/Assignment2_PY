#3 **Using *args and kwargs:
def sum_numbers(*args, **kwargs):
    total_sum = sum(arg for arg in args if isinstance(arg, (int, float)))
    if kwargs:
        return total_sum, kwargs
    else:
        return total_sum
print(sum_numbers(1, 2, 3))  
print(sum_numbers(1,2,x=4,y=5))