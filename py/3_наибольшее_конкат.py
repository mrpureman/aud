def getMaxNum(listOfNums):

    # в число
    listOfNumsInt = [int(item) for item in listOfNums] 

    # сколько разрядов?
    lenNums = max([len(str(item)) for item in listOfNumsInt])
    tempList = []
    templist2 = []

    # добавляем нули к числу
    for i in listOfNums:
        if len(i) < lenNums:
            tempList.append(i + ((lenNums - len(i)) *'0'))
            
            # запоминаем число и его делитель, чтобы потом разделить
            templist2.append([int(i + ((lenNums - len(i)) *'0')), int(str(1)  + ((lenNums - len(i)) *'0'))])
        else:
            tempList.append(i)

    # сортируем         
    tempList = sorted(tempList, reverse=1)

    listOfNums = []

    # Если число есть — делим его на 10, 100, 1000 (зависит от количества разрядов)
    for i in tempList:
        x = i
        for j in templist2:
        
            if int(i) == j[0]:
                x = round(j[0] / j[1])
                
        listOfNums.append(x)
          
    return "".join(map(str, listOfNums))

def main():
    nums = ['41', '4', '005' , '89'] #, '05', '67', '004']
    #nums = ['03', '25', '1' , '07'] #, '05', '67', '004']
    
    print(getMaxNum(nums))


"""    from internet 
    sz = sum(map(len, nums))  # длина сцепленного числа
    dp = [('', nums)] * (sz + 1)  # буфер для динамического программирования
    for i, (head, tail) in enumerate(dp):
        for s in tail:
            head_s, j = head + s, i + len(s)
            if j <= sz and dp[j][0] < head_s:
                new_tail = tail[:]
                new_tail.remove(s)
                dp[j] = (head_s, new_tail)
    print(dp[sz][0])
    """

main()
