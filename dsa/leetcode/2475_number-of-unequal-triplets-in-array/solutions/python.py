from collections import Counter

def solve(nums: list[int]) -> int:
    """
    Calculates the number of unequal triplets using a frequency map.
    If we have counts of each number, the number of triplets (i, j, k)
    with distinct values is the sum of products of frequencies of any 
    three distinct numbers.
    """
    counts = list(Counter(nums).values())
    n = len(counts)
    triplets = 0
    
    # Iterate through all combinations of three distinct values
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                triplets += counts[i] * counts[j] * counts[k]
                
    return triplets
