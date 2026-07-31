## General

After visiting some increasing subsequence, the only information that affects the cost of a future move is the parity of its last value. The exact last index and value do not matter once the accumulated score is known. Maintain `best[0]` and `best[1]`: the greatest scores of any valid visited subsequence ending with an even or odd value among the processed indices.

Initialize only the parity of `nums[0]` with `nums[0]`, because index $0$ is mandatory; mark the other state unreachable. For each later `value` of parity $p$, a subsequence that visits it either extends the best state already ending in $p$ without a penalty, or extends the opposite state and pays `x`. The new state is therefore the larger of `best[p] + value` and `best[1-p] + value - x`. Leave the opposite-parity state unchanged, which represents skipping this index.

**Why one score per parity is enough**

Consider two processed subsequences ending in the same parity. Every future index would add the same value and impose the same parity-change penalty on both, so the subsequence with the smaller current score can never lead to a better future result. Discarding it is safe. The transition examines both possible previous parities for every visited current value, while retaining the untouched opposite state covers skipping. By induction, both states remain optimal after every prefix, and their maximum after the final index is the best permitted score.

## Complexity detail

Let $n$ be the length of `nums`. Each value after the first performs a constant amount of work, so the running time is $O(n)$. The two parity states and a few scalar variables use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Dynamic programming by previous index:** Store the best score ending at every index and scan all earlier indices for each transition. This is correct but requires $O(n^2)$ time and $O(n)$ space.
- **Top-down recursion over index and last parity:** Memoization reduces the state space to $O(n)$, but recursion depth can reach $n$ and the two rolling states are simpler.
- **Greedy immediate gain:** Taking every positive-looking next move can fail because preserving a stronger state of the other parity may enable a better later transition.
- **Mandatory first index:** The solution may stop immediately, but it may never omit `nums[0]` or start from a later value.
- **Large penalty:** Switching parity can remain unprofitable for the entire array; the unchanged state preserves the best same-parity subsequence.
- **Large total score:** Up to $10^5$ values of size $10^6$ may be accumulated, so implementations need an integer type capable of values beyond 32-bit range.
