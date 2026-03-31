class MyHashSet:

    List: data
    def __init__(self):
        self.data = []
        

    def add(self, key: int) -> None:
        self.data.append(key)

    def remove(self, key: int) -> None:
        newdata = []
        for i in self.data:
            if i != key:
                newdata.append(i)
        self.data = newdata

    def contains(self, key: int) -> bool:
        return key in self.data
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)