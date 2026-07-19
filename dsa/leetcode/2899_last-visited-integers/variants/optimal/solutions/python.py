from typing import List

def solve(nums: List[str]) -> List[int]:
    history = []
    results = []
    consecutive_prev = 0
    
    for item in nums:
        if item == "prev":
            consecutive_prev += 1
            # Check if the k-th last element exists
            if consecutive_prev <= len(history):
                # The k-th last element is at index len(history) - k
                results.append(history[-consecutive_prev])
            else:
                results.append(-1)
        else:
            # Reset consecutive count and add integer to history
            consecutive_prev = 0
            history.append(int(item))
            
    return results
