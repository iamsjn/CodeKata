def merge(arr, start_index, mid_index, end_index):
    left_length = mid_index - start_index + 1
    right_length = end_index - mid_index

    L = [0] * left_length
    R = [0] * right_length

    for i in range(left_length):
        L[i] = arr[start_index + i]

    for j in range(right_length):
        R[j] = arr[mid_index + 1 + j]

    i = 0
    j = 0
    k = start_index
    while i < left_length and j < right_length:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i = i + 1
        else:
            arr[k] = R[j]
            j = j + 1
        k = k+1

    while i < left_length:
        arr[k] = L[i]
        i = i + 1
        k = k+1

    while j < right_length:
        arr[k] = R[j]
        j = j+1
        k = k+1


def merge_sort(arr, start_index, end_index):
    if end_index <= 0:
        return
    if(start_index < end_index):
        mid_length = start_index + (end_index - start_index)/2
        merge_sort(arr, start_index, mid_length)
        merge_sort(arr, mid_length + 1, end_index)
        merge(arr, start_index, mid_length, end_index)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)
