class SelectionSort:

    def selectionSort(self, arr):
        return self.__sort(arr)

    def __sort(self, arr):

        for i in range(len(arr)):
            index_minimum = i
            for j in range(index_minimum+1, len(arr)):
                if arr[index_minimum] > arr[j]:
                    index_minimum = j

            min_val = arr[index_minimum]
            arr[index_minimum] = arr[i] 
            arr[i] = min_val
        return arr
                