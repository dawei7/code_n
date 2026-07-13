def solve(grid: list[list[int]]) -> int:
    sources = []
    targets = []
    
    for r in range(3):
        for c in range(3):
            if grid[r][c] > 1:
                for _ in range(grid[r][c] - 1):
                    sources.append((r, c))
            elif grid[r][c] == 0:
                targets.append((r, c))
    
    if not targets:
        return 0
    
    def get_dist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    memo = {}

    def backtrack(idx, current_targets):
        if idx == len(sources):
            return 0
        
        state = (idx, tuple(current_targets))
        if state in memo:
            return memo[state]
        
        res = float('inf')
        src = sources[idx]
        
        for i in range(len(current_targets)):
            if current_targets[i] == -1:
                current_targets[i] = 1
                dist = get_dist(src, targets[i])
                res = min(res, dist + backtrack(idx + 1, current_targets))
                current_targets[i] = -1
        
        memo[state] = res
        return res

    return backtrack(0, [-1] * len(targets))
