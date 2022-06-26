import heapq


class MyHeap:
    def __init__(self, type='min'):
        self.heap = []
        self.removals = []
        self.sign = 1 if type == 'min' else -1

    def insert(self, elem):
        heapq.heappush(self.heap, self.sign * elem)

    def __getitem__(self, idx):
        return self.sign * self.heap[idx]

    def __len__(self):
        return len(self.heap) - len(self.removals)

    def remove(self, elem):
        if elem == self.sign * self.heap[0]:
            heapq.heappop(self.heap)
            while self.removals and self.heap[0] == self.removals[0]:
                heapq.heappop(self.heap)
                heapq.heappop(self.removals)
        else:
            heapq.heappush(self.removals, self.sign * elem)

    def top(self):
        return self.heap[0]
    

# import heapq

# class PriorityQueue:
#     def __init__(self):
#         self.pq = []
#         self.removals = []

#     def insert(self, elem):
#         heapq.heappush(self.pq, -elem)

#     def gettop(self):
#         return -self.pq[0]

#     def remove(self, elem):
#         if elem == -self.pq[0]:
#             heapq.heappop(self.pq)
#             while self.removals and self.pq[0] == self.removals[0]:
#                 heapq.heappop(self.pq)
#                 heapq.heappop(self.removals)
#         else:
#             heapq.heappush(self.removals, -elem)

#     def length(self):
#         return len(self.pq)
