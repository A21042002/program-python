f1 = open("pr.txt","r")

# print(f1.write("hello we are writing in code that will show in text file\n"))
# print(f1.write("hiii we are writing in code that will show in text file\n"))
# print(f1.write("show in text file\n"))
print(f1.read())
print(f1.read(5))
print(f1.readlines(5))
f1.close()