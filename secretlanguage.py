a = input("Enter an secret code :: ")
words =a.split(" ")
choice = int(input("1. code \n 2. decode \n"))
if choice == 1:
    nwords = []
    b = input("enter an random text :: ")
    c = input("enter an random text :: ")
    for word in words:
        if len(word) >= 3:
            stnew = b + word[1:]+word[0] + c
            #     ^     ^
            #     |     first value of user
            #   start
            #  (start : stop : step)
            nwords.append(stnew)
            # print(words)
        else:
            nwords.append(word[::-1])
    print("encoded"," ".join(nwords))

else:
    nwords = []
    for word in words:
        if len(word) >= 6:
            stnew = word[3:-3]
            #     ^     ^
            #     |     first value of user
            #   start
            #  (start : stop : step)
            stnew  = stnew[-1]+ stnew[:-1]
            nwords.append(stnew)
            # print(words)
        else:
            nwords.append(word[::-1])
    print("decoded"," ".join(nwords))
        
