cels_input = input("Введіть температуру С: ")
cels = [float(x) for x in cels_input.split()]
fahrenheit = [C * 9/5 + 32 for C in cels]
print("у Фаренгейтах:", fahrenheit)