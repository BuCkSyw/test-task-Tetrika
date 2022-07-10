def task(x1, y1, x2, y2, x3, y3, x4, y4):
    # определеям верхнюю координату x нижнего прямоугольника
    max1x = max(x1, x2)
    # определеям верхнюю координату y нижнего прямоугольника
    max1y = max(y1, y2)
    # определеям нижнюю координату x верхнего прямоугольника
    min2x = min(x3, x4)
    # определеям нижнюю координату y верхнего прямоугольника
    min2y = min(y3, y4)
    if min2x <= max1x and min2y <= max1y:
        S = (max1x-min2x)*(max1y-min2y)
        print('True')
        print('Площадь пересечения = ', end='')
        return S
    else:
        return False


print(task(1, 1, 5, 5, 3, 3, 9, 9))
