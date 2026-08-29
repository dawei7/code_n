## General

**Reduce unbounded time to one repeating cycle**

For an original array of length `n`, removal takes `n` minutes:

- at time 0, all `n` elements remain;
- at time 1, the first has been removed;
- at time `n`, the array is empty.

Restoration takes another `n` minutes. At time `2 * n`, the complete original array is restored, and the next removal phase starts in the same state as time 0.

The state therefore repeats every `2 * n` minutes. The source computes

`t %= 2 * n`

for every query, so arbitrarily large times are mapped into the canonical cycle range 0 through `2n - 1`.

**Map the removal phase to an original suffix**

When `t < n`, exactly `t` elements have been removed from the left. The current array is the original suffix

`nums[t:]`

with length `n - t`.

Current index `i` exists only if `i < n - t`. When it exists, its original-array position is shifted by the removed prefix length:

`nums[i + t]`.

The first branch implements both facts:

`if t < n and i < n - t`.

At time zero, the length is `n` and the mapping is `nums[i]`.

**Treat the empty minute separately through failed conditions**

At `t == n`, all elements have been removed and none has yet been restored.

The first branch requires `t < n` and fails. The second requires `t > n` and also fails. `ans[j]` keeps its initialized value `-1` for every queried index.

The strict inequalities deliberately isolate the empty state without an explicit equality branch.

**Map the restoration phase to an original prefix**

For `n < t < 2n`, exactly `t - n` elements have been restored in their original removal order. Since elements were removed from left to right, the current array is the original prefix

`nums[:t - n]`.

Current index `i` exists if `i < t - n`. Its value is simply `nums[i]` because the restored prefix has the same indexing as the original.

This is the `elif` branch:

`t > n and i < t - n`.

At time `2n`, modulo reduction produces zero rather than a restoration-phase value, correctly returning to the full-array removal-phase representation.

**Trace the three phase boundaries**

For `nums = [0, 1, 2]`, `n = 3`:

- `t = 2` is removal phase. Length is 1, and current index 0 maps to original index $0+2=2$, value 2.
- `t = 3` is the empty state. Every query returns `-1`.
- `t = 5` is restoration phase. Length is $5-3=2$, so indices 0 and 1 map to original values 0 and 1.
- `t = 6` reduces to zero and represents the full array again.

**Why the answer initialization is useful**

`ans` begins as `[-1] * m`. A query writes a value only when its requested index exists in the current array. All out-of-range cases, including the empty minute, naturally retain `-1`.

This reduces branching and makes invalid-index behavior the default.

**Why the formulas are correct**

The process has exactly the three states described within one cycle: shrinking suffix, empty array, and growing prefix. The branch conditions partition those times.

Each phase's length test matches the current array length, and each mapping selects the element occupying current index `i`. Modulo preserves the state because the full process repeats. Therefore every answer entry is correct.

The original array and query list are not modified.

**A direct state table for one cycle**

The current contents can be summarized without simulation:

- for $0\le t<n$, contents are `nums[t:n]`;
- for $t=n$, contents are empty;
- for $n<t<2n$, contents are `nums[0:t-n]`.

The two source branches are exactly indexed lookups into this table. Writing the state this way makes the off-by-one choices visible: restoration has length zero at $t=n$ and length $n-1$ at $t=2n-1$; the fully restored length $n$ appears at the next cycle's time zero.

This also explains why the second branch uses `t > n` rather than `t >= n` and why modulo does not need a special value for `2n`.

## Complexity detail

Let $q$ be the number of queries and $n$ the original array length.

Each query uses constant-time modulo, comparisons, and at most one array lookup. Total time is $O(q)$; it does not depend on the magnitude of query times.

The returned answer list uses $O(q)$ space. Excluding required output, the method stores only `n`, `m`, and loop variables, so auxiliary working space is $O(1)$. The manifest includes the output and states $O(q)$.

## Alternatives and edge cases

- **Simulate minute by minute:** Query times reach $10^5$ and repeat; simulation repeats identical cycles unnecessarily. Modulo gives direct access.
- **Precompute all cycle arrays:** It uses more storage and copying. The suffix/prefix formulas answer a query without materializing a state.
- **Time zero:** The full original array is present.
- **Time `n`:** The array is exactly empty; both strict phase conditions fail.
- **Time `2n`:** Modulo maps it back to time zero.
- **One-element array:** States alternate between the element and empty every minute.
- **Removal-phase invalid index:** If `i >= n - t`, initialized `-1` remains.
- **Restoration-phase invalid index:** If `i >= t - n`, initialized `-1` remains.
- **Large time:** Only its remainder modulo `2n` matters.
- **Original-index shift:** Removal phase uses `i + t`; restoration phase uses `i`.
- **Query index guarantee:** It is below original length, but may still exceed the shorter current length.
- **Input preservation:** The process is modeled mathematically; no elements are actually removed or appended.
- **Last minute before reset:** At `t = 2n - 1`, the restored prefix has length `n - 1`; one minute later modulo zero restores the final element.
