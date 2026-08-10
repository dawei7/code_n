## General

**Turn the required difference into a unique predecessor**

An arithmetic subsequence with fixed difference `difference` must satisfy

\[
\text{next value} - \text{previous value} = \texttt{difference}.
\]

If the current value is `x`, the value immediately before it must therefore be `x - difference`. This predecessor value is unique. That fact removes the need to compare the current element with every earlier index.

The word subsequence still imposes an order requirement: selected indices must increase. The solution respects that requirement by scanning `arr` from left to right. At the moment it processes `x`, its dictionary summarizes only elements already encountered, so any chain being extended necessarily ends at an earlier index.

**The dynamic-programming state**

The dictionary `f` maps a value \(v\) to the greatest length of a valid arithmetic subsequence, among the processed prefix, that ends with value \(v\). It is a `defaultdict(int)`, so reading a key that is not present yields zero.

For each new value `x`, the exact update is

`f[x] = f[x - difference] + 1`.

There are two cases hidden in this single line. If no earlier valid subsequence ends at `x - difference`, the lookup yields zero, and the new state becomes one. That represents the valid subsequence containing only the current element. If a predecessor chain of length \(L\) does exist, appending the current `x` creates a chain of length \(L+1\), because the new adjacent difference is exactly `difference`.

This is dynamic programming because a best solution for one endpoint value is reused to build a best solution for the next endpoint value. The dictionary replaces a full index-by-index table because the required difference makes only one predecessor value relevant.

**Why one length per value is enough**

Several earlier indices may contain the same value. The future does not care which of those indices ended a chain; it cares only about the longest chain that is already available before a future element arrives. A shorter chain ending at the same value can never be more useful than a longer one, because either chain could append exactly the same future values. Keeping only the maximum length loses no optimal continuation.

The assignment in the exact source does not explicitly call `max`. For nonzero `difference`, this is still safe. Every later occurrence of `x` reads `f[x - difference]`, and that predecessor state can only stay the same or increase as the scan advances. Therefore, a newly assigned length for `x` cannot be smaller than an earlier assigned length. When `difference == 0`, the predecessor key is `x` itself, so the right-hand side reads the old value and adds one. Repeated equal elements consequently extend the chain one at a time, exactly as required.

**A complete trace**

Take `arr = [1, 5, 7, 8, 5, 3, 4, 2, 1]` and `difference = -2`. A value `x` needs predecessor `x - (-2)`, which is `x + 2`.

- Processing 1 finds no earlier 3, so the best chain ending at 1 has length one.
- Processing 5 finds no earlier 7, so its length is one.
- Processing 7 needs an earlier 9, so its length is one.
- Processing 8 needs an earlier 10, so its length is one.
- The next 5 finds the earlier chain ending at 7 and becomes length two, representing `[7, 5]`.
- Processing 3 extends the best chain ending at 5, giving length three, `[7, 5, 3]`.
- Processing 4 can extend an earlier 6 only, so it starts at length one.
- Processing 2 extends the chain ending at 4 and reaches length two.
- The final 1 extends the chain ending at 3 and reaches length four, `[7, 5, 3, 1]`.

After the scan, `max(f.values())` returns four. The constraints guarantee that `arr` contains at least one element, so at least one dictionary value exists when `max` is called.

**Why the recurrence finds the optimum**

Consider the current element `x` at its array index. Every valid arithmetic subsequence ending at this occurrence has either one element or has a previous selected value. In the latter case, that previous value must be exactly `x - difference`. By the state definition, `f[x - difference]` contains the greatest length achievable by such a predecessor chain using earlier indices. Appending `x` gives the greatest possible chain ending at the current occurrence.

Inductively, after processing each prefix, `f[v]` holds the best length ending at \(v\) within that prefix. Every complete valid subsequence has some final value, so taking the maximum over all endpoint states returns the overall longest length.

**Exact behavior of the default dictionary**

Reading a missing predecessor through `f[x - difference]` inserts that predecessor key with value zero. This side effect does not affect correctness: zero is merely the empty predecessor length, and only positive lengths can win the final maximum. It can mean the dictionary contains some values that never appeared in `arr`, in addition to observed endpoint values. There are still at most two relevant keys introduced per array element, so the asymptotic space bound remains linear.

## Complexity detail

Let \(n=\lvert\texttt{arr}\rvert\). The loop performs one dictionary lookup and one dictionary assignment per element. Python hash-table operations take expected \(O(1)\) time, giving expected \(O(n)\) time for the scan. The final `max` examines all stored dictionary values. Because the dictionary has at most \(2n\) keys, that pass is also \(O(n)\). The overall expected running time is \(O(n)\).

In the theoretical worst case of severe hash collisions, dictionary operations can degrade, but the standard complexity claim uses expected hash-table behavior.

The dictionary stores endpoint states and possibly missing predecessor keys inserted by `defaultdict`. Its size is \(O(n)\), so auxiliary space is \(O(n)\). Scalar loop state uses \(O(1)\) more space. The algorithm does not modify `arr`.

## Alternatives and edge cases

- **Dictionary `get` without insertion:** Using `f.get(x - difference, 0)` avoids creating zero-valued keys for predecessor values that never appeared. It has the same expected \(O(n)\) time and \(O(n)\) worst-case auxiliary space with a slightly smaller practical map.
- **Index-based quadratic DP:** Compare every element with every earlier element and extend matching differences. It is straightforward but costs \(O(n^2)\), which is unsuitable when \(n\) can be \(10^5\).
- **Greedy search from each start:** Repeatedly scan ahead for the needed next value. This duplicates work and can also become quadratic; the dictionary DP shares all prefix results.
- **Zero difference:** Every next selected value must equal the previous one. Because the predecessor key equals `x`, the assignment increments that value’s state, so the answer is the greatest frequency of any value.
- **Negative difference:** Subtraction already handles it correctly. For example, with difference \(-2\), the predecessor of 3 is 5; no special branch or reverse scan is needed.
- **Repeated values with nonzero difference:** A later occurrence may benefit from a predecessor chain discovered since an earlier occurrence. The reassignment refreshes its endpoint length, and predecessor states never decrease.
- **Single-element array:** The first update stores length one, and the final maximum returns one. Any one element is an arithmetic subsequence regardless of the requested difference.
- **Subsequence order:** A frequency table over the entire array would be insufficient because it could join values in the wrong index order. The left-to-right update is what enforces valid ordering.
- **Recovering the actual subsequence:** The current state stores lengths only. Reconstructing a chain would require predecessor indices or node records, increasing bookkeeping; the contract asks only for the length.
- **Required import:** The exact source relies on `defaultdict` being available from `collections` through the execution harness or imports. In a standalone file, that import must be present.
