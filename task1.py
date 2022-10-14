#  Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример:
# Входные данные: 'ываабв лповап абвцукв алоабвабв ываываыв'
# Выходные данные: 'лповап ываываыв'
#lambda
txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')

# Вместе с лямбдой и фильтром
result = list(filter(lambda e: 'абв' not in e, lst))
print(result)