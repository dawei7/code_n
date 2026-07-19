from typing import List

def solve(rolls: List[int], k: int) -> int:
    """
    Calculates the length of the shortest impossible sequence of rolls.

    The algorithm greedily counts how many times a complete set of distinct
    rolls from 1 to k can be formed as disjoint subsequences. If 'm' such
    complete sets can be formed, it implies that any sequence of length 'm'
    can be constructed. The shortest impossible sequence will then have length 'm + 1'.

    Args:
        rolls: A list of integers representing the outcomes of dice rolls.
               Each roll is guaranteed to be between 1 and k.
        k: The maximum possible value for a single roll.

    Returns:
        The length of the shortest positive integer sequence (composed of values
        from 1 to k) that cannot be formed as a subsequence of `rolls`.
    """
    
    # `current_sequence_length` tracks the number of complete sets of {1, ..., k}
    # that we have successfully formed. If we form 'm' such sets, it means we can
    # construct any sequence of length 'm'.
    current_sequence_length = 0
    
    # `seen_in_current_block` stores the distinct roll values (from 1 to k)
    # encountered in the current segment of `rolls` as we try to complete
    # a new set of {1, ..., k}.
    seen_in_current_block = set()
    
    for roll in rolls:
        # We only consider rolls that are within the valid range [1, k].
        # Rolls outside this range are irrelevant for forming sequences of 1 to k.
        if 1 <= roll <= k:
            # Add the current roll to our set of seen numbers for the current block.
            # Set.add() handles duplicates efficiently.
            seen_in_current_block.add(roll)
            
            # If the size of the set equals k, it means we have successfully collected
            # all k distinct numbers (1 through k) in the current block of rolls.
            if len(seen_in_current_block) == k:
                # We have completed one "full set" of {1, ..., k}.
                # This allows us to extend the length of sequences we can form by one.
                current_sequence_length += 1
                
                # Clear the set to start collecting for the next "full set"
                # using subsequent rolls.
                seen_in_current_block.clear()
                
    # After iterating through all rolls, `current_sequence_length` holds the maximum
    # number 'm' such that all sequences of length 'm' can be formed.
    # The shortest impossible sequence will therefore have length 'm + 1'.
    return current_sequence_length + 1
