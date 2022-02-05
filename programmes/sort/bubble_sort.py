class BubbleSort:


    def bubbleSort(self, arr):
        return self.__sort(arr)




    def __sort(self,arr):
                
        swapped = True

        while swapped:
            swapped = False
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp
                    swapped = True
        return arr

