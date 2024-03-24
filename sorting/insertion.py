def insertion_sort(arr, n):
    for i in range(0, n):
        temp = arr[i]
        j = i
        while j > 0 and arr[j - 1] > temp:
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = temp
    print(arr)


if __name__ == "__main__":
    arr = [9, 5, 1, 4, 3]
    insertion_sort(arr, len(arr))
