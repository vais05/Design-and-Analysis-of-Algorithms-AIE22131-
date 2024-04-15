#Solve the fractional knapsack problem for the given set of N items with benefit-weight 
#pairs and sack capacity of W. Print the optimal solution. Use the examples discussed in the 
#class

def fractional_knapsack(n, items, capacity):
    # Calculate value-to-weight ratio for each item
    for item in items:
        item.append(item[0] / item[1])

    # Sort items based on value-to-weight ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0
    sack = []

    for item in items:
        if capacity >= item[1]:  # If item fits completely in the sack
            sack.append((item[0], item[1], 1))
            total_value += item[0]
            capacity -= item[1]
        else:  # If item doesn't fit completely, take fraction of it
            fraction = capacity / item[1]
            sack.append((item[0] * fraction, item[1], fraction))
            total_value += item[0] * fraction
            break

    return total_value, sack

# Input
n = int(input("Enter the number of items: "))
items = []
for i in range(n):
    benefit, weight = map(int, input(f"Enter benefit and weight for item {i+1}: ").split())
    items.append([benefit, weight])

capacity = int(input("Enter the sack capacity: "))

# Solve fractional knapsack problem
total_value, sack = fractional_knapsack(n, items, capacity)

# Output
print("Optimal Solution:")
print("Total value obtained:", total_value)
print("Items in the sack:")
for item in sack:
    print("Benefit:", item[0], "- Weight:", item[1], "- Fraction:", item[2])
