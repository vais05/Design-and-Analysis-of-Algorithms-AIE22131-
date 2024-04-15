

def maximumPeople(p, x, y, r):
    events = []
    for i, town_pos in enumerate(x):
        # Mark the start and end of town influence with population
        events.append((town_pos, 'start', p[i]))
        events.append((town_pos, 'end', p[i]))
    for i, cloud_pos in enumerate(y):
        # Mark the start and end of cloud coverage
        events.append((cloud_pos - r[i], 'cloud_start', i))
        events.append((cloud_pos + r[i], 'cloud_end', i))

    events.sort()  # Sort events based on position
    
    current_clouds = set()
    cloud_cover = [0] * len(y)  # Population covered by each cloud
    sunny_population = 0
    for event in events:
        pos, event_type, value = event
        if event_type == 'start':
            if not current_clouds:  # If no clouds, it's sunny
                sunny_population += value
            elif len(current_clouds) == 1:  # If one cloud, add population to that cloud's cover
                cloud_cover[list(current_clouds)[0]] += value
        elif event_type == 'end':
            continue  # End of town influence, not needed for logic
        elif event_type == 'cloud_start':
            current_clouds.add(value)
        elif event_type == 'cloud_end':
            current_clouds.remove(value)
    
    # Find the cloud covering the maximum population
    max_covered_by_single_cloud = max(cloud_cover)
    return sunny_population + max_covered_by_single_cloud

# User input
n = int(input("Enter the number of towns: "))
p = list(map(int, input("Enter the populations of the towns separated by spaces: ").split()))
x = list(map(int, input("Enter the positions of the towns separated by spaces: ").split()))
m = int(input("Enter the number of clouds: "))
y = list(map(int, input("Enter the positions of the clouds separated by spaces: ").split()))
r = list(map(int, input("Enter the ranges of the clouds separated by spaces: ").split()))

# Calculate and print the maximum number of people in sunny towns after removing one cloud
print(maximumPeople(p, x, y, r))
