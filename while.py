# '''is_failed = True
# i = 0
# while is_failed and i<=100:
#     print(f"try {i}")
#     i=i+1
#     if i>100:
#         break
#     print("I gave up!")'
    
# is_failed = True
# i = 0

# while is_failed and i <= 100:
#     print(f"try {i}")
#     i += 1
#     if i > 100:
#         break

# print("I gave up!")'''

# pin = "1234"

# while True:
#     input_pin = input("PIN >>")
# if input_pin == pin:
#     print("CORRECT")
#     break
# else:
#     print("INCORRECT")

# is_failed = True
# i=1
# while is_failed :
#     if i%2!=0:
#         i=i+1
#         continue
#     print(f"Attempt {i}")
#     i=i+1
#     if i>100:
#         break
# print("I gave up")

# if_marks =True
# i =1
# while if_marks:
#     if i%2!=0:
#         i=i+1
#         continue
#     print(f"Attempt {i}")
#     i=i+1
#     if i>=100:
#         break
# print("marks")

# i = 0
# while i<=10:
#     x = 0
#     while x<i:
#         print("chandan",end="")
#         x+=1
#         print("")
#     i+=1
        
# available_seats = 5
# while available_seats > 0:
#     print(f"{available_seats} seats available.")
#     booking = input("Do you want to book a seat? (yes/no):").lower()
    
#     if booking =="yes":
#         available_seats -=1
#         print("Seat booked!")
#     else:
#         print("No booking made.")
# print("All seats are booked!")

# i =1
# while i<=5:
#     print(i)
#     i=i+1 #or i +=1

# sheep_count = 1
# while sheep_count <=10:
#     print(f"Sheep {sheep_count}")
#     sheep_count +=1

# i = 1
# while i<=5:
#     print(i)
#     i+=1

# sheep_count = 1
# while sheep_count <=10:
#     print(f"Sheep {sheep_count}")
#     if sheep_count == 5:
#         print("That's enough counting!")
#         break
# #     sheep_count +=1
# pin = "1234"
# while True:
#     input_pin = input("PIN >> ")
#     if input_pin ==pin:
#        print("CORRECT")
# else:
#     print("INCORRECT")
    
# def hf():
#     print("hello world")
# hf()
           
# integer = -20
# print('Absolute value of - 20 is:',abs(integer))

# print("welcome")
# for x in range(3):
#     print(x)
# print("Good morning college")

# def hello():
#     print("Good Morning")
#     print("mrcet")
# print("hi")
# print("Hello")
# hello()
# print("done!")

# def add(a,b):
#     return a+b
# result= add(12,13)
# print(result)

def sub(a,b):
    return a,b
result =sub(40,30)
print(result)