from hashtable.linked_list import LinkedList

class HashTable():
    def __init__(self, initial_size=256):
        self.initial_size = initial_size
        # important to multiply the NONE to clarify & make the list non -faulty. Will not enter a while loop
        self._buckets = initial_size * [None]

    def add(self, key_to_add, val_to_add):
        key_index = self._hash(key_to_add)

        # build a check to avoid collisions
        # look at the bucket, determine if there's something there
            #if empty, create a LL, else, add to LL
        if self.contains(key_to_add): 
            return "Error"
        if not self._buckets[key_index]:
            self._buckets[key_index] = LinkedList()

        self._buckets[key_index].insert((key_to_add, val_to_add))


    def get(self, key):
        get_hash = self._hash(key)
        tempvar_hash = self._buckets[get_hash]
        current = tempvar_hash.headVal

        while current: 
            if current.value[0] == key:
                return current.value[1]
            current = current.nextVal


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

# # thisruns code as a script
# new_table = HashTable()
# new_table.add("Weird", 24)
# print(new_table)
