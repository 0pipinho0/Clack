import main as m

def calc():
    operation = input("Введите нужную вам категорию (Математика/Геометрия):")
    if operation.lower() == "математика":
        deistvie = input("Введите операцию ( + - * / ):")
        if deistvie == "+":
            a = int(input("Введите a:"))
            b = int(input("Введите b:"))
            return m.plus(a, b)
        elif deistvie == "-":
            a = int(input("Введите a:"))
            b = int(input("Введите b:"))
            return m.minus(a, b)
        elif deistvie == "*":
            a = int(input("Введите a:"))
            b = int(input("Введите b:"))
            return m.umno(a, b)
        elif deistvie == "/":
            a = int(input("Введите a:"))
            b = int(input("Введите b:"))
            return m.delit(a, b)
        else:
            return "Sorry, what the hell are you talking about ?"
    elif operation.lower() == "геометрия":
        deistvie_geom = input("Введите операцию (Площадь круга, Площадь прямоугольника, Периметр прямоугольника):")
        if deistvie_geom == "Площадь круга":
            r = int(input("Введите радиус: "))
            return m.circle(r)
        if deistvie_geom == "Площадь прямоугольника":
            a = int(input("Введите сторону a:"))
            b = int(input("Введите сторону b:"))
            return m.ploshad(a, b)
        if deistvie_geom == "Периметр прямоугольника":
            a = int(input("Введите сторону a:"))
            b = int(input("Введите сторону b:"))
            c = int(input("Введите сторону c:"))
            d = int(input("Введите сторону d:"))
            return m.perimetr(a, b, c, d)
    else:
        return "Sorry, what the hell are you talking about ?"

