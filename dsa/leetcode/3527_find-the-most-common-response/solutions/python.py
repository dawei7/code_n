from collections import Counter
from typing import List

def solve(responses: List[str]) -> str:
    if not responses:
        return ""
    
    # Count the frequency of each response
    counts = Counter(responses)
    
    # Initialize variables to track the best response
    most_common_response = ""
    max_count = -1
    
    # Iterate through the dictionary to find the most frequent
    # and lexicographically smallest string
    for response, count in counts.items():
        if count > max_count:
            max_count = count
            most_common_response = response
        elif count == max_count:
            if response < most_common_response:
                most_common_response = response
                
    return most_common_response
