from collections import defaultdict

def solve(edges: list[list[int]], signalSpeed: int) -> list[int]:
    n = len(edges) + 1
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    def count_divisible_paths(curr, parent, current_dist):
        count = 1 if current_dist % signalSpeed == 0 else 0
        for neighbor, weight in adj[curr]:
            if neighbor != parent:
                count += count_divisible_paths(neighbor, curr, current_dist + weight)
        return count

    results = [0] * n
    
    for i in range(n):
        subtree_counts = []
        for neighbor, weight in adj[i]:
            subtree_counts.append(count_divisible_paths(neighbor, i, weight))
        
        # Calculate pairs: if we have subtrees with counts c1, c2, c3...
        # The number of pairs is the sum of (ci * cj) for all i < j
        total_pairs = 0
        prefix_sum = 0
        for count in subtree_counts:
            total_pairs += prefix_sum * count
            prefix_sum += count
            
        results[i] = total_pairs
        
    return results
