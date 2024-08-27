####
# Quicksort algorithm taken from:
# https://www.geeksforgeeks.org/quick-sort/
# acessed on 08/20/24
# license: none given
# author: unlisted
####
# Python3 implementation of QuickSort
# 
# This function handles sorting part of quick sort start and end points to first and last element of an array respectively 


def partition(arr, low, high):
    
    # Choose the pivot
    pivot = arr[high]
    
    i = low - 1
    
    # Traverse arr[low..high] and move all smaller
    # elements on the left side. Elements from low to 
    # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Move pivot after smaller elements and
    # return its position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# The QuickSort function implementation
def quick_sort(arr, low, high):
    if low < high:
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)

        # Recursion calls for smaller elements
        # and greater or equals elements
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Driver code
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Given array is")
    print(arr)

    quick_sort(arr, 0, len(arr) - 1)

    print("\nSorted array is")
    print(arr)



