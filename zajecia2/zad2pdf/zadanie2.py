def average(numbers: list[float]) -> float:
    if len(numbers) == 0:
        raise ValueError("Lista nie może być pusta")

    for n in numbers:
        if not isinstance(n, float):
            raise TypeError("Elementy musza byc liczbami typu float")

    return sum(numbers) / len(numbers)

try:
    list = []
    print(average(list))
except (TypeError, ValueError) as e:
    print(e)