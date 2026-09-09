class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size: int = capacity
        self.array: list[Any] = [] 

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if len(self.array) == self.size:
            self.resize()
        self.array.append(n)

    def popback(self) -> int:
        return self.array.pop()

    def resize(self) -> None:
        self.size *= 2

    def getSize(self) -> int:
        return len(self.array)
    
    def getCapacity(self) -> int:
        return self.size