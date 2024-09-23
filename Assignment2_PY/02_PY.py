#2 Named arguments:
def create_profile( *,name, age=18, city):
    return f"Name: {name}, Age: {age}, City: {city}"
profile1 = create_profile(name="Rushali", city="Dehradun")
print(profile1)  
profile2 = create_profile(name="Akansha", age=25, city="Lucknow")
print(profile2)