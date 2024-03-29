from Node import Node
from LinkedList import LinkedList


num_list = LinkedList()

node_a = Node(66)
node_b = Node(99)
node_c = Node(44)
node_d = Node(95)
node_e = Node(42)
node_f = Node(17)

print("Length: ", num_list.get_length())
print("Empty?", num_list.is_empty())

num_list.append(node_b)   # Add 99
num_list.append(node_c)   # Add 44, make the tail
num_list.append(node_e)   # Add 42, make the tail

print("Length: ", num_list.get_length())
print("Empty?", num_list.is_empty())

num_list.prepend(node_a)  # Add 66, make the head

num_list.insert_after(node_c, node_d)  # Insert 95 after 44
num_list.insert_after(node_e, node_f)  # Insert 17 after tail (42)

# Output list
print('List after adding nodes:', end=' ') 
num_list.print_list()
print('Reverse List after adding nodes:', end=' ') 
num_list.print_reverse_list()
num_list.remove(node_e)   # Remove the tail (17)
num_list.remove(num_list.head.next)     # Remove the head (66)


# Output final list
print('List after removing nodes:', end=' ')
num_list.print_list()
print('Reverse List after removing nodes:', end=' ')
num_list.print_reverse_list()