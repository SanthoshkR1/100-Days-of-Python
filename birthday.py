birthday = {
   "chandan" : "02-23-2001",
   "santhosh" : "06 -19-2003",
   "srikanth" : "11-12-2000",
   "sagar" : "21-05-2000",
   "venkatesh" : "03-12-1998"
}
print(type(birthday))
print(birthday["chandan"])
print(birthday["santhosh"])
print(birthday["srikanth"])
print(birthday["sagar"])
print(birthday["venkatesh"])

print("using get fuction")
print(birthday.get("chandan"))
print(birthday.get("sudeep",'not found'))

#adding sudeep and appu to the list
birthday["sudeep"] = "02-09-1973"

birthday["appu"] = "17-03-1975"
print(birthday)

#updating dictionary elements
birthday["chandan"] ="09-05-2000"
print(birthday)

#pop()
birthday.pop("chandan")
print(birthday)

del birthday["santhosh"]
print(birthday)

#methods
print(birthday.keys())
print(birthday.values())
print(birthday.items())
