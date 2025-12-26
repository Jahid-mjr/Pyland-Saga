#DEBUG
#INFO
#WARNING
#ERROR
#CRITICAL

# import logging
# logging.basicConfig(filename= "test.log", level= logging.DEBUG)

# logging.info("This is my INFO log")
# logging.warning("This is my warning log")
# logging.error("This is my error log")
# logging.debug("this is my debug log")


import logging
logging.basicConfig(filename= "test.log", level= logging.DEBUG, 
                    format= "%(asctime)s %(levelname)s %(message)s")

num1 = int(input("Input a number: "))
num2 = int(input("Input another number: "))
logging.info("User input %s and %s", num1, num2)



try:
    result = num1/num2
    print(result)
    logging.info("User got : %s", result)
except Exception as e:
    print(e)
    logging.error("Error is happened")
    logging.exception("The error is " + str(e))
