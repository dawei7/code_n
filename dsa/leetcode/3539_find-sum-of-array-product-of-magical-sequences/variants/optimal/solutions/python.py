def solve(nums: list[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    total_sum_of_products = 0
    
    # The product of a sequence grows very quickly.
    # If a sequence contains elements > 1, its length is limited.
    # We handle sequences with 1s separately or via the sliding window.
    
    for i in range(n):
        current_prod = 1
        current_sum = 0
        
        for j in range(i, n):
            val = nums[j]
            
            # Update product and sum
            current_prod *= val
            current_sum += val
            
            # If product exceeds the maximum possible sum of the array,
            # we can stop because it will never equal the sum again.
            # (Assuming positive integers)
            if current_prod > 2 * 10**9: # Heuristic bound
                break
                
            if current_prod == current_sum:
                total_sum_of_products = (total_sum_of_products + current_prod) % MOD
                
    return total_sum_of_products
