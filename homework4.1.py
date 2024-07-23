my_string = input('Введите ваши любимые цвета(хотя бы два): ')
def findLen (my_string):
    x = 0
    for i in my_string:
        x += 1
    return x
print(findLen(my_string))
print(len(my_string))
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ', ''))
print(my_string[0])
print(my_string[-1])