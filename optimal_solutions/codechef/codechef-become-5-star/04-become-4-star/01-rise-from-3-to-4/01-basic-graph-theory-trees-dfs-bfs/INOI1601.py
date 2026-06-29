import sys
sys.setrecursionlimit(2 * 10 ** 5 + 100)

def dfs(node, adj, a, max_disp_list, max_wealth_on_path):
    """
    Performs a Depth First Search to calculate the maximum disparity.

    Args:
        node (int): The current node being visited.
        adj (list[list[int]]): Adjacency list representing the tree.
        a (list[int]): List of wealth values for each node (1-indexed).
        max_disp_list (list[float]): A list containing a single float,
                                     used to simulate pass-by-reference for
                                     the global maximum disparity found so far.
        max_wealth_on_path (int): The maximum wealth encountered on the path
                                  from the root to the parent of the current node.
    """
    max_disp_list[0] = max(max_disp_list[0], max_wealth_on_path - a[node])
    max_wealth_on_path = max(max_wealth_on_path, a[node])
    for neighbor in adj[node]:
        dfs(neighbor, adj, a, max_disp_list, max_wealth_on_path)

def solve():
    n = int(sys.stdin.readline())
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(sys.stdin.readline())
    adj = [[] for _ in range(n + 1)]
    start_node = -1
    for i in range(1, n + 1):
        parent_q = int(sys.stdin.readline())
        if parent_q == -1:
            start_node = i
        else:
            adj[parent_q].append(i)
    max_disp_list = [float('-inf')]
    dfs(start_node, adj, a, max_disp_list, a[start_node])
    sys.stdout.write(str(max_disp_list[0]) + '\n')


if __name__ == "__main__":
    solve()
