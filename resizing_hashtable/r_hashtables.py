# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value, nex, prev):
        self.key = key
        self.value = value
        self.next = nex
        self.prev = prev


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
def hash(string, max):
    hash = 5381
    a = 33
    for i in string:
        hash = (hash * a) + ord(i)

    return hash % max - 1


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    hash_table.count += 1
    current_pair = hash_table.storage[index]
    last_pair = None
    
    while current_pair and current_pair.key != key:
        last_pair = current_pair.prev
        current_pair = current_pair.next

    if current_pair is None:
        new_pair = LinkedPair(key, value, current_pair, last_pair)
        current_pair = new_pair

    else:
        current_pair.value = value





# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    hash_table -= 1
    current_pair = hash_table.storage[index]

    if hash_table.storage[index] == None:
        print(f"Warning: key {key} is not in this table.")

    while current_pair:
        if current_pair.key == key:
            current_pair.prev.next = current_pair.next
            current_pair.next.prev = current_pair.prev



# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    pass


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    # print(hash_table_retrieve(ht, "line_1"))
    # print(hash_table_retrieve(ht, "line_2"))
    # print(hash_table_retrieve(ht, "line_3"))

    # old_capacity = len(ht.storage)
    # ht = hash_table_resize(ht)
    # new_capacity = len(ht.storage)

    # print("Resized hash table from " + str(old_capacity)
    #       + " to " + str(new_capacity) + ".")


Testing()
