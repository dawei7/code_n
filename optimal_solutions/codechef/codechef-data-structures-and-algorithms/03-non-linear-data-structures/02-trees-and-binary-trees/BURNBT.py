


def solve():
    class Solution:
        def map_parents(self, root, target):
            parent = {}
            target_node = None
            q = deque([root])

            while q:
                curr = q.popleft()

                if curr.data == target:
                    target_node = curr

                if curr.left:
                    parent[curr.left] = curr
                    q.append(curr.left)

                if curr.right:
                    parent[curr.right] = curr
                    q.append(curr.right)

            return parent, target_node

        def burn_tree(self, target_node, parent):
            visited = set()
            q = deque([target_node])
            visited.add(target_node)

            time = 0
            while q:
                size = len(q)
                burned = False

                for _ in range(size):
                    curr = q.popleft()

                    # Left child
                    if curr.left and curr.left not in visited:
                        burned = True
                        visited.add(curr.left)
                        q.append(curr.left)

                    # Right child
                    if curr.right and curr.right not in visited:
                        burned = True
                        visited.add(curr.right)
                        q.append(curr.right)

                    # Parent
                    if curr in parent and parent[curr] not in visited:
                        burned = True
                        visited.add(parent[curr])
                        q.append(parent[curr])

                if burned:
                    time += 1

            return time

        def min_time_to_burn(self, root, target):
            if not root:
                return 0

            parent, target_node = self.map_parents(root, target)
            return self.burn_tree(target_node, parent)


if __name__ == "__main__":
    solve()
