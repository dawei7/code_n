## General

**Define a best sum that must end at each index**

Let `f[i]` be the maximum sum of a valid nonempty constrained subsequence whose final selected element is `nums[i]`.

If the previous selected index is `j`, the gap rule requires:

$$
i-k \le j < i.
$$

Among those possible predecessors, only the largest `f[j]` matters. If that largest value is positive, extending it improves the sum. If it is zero or negative, starting a new subsequence at `i` is at least as good. Thus:

$$
f[i]
=
\texttt{nums}[i]
+
\max\left(0,\max_{i-k\le j<i}f[j]\right).
$$

The final answer is the maximum `f[i]` over all ending indices because the best subsequence may end anywhere.

**Why a monotonic deque is useful**

Naively scanning up to `k` predecessor states for every `i` costs $O(nk)$. The deque `q` stores indices whose `f` values are useful candidates for the current sliding window.

It maintains two properties:

1. Indices increase from front to back.
2. Their `f` values strictly decrease from front to back.

Because of the second property, `q[0]` always identifies the largest DP value among retained valid candidates.

**Understand the initial placeholder**

The exact code starts with:

```python
q = deque([0])
f = [0] * n
```

Before index zero has been computed, `f[0]` is the initialized zero. At `i = 0`, the recurrence reads that zero through `q[0]`, so:

```python
f[0] = max(0, f[0]) + nums[0]
```

correctly becomes `nums[0]`. The later back-cleaning removes the placeholder copy of index zero and appends index zero again with its now-final value. This is an unusual but valid way to avoid a separate first-index branch.

**Discard predecessors that are too far away**

Before computing state `i`:

```python
while i - q[0] > k:
    q.popleft()
```

removes any front index whose distance exceeds `k`. Because indices in the deque increase, expired indices can occur only at the front.

The expression has no explicit `q` nonempty guard. The deque nevertheless remains nonempty here: every completed iteration appends its current index, and when `k >= 1`, the immediately preceding index is within distance one at the next iteration. Older entries may expire, but a recent candidate remains.

**Compute the current state and preserve nonempty behavior**

The recurrence is implemented as:

```python
f[i] = max(0, f[q[0]]) + x
```

where `x` is `nums[i]`. If the best valid predecessor is positive, it is extended. Otherwise, the zero causes a fresh subsequence containing only `x`.

Zero is not itself returned as an empty-subsequence answer. `x` is always added, so every `f[i]` represents a nonempty subsequence. `ans` starts at negative infinity, allowing an all-negative input to return its largest negative element rather than the forbidden empty sum zero.

**Remove dominated candidates from the back**

After `f[i]` is known:

```python
while q and f[q[-1]] <= f[i]:
    q.pop()
```

removes every older index with value no greater than the new one. Such an index can never become the best predecessor later:

- `f[i]` is at least as large.
- Index `i` is newer, so it remains inside every future window at least as long.

Keeping the older candidate would therefore serve no purpose. The use of `<=` also removes equal-valued older indices because the newer equal value dominates by longevity.

Finally, `q.append(i)` inserts the current index after all smaller or equal values have been removed, restoring decreasing `f` order.

Unlike some variants, this source appends even negative states. That is still correct. If the maximum at the front is negative, `max(0, ...)` starts fresh. Retaining a negative index also guarantees the queue's nonempty structure.

**Trace the main example**

For `nums = [10,2,-10,5,20]` and `k = 2`:

| Index | Best eligible predecessor | `f[i]` | Best overall |
|---:|---:|---:|---:|
| 0 | 0 | 10 | 10 |
| 1 | 10 | 12 | 12 |
| 2 | 12 | 2 | 12 |
| 3 | 12 from index 1 | 17 | 17 |
| 4 | 17 | 37 | 37 |

The resulting subsequence uses indices 0, 1, 3, and 4, whose consecutive gaps are at most two.

**Why the recurrence and deque are correct**

Every valid subsequence ending at `i` either contains no earlier element or extends a subsequence ending at some valid-window index `j`. The recurrence chooses the best of exactly those cases.

The deque removes only expired indices or older indices dominated by a newer, at-least-as-good state. Hence its front always supplies the maximum eligible `f[j]`. Each computed state is correct, and maximizing them in `ans` yields the best valid nonempty subsequence.

## Complexity detail

Each index is appended once. It can be removed from the back once through domination or from the front once through expiration. Across the full scan, deque operations are therefore $O(n)$ amortized, and all other per-index work is constant. Total time is $O(n)$.

The deque contains only recent nondominated indices and has $O(k)$ size. However, the exact source also allocates `f` with $n$ entries, so its actual auxiliary space is $O(n+k)=O(n)$. The manifest's $O(k)$ space bound is achievable by storing DP values directly with deque entries and keeping only the global answer; that optimization is not present in this file.

## Alternatives and edge cases

- **Max heap:** Store DP values with indices and lazily remove an expired maximum. This gives $O(n\log n)$ time and can retain stale nonmaximum entries.
- **Balanced ordered multiset:** Maintain all DP values in the last `k` indices with frequencies. Maximum lookup and updates cost $O(\log k)$.
- **Direct window scan:** Evaluate the last `k` states for every index in $O(nk)$ time.
- **Deque of value-index pairs:** Store `(f[i], i)` directly and omit the full `f` array, realizing $O(k)$ auxiliary space.
- **All negative numbers:** Every predecessor contribution is reset to zero, and `ans` selects the least negative single element.
- **`k = 1`:** A selected element may follow only the immediately preceding selected index; restarting remains allowed.
- **`k = n`:** Every earlier index can be connected within the constraint, and the recurrence resembles a positive-sum subsequence DP.
- **Equal DP values:** The older index is removed because the newer one stays valid longer.
- **Negative bridge:** A negative state can be worth extending if it still leaves a positive accumulated sum that connects profitable elements within the gap bound.
- **Nonempty requirement:** Initializing `ans` to negative infinity and always adding `x` prevents an empty zero-sum answer.
