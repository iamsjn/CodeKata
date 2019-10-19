class Heap:

    def __swap(self, val1, val2):
        val1 = val1 + val2
        val2 = val1 - val2
        val1 = val1 - val2

    def __max_heapify(self, given_arr, length, i):
        print(given_arr)

        largest = i
        left = 2*i + 1
        right = 2*i + 2

        if left < length and given_arr[left] > given_arr[largest]:
            largest = left

        if right < length and given_arr[right] > given_arr[largest]:
            largest = right

        if largest != i:
            given_arr[i] = given_arr[i] + given_arr[largest]
            given_arr[largest] = given_arr[i] - given_arr[largest]
            given_arr[i] = given_arr[i] - given_arr[largest]
            self.__max_heapify(given_arr, length, largest)

    def build_max_heap(self, given_arr):
        for i in range(((len(given_arr)/2) - 1), -1, -1):
            self.__max_heapify(given_arr, len(given_arr), i)

    def __min_heapify(self, given_arr, length, i):
        print(given_arr)

        smallest = i
        left = 2*i + 1
        right = 2*i + 2

        if left < length and given_arr[left] < given_arr[smallest]:
            smallest = left

        if right < length and given_arr[right] < given_arr[smallest]:
            smallest = right

        if smallest != i:
            given_arr[i] = given_arr[i] + given_arr[smallest]
            given_arr[smallest] = given_arr[i] - given_arr[smallest]
            given_arr[i] = given_arr[i] - given_arr[smallest]
            self.__min_heapify(given_arr, length, smallest)

    def build_min_heap(self, given_arr):
        for i in range(((len(given_arr)/2) - 1), -1, -1):
            self.__min_heapify(given_arr, len(given_arr), i)


if __name__ == '__main__':
    heap = Heap()
    heap.build_max_heap([1, 12, 9, 5, 6, 10])
    heap.build_min_heap([1, 12, 9, 5, 6, 10])
