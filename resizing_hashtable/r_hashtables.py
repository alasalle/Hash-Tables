# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


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

    hash_table.count += 1
    current_pair = hash_table.storage[index]
    
    while current_pair and current_pair.key != key:
        current_pair = current_pair.next

    if current_pair is None:
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
    hash_table -= 1
    current_pair = hash_table.storage[index]

    if hash_table.storage[index] == None:
        print(f"Warning: key {key} is not in this table.")
        return

    while current_pair:
        if current_pair.key == key:
            current_pair.prev.next = current_pair.next
            current_pair.next.prev = current_pair.prev
            return



# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)

    current_pair = hash_table.storage[index]
    
    while current_pair:
        if current_pair.key == key:
            return current_pair.value

    return None






# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    ht = HashTable(hash_table.capacity * 2)

    for i in range(0, hash_table.capacity):
        ht.storage[i] = hash_table.storage[i]
    return ht


def Testing():
    ht = HashTable(10)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_7", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_7"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
