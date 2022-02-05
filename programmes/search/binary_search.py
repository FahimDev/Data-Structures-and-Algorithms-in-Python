
class BinarySearch:
    
    def binary_search(self,target, arr):
        mid_index = 0
        left_index = 0
        right_index = len(arr)-1

        print(target)
        print(arr)

        while left_index <= right_index:
            mid_index = left_index + (right_index - left_index) // 2

            print("Index: ", left_index, mid_index, right_index)

            if target == arr[mid_index]:

                return mid_index
            
            elif target <  arr[mid_index]:

                right_index =  mid_index - 1

            else:
                left_index = mid_index + 1

            print("Index: ", left_index, mid_index, right_index)

        return None
