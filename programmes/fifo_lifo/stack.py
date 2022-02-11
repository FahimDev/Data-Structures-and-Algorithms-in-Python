class StackNode:
    def __init__(self, value):
        self.data = value
        self.down_node = None


class Stack:
    

    def __init__(self, max_size):
        #Protected access
        self._top = None
        self._max_size = max_size
        self._bottom_count = 0




    def push(self, value):

        if self._max_size <= self._bottom_count:
            print("Stack Overflow!")
            return False

        new_node = StackNode(value=value)
        
        if self._top is None:
            self._top = new_node
            self._bottom_count += 1
            print(value, " added in the Stack")
            return True

        current_position = self._top

        new_node.down_node = current_position

        self._top = new_node

        print(value, " added in the Stack")
        self._bottom_count += 1

        return True





    def pop(self):
        
        if self._top is None:
            print("Stack is empty!")
            return False


        print(self._top.data, "has been popped")

        self._top = self._top.down_node
        self._bottom_count += -1

        return True




    def peek(self):

        if self._top is None:
            print("The stack is empty!")
            return None

        return self._top.data




    def show_stack(self):

        if self._top is None:
            print("The stack is empty!")
            return False

        current_item = self._top
        
        while current_item is not None:

            print(current_item.data)
            current_item = current_item.down_node

        return True
