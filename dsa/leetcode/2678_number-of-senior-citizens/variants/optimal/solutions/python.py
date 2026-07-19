from typing import List

def solve(details: List[str]) -> int:
    """
    Counts the number of senior citizens from a list of passenger detail strings.

    A passenger is considered a senior citizen if their age, extracted from
    indices 11 and 12 of their detail string, is strictly greater than 60.

    Args:
        details: A list of strings, where each string is 15 characters long
                 and contains passenger information.

    Returns:
        The total count of senior citizens.
    """
    senior_citizens_count = 0

    for passenger_detail in details:
        # Extract the age substring from indices 11 and 12 (inclusive)
        # Python slicing [11:13] extracts characters at index 11 and 12.
        age_str = passenger_detail[11:13]
        
        # Convert the age string to an integer
        age = int(age_str)
        
        # Check if the passenger is a senior citizen (age strictly greater than 60)
        if age > 60:
            senior_citizens_count += 1
            
    return senior_citizens_count
