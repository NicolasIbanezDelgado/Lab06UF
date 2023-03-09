def decode(password):
    my_str = ''
    for i in range(len(password)):
        curr_num = int(password[i])
        curr_num -= 3
        my_str +=  (str(curr_num))
    password = my_str
    #print(password)
    return password

print(decode("45678888"))
# print(encode("12345555"))