# #string

# #literal assignment

first = "dave"
last = "gray"

# # print(type(first))

# # print(type(first) == str)

# # print (isinstance(first,str))

# # pizza = str("peproni")
# # print(type(pizza))

# # print(type(pizza) == str)

# # print(isinstance(pizza,str))
# # full_name = first+" " + last

# # full_name += "!"
# # print(full_name)
# # decade = str(1990)
# # print(decade)
# multilin = """
# hey, how are you          


# iwas just chaking
#                             all good


# """
# print(len(multilin))
# multilin += "                               "
# multilin = "                               " + multilin
# print(len(multilin))
# print(len(multilin.strip()))
# print(len(multilin.lstrip()))
# print(len(multilin.rstrip()))
# # sentence = "i'm back at work!\they1\n\nwhere\'s these at"
# # print(sentence)

# print(" ")

# title = "menue".upper()
# print(title.center(20, "="))
# print("Coffee".ljust(16, ".") +"$1".rjust(4))
# print("Tea".ljust(16, ".") +"$2".rjust(4))
# print("coffeee".ljust(16, ".") +"$3".rjust(4))
# print(first[0])
# print(first[1:-1])
print(first.startswith("d"))
print(first.endswith("e"))

myvalue = True
x = False
print(type(x))
print(isinstance(myvalue, bool))

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

gpa = 3.28
y = float(1.14)

comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)
import math
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))


zipcode = "10001"
zipvalue = int(zipcode)
print(zipvalue)
