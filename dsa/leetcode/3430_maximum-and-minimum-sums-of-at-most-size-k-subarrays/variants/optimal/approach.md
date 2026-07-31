## General

Reverse the summation: instead of visiting every subarray, determine how many eligible subarrays use each occurrence as their chosen maximum and as their chosen minimum. For maxima, a decreasing stack finds the nearest blocking value on both sides; reversing the comparisons produces the minimum boundaries. One side uses a strict comparison and the other a non-strict comparison. This asymmetry assigns a subarray containing equal extremes to exactly one occurrence rather than counting it more than once.

Suppose an occurrence can extend through $L$ positions on its left and $R$ on its right before reaching a blocking boundary. Choosing $x$ left positions and $y$ right positions creates a containing subarray of length $x+y+1$. Its size is legal precisely when $x+y\le k-1$. Thus its coefficient is the number of integer pairs in the rectangle $0\le x\le L$, $0\le y\le R$ below that diagonal.

Count those pairs in constant time. For the initial left extensions, every one of the $R+1$ right choices fits; afterward, the number of legal right choices decreases arithmetically. A rectangle term plus an arithmetic-series term gives the coefficient. Multiplying each value by its maximum coefficient and minimum coefficient and summing accounts for every eligible subarray twice in exactly the requested way: once for its maximum and once for its minimum.

## Complexity detail

Each index is pushed and popped at most once in each monotonic-stack pass. Boundary construction and contribution accumulation therefore take $O(n)$ time. The two boundary arrays and stack use $O(n)$ auxiliary space. The closed-form coefficient computation is $O(1)$ per index and does not depend on $k$.

## Alternatives and edge cases

- **Enumerate all bounded subarrays:** Maintaining a running minimum and maximum still takes $O(nk)$ time, which becomes quadratic when `k = n`.
- **Deque for every window size:** Repeating a sliding-window calculation for all lengths from `1` through `k` also costs $O(nk)$.
- **Symmetric tie comparisons:** Using strict or non-strict comparisons on both sides double-counts or omits subarrays whose extreme value occurs more than once.
- **Singleton limit:** When `k = 1`, every element is both extremes of its only subarray and contributes twice.
- **Duplicate values:** The asymmetric boundaries assign each subarray to one canonical equal occurrence.
- **Negative values:** Contributions remain signed; no modular reduction is part of the contract.
- **Large totals:** The sum can exceed 32-bit range even though each input value fits comfortably within it.
