
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value): #we use value as a parameter to create the first node
                                 #at the time we initialize the LinkedList
        new_node = Node(value) #This creates a new Node
        self.head = new_node #We have head pointing to the new node
        self.tail = new_node #We have tail pointing to the new node 
        self.length = 1 #Starts the length out by being equal to 1
        #This is our LinkedList Constructor  


    def print_list(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True 
    
        
    def prepend(self, value):
        pass
        
    def insert(self, index, value):
        pass
        

my_linked_list = LinkedList(1)

my_linked_list.append(2)

my_linked_list.print_list()

# print(my_linked_list.head.value) #value of first item, created by my_linked_list
#                                     #this initiates LinkedList Constructor,
#                                     #where the constructor creates the first node
#                                     #at new_node = Node(value)
#                                     #which calls the Node Class and creates the node
                                    
                                    
                                    
                        
    