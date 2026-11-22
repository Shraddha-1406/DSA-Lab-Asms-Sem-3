
# Heap Sort using Max Heap and Min Heap

def heapify(arr, n, i, is_max):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if is_max:
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
    else:
        if left < n and arr[left] < arr[largest]:
            largest = left
        if right < n and arr[right] < arr[largest]:
            largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, is_max)


def heap_sort(arr, is_max):
    n = len(arr)

    # Build Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, is_max)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, is_max)

    return arr


numbers = list(map(int, input("Enter numbers: ").split()))

max_heap_arr = numbers.copy()
min_heap_arr = numbers.copy()

print("Ascending Order (Max Heap):",
      heap_sort(max_heap_arr, True))

print("Descending Order (Min Heap):",
      heap_sort(min_heap_arr, False))
