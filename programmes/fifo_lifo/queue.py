#FIFO

class QueueNode:
    def __init__(self, value):
        self.data = value
        self.next = None


class Queue:
    
    
    def __init__(self, max_length:int):
        self.head = None
        self.tail = 0
        self.max_size = max_length




    def enqueue(self, value):

        if self.max_size == self.tail:
            print("Queue is at its max limit!")
            return False

        node = QueueNode(value=value) 

        if self.head is None:
            
            self.head = node
            self.tail += 1
            print(value," added in the Queue")
            return True

        current_queue = self.head

        while True:

            if current_queue.next is None:
                current_queue.next = node
                self.tail += 1
                print(value," added in the Queue")
                break

            current_queue = current_queue.next 

        return True
        



    def dequeue(self):

        if self.head is None:
            print("No elements to Dequeue!")
            return False

        dequeue_value = self.head.data

        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next

        print(dequeue_value," has been removed from the Queue")

        return True