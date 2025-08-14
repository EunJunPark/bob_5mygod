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

def merge_sort(arr, depth=0):
    pass

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
