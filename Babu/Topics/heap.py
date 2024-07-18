class heap:
    def __init__(self):
        self.heap = []
    def _left_child(self,index):
        return index*2+1
    def _right_child(self,index):
        return index*2+2
    def _parent(self,index):
        return (index-1)//2
    def _swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def _sink_down(self,index):
        base = index
        max = index
        size = len(self.heap)
        while True:
            proceed = False
            left = self._left_child(base)
            right = self._right_child(base)
            if left < size and self.heap[left] > self.heap[base]:
                proceed = True
            elif right < size and self.heap[right] > self.heap[base]:
                proceed = True
            if proceed:
                if self.heap[right] > self.heap[left]:
                    max = right
                else:
                    max = left
                self._swap(max,base)
                base = max
            else:
                return
    def insert(self,value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(self._parent(current),current)
            current = self._parent(current)
    def remove(self):
        if(len(self.heap) == 0):
            return None
        elif(len(self.heap) == 1):
            return self.heap.pop()
        else:
            head = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._sink_down(0)
            return head
    def print(self):
        print(self.heap)

99,72,61,58
if __name__ == "__main__":
    h = heap()
    h.insert(99)
    h.insert(72)
    h.insert(61)
    h.insert(58)
    h.print()
    h.insert(100)
    h.print()
    h.insert(75)
    h.print()
    h.remove()
    h.print()
    h.remove()
    h.print()
    h.remove()
    h.print()
    h.remove()
    h.print()

#     99
# 72      61
# 58


#         100
#     99        61
# 58      72

#         100
#     99        75
# 58      72    61