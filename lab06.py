def encode(password):
    my_str = ''
    for i in range(len(password)):
        curr_num = int(password[i])
        curr_num += 3
        my_str +=  (str(curr_num))
    password = my_str
    print(password)
    return password

def decode(password):
    my_str = ''
    for i in range(len(password)):
        curr_num = int(password[i])
        curr_num -= 3
        my_str +=  (str(curr_num))
    password = my_str
    print(password)
    return password

def main():
    encode("12345555")
    decode(encode("12345555"))

if __name__ == '__main__':
    main()