class Fibonacci:

    def fibo_operator(self, fibo_range:int, recursion = False):
        
        fibo_result = []

        if recursion is True:

            """
            Here we are passing the smallest to largest sequnece (0:n) for 
            recursion at __recur_fibo() function. And for each operation 
            of the loop the Bigger Number it get this function goes to the 
            smallest chunk of that operation and when it finally returns 
            with the final value the recursion function calculates each of its
            pending stpes and finally returns with the total Number.
            """
            for i in range(fibo_range):

                result = self.__recur_fibo(i)
                print(i,"----------------------------------------------------------->",result)
                fibo_result.append(result)

        else:
            fibo_result = self.__fibo_calculation(fibo_range)
        
        return fibo_result




    def __recur_fibo(self,n:int):
        
        if n <= 1:
            print("Return", n)
            return n

        else:
            print("Drop:", n-1, n-2,"Total:", n-1 + n-2)
            return(self.__recur_fibo(n-1) + self.__recur_fibo(n-2))




    def __fibo_calculation(self, n:int):
        
        a = 0
        b = 1
        sum = 0
        i = 0
        fibo_result =[0,1]

        while i < n-2:

            sum  = a + b
            a = b
            b = sum

            fibo_result.append(sum)
            i += 1

        return fibo_result
            



