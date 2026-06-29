import sys
sys.setrecursionlimit(2 * 10 ** 5 + 500)

def is_odd_cycle(u, level, adj, l):
    """
    Performs a DFS traversal to detect if an odd cycle exists in the graph
    starting from node u.
    
    Args:
        u (int): The current node being visited.
        level (list[int]): A list storing the level (distance from the source in DFS tree)
                           of each node. -1 indicates unvisited.
        adj (list[list[int]]): The adjacency list representation of the graph.
        l (int): The current level of node u.
        
    Returns:
        bool: True if an odd cycle is detected, False otherwise.
    """
    level[u] = l
    for v in adj[u]:
        if level[v] == -1:
            if is_odd_cycle(v, level, adj, l + 1):
                return True
        elif (l - level[v]) % 2 == 0:
            return True
    return False

def solve():
    """
    Reads graph input for a single test case, checks if it contains an odd cycle,
    and prints "YES" if it's bipartite (no odd cycles) or "NO" otherwise.
    """
    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    level = [-1] * (n + 1)
    for u in range(1, n + 1):
        if level[u] == -1:
            if is_odd_cycle(u, level, adj, 0):
                sys.stdout.write('NO\n')
                return
    sys.stdout.write('YES\n')

def main():
    """
    Main function to handle multiple test cases.
    """
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    solve()
