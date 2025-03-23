from typing import List

def average(numbers: List[float]) -> float:
    if len(numbers) == 0:
        raise ValueError("Lista nie może być pusta")

    for n in numbers:
        if not isinstance(n, (float, int)):
            raise TypeError("Elementy muszą być liczbami")

    return sum(numbers) / len(numbers)

# Testowanie
try:
    lst = [1.4, 2]
    print(average(lst))  # Przykład z pustą listą
except (TypeError, ValueError) as e:
    print(e)
