# why so hard???
class MinHeap:
    def __init__(self, k):
        self.heap_list = []
        self.ix_list = [0]*k
        self.size = 0

    def up(self, j, i):
        """
        Moves the value up in the tree to maintain the heap property.
        :param i:
        """
        stop = 0
        while (i // 2 > 0) and not stop:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i//2], self.heap_list[i]
                self.ix_list[j] = i // 2
            else:
                # take the index
                stop = 1
            i = i // 2

    def insert(self, i, k):
        """
        Inserts a value into the heap
        """
        self.heap_list += [k]
        self.size += 1
        self.ix_list[i] = self.size-1
        self.up(i, self.size-1)

    def down(self, i):
        """
        Pushes the value at index down the heap tree
        :param i:
        :return:
        """
        while (i * 2) <= self.size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        if (i * 2) + 1 > self.size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[(i * 2) + 1]:
                return i * 2
            else:
                return (i * 2) + 1

    def delete(self, i):
        if self.size == 1:
            self.heap_list.pop()
            self.size -= 1
        else:
            self.heap_list[i], self.heap_list[self.size] = self.heap_list[self.size], self.heap_list[i]
            self.heap_list.pop()
            self.size -= 1
            self.down(self, i)


n, k = map(int, input().split())
a = [i for i in map(int, input().split())]
heap = MinHeap(n)
for i in range(k):
    heap.insert(i, a[i])
print(heap[0])
i, j = 1, k+1
while j < len(a):
    heap.delete(ix[i])
    heap.insert(a[j])
    print(heap[0])
    i, j = i+1, j+1
