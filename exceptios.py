
class JustNotCoolEroor(Exception):
    pass


x=2
try:
    raise JustNotCoolEroor("this is not cool man")
    # raise Exception("i'm acustom exception")
    #if not type(x) is str:
    #    raise TypeError("only string are allowed")
    # print(x/0)
except NameError :
    print("there is an error ")
except ZeroDivisionError:
    print("please don't try to divide numbers by zero")
except Exception as error:
    print(error)
else:
    print(" no errors")
finally:
    print("the final messsage after both error or withouterror")
    
    

