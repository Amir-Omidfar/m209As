



def polishMyData(): 
	rd=open("receivedData.txt","r+")#receivedData
	data=rd.readlines()
	lastOne=data[-1]

	#print("The last One: ", lastOne)
	lastOne=lastOne[:-1]
	lastOne=lastOne[:-1]
	lastOne=lastOne[1:]
	#print("ele removed: ", lastOne)

	pd=open("polishedData.txt","a+")#polishedData
	pd.write("\n")
	pd.write(lastOne)
	pd.close()
	rd.close()






 
