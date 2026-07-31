## General

For any fixed window, choosing a common value $x$ costs the sum of absolute deviations from $x$. Moving $x$ toward the middle while more elements lie on one side strictly decreases that sum, so every median minimizes it. For even `k`, any value between the two middle elements is optimal; using the lower median is sufficient.

Maintain the current window in two heaps. `lower` is a max-heap containing the lower half and includes the chosen median; `upper` is a min-heap containing the upper half. Their logical sizes satisfy `lower_size = upper_size` or `lower_size = upper_size + 1`. Separate sums for both halves turn the window cost into

$$
m\,\texttt{lower_size}-\texttt{lower_sum}
+\texttt{upper_sum}-m\,\texttt{upper_size},
$$

where $m$ is the lower heap's root.

When the window advances, push the entering value into the appropriate heap and mark the leaving value for lazy deletion. Logical sizes and sums change immediately, while a marked physical heap entry is removed only when it reaches a root. Rebalancing transfers one valid root when necessary. Each evaluated window therefore has the correct median partition and exact deviation sum, and the smallest such sum is the requested answer.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Each element is inserted once, marked for deletion once, physically popped at most once, and transferred between heaps only when balancing requires it. Heap operations cost $O(\log k)$, so total time is $O(n\log k)$. The heaps and delayed-deletion counts retain $O(k)$ live or pending entries.

The benchmark defines `size` as $n$, sets $k=n/2$, and uses pseudo-random tiers of 128, 512, and 2048 values. The accepted implementation updates the median in logarithmic time per slide. A correct method that sorts every window performs $O(nk\log k)$ time and must fail only scaling.

## Alternatives and edge cases

- **Sort every window:** This is straightforward and correct but repeats almost the same sort after each one-position slide.
- **Use the arithmetic mean:** The mean minimizes squared error, while this operation count is absolute error and is minimized by a median.
- **Track only the median:** Without both partition sums, computing a window's deviation cost still requires scanning all `k` elements.
- **Remove arbitrary heap entries eagerly:** Binary heaps do not support efficient indexed deletion; lazy deletion preserves logarithmic updates.
- **Even window length:** The lower median and upper median produce the same minimum cost.
- **Duplicate values:** Lazy-deletion counts distinguish how many copies remain pending even though equal values are interchangeable.
- **Negative numbers:** Absolute deviations and heap ordering work unchanged across zero.
- **Already equal window:** Both partition deviations are zero, so the global answer can be zero.
- **`k = n`:** There is exactly one window, and its median cost is returned directly.
