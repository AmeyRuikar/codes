#! /usr/bin/python


arr = [34, 768, 542, 33, 1, 89, 45, 399, 755, 65]

def binary_search( start, stop, x):

    


    mid = int((start + stop) / 2)


    if(arr[mid] == x):

        print("element found AT index: ", mid)
        return 1
    else:

        if(start == stop):
            return

        if(arr[mid] > x):
            print("rec call")
            
            binary_search(start, mid, x)

        else:
             print("rec call")
             binary_search(mid + 1, stop, x)



    
'for binary search array should be in sorted order'
arr.sort()
print("sorted array ->")
print(arr)


x =int( input("enter number to be searched: "))

binary_search(0, len(arr) - 1, x)
