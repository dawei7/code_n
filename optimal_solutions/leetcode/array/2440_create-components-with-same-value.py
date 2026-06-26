import collections

def solve(nums: list[int], edges: list[list[int]]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    
    total_sum = sum(nums)
    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    def can_partition(target: int) -> bool:
        # Returns the sum of the current subtree if it can be partitioned,
        # otherwise returns -1.
        def dfs(u, p):
            current_sum = nums[u]
            for v in adj[u]:
                if v == p:
                    continue
                res = dfs(v, u)
                if res == -1:
                    return -1
                current_sum += res
            
            if current_sum == target:
                return 0
            return current_sum
            
        return dfs(0, -1) == 0

    # We want to maximize k, which means minimizing target_sum = total_sum / k.
    # k can range from n down to 1.
    # target_sum must be a divisor of total_sum.
    # The smallest possible target_sum is max(nums).
    
    max_val = max(nums)
    for k in range(n, 0, -1):
        if total_sum % k == 0:
            target = total_sum // k
            if target >= max_val:
                if can_partition(target):
                    return k - 1
                    
    return 0
