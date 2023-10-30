# Обработка исключений

try:
    print(10 / 10)
except ZeroDivisionError:
    print('Деление на ноль невозможно')
except NameError:
    print('Переменная не определена')
except ValueError:
    print('Невозможно привести к целому числу')
except TypeError:
    print('Ошибка типа данных')
except:
    print('Произошла непредвиденная ошибка')
