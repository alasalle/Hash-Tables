# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f"key: {self.key}, value: {self.value}, next: {self.next}"


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.original_capacity = capacity
        self.storage = [None] * capacity
        self.count = 0


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, m):
    h = 5381
    a = 33
    for i in string:
        h = (h * a) + ord(i)

    return h % m - 1


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)

    current_pair = hash_table.storage[index]
    
    while current_pair and current_pair.key != key:
        current_pair = current_pair.next

    if current_pair is None:
        hash_table.count += 1
        new_pair = LinkedPair(key, value)
        new_pair.next = hash_table.storage[index]
        hash_table.storage[index] = new_pair
        return

    else:
        current_pair.value = value
        return





# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    first = hash_table.storage[index]
    current_pair = first

    if (current_pair is not None):

        if (current_pair.key == key):

            hash_table.storage[index] = None
            return

    while(current_pair is not None):

        if current_pair.key == key: 
            break 

        prev = current_pair
        current_pair = current_pair.next

    if(current_pair == None):

        return None

    prev.next = current_pair.next 

    current_pair = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)

    current_pair = hash_table.storage[index]

    while current_pair and current_pair.key != key:
        current_pair = current_pair.next

    if current_pair is None:
        return None
    
    else:
        return current_pair.value






# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    ht = HashTable(hash_table.capacity * 2)

    for i in range(0, hash_table.capacity):
        ht.storage[i] = hash_table.storage[i]
    return ht


def Testing():
    ht = HashTable(8)

    hash_table_insert(ht, "key-0", "val-0")
    hash_table_insert(ht, "key-1", "val-1")
    hash_table_insert(ht, "key-2", "val-2")
    hash_table_insert(ht, "key-3", "val-3")
    hash_table_insert(ht, "key-4", "val-4")
    hash_table_insert(ht, "key-5", "val-5")
    hash_table_insert(ht, "key-6", "val-6")
    hash_table_insert(ht, "key-7", "val-7")
    hash_table_insert(ht, "key-8", "val-8")
    hash_table_insert(ht, "key-9", "val-9")

    for i in ht.storage:
        print(i)

    hash_table_remove(ht, "key-9")
    hash_table_remove(ht, "key-8")
    hash_table_remove(ht, "key-7")
    hash_table_remove(ht, "key-6")
    hash_table_remove(ht, "key-5")
    hash_table_remove(ht, "key-4")
    hash_table_remove(ht, "key-3")
    hash_table_remove(ht, "key-2")
    hash_table_remove(ht, "key-1")
    hash_table_remove(ht, "key-0")

    hash_table_retrieve(ht, "key-0")
    hash_table_retrieve(ht, "key-1")
    hash_table_retrieve(ht, "key-2")

    for i in ht.storage:
        print(f"2ND: {i}")


Testing()
