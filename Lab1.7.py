m = int(input("Введите количество элементов  массива = "))

array = []
array_new = []

for i in range(1,m + 1,1):
    x = int(input("Введите %d й элемент" %i))
    array.append(x)
    

def del_prime(a,b):
    
    for num in a: #Берем каждый элемент массива
        k = 0
        for i in range(2, num) : #Проверям число элемента 
            if num % i == 0:
                k += 1  
        if k > 0: #Создаем условие через которые должны пройти НЕ простые числа
            b.append(num) #Добавляем элементы массива которые подлежат условию к>0
    return b #Возвращяем динамический массив без простых чисел


del_prime(array, array_new)

print("Результат после удаления:", array_new)




