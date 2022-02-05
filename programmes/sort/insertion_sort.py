class InsertionSort:


    def insertionSort(self, arr):
        return self.__sort(arr)




    def __sort(self,arr):

        for sorted_index in range(len(arr)-1):
            reverse_index = sorted_index
            current_value = arr[sorted_index + 1]
            while reverse_index >= 0 and current_value < arr[reverse_index]:
                arr[reverse_index+1] = arr[reverse_index]
                arr[reverse_index] = current_value #in every swap 'current_value' will be at 'reverse_index+1' index of the Array
                reverse_index += -1 

        return(arr)
