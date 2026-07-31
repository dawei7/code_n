## General

**Every valid choice sequence increases by reward value**

After selecting a reward $v$, the accumulated total is at least $v$. The next reward must exceed that entire total, so it must also exceed $v$. Consequently, every valid sequence is strictly increasing by reward value. Sorting does not remove any useful order, and equal values need only one transition: after one copy is selected, every other copy is no longer greater than the total.

**Represent reachable totals as bits**

Let bit $s$ of an integer `reachable` be $1$ exactly when total $s$ can be formed from the distinct rewards processed so far. Initially the only reachable total is $0$, represented by the integer $1$.

For the next sorted reward $v$, only source totals $s<v$ may select it. The integer `(1 << v) - 1` has precisely its lowest $v$ bits set, so ANDing with it removes every illegal source. Shifting the remaining bits left by $v$ maps each legal total $s$ to the new total $s+v$. ORing those additions into the old bitset preserves the option to skip $v$:

```
reachable |= (reachable & ((1 << value) - 1)) << value
```

Inductively, unchanged bits are exactly the totals attainable without $v$, while shifted bits are exactly the totals attainable with $v$ as their final reward. The mask enforces the strict inequality, so no illegal sequence enters the state set. After all rewards, the highest set bit is therefore the optimum.

**Why the state range remains small enough**

Let $V$ be the maximum reward. Immediately before the last selected value $v\le V$, the accumulated total is less than $v$. After adding it, the result is less than $2v\le2V$. Thus no reachable bit at position $2V$ or above is needed, even though the sum of all input values can be much larger. This bound is what makes bulk bit operations practical under the expanded constraints.

## Complexity detail

Let $n$ be the input length, $V$ the maximum reward, and $w$ the number of bits handled per machine word. Deduplication and sorting cost $O(n\log n)$ time. At most $n$ transitions operate on an $O(V)$-bit integer, costing $O(V/w)$ word operations each, so total time is $O(n\log n+nV/w)$. The distinct sorted values require $O(n)$ space and the bounded bitset requires $O(V/w)$ words, for $O(n+V/w)$ auxiliary space.

## Alternatives and edge cases

- **Scalar boolean DP:** Maintain one boolean for every total below $2V$ and examine all sources below each reward. It is correct in $O(nV)$ time and $O(V)$ space, but the larger limits make those scalar transitions too slow.
- **Two-dimensional DP:** Keeping a reachability row for every processed reward makes the recurrence explicit but consumes $O(nV)$ space, far beyond what the bitset invariant needs.
- **Backtracking or memoized index search:** Exploring valid next indices can still expose exponentially many sequences or an impractically large index-total state space.
- **Duplicate rewards:** Only one copy of a value can ever participate in a valid sequence, so deduplication preserves the answer and avoids repeated large bit operations.
- **Strict inequality:** The mask includes source bits $0$ through $v-1$ but excludes bit $v$. Allowing bit $v$ would incorrectly treat equality as sufficient.
- **Largest possible answer:** A total of $2V-1$ is achievable with rewards $V-1$ and $V$, so storage and cases must permit values above $V$.
