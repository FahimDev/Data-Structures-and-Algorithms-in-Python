#FIFO

class QueueNode:
    def __init__(self, value):
        self.data = value
        self.next = None


class Queue:
    
    
    def __init__(self, max_length:int):
        #Protected access
        self._front = None
        self._tail = 0
        self._max_size = max_length




    def enqueue(self, value):

        if self._max_size == self._tail:
            print("Queue is at its max limit!")
            return False

        node = QueueNode(value=value) 

        if self._front is None:
            
            self._front = node
            self._tail += 1
            print(value," added in the Queue")
            return True

        current_queue = self._front

        while True:

            if current_queue.next is None:
                current_queue.next = node
                self._tail += 1
                print(value," added in the Queue")
                break

            current_queue = current_queue.next 

        return True
        



    def dequeue(self):

        if self._front is None:
            print("No elements to Dequeue!")
            return False

        dequeue_value = self._front.data

        if self._front.next is None:
            self._front = None
        else:
            self._front = self._front.next
        
        self._tail += -1

        print(dequeue_value," has been removed from the Queue")

        return True




    def peek(self):
        
        if self._front is not None:
            return self._front.data
        else:
            print("This Queue is empty!")
            return None




    def show_queue(self):

        if self._front is None:
            print("This Queue is empty!")

        current_position = self._front

        while current_position is not None:

            print(current_position.data)

            current_position = current_position.next

        return True
