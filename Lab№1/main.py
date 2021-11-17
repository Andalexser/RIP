import sys
import math

def get_roots(a, b, c):
    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % discr)

    if discr > 0:
        y1 = (-b + math.sqrt(discr)) / (2 * a)
        y2 = (-b - math.sqrt(discr)) / (2 * a)
        if y1 > 0:
            x1 = math.sqrt(y1)
            x2 = ((-1) * math.sqrt(y1))
            print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
            if y2 > 0:
                x3 = math.sqrt(y2)
                x4 = ((-1) * math.sqrt(y2))
                print("x3 = %.2f \nx4 = %.2f" % (x3, x4))
            elif y2 == 0:
                x3 = 0.0
                print("x3 = %.2f" % (x3))
            else:
                print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
        elif y1 == 0:
            x1 = 0.0
            print("x1 = %.2f" % (x1))
            if y2 > 0:
                x2 = math.sqrt(y2)
                x3 = ((-1) * math.sqrt(y2))
                print("x2 = %.2f \nx3 = %.2f" % (x2, x3))
            elif y2 == 0:
                print("x = %.2f" % (x1))
            else:
                print("x = %.2f" % (x1))
        elif y1 < 0:
            if y2 > 0:
                x1 = math.sqrt(y2)
                x2 = ((-1) * math.sqrt(y2))
                print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
            elif y2 == 0:
                x = 0.0
                print("x = %.2f" % (x))
            elif y2 < 0:
                print("Корней нет")
    elif discr == 0:
        y = -b / (2 * a)
        if y > 0:
            x1 = math.sqrt(y)
            x2 = ((-1) * math.sqrt(y))
            print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
        elif y == 0:
            x = 0.0
            print("x = %.2f" % (x))
        else:
            print("Корней нет")
    else:
        print("Корней нет")
    return discr


def main():
    '''
    Основная функция
    '''
    f = 0
    a = input("a = ")
    if a.isdigit():
        a = float(a)
    else:
        f = 1
        while f == 1:
            try:
                f = 0
                a = float(a)
            except ValueError:
                f = 1
                print("Неправильно введены данные")
                a = input("a = ")
    b = input("b = ")
    if b.isdigit():
        b = float(b)
    else:
        f = 1
        while f == 1:
            try:
                f = 0
                b = float(b)
            except ValueError:
                f = 1
                print("Неправильно введены данные")
                b = input("b = ")
    c = input("c = ")
    if c.isdigit():
        c = float(c)
    else:
        f = 1
        while f == 1:
            try:
                f = 0
                c = float(c)
            except ValueError:
                f = 1
                print("Неправильно введены данные")
                c = input("c = ")
    # Вычисление и вывод корней
    roots = get_roots(a, b, c)

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
wait = input("PRESS ENTER TO CONTINUE.")

