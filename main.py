import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    """선택 정렬을 수행합니다. (리스트를 인자로 받습니다)"""
    n = len(arr)
    # 배열의 전체 요소를 순회 (마지막 요소는 자동으로 정렬됨)
    for i in range(n - 1):
        # 정렬되지 않은 부분에서 가장 작은 값의 인덱스를 찾음
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 찾은 가장 작은 값을 현재 위치(i)의 값과 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(' '.join(map(str, arr)))

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
    print(arr)
    print(f"Insertion Sort 소요시간 : {end - start:.6f} 초")
    

def merge_sort(arr, depth=0):
    pass

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
