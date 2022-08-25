# task 1

s = input('enter string: ')
new_string = ""

if s.isupper():
    new_string = new_string + (s.lower())
elif s.islower():
    new_string = new_string + (s.upper())
else:
    new_string= s
print(new_string)
