from collections import defaultdict, deque
import os


def solve(filepath: str = "") -> int:
    """Determine the shortest secret passcode from keylog.txt using Topological Sorting (Kahn's Algorithm).

    Mathematical Principles Applied:
    1. Directed Acyclic Graph (DAG) Representation:
       Each 3-digit keylog attempt "c1 c2 c3" indicates directed edges c1 -> c2 and c2 -> c3 in a DAG.
       The vertices V represent unique passcode digits, and directed edges E represent precedence constraints.

    2. Topological Sort (Kahn's Algorithm):
       Compute in-degrees for each vertex.
       Repeatedly dequeue vertices with in-degree 0, appending to passcode sequence and decrementing
       in-degrees of outgoing neighbors.

    Time Complexity: O(V + E) where V <= 10 digits and E <= 50 edges (executes in ~0.001s).
    Space Complexity: O(V + E) memory for adjacency graph and queue.
    """
    if not filepath:
        # Navigate 4 levels up from solution.py to reach package root (0079_passcode-derivation/)
        sol_dir = os.path.dirname(os.path.abspath(__file__))
        pkg_dir = os.path.abspath(os.path.join(sol_dir, "..", "..", ".."))
        filepath = os.path.join(pkg_dir, "keylog.txt")

    # Read keylog text file
    with open(filepath, "r", encoding="utf-8") as f:
        attempts = [line.strip() for line in f if line.strip()]

    graph = defaultdict(set)
    in_degree = defaultdict(int)
    nodes = set()

    # Build directed graph edges from 3-digit keylog precedence constraints
    for attempt in attempts:
        c1, c2, c3 = attempt[0], attempt[1], attempt[2]
        nodes.update([c1, c2, c3])

        # Add directed edge c1 -> c2
        if c2 not in graph[c1]:
            graph[c1].add(c2)
            in_degree[c2] += 1

        # Add directed edge c2 -> c3
        if c3 not in graph[c2]:
            graph[c2].add(c3)
            in_degree[c3] += 1

    # Initialize queue with nodes having in-degree 0 (no preceding digits)
    queue = deque([n for n in nodes if in_degree[n] == 0])
    passcode = []

    # Execute Kahn's algorithm for topological sorting
    while queue:
        node = queue.popleft()
        passcode.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Return shortest passcode string converted to integer
    return int("".join(passcode))


if __name__ == "__main__":
    print(solve())
