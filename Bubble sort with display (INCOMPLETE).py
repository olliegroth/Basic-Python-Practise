import time
def bubblesort():
    sorted = False
    user_entry=input("Enter your list of numbers, with a comma separating each number: ")
    numbers = user_entry.split(",")
    for place, value in enumerate (numbers):
        numbers[place] = int(value)
    
    while not sorted:
        changes = False
        time.sleep(0.5)
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                changes = True
            else:
                pass
        if changes == True:
            print(numbers)
        if not changes:
            sorted = True
    return(numbers)

print(bubblesort())