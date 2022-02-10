from .. import ObjMapper

from .singly_linked_list import SinglyLinkedList


class LinedListMenu:
    def __init__(self):
        print("--------------->Linked List Menu<---------------")



    def get_indexed(self):
        ObjMapper.OBJ_MAP['linkedlist_menu'] = ObjMapper.remember(self)




    def menu_window(self,request = None):

        #get indexed by ObjMapper
        self.get_indexed()

        self.__menu_header()

        sorted_response = self.__router(request)

        return sorted_response




    def __get_inputs(self):

        input_arr = []
        input_arr = [item for item in input('Provide number sequence and press ENTER (Example: 2,6,7,8,0,33,99,34,87,65): ').split(',')]
        return input_arr




    def __menu_header(self):

        print("--------------->Linked List Options<---------------")
        print("Options: (A) Singly Linked List | (B) Doubly Linked List | (Exit) Back")
        print("Give input option and press ENTER:")




    def __router(self,request):

        option = input("Option:")

        if option == 'Exit':
            print("--------------->Back To Main Menu<---------------")

            id = ObjMapper.OBJ_MAP['main_menu']
            route = ObjMapper.id2obj(id)
            route.menu_window()


        if option == 'A':

            print('--------------->Singly Linked List<---------------')

            single_link_list = SinglyLinkedList()

            input_items = self.__get_inputs()

            for item in input_items:
                single_link_list.insert(value=item)

            single_link_list.print_singly_list()


        elif option == 'B':

            print('--------------->Doubly Linked List<---------------')

            

        self.menu_window()