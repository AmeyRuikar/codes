#! /usr/bin/python
'Merge-Sort is a popular sorting algorithm based on the divide and conquer paradigm.'
'The working time for merge-sort is bounded by O(nlogn).'
class merge_sort:

    array = []
    n = 0

    def __init__(self):
        self.n = 0
        return
    
    def get_values(self):
        
        self.n = input("enter total number of elements in the array: ")

        self.n = int(self.n)
        
        for i in range(self.n):
            
            print("enter number at position arr[",i,"]")
            x = input("")
            self.array.append(int(x))
        print("Array->",self.array)


        
        
    def sort(self, x, small_n):

        'recurive sort'


        print("array->",x,"  n->", small_n)
        res = []

        n = 0;
              
        if small_n == 1:

            res.append(x[0])
            return res
            
 
        else:

            
            n = int(small_n /2)


            if small_n % 2 == 0:
                temp = x[0:n]            
                temp2 = x[n : small_n]
                arr1 = self.sort(temp, n)
                arr2 = self.sort(temp2, n)
            else:
                temp = x[0:n]
                temp2 = x[n : small_n]
                arr1 = self.sort(temp, n)
                arr2 = self.sort(temp2, n + 1)
                
           
 

            
        'merge the two arrays'

        i = 0
        j = 0

        arr1.append(9999)
        arr2.append(9999)
        'just for comparison'


        print("merge")
        for k in range(small_n):

            if arr1[i] < arr2[j]:

                res.append(arr1[i])
                i = i + 1
                
            else:

                res.append(arr2[j])
                j = j + 1           



        print(res)
        return res


merge_s = merge_sort()

merge_s.get_values()

result_arr = merge_s.sort(merge_s.array,int(merge_s.n))

