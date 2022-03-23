import heapq

class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.removals = []

    def insert(self, elem):
        heapq.heappush(self.pq, -elem)

    def gettop(self):
        return -self.pq[0]

    def remove(self, elem):
        if elem == -self.pq[0]:
            heapq.heappop(self.pq)
            while self.removals and self.pq[0] == self.removals[0]:
                heapq.heappop(self.pq)
                heapq.heappop(self.removals)
        else:
            heapq.heappush(self.removals, -elem)

    def length(self):
        return len(self.pq)
