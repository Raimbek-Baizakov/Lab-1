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

index = int(input("С какого индекса первого массива вставить второй массив = "))

def input_block(a, b, c):
    # Вставляем второй массив в первый с помощью свойства индекса
    array_1[c:с] = array_2 # [c:c] это особенность индекса где второй массив вставляеться в первый начиная с номера "с" 
                           #и при этом сдвигает все элементы первого массива что находятся после "c" не удаляя их
input_block(array_1, array_2, index)


print("Результат после вставки:", array_1)

