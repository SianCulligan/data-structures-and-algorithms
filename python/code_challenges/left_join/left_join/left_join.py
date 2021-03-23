class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    def display(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values

class HashTable():
    def __init__(self, initial_size=256):
        self.initial_size = initial_size
        self._buckets = initial_size * [None]

    def add(self, key_to_add, val_to_add):
        key_index = self._hash(key_to_add)
        if not self._buckets[key_index]:
            self._buckets[key_index] = LinkedList()  
        self._buckets[key_index].insert((key_to_add, val_to_add))

    def get(self, key):
        get_hash = self._hash(key)
        tempvar_hash = self._buckets[get_hash]
        current = tempvar_hash.head
        while current: 
            if current.data[0] == key:
                return current.data[1]
            current = current.next
        return "null"

    def contains(self, key):
        val = self.get(key)
        if val is None: 
            return False
        else: 
            return True   

    def _hash(self, key):
        total = 0 
        for ch in key:
            total += ord(ch)
        primed = total * 19
        index =  primed % self.initial_size
        return index



def left_join(ht_one, ht_two):  
    final_result = []
    for key in ht_one:
        pass