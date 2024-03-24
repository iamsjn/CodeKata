def bubble_sort(arr, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j+1]) = (arr[j + 1], arr[j])
    print(arr)


def bubble_sort(arr, n):
    for i in range(n -1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                (arr[j], arr[j+1]) = (arr[j + 1], arr[j])


def insertion_sort(arr, n):
    for i in range(n-1):
        temp = arr[i]
        j = i

        while j > 0 and arr[j - 1] > temp:
            arr[j] = arr[j -1]
            j = j - 1

        arr[j] = temp


if __name__ == "__main__":
    arr = [9, 15, 21, 34, 34, 3, 4, 5, 8]
    bubble_sort(arr, len(arr))  
