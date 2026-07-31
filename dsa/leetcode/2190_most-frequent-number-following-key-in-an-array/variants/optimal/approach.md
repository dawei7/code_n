## General

**Inspect adjacent pairs exactly once**

Only an index before the final element can contribute a target. Scan those
indices from left to right. Whenever `nums[index] == key`, increment the
counter belonging to `nums[index + 1]`; all other positions are irrelevant.
Because values are restricted to $[1,1000]$, a fixed array indexed by the
target value provides direct counters.

**Maintain the current leader**

After incrementing a target, compare its new count with the count of the
stored answer. Replace the answer only when the new count is larger. The input
guarantees a unique final winner, so temporary ties and their scan order
cannot change the required result.

Every qualifying adjacent pair increments exactly its follower's counter once,
and no nonqualifying pair changes any counter. After the scan, each counter is
therefore the contract's exact frequency. The maintained leader has the
largest counter seen so far after every update, making the final leader the
unique most frequent target.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The scan takes $O(n)$ time. The counter
array always has 1,001 entries because the value domain is fixed independently
of $n$, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Hash-map counting:** Store only followers that occur. This also takes
  expected $O(n)$ time but uses $O(u)$ space for $u$ distinct targets.
- **Rescan for every observation:** For each occurrence of `key`, scan the
  array again to recount its follower. This remains correct but takes
  $O(n^2)$ time.
- The last array element cannot serve as a `key` occurrence with a follower.
- The target may equal `key`, so overlapping adjacent pairs must all count.
- Values that occur often elsewhere do not matter unless they immediately
  follow `key`.
- A target appearing after several separated `key` occurrences accumulates all
  of those observations.
