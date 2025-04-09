# num=1
# while num<=10:
#     print(num)
#     num

# nos=str(input("take anything:"))
# while nos:
#      if nos=="exit":
#         break
#      else:
#         print(nos)
#         nos=str(input("take anything:"))
# for i in range(1,6):
#     for j in range(1,6):
#         k= i*j
#         print(k)
#         # print(len
# num = int(range (9))
# for x in num:
#     if num<=5:
#         print(6*x-1)
#     else:
#         print(6*x+1)


# for x in range(11):
#     print(x*2)    

# num = [1, 3, 5, -5, -2, -9, 10]
# total = sum(x for x in num
#             if x > 0)  # Sum only positive numbers
# print(total)

# num=[5,4,6,7,8,10,23,24]
# lag = max(num)
# # print(lag)
# for x in num:
#     if lag==x:
#         print(lag)
    
def find_highest(numbers):
    lag = max(numbers)  # Assume first number is highest
    for num in numbers:
        if lag==num:
            return lag

def find_lowest(numbers):
    low = min(numbers) # Assume first number is lowest
    for num in numbers:
        if low==num:
            return low

def find_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total / count if count > 0 else 0  # Avoid division by zero

# Example list of numbers
num_list = [5, 4, 6, 7, 8, 10, 23, 24]

# Display results
print("Highest number:", find_highest(num_list))
print("Lowest number:", find_lowest(num_list))
print("Average:", find_average(num_list))
