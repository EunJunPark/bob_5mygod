import time

def bubble_sort(arr):
    pass  # 구현 예정

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
    pass  # 구현 예정

def merge_sort(arr):
    pass  # 구현 예정

def quick_sort(arr):
    pass  # 구현 예정

if __name__ == "__main__":
    # data.txt 읽기
    with open("data.txt", "r") as f:
        data = list(map(int, f.read().replace(",", " ").split()))

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