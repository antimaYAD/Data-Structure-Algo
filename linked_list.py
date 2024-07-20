class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def add_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        self.n += 1

    def delete_node(self, value):
        if self.head is None:
            print("List is empty")
            return
        
        # If the node to be deleted is the head node
        if self.head.data == value:
            self.head = self.head.next
            self.n -= 1
            return

        # Traverse the list to find the node to delete
        curr = self.head
        prev = None
        while curr is not None and curr.data != value:
            prev = curr
            curr = curr.next

        # If the node was not found
        if curr is None:
            print("Value not found in the list")
            return
        
        # Unlink the node to delete it
        prev.next = curr.next
        self.n -= 1
    
    def insert_at_nth_position(self,data,pos):
        new_node = Node(data)
        
        if pos < 1 or pos > len(self.n + 1):
            print("Invalid Position to ask")
            return
        
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            self.n += 1 
        else:
            
            curr = self.head
            for i in range(1, pos - 1):
                if curr is None:
                    print("Invalid position")
                    return
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
        self.n += 1
        
    #delete the middle node of list
    def delete_middle_node(self):
        if self.head == None:
            return None
        if self.head.next == None:
            del sef.head
            return None
        
        curr = self.head
        midindex = self.n // 2
        for i in range (1,midindex - 1):
            curr = curr.next
            
        curr = c 
    
    def get_middle(self):
        v= []
        curr = self.head
        while curr is not None:
            v.append(curr.data)
            curr = curr.next
            
        midindex = len(v) // 2
        print(v[midindex])
        return
        

    def print_list(self):
        if self.head is None:
            print("List is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.data, end=" ")
                curr = curr.next
        print() 


linked_list = LinkedList()
linked_list.add_at_begin(10)
linked_list.add_at_end(20)
linked_list.add_at_begin(5)
linked_list.print_list()  
linked_list.get_middle()


# linked_list.delete_node(10)
# linked_list.print_list()  # Output: 5 20

# linked_list.delete_node(5)
# linked_list.print_list()  # Output: 20

# linked_list.delete_node(30)  # Output: Value not found in the list
# linked_list.print_list()  # Output: 20
