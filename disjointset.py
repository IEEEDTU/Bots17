class DisjointSet:
    def __init__(self):
        self.Arr = []
        self.Size = []

    def initialize(self):
        for i in range(169):
            self.Arr.append(i)
            self.Size.append(1)

        for i in range(1, 12):
            self.Arr[i], self.Arr[156 + i] = 1, 2  # Top and Bottom virtual cells.
            self.Arr[13 * i], self.Arr[13 * i + 12] = 3, 4  # Left and Right virtual cells.

    def calc_id(self, x, y):
        return x * 13 + y

    def root(self, i):
        # TODO: define correctly
        pass

    def merge(self, a, b):
        root_a, root_b = self.root(a), self.root(b)
        if root_a in [1, 2, 3, 4]:
            self.Arr[root_b], self.Size[root_a] = self.Arr[root_a], self.Size[root_a] + self.Size[root_b]
        elif root_b in [1, 2, 3, 4]:
            self.Arr[root_a], self.Size[root_b] = self.Arr[root_b], self.Size[root_b] + self.Size[root_a]
        elif root_a != root_b:
            if self.Size[root_a] < self.Size[root_b]:
                self.Arr[root_a], self.Size[root_b] = self.Arr[root_b], self.Size[root_b] + self.Size[root_a]
            else:
                self.Arr[root_b], self.Size[root_a] = self.Arr[root_a], self.Size[root_a] + self.Size[root_b]

    def find_set(self, a, b):
        return self.root(a) == self.root(b)
