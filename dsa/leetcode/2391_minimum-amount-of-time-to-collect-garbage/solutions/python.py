from typing import List

def solve(garbage: List[str], travel: List[int]) -> int:
    # Total time = (sum of all garbage units) + (sum of travel times)
    # Each truck only travels up to the last house containing its specific type.
    
    total_pickup_time = 0
    last_house_indices = {'M': 0, 'P': 0, 'G': 0}
    
    # Calculate total pickup time and find the last house for each type
    for i, house in enumerate(garbage):
        total_pickup_time += len(house)
        for char in house:
            last_house_indices[char] = i
            
    # Calculate prefix sums for travel times to quickly get travel duration
    # travel_prefix[i] is the time to reach house i from house 0
    travel_prefix = [0] * len(garbage)
    for i in range(len(travel)):
        travel_prefix[i + 1] = travel_prefix[i] + travel[i]
        
    total_travel_time = 0
    for char in ['M', 'P', 'G']:
        last_idx = last_house_indices[char]
        total_travel_time += travel_prefix[last_idx]
        
    return total_pickup_time + total_travel_time
