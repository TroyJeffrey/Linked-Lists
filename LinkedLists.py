# Troy Jeffrey Amegashie
# Linked Lists in Python
# 02/24/2020


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_to_end(self, data):
        new_node = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_head(self):
        new_node = self.head
        self.head = self.head.next
        return new_node.data

    def remove_end(self):
        current = self.head
        previous = self.head
        while current.next:
            previous = current
            current = current.next
        previous.next = None
        return current.data

    def search_list(self, x):
        current = self.head
        while current:
            if current.data == x:
                return True
            current = current.next
        return False

    def clear_list(self):
        current = self.head
        while current:
            prev = current.next  # move next node
            del current.data
            current = prev
