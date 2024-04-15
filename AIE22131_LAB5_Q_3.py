def maximumPeople(town_populations, town_locations, cloud_locations, cloud_ranges):
    n = len(town_populations)
    m = len(cloud_locations)
    
    # Initialize total population in sunny towns
    total_sunny_population = sum(town_populations)
    
    # Initialize population covered by each cloud
    cloud_covered_population = [0] * m
    
    # Count population covered by each cloud
    for i in range(n):
        for j in range(m):
            if abs(town_locations[i] - cloud_locations[j]) <= cloud_ranges[j]:
                cloud_covered_population[j] += town_populations[i]
    
    # Find the cloud that covers the maximum population
    max_population_covered = max(cloud_covered_population)
    max_population_index = cloud_covered_population.index(max_population_covered)
    
    # Subtract the population covered by the cloud from the total sunny population
    total_sunny_population -= max_population_covered
    
    return total_sunny_population

# Input
n = int(input("Enter the number of towns: "))
town_populations = list(map(int, input("Enter the populations of each town: ").split()))
town_locations = list(map(int, input("Enter the locations of each town: ").split()))

m = int(input("Enter the number of clouds: "))
cloud_locations = list(map(int, input("Enter the locations of each cloud: ").split()))
cloud_ranges = list(map(int, input("Enter the range of each cloud: ").split()))

# Output
print("Maximum number of people in sunny towns after removing exactly one cloud:", 
      maximumPeople(town_populations, town_locations, cloud_locations, cloud_ranges))
