m = int(input("Введите количество элементов  массива = "))

array = []
positive = []
negative = []
zero = []

for i in range(1,m + 1,1):
    x = int(input("Введите %d й элемент" %i))
    array.append(x)
    

def distribution(a,p,n,z):
    for num in a: #Берем каждый элемент заданного массива на проверку
        if num > 0: 
            p.append(num) 
        if num == 0:
            z.append(num)
        if num < 0:
            n.append(num)
    return p, n, z #Возвращяем каждый массив
    
    


distribution(array,positive,negative,zero)

print("Массив с положительными числами = " ,positive)
print("Массив с отрицательными числами = " ,negative)
print("Массив с нулевыми числами = " ,zero)




