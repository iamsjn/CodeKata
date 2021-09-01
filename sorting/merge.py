import math
# def merge(arr, start_index, mid_index, end_index):
#     left_length = mid_index - start_index + 1
#     right_length = end_index - mid_index

#     L = [0] * left_length
#     R = [0] * right_length

#     for i in range(left_length):
#         L[i] = arr[start_index + i]

#     for j in range(right_length):
#         R[j] = arr[mid_index + 1 + j]

#     i = 0
#     j = 0
#     k = start_index
#     while i < left_length and j < right_length:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i = i + 1
#         else:
#             arr[k] = R[j]
#             j = j + 1
#         k = k+1

#     while i < left_length:
#         arr[k] = L[i]
#         i = i + 1
#         k = k+1

#     while j < right_length:
#         arr[k] = R[j]
#         j = j+1
#         k = k+1


# def merge_sort(arr, start_index, end_index):
#     if end_index <= 0:
#         return
#     if(start_index < end_index):
#         mid_index = start_index + (end_index - start_index)/2
#         merge_sort(arr, start_index, mid_index)
#         merge_sort(arr, mid_index + 1, end_index)
#         merge(arr, start_index, mid_index, end_index)


# if __name__ == "__main__":
#     arr = [12, 11, 13, 5, 6, 7]
#     merge_sort(arr, 0, len(arr) - 1)
#     print(arr)


class MergeSort:

    def merge(self, arr, start_index, mid_index, end_index):
        left_length = (mid_index - start_index) + 1
        right_length = end_index - mid_index

        L = [None] * left_length
        R = [None] * right_length

        for i in range(0, left_length, 1):
            L[i] = arr[start_index + i]

        for i in range(0, right_length, 1):
            R[i] = arr[(mid_index + i) + 1]

        i = 0
        j = 0
        k = start_index
        while i < left_length and j < right_length:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i = i + 1
            else:
                arr[k] = R[j]
                j = j+1

            k = k+1

        while i < left_length:
            arr[k] = L[i]
            k = k+1
            i = i+1

        while j < right_length:
            arr[k] = R[j]
            k = k+1
            j = j+1

    def sort(self, arr, start_index, end_index):
        if end_index <= 0 or start_index >= end_index:
            return

        mid_index = math.floor((start_index + end_index) / 2)
        self.sort(arr, start_index, mid_index)
        self.sort(arr, mid_index + 1, end_index)
        self.merge(arr, start_index, mid_index, end_index)


if __name__ == "__main__":
    arr = [14, 7, 3, 12, 9, 11, 6, 4, 1, 2, 13, 18]
    merge_sort = MergeSort()
    merge_sort.sort(arr, 0, (len(arr) - 1))
    print(arr)
