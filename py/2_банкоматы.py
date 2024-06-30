import math
def calcLen(atm_s, len_btwn_atm_s, new_atm_s):
    # чекаем ошибку ввода
    if len(len_btwn_atm_s) >= atm_s or  atm_s - 1 < len(len_btwn_atm_s) : return 'Incorrect length between atm'
    new_optimal_lens = []

    new_lens = (atm_s + new_atm_s) - 1
    # общее расстояние
    sumLens = sum(len_btwn_atm_s)

    # общую сумму делим количество расстояний 
    x = sumLens / new_lens

    for i in len_btwn_atm_s:
        # количество банкоматов-соседей для новых банкоматов
        atmN = math.trunc(i / x)
        # расстояние слишком мало (меньше 1) — не трогаем.
        if atmN == 0: atmN = 1

        # вставляем банкоматы и выводим новое расстояние
        for j in range(atmN):
            new_optimal_lens.append(round(i / atmN, 2))

    return new_optimal_lens

def main():
    atm_s = 5
    len_btwn_atm_s = [100, 30, 20, 80] 

    new_atm_s = 3
    print(calcLen(atm_s, len_btwn_atm_s, new_atm_s))
  
main()