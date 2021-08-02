# A dictionary in python is the unordered and changeable collection of data values that holds key-value pairs
#A dictiobnary is mutable
#A dictionary in python is declared by enclosing a comma-seperated list of key-value paird uding curly braces
#syntax for python dictionary:-
student1={'Name':'nithin','branch':'ECE','section':'IOT','Roll':122010406004}
#print(type(student1))
#print(student1)
#Duplicate keys are not allowed in dictionaries i.e if we give a key name again the previous one will be replaced with this.

#print(student1['Name'])

#updating a key in dict
student1.update({'Member':'ncc'})#dont forget to keep curly bracket
#print(student1)#after updating a new key value pair is added

#deleting a key from the  dict

#del student1['Name']
#print(student1) #noe naame is deleted

#items-this function returns list of tuples i.e key-value pair
#print(student1.items())
#list of only keys
#print(student1.keys())

#for i in student1.keys():
    #print(student1[i])









        
