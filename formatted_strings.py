#STRING CONCATINATION
'''first = "Santhosh"
last = "Shetty"
full = first + " " + last
print(full) 


first = "Santhosh"
last = "Shetty"
full = f"{len(first)} {last}"
print(full)
'''
#useful string methods
course = "  Python Programming" 
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())#useful when u get the input from the user leftstrip and rightstrip
print(course.find("Pro"))#finding the index of the character or a substring in a string
print(course.find("pro"))
print(course.replace("P","-"))
print("Programming" in course)
print("Programming" not in  course)
items1 = {
    "name" : "milk",
    "weight" : 1,
    "price" : 50
}
items2 = {
    "name" : "sugar",
    "weight" : 2,
    "price" : 99.9
}
items=[items1,items2]
print(items)