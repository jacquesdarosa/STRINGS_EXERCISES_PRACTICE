
# task 1


def finding_Nemo():
    S = input('enter string here : ')

    index = S.find('Nemo')

    if index == -1:
        print("I can't find Nemo")
    else:
        print('I found Nemo at', index)
    
finding_Nemo()
print()