
#Read Mode
#----------------------------
# f = open("test.txt", "r")
# data = f.read()
# print(data)
# f.close()


#Write Mode
#------------------------------
# f = open("jahid.txt", "w")
# f.write("hello")
# f.close()


#Append Mode
#------------------------------
# f = open("test.txt", "a")
# f.write("\nAmi Jani na ami ke")
# f.close()


#Read & Write Mode
#----------------------------
# f = open("test.txt", "r+")
# data = f.read()
# print(data)
# f.write("\nUpdate korsi")
# f.close()

# f = open("test.txt", "r")
# data1 = f.read()
# print(data1)
# f.close()


#-------------------------------
# with open("test.txt", "r") as f :
#     data = f.read()
#     print(data)


#File Remove
#------------------------------
# import os
# os.remove("t.txt")


#Read line by line
#------------------------------

# with open("test.txt", "r") as f:
#     data = f.readline()
#     print(data)
#     data1 = f.readline()
#     print(data1)


#Read Word By Word
#------------------------------
# with open("test.txt", "r") as f:
#     data = f.read(30)
#     print(data)


#Replace Word
#-------------------------------
# with open("replace.txt", "r") as f:
#     data = f.read()
#     new_data = data.replace("Jahid","Rayhan")
#     print(new_data)

# with open("replace.txt", "w") as f:
#     f.write(new_data)
