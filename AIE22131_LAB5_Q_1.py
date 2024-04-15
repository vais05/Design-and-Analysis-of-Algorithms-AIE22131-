#Alice is a kindergarten teacher. She wants to give some candies to the children in her class. All the
#children sit in a line and each of them has a rating score according to his or her performance in the class.
#Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with
#the higher rating must get more candies. Alice wants to minimize the total number of candies she must
#buy.
#For example, assume her students' ratings are [4, 6, 4, 5, 6, 2]. She gives the students candy in the
#following minimal amounts: [1, 2, 1, 2, 3, 1]. She must buy a minimum of 10 candies
def candies(n, arr):
    """
    Calculate the minimum candies needed for the ratings.
    
    :param n: int - The number of children in the class.
    :param arr: List[int] - The ratings of each child.
    :return: int - The minimum number of candies required.
    """
    candies = [1] * n  # Step 1: Give each child at least one candy
    
    # Step 2: Left to right sweep
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    # Step 3: Right to left sweep
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    # Step 4: Sum up the candies
    return sum(candies)

# Taking user input
n = int(input("Enter the number of children: "))
arr = [int(input(f"Enter rating for child {i+1}: ")) for i in range(n)]

# Calculate and print minimum candies needed
print(f"Minimum candies Alice must buy: {candies(n, arr)}")
