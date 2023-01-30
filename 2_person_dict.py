person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)
# the name of the second child 

print(type(person['children']))
print(person["children"][1])

# the name of the cat 
print(type(person["pets"]))
print 
#use a for looop to list each child 
for i in person["children"]:
    print(i)

# print out the pets in the format; 
# 'type of pet : dog name of pet ; Fido' 
for i,j in person["pets"].items():
    priint(f"Type of pet:{i} name of pets: {J}")