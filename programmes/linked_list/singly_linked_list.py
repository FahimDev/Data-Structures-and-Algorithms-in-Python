
class SinglyLinkedListNode:

    def __init__(self, value, next_node = None):
        self.data = value
        self.next = next_node




class SinglyLinkedList:

    def __init__(self):
        self.head = None


    def insert(self, value):

        new_node = SinglyLinkedListNode(value=value)
        
        if self.head is None:

            self.head = new_node
            
            return

        current_node = self.head
        

        while True:

            if current_node.next is None:
                
                current_node.next = new_node
                break

            else:

                current_node = current_node.next




    def print_singly_list(self):

        current_node = self.head

        print(">>--Singly Linked List--<<")
        print("Head=> ", current_node.data)

        current_node = self.head.next
        
        while True:
            
            if current_node.next is None:
                print("Tail=> ", current_node.data)
                break
            else:
                print("element=> ", current_node.data)
                current_node = current_node.next


