import time

def bubble_sort(arr):
    start = time.time()
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end = time.time()
    print("\n==========BUBBLE SORT==========")
    print(arr)
    print(f"Bubble Sort 소요시간 : {end - start:.6f} 초")

def selection_sort(arr):
    start = time.time()
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    end = time.time()
    print("\n==========SELECTION SORT==========")
    print(arr)
    print(f"Selection Sort 소요시간 : {end - start:.6f} 초")


def insertion_sort(arr):
    start = time.time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    end = time.time()
    print("\n==========INSERTION SORT==========")
    print(arr)
    print(f"Insertion Sort 소요시간 : {end - start:.6f} 초")
    

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
        print("\n==========MERGE SORT==========")
        print(arr)
        

def quick_sort(arr):
    start = time.time()
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
    end = time.time()
    print("\n==========QUICK SORT==========")
    print(arr)
    print(f"Quick Sort 소요시간 : {end - start:.6f} 초")


def heap_sort(arr):
    start = time.time()
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
    end = time.time()
    print("\n==========HEAP SORT==========")
    print(arr)
    print(f"Heap Sort 소요시간 : {end - start:.6f} 초")
    
if __name__ == "__main__":
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
        if name == "Merge Sort":
            start = time.time()
            func(arr_copy)
            end = time.time()
            print(f"Merge Sort 소요시간 : {end - start:.6f} 초")
            continue
        func(arr_copy)
