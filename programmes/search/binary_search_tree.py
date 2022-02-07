from ..graph.tree.binary_tree import BinaryTree


class BinarySearchTree:

    def __init__(self) -> None:
        self.binary_tree = self.__construct_tree()
        



    def __construct_tree(self):

        content_list = self.__get_inputs()
        
        tree_obj = BinaryTree()
        for item in content_list:
            tree_obj.insert(item)

        return tree_obj




    def __get_inputs(self):

        input_arr = []
        input_arr = [item for item in input('Provide a sequence and press ENTER (Example: 2,6,7,8 or g,c,d,b,e,f): ').split(',')]
        #Demo: g,c,b,a,e,d,f,i,h,j,k
        return input_arr




    def find_with_bst(self,target):
        
        current_node = self.binary_tree.root

        while True:
            if target == current_node.data:
                return True
            elif target < current_node.data:
                current_node = current_node.left_node
            elif target > current_node.data:
                current_node = current_node.right_node
            elif current_node.left_node == None and current_node.right_node == None:
                break

        return False


