# task 1 -- Peer's solution
def Functioninator_8000(word:str):

    if (    word[-1].lower() == "a" 
        or  word[-1].lower() == "e"
        or  word[-1].lower() == "i"
        or  word[-1].lower() == "o"
        or  word[-1].lower() == "u"):
        inator = "-inator "
    else:
        inator = "inator "
    return word + inator  + str(len((word))) + "000"



print(Functioninator_8000("Shrink"))
print(Functioninator_8000("Doom"))
print(Functioninator_8000("EvilClone"))


'''def inatorInator(text:str):
    """
    Function to check if a given words last char is a consonant.
    If so add inator, else -inator
    return with len of the given word and add "000" to the line
    """
    if (   text[-1].lower() == "a"
        or text[-1].lower() == "e"
        or text[-1].lower() == "i"
        or text[-1].lower() == "o"
        or text[-1].lower() == "u"):
        inator = "-inator "
    else:
        inator = "inator "
    return text + inator  + str(len((text))) + "000"


# Test some words and print them out
print(inatorInator("Shrink"))
print(inatorInator("Doom"))
print(inatorInator("EvilClone"))'''
