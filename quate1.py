a= int(input("Введіть число a: "))
numbers = [x for x in range(1, a+1) if x % 3 == 0 and x % 5 != 0]
print("Кратні 3 і некратні 5:", numbers)