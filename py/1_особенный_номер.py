import re

def getGoodNum(srcStr):
    outStr = ""
    findNums = re.findall(r'(\b\d{2,4}\b)\\(\b\d{2,5}\b)', srcStr)
    for i in findNums:      
       outStr+= f'{int(i[0]):04}' + "\\"+f'{int(i[1]):05}' + "\n"
    return outStr

def main():
    inputStr = r'Адрес 5467\456. Номер 405\549'
    print(getGoodNum(inputStr))

main()
