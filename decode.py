def decode(password):
    my_str = ''
    #empty strig
    for i in range(len(password)):
        #for loop that iterates the string
        curr_num = int(password[i])
        curr_num -= 3
        if curr_num < 0:
            #if statment to avoid negatives
            curr_num += 10
        my_str +=  (str(curr_num))
        #concatenates the string
    password = my_str
    #returns the password
    return password
