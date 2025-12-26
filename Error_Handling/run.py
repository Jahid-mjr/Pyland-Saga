while True:


    try:
        num1 = int(input("Enter a number : "))
        num2 = int(input("Enter another number : "))
        result = (num1/num2)
        print(result)       
    except ZeroDivisionError as e:
        print("You can not divide a number by zero.")
    except ValueError as e:
        print("Invalid Value")
    except Exception as e:
        print(e)
    finally:
        print("\nMade By Jahid\n")
