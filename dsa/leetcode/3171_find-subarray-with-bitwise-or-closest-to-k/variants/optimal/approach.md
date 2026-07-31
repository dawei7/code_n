## General

**Group subarrays by their right endpoint**

Suppose `previous` contains every distinct bitwise OR obtained by a non-empty subarray ending immediately before the current position. For the next value `number`, every subarray ending here is either the one-element subarray `[number]` or an older ending subarray extended by `number`. Its OR is therefore `number` or `value | number` for some `value` in `previous`. Building `current` from exactly those possibilities neither omits nor invents a candidate.

The answer can be updated from all values in `current`, after which `current` becomes the state for the next index. Returning immediately when the difference reaches `0` is safe because an absolute difference cannot be negative.

**Why the state stays small**

Consider the OR values for subarrays ending at one fixed index as their left endpoints move left. Each extension can only set additional bits; it can never clear a bit. Whenever the OR changes, at least one previously unset bit becomes set. A value no larger than $M$ has $O(\log M)$ relevant bit positions, so there are only $O(\log M)$ distinct OR values for one endpoint. A set merges different subarrays as soon as they produce the same OR.

Together, these observations prove that every legal subarray OR is examined while the algorithm retains only the distinct values needed for the next step.

## Complexity detail

Let $n$ be the length of `nums` and let $M = \max(\texttt{k}, \max(\texttt{nums}))$. Each of the $n$ positions extends at most $O(\log M)$ distinct OR states, giving $O(n \log M)$ time. The two endpoint-state sets each contain at most $O(\log M)$ values, so the auxiliary space is $O(\log M)$.

## Alternatives and edge cases

- **Enumerate every subarray:** Accumulating an OR for every pair of endpoints is correct, but it takes $O(n^2)$ time and cannot scale to $n = 10^5$.
- **Segment tree plus binary search:** Range-OR queries can support a more elaborate search over change points, but the endpoint-state compression is simpler and already achieves the required bound.
- **Ordinary sliding window:** Bitwise OR does not have a simple inverse when the left endpoint moves, because removing a value may or may not clear each bit depending on the other values in the window.
- **Duplicate OR states:** Several starting positions may yield the same OR at one endpoint; deduplicating them is essential for the logarithmic state bound and does not lose any possible answer.
- **One-element and exact matches:** Every number begins a fresh subarray, and a difference of `0` can be returned immediately.
