from .queue import Queue
from .queue import QueueNode

class PriorityQueue(Queue):

    #Override
    def enqueue(self, value):

        if self._max_size == self._tail:
            print("Priority Queue is at its max limit!")
            return False

        new_node = QueueNode(value= value)

        if self._front is None:
            self._front = new_node
            self._tail += 1
            print(value," added in the Priority Queue")
            return True

        current_queue = self._front

        while True:

            if current_queue.data < new_node.data:

                    current_queue.data, new_node.data = new_node.data, current_queue.data

            if current_queue.next is None:

                current_queue.next = new_node

                self._tail += 1
                print(value," added in the Priority Queue")

                break
            
            current_queue = current_queue.next
                
        return True
        #return super().enqueue(value)