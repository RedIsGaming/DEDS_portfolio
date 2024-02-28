# Stap 1: Bekend worden met de datastructuren, done
# Stap 2: Kies er 3, ik ga voor list, set en str
# Stap 3:
# - Bubblesort (list), O(n^2)
# - Sum de unieke waardes (set), O(n)
# - Get first character (str), O(1)
from __future__ import annotations


def bubblesort(data: list) -> None:
     for _ in range(len(data)):
        for index in range(len(data) - 1):
            if data[index] > data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]


def sum_unique_values(data: list[int]) -> int:
    # return sum(set(data))
    totaal = 0
    for item in set(data):
        totaal += item
    return totaal


def get_first_charcter(data: str) -> str:
    return data[0]
