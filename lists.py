users = ['dave', 'john','sarh']


data = ['dave', 42 , True]

elist = []


users.append('Elsa')




print(len(users)) 
users += ['jason']


users.extend(['Robert', 'Jimmy'])

# print(users)


users.insert(0, 'bob')

users[2:2] = ['eddie', 'alex']

print(users)

users[1:3] = ['Robert', 'Jpj']


users.remove('bob')

users.remove('Robert')

print(users.pop())
print(users)
# del(users[0])
data.clear()
print(data)

users.sort(key = str.lower)
print(users)


nums  = [4,42,35,3]
# nums.reverse()

# nums.sort(reverse=True)
# print(nums)


# print(sorted(nums, reverse=True))
numscopy= nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)

print(type(nums))

mylist = list([1, "Neilarmstrong", True])
print(mylist)

tuplee = tuple(('dave', 42 , True))

bever = (1,2,3,4)

print(tuplee)
print(bever)


newlist  = list(tuplee)

newlist.append('neil')
newtuple = tuple(newlist)

print(newtuple)

(one, two, three, *hey) = bever

print(one,three)