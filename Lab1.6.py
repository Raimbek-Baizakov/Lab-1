m = int(input("Введите количество элементов  массива = "))

array_1 = []

for i in range(1,m + 1,1):
    x = int(input("Введите %d й элемент" %i))
    array_1.append(x)

index_1 = int(input("С какого индекса первого массива удалить элементы = "))
index_2 = int(input("До какого индекса первого массива удалить элементы = "))

def input_block(a, c, d):
    # Удаляем элементы массива с помощью свойства индекса
    del a[c:d]

input_block(array_1, index_1, index_2)


print("Результат после удаления:", array_1)


