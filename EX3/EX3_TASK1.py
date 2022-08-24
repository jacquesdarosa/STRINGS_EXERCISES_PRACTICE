#task 1

Message = "I'm 51 years old now"

translated = '' #cipher text is stored in this variable


i = len(Message) - 1

while i >= 0:
  
  translated = translated + Message[i]

  i = i - 1

print(translated)