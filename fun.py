def hello_world():
    print("hellooo")
  
    
hello_world()


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return    
    return(num1+num2)


total = sum(7,2)
print(total)

# we use the args when we dont kno how many values we are passing like the num1 and num2 the * make it tuple
def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "John", "Sara")

#
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first= "muse", last = "debru")