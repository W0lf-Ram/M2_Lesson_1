first = input('Введите первое число: ')
second = input('Ведите второе число: ')
third = input('Ведите третье число: ')
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)