def heapify(A, l, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < l and A[left] < A[smallest]:
        smallest = left

    if right < l and A[right] < A[smallest]:
        smallest = right

    if smallest != i:
        A[i] = A[i] + A[smallest]
        A[smallest] = A[i] - A[smallest]
        A[i] = A[i] - A[smallest]
        heapify(A, l, smallest)


def delete(A, i):
    A[i] = A[len(A)-1]
    del A[len(A)-1]


def build_heap(A):
    n = len(A)
    for i in range((int(n/2) - 1), -1, -1):
        heapify(A, n, i)


def cookies(k, A):
    i = 0
    c = 0
    while i < len(A):
        s = (A[i] * 1 + A[i+1] * 2)
        if A[i] < k and A[i+1] < k:
            delete(A, i)
            build_heap(A)
            delete(A, i)
            build_heap(A)
            A.append(s)
            build_heap(A)
            c = c + 1
        else:
            i = k

    print(c)


if __name__ == "__main__":
    N = 6
    K = 7
    A = [1, 2, 3, 9, 10, 12]
    cookies(K, A)
