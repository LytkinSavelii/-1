numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
Len_ = len(numbers)
left = sum(numbers[:4])
right = sum(numbers[5:])
Sum_ = left + right
Ave_ = Sum_/Len_
numbers[4] = Ave_
print("Измененный список:", numbers)
