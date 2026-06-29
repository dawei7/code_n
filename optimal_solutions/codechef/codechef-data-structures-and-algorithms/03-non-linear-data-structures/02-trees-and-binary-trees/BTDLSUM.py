


def solve():
    class Solution:
        def deepLSum(self, root, maxLevel, curLevel, ans):
            if not root:
                return
            if curLevel > maxLevel[0]:
                ans[0] = root.val
            elif curLevel == maxLevel[0]:
                ans[0] += root.val
            maxLevel[0] = max(maxLevel[0], curLevel)
            self.deepLSum(root.left, maxLevel, curLevel + 1, ans)
            self.deepLSum(root.right, maxLevel, curLevel + 1, ans)

        def deepestLeavesSum(self, root):
            maxLevel = [0]
            ans = [0]
            self.deepLSum(root, maxLevel, 0, ans)
            return ans[0]


if __name__ == "__main__":
    solve()
