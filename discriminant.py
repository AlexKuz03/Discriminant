class discriminant:
    def __init__(self):
        pass

    def __is_correctly(self, a, b, c):
        try:
            float(a)
            1/float(a)
            float(b)
            float(c)
            return True
        except ValueError:
            return False
        except ZeroDivisionError:
            return False

    def counting_value(self, a, b, c):
        if not(discriminant.__is_correctly(self, a, b, c)):
            print("Ошибка, неверные значения")
        else:
            a = float(a)
            b = float(b)
            c = float(c)
            D = b ** 2 - 4 * a * c
            if D < 0:
              print("Корней нет")
            elif D == 0:
                x = -b / (2*a)
                print("Один корень, х =", x)
            else:
                x1 = (-b - D ** .5) / (2 * a)
                x2 = (-b + D ** .5) / (2 * a)
                print("Два корня, х1 =", x1, "x2 =", x2)

