# task 1
import re
s = input('enter string: ')
'''new_string = ""

if s.isupper():
    new_string = new_string + (s.lower())
elif s.islower():
    new_string = new_string + (s.upper())
else:'''
i = 0
j = [] #Declaring empty List
for i in range(len(s)): #For Accessing elements in string. 
    if s[i]==s[i].lower(): #For finding the Lower-case or Upper-case elements
     j.append(s[i].upper()) #Adding the new changed Upper-case element to j
    else :
        j.append(s[i].lower()) #Adding the new changed Lower-case elements to j
f = ''.join([str(elem) for elem in j])  #converting list to String
print(f)