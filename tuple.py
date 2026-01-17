# #======== tuple ========
# # tuple is not mutable /immutable
tup = (1,2,3,4,5,5)
# print(tup)

# ======== tuple method =======
temp = list(tup)
temp.append(6)
temp.pop(5)
temp.reverse()
temp[2]=9
tup = tuple(temp)
print(tup)
print(type(tup))
# ========================
tup1 = (1,2,3,4,5)
concate = tup +tup1
print(concate)
# ========================
# c = concate.count(1)
# c = concate.index(1)
c = concate.index(1,3,8)
print(c)