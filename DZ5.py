# Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)

import random
list = [1,2,3,4,5]
print ("Задан список: " + str(list))
for i in range(len(list)-1, 0, -1):
    j = random.randint(0, i + 1) 
    list[i], list[j] = list[j], list[i] 
print ("Перемешанный список: " +  str(list))