## General

**Track both the candidate trip and the global supply**

For station `i`, define the net tank change as `gas[i] - cost[i]`. The car can continue only while the running sum from its chosen start is nonnegative.

The competitive solution maintains two different sums:

- `current_sum` is the tank balance for the candidate start currently being tested;
- `total_sum` is the net gas over every station processed, independent of candidate resets.

It also stores `start`, initially zero. A single left-to-right pass either confirms this candidate through the next leg or proves that an entire interval of candidate starts can be discarded.

**Why a failed segment can be skipped completely**

Suppose the current candidate is `start`, and its running sum first becomes negative after processing station `i`. The car starting at `start` cannot cross the leg from `i` to `i + 1`.

The code sets `start = i + 1` and resets `current_sum` to zero. This does more than reject the old `start`: it safely rejects every station between the old start and `i`.

To see why, consider an intermediate station `k`. Because failure at `i` is the first failure since the last reset, the accumulated net gas from the old start through `k - 1` was nonnegative. The total from `k` through `i` equals:

$$
\text{sum(old start through i)}
-
\text{sum(old start through k-1)}.
$$

The first quantity is negative and the second is nonnegative, so their difference is negative. A car beginning at `k` with an empty tank would also fail by station `i`. None of those stations can be the answer, and `i + 1` is the earliest remaining candidate.

Resetting `current_sum` does not discard information needed to decide existence, because `total_sum` continues accumulating every net change.

**Why nonnegative total supply is necessary**

After one complete circuit, the final tank would equal:

$$
\sum_{i=0}^{n-1}(\texttt{gas[i]}-\texttt{cost[i]}).
$$

Starting at another station changes the order of additions but not their sum. If `total_sum < 0`, all stations together provide less gas than the route consumes. No start can complete the circuit, so the code returns `-1`.

**Why the remaining candidate works when the total is sufficient**

After the last reset, `current_sum` never becomes negative while scanning from `start` through station `n - 1`. Thus the candidate can traverse the suffix of the array.

What remains is the wrapped prefix from station zero through `start - 1`. Every earlier segment was abandoned only when its own accumulated sum became negative. The total of all abandoned material plus the surviving suffix is `total_sum`.

Because the surviving suffix traversal ends with `current_sum >= 0` and the global total is nonnegative, the suffix leaves enough accumulated gas to absorb the deficits encountered in the wrapped prefix. Another way to state the standard greedy result is that `start` lies immediately after the last position where the running prefix balance reached a new failure boundary; relative to that start, all circular prefix sums are nonnegative when the overall sum is nonnegative.

The elimination proof ensures that no skipped index could work, and the total-supply condition ensures the final candidate does work. Under the Reference guarantee, that feasible station is unique.

In the first gas example, starts zero, one, and two are eliminated when their combined segment falls below zero. Station three becomes the next candidate. Its gains over stations three and four provide enough reserve to traverse the earlier deficit after wrapping.

**The strict negative test is intentional**

The reset happens only when `current_sum < 0`. A zero tank is allowed: the car may arrive or depart with exactly enough fuel. Resetting on zero would incorrectly discard a candidate that remains feasible and would disturb the elimination reasoning.

Similarly, `total_sum >= 0` includes the case where the complete circuit ends with an empty tank, which is valid.

## Complexity detail

Let $n$ be the number of stations.

The `for` loop visits each index exactly once. Every iteration performs constant-time subtraction, additions, comparison, and possibly three assignments. Total time is $O(n)$.

Only `start`, `total_sum`, `current_sum`, `i`, and `diff` are stored. No array of net changes is built, so auxiliary space is $O(1)$. The inputs are read without modification.

The proof eliminates a whole segment after a failure even though the implementation merely changes two scalar values. That elimination is what avoids restarting a full simulation from each station and reduces $O(n^2)$ brute force to one pass.

## Alternatives and edge cases

- **Bidirectional block growth:** Begin with one station, append clockwise, and prepend earlier stations whenever the block total is negative. It also runs in $O(n)$ time and $O(1)$ space but needs a less familiar invariant.
- **Minimum prefix sum:** Compute cumulative net gas and start immediately after its minimum point when the total is nonnegative. It is mathematically equivalent to the greedy reset boundaries.
- **Brute-force simulation:** Try each start and stop on its first negative tank. It is direct but can inspect $n$ legs for each of $n$ starts.
- **One station:** The pass keeps start zero if its net is nonnegative and returns `-1` otherwise.
- **Exactly zero tank:** Zero is feasible, so both comparisons correctly use strict negativity for failure.
- **Several local deficits:** Each reset discards the entire failed interval. `total_sum` deliberately does not reset, because all deficits still count toward global feasibility.
- **All stations locally nonnegative:** No reset occurs and the function returns zero. If several starts would work, that would fall outside the stated unique-answer guarantee.
- **Candidate becomes `n`:** A failure at the final station sets `start` to `n`, but that happens with a negative total for the final active segmentation when no later station remains. The global feasibility check returns `-1`; under a valid feasible instance, the returned index remains within the array.
- **Equal input lengths:** The contract guarantees matching lengths. If `cost` were shorter, indexing would fail; the algorithm does not validate malformed input.
- **Large totals:** Python integers expand as needed. A fixed-width implementation should ensure the accumulator covers the maximum possible total magnitude.
