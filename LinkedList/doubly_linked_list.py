class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    # Define the order to implement functions next time! Just leave 
    # Do it my leaving the function declarations and nothing else!
        
    def print_forward(self):
        if self.count == 0:
            print('Doubly Linked List is empty :)')
            return
        itr = self.head
        print('Printed Forwards')
        while True: 
            if itr.next == None:
                print(itr.data)
                break
            print(itr.data, "--> ", end="")
            itr = itr.next

    def print_backward(self):
        if self.count == 0:
            print('Doubly Linked List is empty :)')
            return
        itr = self.tail
        print('Printed Backwards')
        while True: 
            if itr.prev == None:
                print(itr.data)
                break
            print(itr.data, "--> ", end="")
            itr = itr.prev

    def get_length(self):
        return self.count
            

    def insert_at_beginning(self, data):
        if self.count == 0:
            self.head = self.tail = Node(data, None, None)
            self.count = self.count + 1
        else:
            self.head.prev =  self.head = Node(data, self.head, None)
            self.count = self.count + 1
        self.print_forward()
        self.print_backward()


    def insert_at_end(self, data):
        if self.count == 0:
            self.head = self.tail = Node(data, None, None)
            self.count = self.count + 1
        else:
            self.tail.next = self.tail = Node(data, None, self.tail)
            self.count = self.count + 1
        self.print_forward()
        self.print_backward()

    def insert_at(self, index, data):


        # Input Validation
        if index < 0:
            print("Invalid Index, index must be positive!")
            return
        if index > self.count:
            print("Invalid Index, index cannot be greater than length of linkedlist")
            return
        
        # If list is empty
        if self.count == 0:
            self.head = self.tail = Node(data, None, None)
            self.count = self.count + 1
            print('List is empty data was inserted at the beginning of the list!')
            self.print_forward()
            self.print_backward()
            return
        

        # Want to replace the head
        if index == 0:
            self.head.prev = self.head =  Node(data, self.head, None)
            self.print_forward()
            self.print_backward()
            self.count = self.count + 1
            return
        
        # Want to replace the tail
        if index == self.count - 1:
            new_node = Node(data, self.tail, self.tail.prev)
            self.tail.prev.next = new_node
            self.tail.prev = new_node
            self.print_forward()
            self.print_backward()
            self.count = self.count + 1
            return
        
        # Starting after the head
        itr = self.head.next
        count = 1

        # For all other cases
        while True:
            if count == index:
                new_node = Node(data, itr, itr.prev)
                itr.prev.next = new_node
                itr.prev = new_node
                self.count = self.count + 1
                break
            itr = itr.next
            count = count + 1
            if count == self.count:
                break
        self.print_forward()
        self.print_backward()

    def remove_at(self, index):
        # Input Validation
        if index < 0:
            print("Invalid Index, index must be positive!")
            return
        if index > self.count:
            print("Invalid Index, index cannot be greater than length of linkedlist")
            return
        
        # If list is empty
        if self.count == 0:
            print('List is empty data was inserted at the beginning of the list!')
            return

        # Want to remove the head
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.print_forward()
            self.print_backward()
            self.count = self.count - 1
            return
        
        # Want to replace the tail
        if index == self.count - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.print_forward()
            self.print_backward()
            self.count = self.count - 1
            return
        
        # Starting After The Head
        itr = self.head.next
        count = 1

        # For all other cases
        while True:
            if count == index:
                itr.prev.next = itr.next
                itr.next.prev = itr.prev
                break
            itr = itr.next
            count = count + 1
            if count == self.count:
                break
        self.print_forward()
        self.print_backward()

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_beginning(data)


    def insert_after_value(self, data_after, data_to_insert):
        # If list is empty
        if self.count == 0:
            self.head = self.tail = Node(data_to_insert, None, None)
            self.count = self.count + 1
            print('List is empty data was inserted at the beginning of the list!')
            self.print_forward()
            self.print_backward()
            return
        

        # Want to replace after the head
        if self.head.data == data_after:
            print("This ran")
            new_node = Node(data_to_insert, self.head.next, self.head)
            self.head.next.prev = new_node
            self.head.next = new_node
            self.print_forward()
            self.print_backward()
            self.count = self.count + 1
            return
        
        # Want to replace after the tail
        if self.tail.data == data_after:
            new_node = Node(data_to_insert, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node
            self.print_forward()
            self.print_backward()
            self.count = self.count + 1
            return
        
        # Starting after the head
        itr = self.head.next
        count = 1

        # For all other cases
        while True:
            if itr.data == data_after:
                new_node = Node(data_to_insert, itr.next, itr)
                itr.next.prev = new_node
                itr.next = new_node
                self.count = self.count + 1
                break
            itr = itr.next
            count = count + 1
            if count == self.count:
                break
        self.print_forward()
        self.print_backward()

    def remove_by_value(self, data):
        # If list is empty
        if self.count == 0:
            print('List is empty data was inserted at the beginning of the list!')
            return

        # Want to remove the head
        if self.head.data == data:
            self.head.next.prev = None
            self.head = self.head.next
            self.print_forward()
            self.print_backward()
            self.count = self.count - 1
            return
        
        # Want to remove the tail
        if self.tail.data == data:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.print_forward()
            self.print_backward()
            self.count = self.count - 1
            return
        
        # Starting After The Head
        itr = self.head.next
        count = 1

        # For all other cases
        while True:
            if itr.data == data:
                itr.prev.next = itr.next
                itr.next.prev = itr.prev
                break
            itr = itr.next
            count = count + 1
            if count == self.count:
                break
        self.print_forward()
        self.print_backward()

if __name__ == '__main__':
    DLL = DoublyLinkedList()
    DLL.insert_at_beginning(8)
    DLL.insert_at_beginning(9)
    DLL.insert_at_beginning(10)
    DLL.insert_at_end('Hammy')
    DLL.insert_at(1, "abby")
    DLL.remove_at(0)
    DLL.remove_at(3)
    DLL.insert_at_beginning("happy")
    DLL.remove_at(0)
    DLL.remove_at(1)
    DLL.insert_values([1,2,3,4,5,6])
    DLL.insert_after_value(5, "yayyy")
    DLL.remove_by_value(6)
    DLL.remove_by_value(8)
    DLL.remove_by_value(3)

