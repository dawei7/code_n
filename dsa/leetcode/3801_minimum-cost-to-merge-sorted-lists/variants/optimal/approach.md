## General

Let $L$ be the number of original lists. Represent any subset of them by an $L$-bit mask. No matter how the lists in one subset were merged, their final sorted contents, length, and median are fixed: they are the sorted union of exactly those original elements. This removes the intermediate merge order from the state.

Precompute `size[mask]` from the mask with its lowest set bit removed. To obtain every subset median without storing every merged array, flatten all input values as `(value, owner-list-index)` pairs and sort them once. For a mask, scan that common ordering while counting only pairs whose owner bit is present. The element at zero-based position `(size[mask] - 1) // 2` is exactly the problem's left median.

Define `dp[mask]` as the minimum cost to merge the lists selected by `mask` into one list. A singleton mask needs no merge, so its value is zero. For a larger mask, consider the final operation. Immediately before it, the selected originals must have been divided into two nonempty disjoint submasks `left` and `right`. Both parts were optimally merged first, and their final merge costs

$$
\texttt{size[mask]}
+ \lvert\texttt{median[left]}-\texttt{median[right]}\rvert.
$$

Therefore minimize

$$
\texttt{dp[left]}+\texttt{dp[right]}+\texttt{size[mask]}
+ \lvert\texttt{median[left]}-\texttt{median[right]}\rvert
$$

over all proper partitions of `mask`. Require `left` to contain the lowest set bit of `mask` so the symmetric partition is examined only once.

Every candidate consists of two legal optimal subplans followed by their legal final merge. Conversely, the final operation of any complete plan induces one of the enumerated partitions, and the recurrence charges exactly its two earlier costs plus its final cost. Induction on the number of set bits therefore proves that every `dp[mask]` is minimal.

## Complexity detail

Let $L=\lvert\texttt{lists}\rvert$ and let $N$ be the total number of elements. Sorting the tagged elements costs $O(N\log N)$. Scanning them for all masks costs $O(N2^L)$. Across all masks, enumerating every submask partition costs $O(3^L)$. The total time is $O(3^L + N2^L + N\log N)$. The size, median, and DP arrays use $O(2^L)$ space, while the flattened ordering uses $O(N)$, giving $O(2^L+N)$ auxiliary space.

## Alternatives and edge cases

- **Greedily merge the cheapest current pair:** A locally inexpensive merge changes both the length and median used by later costs, so it need not belong to a globally optimal merge tree.
- **Enumerate complete merge sequences:** Trying every pair at every stage repeats the same merged subsets through many different histories and grows far faster than subset DP.
- **Store every subset's merged list:** This can compute medians, but retains $O(N2^L)$ element references. A single tagged ordering yields the same medians with $O(N+2^L)$ space.
- **Average the two middle values:** The contract uses the left middle element for an even-length list; computing the usual arithmetic-average median changes merge costs.
- **Duplicate values:** Tagging an element by its owner list preserves subset membership. The ordering among equal values is irrelevant because any of them contributes the same median value.
- **Negative or large values:** Only ordering and absolute differences matter; use a sufficiently wide integer type for accumulated costs.
