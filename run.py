from programmes.menu import Menu
#As This file is acting as Main the 'programmes' folder will act as a "package".  [do not use '.programmes']  

import gc #garbage collector
#https://docs.python.org/3/library/gc.html

 #PEP 8 -- Style Guide for Python Code
 #https://www.python.org/dev/peps/pep-0008/


def main():

    try:

        main_menu = Menu() #Creating instance 
        main_menu #Calling instance 

    except Exception as e:

        print(e)




if __name__ == '__main__':
    main()