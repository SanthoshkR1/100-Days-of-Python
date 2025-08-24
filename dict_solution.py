#1 - basic dictionary operations
'''
dishes ={
    "Bengaluru" : "Bisi Bele Bath",
    "Mysuru" : "Mysore Pak",
    "Mangaluru" : "Neer Dosa",
    "Mandya" : "Ragi Mudde",
    "Davangere" : "Benne Dosa"
}

dishes["Hassan"] = "Idli" #add

dishes["Bengaluru"] = "Bengaluru Bath" # update

del  dishes["Mysuru"] #delete

print(dishes.keys())
print(dishes.values())
'''
#2 - nested dictionery
d = {
    "friend_1" :{
        "name" : "darshan",
        "fav-subject" :"chemistery",
        "fav_food" : "Biriyani"
    },
    "friend_2" : {
        "name" : "sudeep",
        "fav_subject" : "maths",
        "fav_food" : "mutton biriyani"
    }
}
print(d["friend_1"]["fav_food"])
#or
f=d["friend_1"]
print(f["fav_food"])