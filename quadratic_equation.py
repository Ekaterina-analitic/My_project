print('Программа для решения квадратных уравнений')

incorrect_data = True
while incorrect_data:
    try:
        a = int(input('Введите число a: '))
        b = int(input('Введите число b: '))
        c = int(input('Введите число c: '))
        incorrect_data = False
    except ValueError:
        print('Введены некорректные данные. Введите числовые значения для коэффициентов уравнения.')

D = b ** 2 - 4 * a * c
print('Дискриминант D = ', D)
if D > 0:
    x1 = (-b + D ** 1 / 2) / 2 * a
    x2 = (-b - D ** 1 / 2) / 2 * a
    print('Уравнение имеет два корня:')
    print('x1 = ', x1)
    print('x2 = ', x2)
elif D == 0:
    x = -b / 2 * a
    print('Уравнение имеет один корень:')
    print('x1 = ', x)
else:
    print('Уравнение не имеет действительных корней')
