#task 1

Message = "My secret is none of your business"

translated = '' #cipher text is stored in this variable


i = len(Message) - 1

while i >= 0:
  
  translated = translated + Message[i]

  i = i - 1

print(translated)