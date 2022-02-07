from .sort.menu import SortMenu
from .search.menu import SearchMenu
from .linked_list.menu import LinedListMenu
from .graph.menu import GraphMenu

from . import ObjMapper


class Menu:
    __BANNER = '''
    ------------------------------------------------------------------------
    Welcome to the Data Structure Sample Code Collection of Md. Ariful Islam
            [fahim.arif0373@outlook.com | ariful@ieee.org]
    ------------------------------------------------------------------------
    '''


    def __init__(self):
        self.__BANNER
        self.menu_window()




    def menu_window(self):

        ObjMapper.OBJ_MAP['main_menu'] = ObjMapper.remember(self)

        self.__menu_header()
        self.__router()




    def __menu_header(self):
        print("--------------->MENU<---------------")
        print("Options: (A) Sorting | (B) Search | (C) Linked List | (D) Stack | (D) Queue | (D) Priority Queue | (D) Graph | (Exit) Exit")
        print("Give input option and press ENTER:")




    def __router(self):

        option = input()

        if option == 'A':

            sort_menu = SortMenu()
            sort_menu.menu_window()

        elif option == 'B':

            search_menu = SearchMenu()
            search_menu.menu_window()

        elif option == 'C':
            pass
        elif option == 'D':

            graph_menu = GraphMenu()
            graph_menu.menu_window()
            
        elif option == 'Exit':
            print("--------------->EXIT<---------------")