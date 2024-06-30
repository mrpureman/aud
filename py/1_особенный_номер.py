import re

def getGoodNum(srcStr):
    outStr = ""
    # ищем совпадения регуляркой. Принимаем только 2-4\2-5 числа.
    findNums = re.findall(r'(\b\d{2,4}\b)\\(\b\d{2,5}\b)', srcStr)
    
    # перебираем и форматируем числа, скидываем в строку.
    for i in findNums:      
       outStr+= f'{int(i[0]):04}' + "\\"+f'{int(i[1]):05}' + "\n"
    return outStr

def main():
    inputStr = r'Адрес 5467\456. Номер 405\549'
    print(getGoodNum(inputStr))

main()
