from Node import *

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
        self.length = 0

    def append(self, new_node):
        self.tail.next = new_node
        self.tail = new_node
        self.length+=1

    def prepend(self, new_node):
        new_node.next = self.head.next
        self.head.next = new_node
        if (self.head == self.tail):
            self.tail == new_node
        self.length+=1

    def insert_after(self, current_node, new_node):
        if current_node == self.tail: # Insert after tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node
        self.length+=1
   
    def remove_after(self, current_node):
        if (current_node is not None and current_node.next is not None):
            successor_node = current_node.next.next
            current_node.next = successor_node

            if (successor_node is None):
                self.tail = current_node # Remove tail
        self.length-=1

    def get_length(self):
        return self.length

    def is_empty(self):
        return (self.length==0)

    def print_list(self):
        node = self.head.next
        while node != None:
            print(node.data, end=' ')
            node = node.next
        print()

    def print_reverse_list(self):
        node = self.tail    #O(1)
        if self.is_empty(): #O(1)
            print()
            return
        else:
            print(node.data, end=' ')
            while node != self.head.next:                # O(N^2)
                prevnode = self.head
                while prevnode.next != node:        
                    prevnode = prevnode.next
                node = prevnode
                print(node.data, end=' ')
        print()