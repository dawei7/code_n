from typing import List

def solve(queries: List[str], dictionary: List[str]) -> List[str]:
    """
    Determines which query words are within two edits of any word in the dictionary.
    """
    result = []
    
    for query in queries:
        is_valid = False
        for word in dictionary:
            # Count differences between query and dictionary word
            diff_count = 0
            for i in range(len(query)):
                if query[i] != word[i]:
                    diff_count += 1
                
                # Optimization: break early if edits exceed 2
                if diff_count > 2:
                    break
            
            if diff_count <= 2:
                is_valid = True
                break
        
        if is_valid:
            result.append(query)
            
    return result
