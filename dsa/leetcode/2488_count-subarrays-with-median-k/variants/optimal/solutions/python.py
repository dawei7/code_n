def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    k_index = -1
    for i in range(n):
        if nums[i] == k:
            k_index = i
            break
    
    # counts stores the frequency of prefix sums to the left of k_index
    # We use a dictionary to store the balance: (count of > k) - (count of < k)
    counts = {0: 1}
    current_balance = 0
    
    # Traverse left from k_index to store prefix balances
    for i in range(k_index - 1, -1, -1):
        if nums[i] < k:
            current_balance -= 1
        else:
            current_balance += 1
        counts[current_balance] = counts.get(current_balance, 0) + 1
        
    ans = 0
    current_balance = 0
    # Traverse right from k_index and check for valid subarrays
    # A subarray is valid if the total balance is 0 or 1
    for i in range(k_index, n):
        if nums[i] < k:
            current_balance -= 1
        elif nums[i] > k:
            current_balance += 1
            
        # We need total_balance to be 0 or 1
        # left_balance + right_balance = 0 => left_balance = -right_balance
        # left_balance + right_balance = 1 => left_balance = 1 - right_balance
        ans += counts.get(-current_balance, 0)
        ans += counts.get(1 - current_balance, 0)
        
    return ans
