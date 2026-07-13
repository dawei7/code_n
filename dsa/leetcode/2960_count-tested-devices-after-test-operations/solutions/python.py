def solve(batteryPercentages: list[int]) -> int:
    """
    Calculates the number of tested devices by tracking the number of 
    successful tests performed so far.
    """
    tested_count = 0
    
    for battery in batteryPercentages:
        # The effective battery is the original battery minus the number 
        # of devices already tested.
        if battery - tested_count > 0:
            tested_count += 1
            
    return tested_count
