#Nicolas Ibanez Delgado
#This is my own encoder function that I made
from decode import *
loop = True

def encode(password):
    my_str = ''
    #empty string

    for i in range(len(password)):
        #for loop that iterates the string
        curr_num = int(password[i])
        #encodes character
        curr_num += 3
        if curr_num >= 10:
            #if statement to correctly decode vaalues > 10
            curr_num = curr_num - 10
        my_str +=  (str(curr_num))
        #concatenates the string
    password = my_str
    #returns the string
    return password



while loop == True:
    print('Menu\n------------- \n1. Encode\n2. Decode\n3. Quit')
    menu = int(input("Please enter an option: "))
    if menu == 1:
        password = input('Please enter your password to encode: ')
        encode(password)
        print( "Your password has been encoded and stored!")
        #print(encode(password))
        continue
    elif menu == 2:
        #print(decode(encode(password)))
        #Couldn't I juse hvae printed encode and then the initial password? Without decoding it? 
        print (f'The encoded password is {encode(password)}, and the original password is {decode(encode(password)) }.')
        continue
    elif menu == 3:
        loop = False
        break
