from typing import List

def solve(board: List[List[int]]) -> int:
    m = len(board)
    n = len(board[0])
    
    # For each row, find the top 3 elements (val, row, col)
    row_best = []
    for r in range(m):
        best_in_row = []
        for c in range(n):
            best_in_row.append((board[r][c], r, c))
        best_in_row.sort(key=lambda x: x[0], reverse=True)
        row_best.append(best_in_row[:3])
        
    def merge_best(list1, list2):
        combined = list1 + list2
        combined.sort(key=lambda x: x[0], reverse=True)
        res = []
        seen_cols = set()
        for val, r, c in combined:
            if c not in seen_cols:
                seen_cols.add(c)
                res.append((val, r, c))
                if len(res) == 3:
                    break
        return res

    # prefix[i] stores the top 3 elements with distinct columns from rows 0..i
    prefix = [[] for _ in range(m)]
    prefix[0] = row_best[0]
    for i in range(1, m):
        prefix[i] = merge_best(prefix[i-1], row_best[i])
        
    # suffix[i] stores the top 3 elements with distinct columns from rows i..m-1
    suffix = [[] for _ in range(m)]
    suffix[m-1] = row_best[m-1]
    for i in range(m-2, -1, -1):
        suffix[i] = merge_best(suffix[i+1], row_best[i])
        
    max_sum = -10**18
    
    # Iterate over the middle row i
    for i in range(1, m-1):
        # We choose one from prefix[i-1], one from row_best[i], one from suffix[i+1]
        for p_val, p_r, p_c in prefix[i-1]:
            for curr_val, curr_r, curr_c in row_best[i]:
                if curr_c == p_c:
                    continue
                for s_val, s_r, s_c in suffix[i+1]:
                    if s_c == p_c or s_c == curr_c:
                        continue
                    max_sum = max(max_sum, p_val + curr_val + s_val)
                    
    return max_sum
