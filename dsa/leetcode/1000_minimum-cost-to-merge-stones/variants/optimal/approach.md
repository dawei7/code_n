## General
**Reject impossible pile counts first:** Every move reduces the number of piles by exactly $K-1$. Starting with $N$ piles can reach one only when $N-1$ is divisible by $K-1$. This condition is also sufficient because interval merges can then be scheduled until one pile remains.

**Store the best cost for each interval:** Let `dp[left][right]` be the minimum cost to reduce that interval as far as its length permits. Split an interval after `middle`, combining the best left and right costs. Only split positions separated by $K-1$ need consideration, because the left part must be reducible to one pile before it can participate in the eventual merge.

When an interval length satisfies `(length - 1) % (k - 1) == 0`, its partial piles can be merged into one, so add the interval's total stone count. Prefix sums provide that total in constant time. Considering every legal final split covers every valid merge tree, and choosing the minimum yields the optimal cost.

## Complexity detail
There are $O(N^2)$ intervals. Each examines at most $O(N/(K-1))$ legal split points, so time is $O(N^3/(K-1))$. The interval table and prefix sums use $O(N^2)$ space.

## Alternatives and edge cases
- **Enumerate merge sequences:** Recursively trying every legal consecutive group is correct but can visit exponentially many pile configurations.
- **Three-dimensional pile-count DP:** Explicitly storing the cost to reduce each interval to every pile count is general but uses $O(N^2K)$ space.
- **One initial pile:** The answer is zero because no merge is required.
- **Merge size larger than the row:** More than one pile cannot be reduced when `k > n`.
- **Exact full-row merge:** When `k == n`, one move costs the sum of all piles.
