from .tree.binary_tree import BinaryTree


from .. import ObjMapper


class GraphMenu:
    def __init__(self):
        print("--------------->Graph Menu<---------------")



    def get_indexed(self):
        ObjMapper.OBJ_MAP['graph_menu'] = ObjMapper.remember(self)




    def menu_window(self,request = None):

        #get indexed by ObjMapper
        self.get_indexed()

        self.__menu_header()

        sorted_response = self.__router(request)

        return sorted_response




    def __menu_header(self):

        print("--------------->Graph Options<---------------")
        print("Options: (A) Binary Tree | (B) Loading... | (Exit) Back")
        print("Give input option and press ENTER:")




    def __get_inputs(self):

        input_arr = []
        input_arr = [item for item in input('Provide a sequence and press ENTER (Example: 2,6,7,8 or g,c,d,b,e,f): ').split(',')]
        return input_arr




    def __router(self,request):

        option = input("Option:")

        if option == 'Exit':
            print("--------------->Back To Main Menu<---------------")

            id = ObjMapper.OBJ_MAP['main_menu']
            route = ObjMapper.id2obj(id)
            route.menu_window()


        input_arr = self.__get_inputs()

        if option == 'A':

            print('--------------->Binary Tree<---------------')

            #Creating Binary Tree
            binary_tree_obj = BinaryTree()

            #Inserting each content to form the tree
            for value in input_arr:

                binary_tree_obj.insert(value)

            binary_tree_obj.show_tree()


