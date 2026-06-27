def solve(fruits: list[int], baskets: list[int]) -> int:
    """
    Greedily assigns fruits to the first available basket that can hold them.
    """
    count = 0
    n = len(baskets)
    used = [False] * n
    
    for fruit in fruits:
        for i in range(n):
            if not used[i] and baskets[i] >= fruit:
                used[i] = True
                count += 1
                break
                
    return count
