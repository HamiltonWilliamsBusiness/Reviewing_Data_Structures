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
        if self.count == 0:
            self.head = self.tail = Node(data, None, None)
            self.count = self.count + 1
            print('List is empty data was inserted at the beginning of the list!')
            self.print_forward()
            self.print_backward()
            return
        count = 0
        if index == 0:
            self.head.prev = Node(data, self.head, None)
            return
        if index == self.count:
            self.tail.prev = Node(data, self.tail, self.tail.prev)
            return
        itr = self.head.next

        while True:
            if count == index:
                itr.prev = Node(data, itr, itr.prev)
            itr = itr.next
            count = count + 1
        self.print_forward()
        self.print_backward()

    def remove_at(self, index):
        pass

    def insert_values(self, data_list):
        pass

    def insert_after_value(self, data_after, data_to_insert):
        pass

    def remove_by_value(self, data):
        pass

if __name__ == '__main__':
    DLL = DoublyLinkedList()
    DLL.insert_at_beginning(8)
    DLL.insert_at_beginning(9)
    DLL.insert_at_beginning(10)
    DLL.insert_at_end('Hammy')
    # DLL.insert_at(0, "abby")

