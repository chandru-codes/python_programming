a={ "name":"chandru",
    "clg": "psg",
    "dept":"eee-sw",
    "location":"cbe"
}

print(type(a))
print(a)
# for displaying keys and values seperately
print(a.keys())
print(a.values())

# adding key:value pair outside of the dictionary
a["age"]="22"
print(a)

# changing the values of the keys:-
a["location"]="chennai"
    #(or)
a.update({"location":"chennai"})
print(a)

# removing the elements

#using pop()
a.pop("dept")
print(a)

#using del()
del a["dept"]
print(a)


