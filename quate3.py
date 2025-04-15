b = int(input("Введіть число b: "))
even_squares = [x**2 for x in range(1, b+1) if x % 2 == 0]
print("Квадрати парних чисел:", even_squares)