

def getMaxNum(listOfNums):
    #listOfNums = sorted(listOfNums)
    # to Int
    listOfNumsInt = [int(item) for item in listOfNums] 
    #print(listOfNums)

    lenNums = max([len(str(item)) for item in listOfNumsInt])
    tempList = []
   # print(lenNums)


    zeroIndexes = []
    templist2 = []
    for i in listOfNums:
        if len(i) < lenNums:
            tempList.append(i + ((lenNums - len(i)) *'0'))

            zeroIndexes.append(int(str(1)  + ((lenNums - len(i)) *'0')))
            templist2.append([int(i + ((lenNums - len(i)) *'0')), int(str(1)  + ((lenNums - len(i)) *'0'))])
        else:
            tempList.append(i)
            zeroIndexes.append(1)
            
    tempList = sorted(tempList, reverse=1)
    
    print(lenNums)
    print(zeroIndexes)
    
    listOfNums = []
    print("templis2= " + str(templist2))
    for i in tempList:
        x = int(i)
        for j in templist2:
        
            if int(i) == j[0]:
                x = round(j[0] / j[1])
                

        listOfNums.append(x)
           


    return listOfNums # "".join(map(str, listOfNums))


    




def main():
    nums = ['562', '03', '83'] #, '05', '67', '004']
    print(getMaxNum(nums))


main()
ss