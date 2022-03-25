def ask():
    more = input("Do you want to make more usernames? ")
    if more.lower() == "yes":
        username()
    else:
        x = False

x = True
while x == True:
    def username():
        try:
            name = str(input("What is your name? "))
            n = name.split(" ")
            first = n[0]
            last = n[1]
            username = (str(first) + str(last))
            print("Your username is: "+username)
            ask()
            x = False
        except:
            print("Please use a space in your name\n")
    username()
