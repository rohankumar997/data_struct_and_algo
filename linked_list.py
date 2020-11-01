
# # A simple Python program for traversal of a linked list
#
# # Node class
# class NODE:
#     # Function to initialise the node object
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# # Linked List class contains a Node object
# class LINKED_LIST():
#     # Function to initialize head
#     def __init__(self):
#         self.head = None
#
#     # This function prints contents of linked list
#     def print_list(self):
#         temp = self.head
#         while(temp):
#             print(temp.data)
#             temp=temp.next
#
#
# LISTT =  LINKED_LIST()
#
# LISTT.head = NODE(1)
# second = NODE(6)
# third = NODE(3)
#
# LISTT.head.next = second
# second.next = third
#
# LISTT.print_list()


class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head=None

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next


e1=LinkedList()
e1.head=Node(1)

e2=Node(2)
e3=Node(3)

e1.head.next=e2
e2.next=e3

print(e1.print_list())