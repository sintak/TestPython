from collections import deque
class RingBuffer(deque):
    def __init__(self, size_max):
        deque.__init__(self)
        self.size_max = size_max
    def _full_append(self, datum):
        deque.append(self, datum)
        self.popleft()
    def append(self, datum):
        deque.append(self, datum)
        if len(self) == self.size_max:
            self.append = self._full_append
    def tolist(self):
        return list(self)

if __name__ == '__main__':
    print('hallo')
    x = RingBuffer(5)
    print(x.tolist())
    x.append(1); x.append(2); x.append(3); x.append(4)
    print(x.tolist())
    print(x.append(5))
    print(x.tolist())
    print(x.append(6))
    print(x.tolist())
    print(x.append(7))
    print(x.tolist())
