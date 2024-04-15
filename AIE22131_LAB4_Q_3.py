#Given two arrays array_One[] and array_Two[] of same size N. We need to first rearrange 
#the arrays such that the sum of the product of pairs (1 element from each) is minimum. That 
#is SUM (A[i] * B[i]) for all i is minimum.
#• Time complexity of Brute Force Approach: O((N!)^2)
#• Time complexity of Greedy Algorithm: O(N logN)

def min_sum_of_products(array_One, array_Two):
    # Sort both arrays
    array_One.sort()
    array_Two.sort(reverse=True)  # Sort in reverse order

    # Calculate the sum of products
    min_sum = sum(array_One[i] * array_Two[i] for i in range(len(array_One)))

    return min_sum

# Input
array_One = list(map(int, input("Enter the elements of array_One separated by space: ").split()))
array_Two = list(map(int, input("Enter the elements of array_Two separated by space: ").split()))

# Output
print("Minimum sum of products after rearranging the arrays:", min_sum_of_products(array_One, array_Two))

