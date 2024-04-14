'''

This is Evan Purutcuoglu's main.py file

'''

def encode(x):
    x = str(x)
    y = ""
    for num in x:
        y += (str(int(num)+33 % 10))
    return y

def decode(x):
    y = ""

    # just finish this function and everything else will work. (you shouldn't have to change anything outside of this function.) 

    return y

def main():

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option = input("Please enter an option: ")

        if option == "1":
            original = str(input("Please enter your password to encode: "))
            passwordEnc = encode(original)
            print("Your password has been encoded and stored!\n")
        if option == "2":
            passwordDec = decode(passwordEnc)
            print("The encoded password is", passwordEnc, "and the original password is", passwordDec, "\n")
        if option == "3":
            break




if __name__ == "__main__":
    main()


