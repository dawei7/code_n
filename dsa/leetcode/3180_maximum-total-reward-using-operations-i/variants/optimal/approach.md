## General

**Why useful rewards appear in increasing order**

Suppose a reward of value $v$ is selected. The new total is at least $v$, so every later selected reward must be strictly greater than $v$. Every valid sequence is therefore increasing by value, regardless of the indices' original order. Sorting is safe, and duplicate values need to be processed only once: after one copy is selected, the total is already at least that value, so another copy can never satisfy the strict inequality.

**Encode every reachable total in one integer**

Use bit $s$ of `reachable` to mean that total $s$ can be obtained from the distinct rewards processed so far. Initially only total $0$ is reachable, so the bitset is the integer $1$.

Before processing a reward $v$, the only totals allowed to select it are $s<v$. The mask `(1 << v) - 1` keeps exactly bits $0$ through $v-1$. Shifting those surviving bits left by $v$ turns every legal source total $s$ into its new total $s+v$:

```
(reachable & ((1 << value) - 1)) << value
```

OR this shifted set into `reachable` so that both skipping and selecting $v$ remain represented. Inductively, after each distinct reward, the set bits are exactly all totals attainable from the processed rewards: unchanged bits cover sequences that skip $v$, and shifted bits cover every sequence whose last choice is $v$. No illegal source total is shifted because the mask removes all $s\ge v$.

If $V$ is the largest reward, every reachable total is less than $2V$. Indeed, immediately before the final selected reward $v\le V$, the total is smaller than $v$, so the new total is below $2v\le2V$. The integer bitset therefore stays bounded, and its highest set bit is the maximum attainable reward.

## Complexity detail

Let $n$ be the input length, $V$ the maximum reward, and $w$ the number of bits processed per machine word. Deduplication and sorting take $O(n\log n)$ time. There are at most $n$ bitset transitions, each operating on $O(V)$ bits in $O(V/w)$ word operations, for $O(n\log n+nV/w)$ total time. The distinct sorted values use $O(n)$ space and the bounded bitset uses $O(V/w)$ words, for $O(n+V/w)$ auxiliary space.

## Alternatives and edge cases

- **Scalar one-dimensional DP:** Store a boolean for every total below $2V$ and scan legal sources for each reward. This has the same state meaning but costs $O(nV)$ scalar time and $O(V)$ space.
- **Two-dimensional prefix DP:** Record reachability after every reward and total. It makes the transition explicit but uses $O(nV)$ space that is unnecessary once the previous states are encoded in the bitset.
- **Backtracking over indices:** Trying every valid next reward directly can revisit exponentially many choice sequences and is too slow at the maximum input length.
- **Duplicate rewards:** Multiple equal values do not create extra opportunities, because selecting one makes every equal copy ineligible. Deduplicating preserves all achievable totals.
- **Strict inequality:** The low-bit mask must exclude bit $v$. A source total equal to $v$ cannot select reward $v$ because the rule requires the reward to be strictly greater.
- **Maximum total:** The answer can be as large as $2V-1$, not merely $V$. Rewards $V-1$ and $V$ demonstrate that the upper bound is attainable.
