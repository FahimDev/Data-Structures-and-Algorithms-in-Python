
class MergeSort:

    def merge_sort(self, arr):
        
        # len() function starts counting from 1 
        if len(arr) > 1:
            
            mid_index = len(arr) // 2
            # Deviding the array from the middle index (with Range ':' )
            left_arr = arr[:mid_index]
            right_arr = arr[mid_index:]

            #Recursion to get the one indexed array in both Left and Right side array.
            self.merge_sort(left_arr)
            self.merge_sort(right_arr)

            # Temporary index with default value = 0
            # i for Left Side index | j for Right side index | k for actual array index
            i = j = k = 0

            while i < len(left_arr) and j < len(right_arr):
                
                if left_arr[i] < right_arr[j]:

                    arr[k] = left_arr[i]
                    i += 1

                else:
                    
                    arr[k] = right_arr[j]
                    j += 1

                #after every step of sort swapping we must increase the actual array index number 
                k += 1

            #Balance if there is any missing index ( There can be same values in multiple indexs also )
            #if any index got missing from Left/Right sub array in the upper While Loop This two While Loop will work
            
            # Balance for left side  
            while i < len(left_arr):
                
                arr[k] = left_arr[i]

                i += 1
                k += 1

            #Balance for right side
            while j < len(right_arr):
                
                arr[k] = right_arr[j]

                j += 1
                k += 1

        # when the array is will have only one index it will start returning to its previous state. 
        # If the Function is called by Recursion the return will go back to itself (Think like a STACK)
        """
        ---> But when all the Recursion calls are over The Final Sorted Result will return 
            to the main caller as Final Result.
            (Where obj instance was created and method was called for the first time)
        """ 
        return arr


        def show_array(self):

            for item in arr:
                print(item)
