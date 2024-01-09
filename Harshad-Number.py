# Harshad Number

n = int(input("Enter n: ")) #nth harshad number
harshad = [] #All harshad numbers
numbers = [] #Sum of current iterations digits
i = 1
while len(harshad) != n: #Adding to harshad list until the nth number
    ii = 0
    a = 0
    numbers = [int(x) for x in str(i)] #Seperates the numbers in i
    for ii in numbers: #Sums the numbers
        a = a + ii
    if i%a == 0: #If it is perfectly divisible add it to harshad list
        harshad.append(i)
    i+=1 #Repeat until the list is long enough
print("\nThe",str(n)+"th harshad number is",harshad[n-1])