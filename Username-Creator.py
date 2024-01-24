import re

def username():
    try:
        name = str(input("What is your name? "))
        splitName = name.split(" ")
        generatedUsername = f'{str(splitName[0])}.{str(splitName[1])}'
        print(f'Your username is: {generatedUsername}')
    except: # Use regex to make sure users enter their name in name (space) surname format :)
        print("Please use a space in your name\n")

while True:
    doYouWantUsername = input("Do you want to make (another) a username? ")
    if doYouWantUsername.lower() == "yes" or doYouWantUsername.lower() == "y":
        username()
    else:
        exit()