import time

def bubble_sort(arr):
    pass  # 구현 예정

def selection_sort(arr):
    pass  # 구현 예정

def insertion_sort(arr):
    pass  # 구현 예정

def merge_sort(arr):
    pass  # 구현 예정

def quick_sort(arr):
    def _quick_sort(a, low, high):
        if low < high:
            pivot_index = _partition(a, low, high)
            _quick_sort(a, low, pivot_index - 1)
            _quick_sort(a, pivot_index + 1, high)

    def _partition(a, low, high):
        pivot = a[high]
        i = low
        for j in range(low, high):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[high] = a[high], a[i]
        return i

    _quick_sort(arr, 0, len(arr) - 1)

    print("Quick Sort Output:", arr)


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        raw = f.read().replace(",", " ")
        data = list(map(int, raw.split()))

    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
    ]

    for name, func in algorithms:
        arr_copy = data.copy()
        start = time.time()
        func(arr_copy)
        end = time.time()
        print(f"{name}: {end - start:.6f} 초")