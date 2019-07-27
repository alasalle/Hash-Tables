

# Each ListNode holds a reference to its previous node
# as well as its next node in the List.
class ListNode:
    def __init__(self, value, key, prev=None, nex=None):
        self.key = key
        self.prev = prev
        self.value = value
        self.next = nex

# Wrap the given value in a ListNode and insert it
# after this node. Note that this Node could already
# have a next node it is pointing to.
    def insert_after(self, value, key):
        current_next = self.next
        self.next = ListNode(value, key, self, current_next)
        if current_next:
            current_next.prev = self.next

# Wrap the given value in a ListNode and insert it
# before this node. Note that this Node could already
# have a previous node it is pointing to.
    def insert_before(self, value, key):
        current_prev = self.prev
        self.prev = ListNode(value, key, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

# Rearranges this ListNode's previous and next pointers
# accordingly, effectively deleting this ListNode.
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    def replace(self, new):
        if self.prev:
            self.prev.next = new
        if self.next:
            self.next.prev = new


# Our doubly-linked list class. It holds references to
# the list's head and tail nodes.
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

# Wraps the given value in a ListNode and inserts it
# as the new head of the list. Don't forget to handle
# the old head node's previous pointer accordingly.
    def add_to_head(self, value, key):
        self.length += 1
        print(f"SELF.HEAD 1ST: {self.head}, SELF.TAIL 1ST: {self.tail}")
        if not self.head and not self.tail:
            new_node = ListNode(value, key, None, None)
            self.head = new_node
            self.tail = new_node
            print(f"SELF.HEAD 2ND: {self.head.key}, SELF.TAIL 2ND: {self.tail.key}")
        else:
            print(f"SELF.HEAD 3RD: {self.head}, SELF.TAIL 3RD: {self.tail.key}")
            self.head.insert_before(value, key)

# Removes the List's current head node, making the
# current head's next node the new head of the List.
# Returns the removed Node.
    def remove_from_head(self):
        if not self.head and not self.tail:
            return None
        self.length -= 1
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            return current_head.value
        current_head = self.head
        self.head = self.head.next
        self.head.prev = None
        return current_head.value

# Wraps the given value in a ListNode and inserts it
# as the new tail of the list. Don't forget to handle
# the old tail node's next pointer accordingly.
    def add_to_tail(self, value, key):
        new_node = ListNode(value, key, None, None)
        self.length += 1
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

# Removes the List's current tail node, making the
# current tail's previous node the new tail of the List.
# Returns the removed Node.
    def remove_from_tail(self):
        if not self.head and not self.tail:
            return None
        self.length -= 1
        if self.head == self.tail:
            current_tail = self.tail
            self.head = None
            self.tail = None
            return current_tail.value
        current_tail = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return current_tail.value

# Removes the input node from its current spot in the
# List and inserts it as the new head node of the List.
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        key = node.key
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value, key)

# Removes the input node from its current spot in the
# List and inserts it as the new tail node of the List.
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        key = node.key
        if node is self.head:
            self.remove_from_head()
            self.add_to_tail(value, key)
        else:
            node.delete()
            self.length -= 1
            self.add_to_tail(value, key)

    def delete(self, node):
        self.length -= 1
        if not self.head and not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    def replace(self, node, key, value):
        new = ListNode(value, key, node.prev, node.next)
        if not self.head and not self.tail:
            return
        if self.head == self.tail:
            self.head = new
            self.tail = new
        elif self.head == node:
            self.head = new
            node.replace(new)
        elif self.tail == node:
            self.tail = new
            node.replace(new)
        else:
            node.replace(new)

    def get_max(self):
        if not self.head:
            return None
        max_val = self.head.value
        current = self.head
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val

    # Finds and deletes the first instance of a given value
    def find_and_replace(self, value, key):
        current = self.head
        while current:
            if current.key == key:
                self.replace(current, key, value)
                return
            current = current.next

        # Print an error if value not found
        print("Error, " + str(key) + " not found")
