# dictionaries
band = {
    "vocals": "plant", 
    "guitar" : "page",
}

band2 = dict(vocals="plant", giutar = "page")

print(band)
print(type(band2))

print(band['vocals'])
print(band.get("guitar"))

print(band.keys())
print(band.values())

#print all key valeues with there values

print(band.items())

#verify

print("guitar"in band)
 
 
#change values

band["vocals"] = "converdale"
band.update({"bass": "Jpj"})

print(band)

#remove items

print(band.pop("bass"))
print(band)

band["drums"] = "bonham"
print(band)

print(band.popitem())#tuple

print(band)

# deleate and clear
band["drums"] = "bonham"
del band["drums"]

print(band)

band2.clear()
print(band2)

del band2

#coping dictionaries


# band2 = band #create a reference
# print("bad copy")
# print(band2)
# print(band)

# band2["drums"] = "dave"
# print(band)

band2 = band.copy()
band2['drums'] = "dave"
print("good copy")
print(band)
print(band2)

#using the dict constructor function
band3 = dict(band)
print("good copy12")
print(band3)

#constructing nested dictionaryes

member1 = {
    "name": "plant",
    "instrument":"vocals"
}
member2 = {
    "name": "page",
    "instrument":"guitar"
}
band = {
    "member1": member1,
    "member2":member2
}
print(band)
print(band["member1"]["name"])

#moving on to sets

nums = {1,2,3,4}

nums0 = set((5,6,7,8))

print(nums)
print(nums0)
print(type(nums))
print(len(nums))

#no duplicates allowed
nums = {1,2.2,3,4}
print(len(nums))

#true is a dupe of 1, false is a dup of 0
nums = {1, True, 2,False, 3, 4,0}
print(nums)

#cheak avalue is in aset
print(4 in nums)

#but you can't refer to an elementin the set with an index position or a key

# adding a new element to a set
nums.add(8)
print(nums)

# add elements frome one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)

# you can use update with lists,tuples, dics 9355 

#merge sets to create new sets
one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print(mynewset)

# keep only the duplicates
one = {1,2,3}
two = {5,6,7,3,2}

one.intersection_update(two)
print(one)

# keep everything except the dupliates
one = {1,2,3}
two = {4,3,2}

one.symmetric_difference_update(two)
print(one)

