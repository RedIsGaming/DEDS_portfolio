from __future__ import annotations      # niet nodig voor python 3.10 en hoger

import random


def bubblesort(data: list[int]) -> None:
    for _ in range(len(data)):
        for index in range(len(data) - 1):
            if data[index] > data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]


def mergesort(data: list[int]) -> None:
    if len(data) <= 5:
        return bubblesort(data)

    left = data[:len(data) >> 1]
    right = data[len(data) >> 1:]

    mergesort(left)
    mergesort(right)

    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result += left + right

    for i in range(len(data)):
        data[i] = result[i]


def bogosort(data: list[int]) -> None:
    def check() -> bool:
        for item1, item2 in zip(data[:-1], data[1:]):
            if item1 > item2:
                return False
        return True

    while not check():
        random.shuffle(data)


def main() -> None:
    print("Shuffling...")
    items = [random.randint(-100, 100) for _ in range(20)]

    import timeit

    print(f"Sorting the following items: {items}")
    print("Bubble-sorting...")

    items = [random.randint(-100, 100) for _ in range(20)]
    bubblesort(items)   # 0.276 seconden voor 10000 keer (20 items)
    print(f"Sorted items: {items}")
    print("Duration:", timeit.timeit("bubblesort(items)", "from __main__ import bubblesort\nimport random\nitems = [random.randint(-100, 100) for _ in range(20)]", number=10000))

    print("Shuffling...")
    random.shuffle(items)

    print("Merge-sorting...")
    mergesort(items)    # 0.218 seconden voor 10000 keer (20 items)
    print(f"Sorted items: {items}")
    print("Duration:", timeit.timeit("mergesort(items)", "from __main__ import mergesort\nimport random\nitems = [random.randint(-100, 100) for _ in range(20)]", number=10000))

    print("Shuffling...")
    random.shuffle(items)

    print("Bogo-sorting...")
    print("Ik moest er minstens 20 items in stoppen, dus dit kan even duren...")
    bogosort(items)     # Veel te lang seconden voor 1 keer (20 items)
    print(f"Sorted items: {items}")
    print("Duration:", timeit.timeit("bogosort(items)", "from __main__ import bogosort\nimport random\nitems = [random.randint(-100, 100) for _ in range(20)]", number=1))


if __name__ == "__main__":
    main()
