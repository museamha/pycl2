squared = lambda num : num*num
# lambda num:num *num


print(squared(2))

addtwo = lambda num:num +2
#lambda num:num +2

print(addtwo(12))

sum_total = lambda a,b:a+b
print(sum_total(3,4))

################
# when to use lamda

def funcbulder(x):
    return lambda num: num + x

addten = funcbulder(10)
addtwenty = funcbulder(20)

print(addten(7))
print(addtwenty(7))

####################
# what is a higher order function: it is a function that takes other functions as argumrnts or a function that retuns a function as its value

# when usind map the fist argument is the function and he second argument is the data collection method like tulips dictionaries and others

numbers = [3,4,5,12,11,34,56]

squared_nums = map(lambda num:num*num, numbers)

print(list(squared_nums))

##############################
#

odd_nums = filter(lambda num:num % 2 !=0, numbers)
print(list(odd_nums))

#############################

from functools import reduce


numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc+curr, numbers)

print(total)