#Given an array of N integer, we have to maximize the sum of arr[i] * i, where i is the index 
#of the element (i = 0, 1, 2, ..., N). We can rearrange the position of the integer in the array 
#to maximize the sum.

def maximize_sum(arr):
    n = len(arr)
    # Sort the array
    arr.sort()
    # Calculate the sum
    max_sum = sum(arr[i] * i for i in range(n))
    return max_sum

# Input
arr = list(map(int, input("Enter the array of integers separated by space: ").split()))

# Output
print("Maximum sum after rearranging the array:", maximize_sum(arr))
