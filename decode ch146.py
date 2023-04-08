abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#encode:
def encode(enter, num):
    encoded = ""
    for i in enter:
        for k in abc:
            if i == k:
                index = abc.index(k)
                newnum = index + num
                if (newnum > 26):
                    b = (newnum-26)
                    n = abc[b]
                else:
                    n = abc[newnum]
            elif i == " ":
                n = " "
        encoded +=n
    return encoded


def decode(enter, num):
    decoded = ""
    for i in enter:
        for k in abc:
            if i == k:
                index = abc.index(k)
                newnum = index - num
                n = abc[newnum]
            elif i == " ":
                n  = " "
        decoded +=n
    return decoded




cont = True
while cont:
    menu = print(" 1. Encode a string. \n 2. Decode a string. \n 3. Quit.")
    choice = int(input("Please choose a number. "))
    if choice == 1:
        zonk = input("Please enter your string. ")
        num = int(input("Choose how many you want to set it off by. "))
        print(encode(zonk, num))
    elif choice == 2:
        bonk = input("Please enter your code. ")
        num = int(input("Choose encryption number. "))
        print(decode(bonk, num))
    elif choice == 3:
        cont = False
        break

