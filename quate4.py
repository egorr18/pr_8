text = input("Введіть текст: ")
wlengths = [len(word) for word in text.split()]
print("Довжини слів:", wlengths)