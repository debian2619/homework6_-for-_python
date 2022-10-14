#enumerate
colors = ['red', 'green', 'blue']
ind = 1
for color in colors:
    print(str(ind) + '-й цвет: ' + color)
    ind += 1

print(colors)

colors = ['red', 'green', 'blue']
for i, item in enumerate(colors, 1):
    print(str(i) + '-ое значение равно ' + str(item))