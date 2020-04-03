try:
    # value = 10/0
    number = int(input("Enter a number: "))
    print(number)

# except:
#     print("Invalid Input") # too general
except ZeroDivisionError as err:
    print(err)
except ValueError as errVal:
    print(errVal)
