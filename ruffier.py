# Модуль для расчета результатов

# Здесь должен быть твой код
def ruffier_index(P1, P2, P3):
    IR = (4*(P1+P2+P3) - 200)/10
    return IR


def ruffier_level(age):
    norm_age = (min(age, 15) - 7 ) // 2
    result = 21 - norm_age * 1.5
    return result


def ruffier_result(index, level):
    if index >= level:
        return 0
    level -= 4
    if index >= level:
        return 1
    level -= 5
    if index >= level:
        return 2
    level -= 5.5
    if index >= level:
        return 3
    return 4

def test (P1, P2, P3, age):
    r_index = ruffier_index(P1, P2, P3)
    result = ruffier_result(r_index, ruffier_level(age))
    if result == 0:
        return "Низкий"
    elif result == 1:
        return "Удв"
    elif result == 2:
        return "Средний"
    elif result == 3:
        return "Выше среднего"
    elif result == 4:
        return "Высокий"