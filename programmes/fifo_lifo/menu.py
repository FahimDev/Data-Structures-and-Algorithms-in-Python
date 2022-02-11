from .. import ObjMapper

from .stack import Stack
from .queue import Queue
from .priority_queue import PriorityQueue


class FifoLifoMenu:
    def __init__(self):
        print("--------------->FIFO & LIFO Menu<---------------")



    def get_indexed(self):
        ObjMapper.OBJ_MAP['lifo_fifo_menu'] = ObjMapper.remember(self)




    def menu_window(self,request = None):

        #get indexed by ObjMapper
        self.get_indexed()

        self.__menu_header()

        sorted_response = self.__router(request)

        return sorted_response


    def __menu_header(self):

        print("--------------->FIFO & LIFO Options<---------------")
        print("Options: (A) Stack | (B) Queue | (C) Priority Queue | (B) Circular Queue | (Exit) Back")
        print("Give input option and press ENTER:")




    def __router(self,request):

        option = input("Option:")

        if option == 'Exit':
            print("--------------->Back To Main Menu<---------------")

            id = ObjMapper.OBJ_MAP['main_menu']
            route = ObjMapper.id2obj(id)
            route.menu_window()


        if option == 'A':

            print('--------------->Stack<---------------')

            max_length = int(input("Provide max size of the Stack:"))

            jar = Stack(max_length)

            while True:

                operation = int(input("(1) Add Element | (2) Remove Element | (3) Peek Element | (4) Show Queue | (0) Turn off Stack Operations"))

                if operation == 1:

                    value = input("Provide a value to add in the Stack:")
                    jar.push(value)

                elif operation == 2:

                    jar.pop()

                elif operation == 3:

                    print(jar.peek())

                elif operation == 4:

                    jar.show_stack()

                elif operation == 0:
                    break


        elif option == 'B':

            print('--------------->Queue<---------------')

            max_length = int(input("Provide max size of the Queue:"))

            q = Queue(max_length)

            while True:

                operation = int(input("(1) Add Element | (2) Remove Element | (3) Peek Element | (4) Show Queue | (0) Turn off Queue Operations"))

                if operation == 1:

                    value = input("Provide a value to add in the Queue:")
                    q.enqueue(value)

                elif operation == 2:

                    q.dequeue()

                elif operation == 3:

                    print(q.peek())

                elif operation == 4:

                    q.show_queue()

                elif operation == 0:
                    break

        elif option == 'C':

            print('--------------->Priority Queue<---------------')

            max_length = int(input("Provide max size of the Priority Queue:"))

            pq = PriorityQueue(max_length)

            while True:

                operation = int(input("(1) Add Element | (2) Remove Element | (3) Peek Element | (4) Show Queue | (0) Turn off Queue Operations"))

                if operation == 1:

                    value = input("Provide a value to add in the Queue:")
                    pq.enqueue(value)

                elif operation == 2:

                    pq.dequeue()

                elif operation == 3:

                    print(pq.peek())

                elif operation == 4:

                    pq.show_queue()

                elif operation == 0:
                    break

            

        self.menu_window()