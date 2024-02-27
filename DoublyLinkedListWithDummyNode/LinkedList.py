from Node import *

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def append(self, new_node):
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        
        self.length+=1

    def prepend(self, new_node):
        first_node = self.head.next
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next = new_node
        first_node.prev = new_node

        self.length+=1

    def insert_after(self, current_node, new_node):
        if current_node == self.tail:
            # Can't insert after dummy tail
            return
        successor_node = current_node.next
        new_node.next = successor_node
        new_node.prev = current_node
        current_node.next = new_node
        successor_node.prev = new_node
        self.length+=1
   
    def remove(self, current_node):
        if current_node == self.head or current_node == self.tail:
            # dummy node cannot be removed
            return
        successor_node = current_node.next
        predecessor_node = current_node.prev
        successor_node.prev = predecessor_node
        predecessor_node.next = successor_node
        self.length -= 1

    def get_length(self):
        return self.length

    def is_empty(self):
        return (self.length==0)

    def print_list(self):
        node = self.head.next
        while node != self.tail:
            print(node.data, end=' ')
            node = node.next
        print()

    def print_reverse_list(self):
        node = self.tail.prev    #O(1)
        while node != self.head:
            print(node.data, end=' ')
            node = node.prev
        print()