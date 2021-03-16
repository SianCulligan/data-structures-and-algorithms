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

        if tempvar_hash is None: 
            return "null"
        
        current = tempvar_hash.head

        while current: 
            if current.data[0] == key:
                return current.data[1]
            current = current.next
        return "null"


    def contains(self, key_to_check):
        get_hash = self._hash(key_to_check)
        tempvar_hash = self._buckets[get_hash]
        if tempvar_hash is None: 
            return False       
        current = tempvar_hash.head
        while current:
            if current.data[0] == key_to_check:
                return True
            current = current.next
        return False
    
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


def repeated_word(verse):
    verse = verse.replace(",", "")
    new_table = HashTable()
    split_it_up = verse.split()




    num_of_words = len(split_it_up)
    print(num_of_words)
    no_words = "No repeating words ¯\_(ツ)_/¯"
    # add words to hashtable? 
    # run the 'contains method' to see if HT contains that key, if so return word, if not, add it
    for word in split_it_up: 
        print("WRD", word)
        check_word = new_table.contains(word)
        if check_word is True:
            return word, num_of_words
        else:
            new_table.add(word, 1)
    
    return no_words, num_of_words
            
            
repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")