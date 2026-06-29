


def solve():
    '''
    class Node:
        def __init__(self, val = 0, neighbors = []):
            self.val = val
            self.neighbors = neighbors
    '''

    class Solution:
        def __init__(self):
            self.visited = {}

        # @param node, a undirected graph node
        # @return a undirected graph node
        def cloneGraph(self, node):
            if node not in self.visited:
                new_node = Node(node.val)
                self.visited[node] = new_node
                new_node.neighbors = [self.cloneGraph(neighbor) for neighbor in node.neighbors]
            return self.visited[node]


if __name__ == "__main__":
    solve()
