# 数组的实现

class MyArray(object):
    def __init__(self, capacity: int):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index: int, element):
        if index < 0 or index > self.size:
            raise Exception("超出数组实际元素范围")
        for i in range(self.size - 1, -1, -1):
            self.array[i+1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def remove(self, index: int):
        if index < 0 or index > self.size:
            raise Exception("超出数组实际元素范围")
        for i in range(index, self.size):
            self.array[i] = self.array[i+1]
        self.size -= 1

    def insert_v2(self, index: int, element):
        # 扩容
        if index < 0 or index > self.size:
            raise Exception("超出数组实际元素范围")
        if self.size >= len(self.array):
            self.resize()
        for i in range(self.size - 1, -1, -1):
            self.array[i+1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def resize(self):
        array_new = [None] * len(self.array) * 2
        for i in range(self.size):
            array_new[i] = self.array[i]
        self.array = array_new

    def output(self):
        for i in range(self.size):
            print(self.array[i])


if __name__ == "__main__":
    array = MyArray(4)
    array.insert(0, 1)
    array.insert(0, 2)
    array.insert(0, 3)
    array.insert(0, 4)
    # array.insert(0, 5)
    array.output()

    array_v2 = MyArray(4)
    array_v2.insert_v2(0, 1)
    array_v2.insert_v2(0, 2)
    array_v2.insert_v2(0, 3)
    array_v2.insert_v2(0, 4)
    array_v2.insert_v2(0, 5)
    array_v2.insert_v2(0, 12)
    array_v2.remove(2)
    array_v2.output()
