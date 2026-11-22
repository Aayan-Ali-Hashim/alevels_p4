first_number = int(input("enter first number"))
second_number = int(input("enter second number"))
third_number = int(input("enter third number"))
if first_number >= second_number and first_number >= third_number:
    print(first_number)
elif second_number >= first_number and second_number >= third_number:
    print(second_number)
else:
    print(third_number)



