class MaxHeap:
    def __init__(self):
        self.heap = []          # list of (priority, patient_id, timestamp)
        self.pos = {}           # patient_id -> index in heap

    def isEmpty(self):
        return len(self.heap) == 0

    def maxHeapify(self, i):
        left = 2*i + 1
        right = 2*i + 2
        largest = i

        if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
            largest = left
        if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.pos[self.heap[i][1]] = i
            self.pos[self.heap[largest][1]] = largest
            self.maxHeapify(largest)

    def insert(self, patient_id, priority, timestamp):
        self.heap.append((priority, patient_id, timestamp))
        idx = len(self.heap) - 1
        self.pos[patient_id] = idx

        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[parent][0] < self.heap[idx][0]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                self.pos[self.heap[parent][1]] = parent
                self.pos[self.heap[idx][1]] = idx
                idx = parent
            else:
                break

    def extractMax(self):
        if self.isEmpty():
            return None

        root = self.heap[0]
        last = self.heap.pop()
        if not self.isEmpty():
            self.heap[0] = last
            self.pos[last[1]] = 0
            del self.pos[root[1]]
            self.maxHeapify(0)
        else:
            del self.pos[root[1]]

        return root

    def increasePriority(self, patient_id, new_priority):
        if patient_id not in self.pos:
            return False

        idx = self.pos[patient_id]
        old_priority = self.heap[idx][0]
        if new_priority <= old_priority:
            return False

        old_timestamp = self.heap[idx][2]
        self.heap[idx] = (new_priority, patient_id, old_timestamp)

        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[parent][0] < self.heap[idx][0]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                self.pos[self.heap[parent][1]] = parent
                self.pos[self.heap[idx][1]] = idx
                idx = parent
            else:
                break
        return True


if __name__ == "__main__":
    h = MaxHeap()
    h.insert("P001", 5, "08:30")
    h.insert("P002", 10, "08:35")
    h.insert("P003", 3, "08:40")
    print("Extract max:", h.extractMax())  # (10, 'P002', '08:35')
    print("Extract max:", h.extractMax())  # (5, 'P001', '08:30')
    print("Is empty?", h.isEmpty())        # False
    print("Extract max:", h.extractMax())  # (3, 'P003', '08:40')
    print("Is empty?", h.isEmpty())        # True

    h.insert("P004", 4, "09:00")
    h.increasePriority("P004", 9)
    print("After increase, max:", h.extractMax())  # (9, 'P004', '09:00')