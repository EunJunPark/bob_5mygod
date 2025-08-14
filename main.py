import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    pass  # 구현 예정

def insertion_sort(arr):
    pass  # 구현 예정

def merge_sort(arr):
    pass  # 구현 예정

def quick_sort(arr):
    pass  # 구현 예정

if __name__ == "__main__":
    # data.txt 읽기
    with open("data.txt", "r") as f:
        data = list(map(int, f.read().split()))

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