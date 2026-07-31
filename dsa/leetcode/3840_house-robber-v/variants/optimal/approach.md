## General

**The only new conflict is at the preceding house**

Let $D_i$ be the maximum money obtainable from indices $0$ through $i$, and use $D_{-1}=D_{-2}=0$. At house $i$, skipping it preserves $D_{i-1}$. Taking it contributes `nums[i]`, and the prefix that can be combined with it depends only on the color relationship at the boundary:

- If $i>0$ and `colors[i] != colors[i - 1]`, house $i$ is compatible with every valid optimal selection through $i-1$, even when that selection includes $i-1$. The take value is therefore `nums[i] + D[i - 1]`.
- For the first house, or when the two adjacent colors are equal, taking $i$ forbids taking $i-1$. The best compatible prefix ends at $i-2$, so the take value is `nums[i] + D[i - 2]`.

In either case, $D_i$ is the greater of the skip and take values. These are exhaustive: every valid selection either excludes $i$, or includes it and must obey exactly the boundary condition above. The selected prefix is already optimal by the definition of $D$, so the recurrence cannot miss a better valid choice.

Only $D_{i-1}$ and $D_{i-2}$ are needed for the next transition. Keep those two values in rolling variables and replace them after each house, leaving the final $D_{N-1}$ as the answer.

## Complexity detail

Let $N$ be the number of houses. Each house performs one color comparison and a constant amount of arithmetic, so the time complexity is $O(N)$. The two rolling DP values use $O(1)$ auxiliary space. The returned sum can reach $10^{10}$; Python integers handle it directly, while fixed-width implementations need a 64-bit integer type.

The benchmark defines size as $N$ and gives every house the same color, forcing the restrictive recurrence at every boundary. The accepted rolling DP and an independent full-array DP both grow linearly. A correct control that recomputes the entire DP for every successive prefix repeats the same work and grows as $O(N^2)$.

## Alternatives and edge cases

- **Full DP array:** Store every $D_i$ and apply the same transition. This is equally fast but uses $O(N)$ auxiliary space instead of two values.
- **Top-down memoization:** Recursing on prefix endpoints with memoization also visits each state once, but adds $O(N)$ memo and call-stack space and risks recursion-depth limits.
- **Parity or fixed-alternation choices:** Selecting all even or all odd indices is not generally optimal because unequal adjacent colors permit both houses, and unequal money values change which same-color neighbor should be skipped.
- **Subset enumeration:** Testing every chosen-index set is a useful small oracle, but its $O(2^N N)$ work cannot satisfy the input limit.
- **Single house:** With no preceding boundary, taking the only positive value is optimal.
- **Different adjacent colors:** Both adjacent houses may be selected; treating all adjacency as forbidden solves a different House Robber contract.
- **Repeated color at a distance:** Equal colors restrict only neighboring houses, so non-adjacent occurrences may both be selected.
- **Large totals:** Up to $10^5$ houses may each contribute $10^5$, so fixed-width implementations must not store the answer in a 32-bit integer.
