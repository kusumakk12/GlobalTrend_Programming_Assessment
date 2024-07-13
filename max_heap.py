class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)

    def delete(self):
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return max_val

    def get_max(self):
        return self.heap[0] if self.heap else None

    def _sift_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def _sift_down(self, i):
        max_index = i
        size = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            if left < size and self.heap[left] > self.heap[max_index]:
                max_index = left
            if right < size and self.heap[right] > self.heap[max_index]:
                max_index = right
            if i == max_index:
                break
            self.heap[i], self.heap[max_index] = self.heap[max_index], self.heap[i]
            i = max_index 

if __name__ == "__main__":
    max_heap = MaxHeap()
    elements = eval(input("enter values"))
    for element in elements:
        max_heap.insert(element)
        print(f"Inserted {element}. Heap is now: {max_heap.heap}")

    print(f"Maximum element: {max_heap.get_max()}")

    print("Deleting elements:")
    while max_heap.heap:
        print(f"Deleted: {max_heap.delete()}. Heap is now: {max_heap.heap}")
