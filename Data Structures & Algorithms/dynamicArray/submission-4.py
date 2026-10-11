class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.darr = [None] * self.capacity

    def get(self, i: int) -> int:
        return self.darr[i]

    def set(self, i: int, n: int) -> None:
        self.darr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.darr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.darr[self.size]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_darr = [None] * self.capacity

        for i in range(self.size):
            new_darr[i] = self.darr[i]
        self.darr = new_darr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity