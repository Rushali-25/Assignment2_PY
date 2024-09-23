#10 **Recursive Function with *args and kwargs (Flattening a List):
def flatten_list(*args, **kwargs):
    flattened = []
    for item in args:
        if isinstance(item, list):
            flattened.extend(flatten_list(*item))
        else:
            flattened.append(item)
    
    return flattened

nested_list = [1, [2, 3], [4, [5, 6]], 7]
result = flatten_list(nested_list)
print(result)
