import time

def bubble_sort(arr):
    pass  # 구현 예정

def selection_sort(arr):
    pass  # 구현 예정

def insertion_sort(arr):
    pass  # 구현 예정

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

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