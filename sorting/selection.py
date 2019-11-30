def selection_sort(arr, n):
    for i in range(n-1):
        minimum = i
        j = i + 1
        while j <= n-1:
            if arr[j] < arr[minimum]:
                minimum = j
            j = j+1
        (arr[i], arr[minimum]) = (arr[minimum], arr[i])
    print(arr)


if __name__ == "__main__":
    arr = [9, 15, 21, 34, 34, 3, 4, 5, 8]
    selection_sort(arr, len(arr))
