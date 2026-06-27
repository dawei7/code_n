def solve(nums: list[int]) -> int:
    def get_max_digit(n: int) -> int:
        max_d = 0
        while n > 0:
            max_d = max(max_d, n % 10)
            n //= 10
        return max_d

    # Stores the largest number found so far for each max digit (0-9)
    max_val_for_digit = {}
    max_sum = -1

    for num in nums:
        d = get_max_digit(num)
        
        if d in max_val_for_digit:
            # If we have seen this max digit before, calculate the sum
            current_sum = num + max_val_for_digit[d]
            max_sum = max(max_sum, current_sum)
            # Update the stored value if the current number is larger
            max_val_for_digit[d] = max(max_val_for_digit[d], num)
        else:
            # First time seeing this max digit
            max_val_for_digit[d] = num
            
    return max_sum
