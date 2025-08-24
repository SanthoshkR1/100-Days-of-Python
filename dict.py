# meanings ={
#     "bat" : "used to hit",
#     "ball" :"this is used to throw",
#     "wicket" :"protecting the stumps"
    
# }

# my_dict = {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3"
# }


# birthday = {
#     "chandan" : "07-06-2002",
#     "darshan" : "27-09-2004",
#     "virat" : "05-11-1988",
#     "santhosh": "11-01-2001",
#     "kanth":"11-12-2000"
# }
# print(type(birthday))
# print(birthday["chandan"])
# print(birthday["darshan"])
# print(birthday["virat"])
# print(birthday["santhosh"])
# print(birthday["kanth"])
# #or use get() method 
# print(birthday.get("virat"))
# print(birthday.get("sudeep",'not found'))
# print(birthday.get("yash",'not found'))

# print(birthday)
# print("Adding sudeep to the list")#adding an item to the dictionary elements
# birthday["sudeep"] ="02-09-1973"
# print("adding power star appu to the list")
# birthday["appu"] ="17-03-1975"
# print(birthday)

# #updating dictionary elements
# print("updating...")
# birthday["chandan"]="09-08-1999"
# print(birthday)
# birthday.pop("chandan")
# #del birthday["chandan"]

# print('"------------------------------------------------------------"')
# #methods
# print(birthday.keys()) 
# print(birthday.values())
# print(birthday.items())#in list having tuple with (key,value) used in problem solving  key value pairs giving tuple in list
# print(birthday)

# new_birthday ={"kiran" : "01-03-2000"}
# birthday.update(new_birthday)
# print(new_birthday)

# #or
# dic = {
#     "str" : "str",
#     "st" : 123,
#     "f" :10.2,
#     (1) : "dojhod", #can use tuple cannot use list no strict guildlines
#     12 : "esj" ,
#     "friends" : ["chandan" ,"amar"]
# }
# print(dic)

# item1 ={
#      "name" : "Milk" ,
#      "weight" : 1,
#      "price" : 50
# }
# item2 ={
#     "name" : "Sugar",
#     "weight" : 2,
#     "price" : 99.9
# }
# items =[item1,item2]
# print(f"Total Weight: {item1["weight"]+item2['weight']} kg ")
# #above is list of Dicts 

birthday = {
    "chandan" : "03-03-2923",
    "k l Rahul" : "18-04-1982",
    "darshan" : "33-02-2229",
    "shiva" : "01-01-2001",
    "nelesh" : "02-39-2022"
    
}
print(birthday.keys())
print(birthday.items())