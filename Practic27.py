def proga(a, b):
    digits = [int(d) for d in str(a)]
    count = len(digits)
    
    if b == "1":
        for j in range(count):
            for i in range(count - 1):
                if digits[i] > digits[i+1]:
                    digits[i], digits[i+1] = digits[i+1], digits[i] 
        print("Результат (Bubble Sort):", digits)

    elif b == "2":
        for i in range(count):
            min_idx = i
            for j in range(i + 1, count):
                if digits[j] < digits[min_idx]:
                    min_idx = j
            digits[i], digits[min_idx] = digits[min_idx], digits[i]         
        print("Результат (Selection Sort):", digits)
    
    elif b == "3":
        for i in range(1, count):
            key = digits[i]  
            j = i - 1
            while j >= 0 and digits[j] > key:
                digits[j + 1] = digits[j]
                j -= 1
            digits[j + 1] = key
        print("Результат (Insertion Sort):", digits)

while True:
     try:
        a =int(input("Введите числа в однру строку: "))
        b = input("Введите какой алгоритм сортировки выберите(1.Bubble Sort 2.Selection Sort): ")
        if b in ["1", "2", "3"]:
            break
        else:
             print("Такого алгоритма нет.")
     except ValueError:
          print("Ошибка в вводе данных.Повторите ввод.")
proga(a,b)