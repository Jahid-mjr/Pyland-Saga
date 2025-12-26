from string import *
from itertools import product

count = 0
val = ascii_letters + digits + punctuation



with open("Password_Warehouse.txt", "a") as file:
    for i in range(3,4):
        for j in product(val, repeat= i):
            word = "".join(j)
            
            try:
                file.write(word)
                file.write("\n")
                count = count +1
                print(f"{count} No. Password is : {word}")  # count pisaiya jaibe 
            except Exception as e:
                print(e)