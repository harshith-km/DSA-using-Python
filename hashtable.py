class Hashtable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h% self.MAX

    # def add_item(self, key, value):
    #     hk = self.get_hash(key)
    #     self.arr[hk]=value
    def __setitem__(self, key, value):
        hk = self.get_hash(key)
        self.arr[hk]=value

    # def getitem(self,key):
    #     hk = self.get_hash(key)
    #     return self.arr[hk]
    def __getitem__(self,key):
        hk = self.get_hash(key)
        return self.arr[hk]

    def __delitem__(self, key):
        hk = self.get_hash(key)
        self.arr[hk] = None

n = Hashtable()
# print(n.arr)
# print(n.get_hash('march 9'))
n['march 9'] = 130
print(n['march 9'])

del n['march 9']
print(n['march 9'])


