# Simple self adjusting hashmap. Stores a key and value. Key must be an integer and unique.
# The hash is just the length of the array that the key, value is stored in
class HashTable:
    def __init__(self):
        self.data = [None]

    def __iter__(self):
        return iter(self.data)

    def __next__(self):
        self.idx += 1
        try:
            return self.data[self.idx - 1]
        except IndexError:
            self.idx = 0
            raise StopIteration

    def __len__(self):
        return len(self.data)

    # O(1)
    # Uses a key to return a value.
    def search(self, key):
        if self.data[key % len(self.data)] is not None:
            return self.data[key % len(self.data)][1]
        return None

    # O(n)
    # Uses key to store value. Doubles length if there is a collision. This was the simplest way to solve conflicts.
    def add(self, key, value):
        if self.data[key % len(self.data)] is not None:  # checks for conflict
            self.data = self.data + ([None] * len(self.data))  # doubles the size of the array
            for x in range(0, len(self.data)):  # loop though list and moves any items that are in the wrong spot
                if self.data[x] is not None:    # checks to make sure item is not None which would cause an error
                    if self.data[x][0] % len(self.data) != x:   # moves items to correct location
                        self.data[self.data[x][0] % len(self.data)] = self.data[x]
                        self.data[x] = None

        self.data[key % len(self.data)] = [key, value]
        return
