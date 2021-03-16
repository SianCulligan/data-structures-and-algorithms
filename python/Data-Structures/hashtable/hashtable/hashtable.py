# from hashtable.linked_list import LinkedList

class HashTable():
    def __init__(self, initial_size=256):
        self.initial_size = initial_size
        # important to multiply the NONE to clarify & make the list non -faulty. Will not enter a while loop
        self._buckets = initial_size * [None]
    

    def add(self, key_to_add, val_to_add):
        key_index = self._hash(key_to_add)
        # build a check to avoid collisions
        # look at the bucket, determine if there's something there
        #     #if empty, create a LL, else, add to LL
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
    
# Add an underscore to the front of the hash function to indicate this is a 'private' function and shouldn't be messed with
    def _hash(self, key):
        total = 0 
        for ch in key:
            total += ord(ch)

        primed = total * 19
        index =  primed % self.initial_size
        return index


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        # if list is empty
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


