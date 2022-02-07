from posixpath import split

from numpy import sort
from ..sort.menu import SortMenu
from .binary_search import BinarySearch
from .binary_search_tree import BinarySearchTree


import time

from .. import ObjMapper


class SearchMenu:


    def __init__(self):
        print("--------------->Search Menu<---------------")




    def get_indexed(self):
        ObjMapper.OBJ_MAP['search_menu'] = ObjMapper.remember(self)




    def menu_window(self):

        #get indexed by ObjMapper
        self.get_indexed()

        self.__menu_header()

        self.__router()




    def __menu_header(self):

        print("--------------->Search Options<---------------")
        print("Options: (A) Linear Search | (B) Binary Search | (C) Binary Search Tree | (Exit) Back")
        print("Give input option and press ENTER:")




    def __router(self):

        option = input("Option:")

        search =  None
        
        if option == 'A':

            print('--------------->Linear Search<---------------')
            

        elif option == 'B':

            print('--------------->Binary Search<---------------')

            print('For Binary Search we must sort the number sequence first. Please, select a Sorting Algorithm first.')

            start = time.time()

            #If Sort Menu instance is not indexed in the ObjMapper Create NEW and get indexed.
            if 'sort_menu' not in ObjMapper.OBJ_MAP:
                indexed = SortMenu()
                indexed.get_indexed()
            
                
            sorted = self.__getSorted()


            print(sorted)

            target = int(input("Search Element:"))

            search =  BinarySearch()

            target_index = search.binary_search(target, sorted)

            if target is None:
                print("Search item not found in the List!")
            else:
                print("Content Found at index: ",target_index)

            end = time.time()
            print(end - start)

        elif option == 'C':
            
            print('--------------->Binary Search Tree<---------------')
            search = BinarySearchTree()

            target = input('Please, input search content:')

            target = search.find_with_bst(target)

            if target:
                print("Search Content Found!")
            else:
                print("Search content doesent exist...")

        elif option == 'Exit':
            print("--------------->Back To Main Menu<---------------")

            id = ObjMapper.OBJ_MAP['main_menu']
            route = ObjMapper.id2obj(id)
            route.menu_window()

        print('\n')

        #Back to Search Menu
        self.menu_window()




    def __getSorted(self):

        id = ObjMapper.OBJ_MAP['sort_menu']
        route = ObjMapper.id2obj(id)
        sorted_list = route.menu_window('api')
        return sorted_list
        


