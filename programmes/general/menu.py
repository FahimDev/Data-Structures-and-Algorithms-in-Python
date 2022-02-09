import time

from .. import ObjMapper

from .fibonacci import Fibonacci


class GeneralMenu:
    def __init__(self):
        print("--------------->General Menu<---------------")



    def get_indexed(self):
        ObjMapper.OBJ_MAP['general_menu'] = ObjMapper.remember(self)




    def menu_window(self,request = None):

        #get indexed by ObjMapper
        self.get_indexed()

        self.__menu_header()

        sorted_response = self.__router(request)

        return sorted_response




    def __menu_header(self):

        print("--------------->General Options<---------------")
        print("Options: (A) Fibonacci (Recursion) | (B) Fibonacci | (Exit) Back")
        print("Give input option and press ENTER:")




    def __router(self,request):

        option = input("Option:")

        if option == 'Exit':
            print("--------------->Back To Main Menu<---------------")

            id = ObjMapper.OBJ_MAP['main_menu']
            route = ObjMapper.id2obj(id)
            route.menu_window()


        if option == 'A':

            print('--------------->Fibonacci: Recursion<---------------')

            fibo_range = input('Please input Fibonacci range: ')

            fibonacci = Fibonacci()
            
            start = time.time()
            print(fibonacci.fibo_operator(int(fibo_range),recursion=True))
            end = time.time()


            print("Time: ",end - start)

        elif option == 'B':

            print('--------------->Fibonacci<---------------')

            fibo_range = input('Please input Fibonacci range: ')

            fibonacci = Fibonacci()

            start = time.time()
            print(fibonacci.fibo_operator(int(fibo_range),recursion=False))
            end = time.time()


            print("Time: ",end - start)

        self.menu_window()
        


            


