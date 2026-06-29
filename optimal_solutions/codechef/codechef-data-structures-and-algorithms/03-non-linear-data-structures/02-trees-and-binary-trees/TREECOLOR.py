


def solve():
    def distinctColorsInSubtrees(N: int, C: list[int], edges: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(N)]
        for u, v in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        ans = [0] * N

        def dfs(node: int, parent: int) -> set:
            current_colors = {C[node]}

            for child in adj[node]:
                if child != parent:
                    child_colors = dfs(child, node)

                    # Small-to-Large Merging Trick
                    if len(current_colors) < len(child_colors):
                        current_colors, child_colors = child_colors, current_colors

                    # Merge the smaller set into the larger one
                    current_colors.update(child_colors)

            ans[node] = len(current_colors)
            return current_colors

        dfs(0, -1)
        return ans


if __name__ == "__main__":
    solve()
