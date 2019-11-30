def insertion_sort(arr, n):
    for i in range(1, n):
        k = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > k:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j+1] = k
    print(arr)


if __name__ == "__main__":
    arr = [9, 5, 1, 4, 3]
    insertion_sort(arr, len(arr))
