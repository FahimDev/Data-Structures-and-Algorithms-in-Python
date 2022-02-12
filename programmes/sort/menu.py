from posixpath import split
from .bubble_sort import BubbleSort
from .selection_sort import SelectionSort
from .insertion_sort import InsertionSort
from .merge_sort import MergeSort
#from ..menu import Menu

import time

from .. import ObjMapper


class SortMenu:


    def __init__(self):
        print("--------------->Sort Menu<---------------")



    def get_indexed(self):
        ObjMapper.OBJ_MAP['sort_menu'] = ObjMapper.remember(self)




    def menu_window(self,request = None):

        #get indexed by ObjMapper
        self.get_indexed()

        self.__menu_header()

        sorted_response = self.__router(request)

        return sorted_response




    def __menu_header(self):

        print("--------------->Sort Options<---------------")
        print("Options: (A) Bubble Sort | (B) Selection Sort | (C) Insertion Sort | (D) Merge Sort | (Exit) Back")
        print("Give input option and press ENTER:")




    def __get_inputs(self):

        input_arr = []
        input_arr = [int(item) for item in input('Provide number sequence and press ENTER (Example: 2,6,7,8,0,33,99,34,87,65): ').split(',')]
        return input_arr


  
        
    def __router(self,request):

        option = input("Option:")


        if option == 'Exit':
            print("--------------->Back To Main Menu<---------------")

            id = ObjMapper.OBJ_MAP['main_menu']
            route = ObjMapper.id2obj(id)
            route.menu_window()


        input_arr = self.__get_inputs()
        sorted_response = []

        if option == 'A':

            print('--------------->Bubble Sort<---------------')
            
            bubble_sort = BubbleSort()

            start = time.time()

            sorted_response = bubble_sort.bubbleSort(input_arr)

            print(sorted_response)

            end = time.time()
            print(end - start)

        elif option == 'B':

            print('--------------->Selection Sort<---------------')

            selection_sort = SelectionSort()
            
            sorted_response = selection_sort.selectionSort(input_arr)

            print(sorted_response)

        elif option == 'C':
            
            print('--------------->Insertion Sort<---------------')

            insertion_sort = InsertionSort()

            sorted_response = insertion_sort.insertionSort(input_arr)

            print(sorted_response)

        elif option == 'D':
            
            print('--------------->Merge Sort<---------------')

            merge_sort = MergeSort()

            sorted_response = merge_sort.merge_sort(input_arr)

            print(sorted_response)


        else:
             print('--------------->Option unknown!<---------------')
            


        if request == 'api':
            return sorted_response

        print('\n')

        #Back to Sort Menu
        self.menu_window()


