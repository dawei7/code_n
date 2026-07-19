from typing import List

def solve(price: List[int], k: int) -> int:
    price.sort()
    
    def can_achieve(min_diff: int) -> bool:
        count = 1
        last_price = price[0]
        for i in range(1, len(price)):
            if price[i] - last_price >= min_diff:
                count += 1
                last_price = price[i]
                if count >= k:
                    return True
        return False

    low = 0
    high = price[-1] - price[0]
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_achieve(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return ans
