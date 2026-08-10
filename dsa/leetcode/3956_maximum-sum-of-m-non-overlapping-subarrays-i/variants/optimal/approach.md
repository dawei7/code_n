## General

The source builds solutions by the exact number of selected subarrays. One dynamic-programming layer represents $q-1$ subarrays, and the next layer adds a $q$th subarray of allowed length. A monotonic deque finds the best start for every possible end in constant amortized time.

The maximum across layers one through `m` implements “at least one and at most `m`.”

**Prefix sums turn subarray sums into endpoint arithmetic**

Define:

$$
P[i]=\sum_{t=0}^{i-1}\texttt{nums}[t],
\qquad P[0]=0.
$$

The sum of the half-open subarray `nums[start:end]` is:

$$
P[end]-P[start].
$$

Using half-open endpoints makes its length exactly `end - start`. The permitted length condition becomes:

$$
l\le end-start\le r,
$$

or equivalently:

$$
end-r\le start\le end-l.
$$

**Meaning of the DP layers**

For a fixed round $q$:

- `previous[i]` is the best total using exactly $q-1$ non-overlapping valid subarrays contained in the first `i` elements;
- `current[i]` is the corresponding best total using exactly $q$ subarrays.

Before the first round, selecting exactly zero subarrays has value zero for every prefix, so `previous` is initialized to all zeroes.

Impossible states in later layers use negative infinity. This is important when array values are negative: zero must not masquerade as a valid solution with a positive number of selected subarrays.

**Transition by choosing the final subarray**

Suppose the $q$th and final selected subarray ends at exclusive endpoint `end` and begins at `start`. Earlier selected subarrays must fit completely in the prefix ending at `start`. Their best value is `previous[start]`.

The combined total is:

$$
\texttt{previous[start]}+P[end]-P[start]
=P[end]+\bigl(\texttt{previous[start]}-P[start]\bigr).
$$

For a fixed `end`, $P[end]$ is constant. The transition only needs the maximum key

`previous[start] - prefix[start]`

over starts in the valid window `[end - r, end - l]`.

**Maintain the maximum key in a deque**

As `end` increases by one, the valid start window also shifts by one. The source stores promising start indices in `candidates`.

First, `start = end - l` is the newest index whose subarray would have the minimum legal length. If it is nonnegative and `previous[start]` is reachable, its key is computed.

While the deque's last key is less than or equal to the new key, that older index is removed. It can never be preferable:

- the new key is at least as large;
- the new start expires later because its index is larger.

The new start is then appended. Keys are strictly decreasing from front to back.

Next, any front index smaller than `end - r` is removed because it would create a subarray longer than `r`.

After these steps, the deque front is a valid start with the maximum transition key.

**Allow the last chosen subarray to end earlier**

`current[end]` should represent the best exact-$q$ solution anywhere within the first `end` elements, not necessarily one whose last interval ends at `end`.

The source begins with:

`current[end] = current[end - 1]`.

This skips `nums[end - 1]` and carries forward a solution ending earlier.

If the deque is nonempty, it also tries the best subarray ending exactly at `end`:

`prefix[end] + previous[candidates[0]] - prefix[candidates[0]]`.

The maximum of these choices gives the state definition.

Because the earlier layer stops at `start` and the new half-open interval begins there, selected subarrays never overlap. They may touch at a boundary, which is legal.

**Collect between one and `m` subarrays**

After finishing one layer, `current[n]` is the best total with exactly $q$ selected subarrays in the full array. The source updates `answer` before assigning `previous = current` for the next round.

No more than `n // l` disjoint subarrays can fit because each has length at least `l`. The outer loop therefore runs only

`min(m, n // l)`

layers.

Taking the maximum layer answer enforces at least one selection while permitting fewer than `m`. This is crucial when additional subarrays would have negative sums.

**Why the recurrence is exhaustive**

Any exact-$q$ solution in a prefix either does not use the final element, represented by `current[end - 1]`, or has a last subarray ending at `end`. In the second case, its start lies in the deque's length window and its preceding $q-1$ intervals form a `previous[start]` solution.

Conversely, every deque transition combines nonoverlapping valid parts and creates exactly $q$ allowed subarrays. The recurrence includes all and only feasible solutions, so each layer optimum is exact.

## Complexity detail

Let $N$ be the array length and

$$
Q=\min(m,\lfloor N/l\rfloor).
$$

Within one layer, each start index enters the deque once and leaves from the front or back at most once. The scan is $O(N)$. Across $Q$ layers, time is $O(QN)$, bounded by the manifest's $O(mN)$.

Prefix, `previous`, and `current` arrays each use $O(N)$ space. The deque holds at most $O(N)$ indices. Since layers reuse arrays rather than storing all $m$ layers, additional space is $O(N)$.

## Alternatives and edge cases

- **Try every start for every end:** The direct transition costs $O(r-l+1)$ per state and can produce $O(mN^2)$ time. The deque maintains the range maximum.
- **Use zero for impossible exact-count states:** This would allow nonexistent subarray sets to dominate negative valid sums. Negative infinity preserves feasibility.
- **Compute exactly `m` only:** The statement permits fewer selections, and all-negative arrays are best served by one subarray.
- **Allow zero selected subarrays in the answer:** That would incorrectly return zero when every valid subarray sum is negative.
- **Forget `current[end - 1]`:** Then every state would force its last subarray to end at the current endpoint and miss earlier optima.
- **Expire starts before adding the newest:** Either order can work carefully, but the source adds `end - l` and then removes values below `end - r`, leaving the exact inclusive window.
- **Equal deque keys:** Keeping the newer start is safe because it gives the same value and remains valid longer.
- **`l = r`:** The valid-start window has one index per end, and the deque reduces to fixed-length transitions.
- **`m > n // l`:** Extra rounds are impossible and skipped.
- **All values negative:** Exact layers remain negative; the maximum over positive layer counts chooses the least harmful valid selection.
- **Adjacent selected subarrays:** Half-open intervals may end and start at the same index without sharing an element.
- **Large sums:** Python integers safely hold prefix and DP totals beyond 32-bit limits.
