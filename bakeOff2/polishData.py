rd=open("receivedData.txt","r+")


data=rd.readlines()
lastOne=data[-1]

print("The last One: ", lastOne)
lastOne=lastOne[:-1]
lastOne=lastOne[:-1]
lastOne=lastOne[1:]
print("ele removed: ", lastOne)





 
