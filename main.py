import time

def bubble_sort(arr):
    pass  # 구현 예정

def selection_sort(arr):
    pass  # 구현 예정

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