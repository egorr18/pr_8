c = int(input("Введіть число c: "))
numbers = [
    x for x in range(2, c+1)
    if len([d for d in range(1, x + 1) if x % d == 0]) > 2
]
print("Складні", numbers)