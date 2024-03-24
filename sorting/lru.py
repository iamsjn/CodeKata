from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._map = OrderedDict()

    def get(self, key: int) -> int:
        return self._map.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if len(self._map.items()) == self._capacity:
            self._map.popitem(last=False)

        self._map[key] = value
        return None


# Your LRUCache object will be instantiated and called as such:
if __name__ == "__main__":
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))

    obj.put(3, 3)
    print(obj.get(2))

    obj.put(4, 4)
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))
