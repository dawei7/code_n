from typing import List

def solve(message: List[str], bannedWords: List[str]) -> bool:
    """
    Determines if a message is spam by checking if at least two words
    from the message exist in the bannedWords set.
    """
    banned_set = set(bannedWords)
    spam_count = 0
    
    for word in message:
        if word in banned_set:
            spam_count += 1
            # If we find at least two banned words, it's spam.
            if spam_count >= 2:
                return True
                
    return False
