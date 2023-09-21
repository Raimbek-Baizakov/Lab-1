m = int(input("Введите количество элементов первого массива = "))
n = int(input("Введите количество элементов второго массива = "))
array_1 = []
array_2 = []
for i in range(1,m + 1,1):
    x = int(input("Введите %d й элемент" %i))
    array_1.append(x)
    
for j in range(1,n + 1,1):
    y = int(input("Введите %d й элемент" %j))
    array_2.append(y)

def input_block(a,b):
    # Добавляем второй массив к концу первого с помощью суммы двух массивов
    print(array_1 + array_2) 
     


input_block(array_1,array_2)

