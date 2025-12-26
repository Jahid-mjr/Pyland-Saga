# 1 Compile time Error
# 2 Logical Error
# 3 Run time Error




# Run time error handling:
 
# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter another number : "))

# try:
#     result = (num1/num2)
#     print(result)
# except Exception as e:
#     print("You can not divide a number by zero.")


# but ai ager tate sob error i zero divide error asbe

num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))

try:
    print("Open")
    result = (num1/num2)
    print(result)
    num3 = int(input("Enter another number : "))

except ZeroDivisionError as e:
    print("You can not divide a number by zero.")
except ValueError as e:
    print("Invalid Value")
except Exception as e:
    print(e)
finally:
    print("Close")

print("Made by Zero")