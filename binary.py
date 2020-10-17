# # Implement Binary Search
# # Algorithm
# #     1.Keep track of two pointers First and Last, these are incremented or decremented to limit the part of the list to be searched.
# #     2.Find the middle element of the list: mid = ( length of the list )/2
# #     3.Compare the middle element with the value to be found
# #     4.Check if the middle element is lesser than the value to be found:
# #     5.If yes, the element must lie on the second half of the list
# #     6.If no, the element must lie on the first half of the list
# #     7.Repeat steps 1 through 3 until the element is found or the end of the list is reached.
# # Note:The array or list should be shorted.


# def binarySearch(ls, data):
#    first = 0
#    last = len(ls)-1
#    done = False
#    while first <= last and not done:
#        mid = (first+last)//2
#        if ls[mid] == data:
#            done = True
#        else:
           
#             if ls[mid]>data:
#                 last = last-1
#             else:
#                 first = first+1
#     return done
# print(binarySearch([2,5,7,8,9,11,14,16],4))


















# # Iterative Binary Search Function 
# # It returns index of x in given array arr if present, 
# # else returns -1 
# def binary_search(arr, x): 
#     low = 0
#     high = len(arr) - 1
#     mid = 0
  
#     while low <= high: 
  
#         mid = (high + low) // 2
  
#         # Check if x is present at mid 
#         if arr[mid] < x: 
#             low = mid + 1
  
#         # If x is greater, ignore left half 
#         elif arr[mid] > x: 
#             high = mid - 1
  
#         # If x is smaller, ignore right half 
#         else: 
#             return mid 
  
#     # If we reach here, then the element was not present 
#     return -1
  
  
# # Test array 
# arr = [ 2, 3, 4, 10, 40 ] 
# x = 10
  
# # Function call 
# result = binary_search(arr, x)






















# Python 3 program for recursive binary search. 
# Modifications needed for the older Python 2 are found in comments. 
  
# Returns index of x in arr if present, else -1 
def binary_search(arr, low, high, x): 
  
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binary_search(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 