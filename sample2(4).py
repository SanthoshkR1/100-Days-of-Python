'''x = 1
print(id(x))

x = x + 1
print(id(x))
       
#using list can mutable the memory address
x = [1,2,3]
print(id(x))

x.append(4)
print(id(x))

course = "python programming"
print(len(course))
print(course[0])

print(course[-1])
print(course[0:3])
print(course[0:4])
print(course[0:])
print(course[2:8])
course ="cloud computing"
print(len(course))
print(course[0:8])
print(course[-3])
print(course[:])

print(id(course))
print(id(course[0]))
print(id(course[1]))
'''
#escape sequences
message = """python
programming
"""
message ="python \\ programming"
message ="python \n programming"
message = """python
is high level
programming
"""
print(message) 