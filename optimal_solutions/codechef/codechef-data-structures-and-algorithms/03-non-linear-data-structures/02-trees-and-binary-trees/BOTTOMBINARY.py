


def solve():
    class Solution:
        def bottom_view(self, root):
            if not root:
                return []
            mp = {}  # hd -> (depth, value)
            min_hd = max_hd = 0
            q = deque([(root, 0, 0)])  # node, horizontal distance, depth

            while q:
                node, hd, depth = q.popleft()
                min_hd = min(min_hd, hd)
                max_hd = max(max_hd, hd)

                # Overwrite if not present, or deeper, or same depth (later BFS node)
                if (hd not in mp) or (depth >= mp[hd][0]):
                    mp[hd] = (depth, node.val)

                if node.left:
                    q.append((node.left, hd - 1, depth + 1))
                if node.right:
                    q.append((node.right, hd + 1, depth + 1))

            result = []
            for hd in range(min_hd, max_hd + 1):
                if hd in mp:
                    result.append(mp[hd][1])
            return result


if __name__ == "__main__":
    solve()
