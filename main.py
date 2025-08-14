import time

def bubble_sort(arr):
    pass  # 구현 예정

def selection_sort(arr):
    pass  # 구현 예정

def insertion_sort(arr):
    pass  # 구현 예정

def merge_sort(arr, depth=0):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left, depth + 1)
        merge_sort(right, depth + 1)

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

    if depth == 0:
        print(arr)
    

def quick_sort(arr):
    pass  # 구현 예정

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    print(arr)

if __name__ == "__main__":
    # data.txt 읽기
    with open("data.txt", "r") as f:
        data = list(map(int, f.read().replace(',', ' ').split()))

    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort),
    ]

    for name, func in algorithms:
        arr_copy = data.copy()
        start = time.time()
        func(arr_copy)
        end = time.time()
        print(f"{name}: {end - start:.6f} 초")