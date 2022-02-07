from dataclasses import dataclass
from tkinter.messagebox import NO
from turtle import left, right


class BinaryTreeNode:
        
        
    def __init__(self,value,left_node = None, right_node = None):
        self.data = value 
        self.left_node = left_node
        self.right_node = right_node




class BinaryTree:

    def __init__(self):
        self.root = None




    def insert(self,value):
        
        new_node = BinaryTreeNode(value)

        if self.root is None:
            self.root = new_node
            #print(new_node.data, " is the Root of the tree...")
            return


        current_node = self.root

        while True:

            if value < current_node.data:

                if current_node.left_node is None:

                    current_node.left_node = new_node
                    #print(new_node.data, " is the left child of ", current_node.data)
                    break

                else:

                    current_node = current_node.left_node

            else:
                
                if current_node.right_node is None:

                    current_node.right_node = new_node
                    #print(new_node.data, " is the right child of ", current_node.data)
                    break

                else:

                    current_node = current_node.right_node




    # breadth-first traversal
    def show_tree(self):

        print('Under Construction....')

