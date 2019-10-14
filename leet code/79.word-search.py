def multi_dimentional_list():
    multi_list = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
    for list in multi_list:
        print(list)


def different_ways_to_create_array():
    # First method to create a 1 D array
    N = 5
    arr = [0]*N
    print(arr)

    # Second method to create a 1 D array
    N2 = 5
    arr2 = [0 for i in range(N2)]
    print(arr2)


if __name__ == "__main__":
    multi_dimentional_list()
    different_ways_to_create_array()
