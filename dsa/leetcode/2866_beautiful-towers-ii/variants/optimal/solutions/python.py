def solve(maxHeights: list[int]) -> int:
    n = len(maxHeights)
    
    def get_sums(arr):
        sums = [0] * n
        stack = []  # Stores indices
        current_sum = 0
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                prev_idx = stack[-1] if stack else -1
                # Remove the contribution of the popped element
                current_sum -= (idx - prev_idx) * arr[idx]
            
            # Add contribution of current element
            prev_idx = stack[-1] if stack else -1
            current_sum += (i - prev_idx) * arr[i]
            sums[i] = current_sum
            stack.append(i)
        return sums

    left_sums = get_sums(maxHeights)
    right_sums = get_sums(maxHeights[::-1])[::-1]
    
    max_total = 0
    for i in range(n):
        # Total sum = left_sum + right_sum - peak_height
        total = left_sums[i] + right_sums[i] - maxHeights[i]
        if total > max_total:
            max_total = total
            
    return max_total
