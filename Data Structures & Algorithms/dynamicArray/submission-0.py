class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if self.array[i] is None:
            self.size += 1
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        print("popback", f"before:{self.size=}")
        self.size -= 1
        print("popback", f"after:{self.size=}")
        print("popback", f"array:{self.array=}")
        ret = self.array[self.size]
        self.array[self.size] = None
        return ret

    def resize(self) -> None:
        self.capacity *= 2
        bigger = [None] * self.capacity
        for i in range(self.size):
            bigger[i] = self.array[i]
        self.array = bigger

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity



"""
capacity = 2
size = 2
array = [1, None]


capacity = 2
size = 2
array = [1, 3]

"""
