# #if elif else
# x = 10
# if x ==10:
#     print("yes x is 10")
    
# x = 23
# if x % 2==0: #checking if x is 0
#     print("x is even")
# else:
#     print("x is odd")

# santhosh ="IT employee"    
# if santhosh =="IT employee":
#     print("yes he is working in it company")
# else:
#     print("he will be working in IT company")

# signal = input("What's the current signal color: ")
# if signal =="red":
#     print("stop") 
# elif signal =="yellow":
#     print("Ready")  
# elif signal =="green":
#     print("safe") 
# else:
#     print("go")
    
# att = 75
# is_teacher_friend = True
# if att >=75:
#     print("EXAM")
# elif att>=75 or is_teacher_friend:
#     print("EXAM")
# else:
#     print("NO  EXAM")

# age = 16
# has_student_id=True
# if age < 18 and has_student_id:
#     print("you are eligible for the student discount")
# else:
#     print("you are not eligible for the student discount")

# age = int(input("enter your age: "))
# if age <5:
#     print("Ticket is free")
# elif age <=12:
#     print("you get a child discount")
# elif age>=60:
#     print("you get a senior citizen dicount")
# else:
#     print("you pay the full fare.")

gender=input("gender>> ")
age=int(input("age>> "))
conductor_is_freind = True
if gender=="female":
    print("Ticket is free")
else:
    if age<5:
        print("ticket is free")
    elif age <=12:
        print("you get half price")
    elif age>=60:
        print("you get a discount")
        if conductor_is_freind =="True":
            print("75% is free")
    else:
        print("you pay the full fare")
    
    