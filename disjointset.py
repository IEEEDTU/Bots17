class DisjointSet:
    def __init__(self):
        self.Arr = []
        self.Size = []

    def initialize(self):
        for i in range(0, 169):
            self.Arr.append(i)
            self.Size.append(1)

        for i in range(1, 13):
            self.Arr[i], self.Arr[117 + i] = 1, 117  # Top and Bottom virtual cells.
            self.Arr[13 * i], self.Arr[13 * i + 12] = 13, 25  # Left and Right virtual cells.

    def calc_id(self,x, y):
        return (x + 1) * 13 + (y + 1)

    def root(self, i):
        if self.Arr[i] != i:
            self.Arr[i] = self.root(self.Arr[i])
        return self.Arr[i]

    def merge(self, a, b):
        root_a, root_b = self.root(a), self.root(b)
        if root_a != root_b:
            if self.Size[root_a] < self.Size[root_b]:
                self.Arr[root_a], self.Size[root_b] = self.Arr[root_b], self.Size[root_b] + self.Size[root_a]
            else:
                self.Arr[root_b], self.Size[root_a] = self.Arr[root_a], self.Size[root_a] + self.Size[root_b]

    def find_set(self, a, b):
        return self.root(a) == self.root(b)

