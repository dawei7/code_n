## General

The answer is a length, so the source turns the optimization problem into a feasibility question:

> Can at most `maxC` modifications make every stable subarray have length at most `limit`?

If a particular `limit` is feasible, every larger limit is also feasible because it relaxes the requirement. This monotonicity permits binary search for the smallest feasible value.

The difficulty lies in evaluating one `limit` quickly. The source combines constant-time range-GCD queries with an interval-hitting greedy algorithm.

**Reducing the condition to fixed-length windows**

To guarantee that no stable subarray is longer than `limit`, it is enough to break every stable window of length:

`window = limit + 1`.

Why is that sufficient? Any subarray longer than `limit` contains at least one contiguous window of length `limit + 1`. If the longer subarray has GCD greater than 1, every element in it is divisible by some common factor, so every contained shorter window also has GCD greater than 1. Therefore, a surviving overlong stable subarray would imply a surviving stable window of exactly `limit + 1`.

The converse is immediate: a stable window of length `limit + 1` itself violates the proposed maximum. Thus the feasibility test needs to hit exactly those fixed-length windows whose GCD is greater than 1.

**What one modification can do**

The problem allows an element to be changed to any integer. Conceptually, the algorithm can change a selected position to 1. Any subarray containing 1 has overall GCD 1, so it is not stable. One modification therefore breaks every bad window containing that position.

The source does not actually mutate `nums` because only the minimum possible final stability factor is requested. It records the most recently selected position in `last_changed`. Windows containing that position are treated as already broken; windows not containing it still consist entirely of original values, so their GCD can be queried from the unchanged array.

**Precomputing logarithms**

`logarithm[length]` stores `\lfloor\log_2 length\rfloor`. The recurrence:

`logarithm[length] = logarithm[length // 2] + 1`

builds all values from 2 through `n` in linear time. These entries later select the largest power-of-two block that fits inside a query interval.

**Building the GCD sparse table**

Level 0 is a copy of `nums`, so `sparse_table[0][left]` is the GCD of a block of length 1 beginning at `left`.

At level `power`, each block has width `2^power`. It consists of two adjacent half-blocks of width `2^(power-1)`. The list comprehension calculates:

`gcd(previous[left], previous[left + half])`.

Therefore, `sparse_table[power][left]` stores the GCD of:

`nums[left : left + 2**power]`.

Induction over the levels proves this meaning for every stored block.

**Answering a range GCD in constant time**

For inclusive interval `[left, right]`, let `level` be the floor of its base-2 logarithm and `width = 2**level`. The query takes:

- one width-sized block beginning at `left`;
- one width-sized block ending at `right`.

Together these blocks cover the whole interval and may overlap. Overlap is safe for GCD because the operation is idempotent: including the same value more than once does not change the result. Taking the GCD of the two stored block values therefore equals the GCD of the complete query interval.

This overlapping-block trick makes `range_gcd` an `O(1)` operation. It would not work for a non-idempotent operation such as sum, where overlap would double-count values.

**Scanning bad windows from left to right**

For a fixed `limit`, `feasible` considers every possible left endpoint of a window of length `limit + 1`.

If `last_changed >= left`, the previously selected position lies inside the current window. The selected position can be regarded as changed to 1, so this window is already non-stable and can be skipped without a GCD query.

Otherwise, the window contains no earlier selected position. Its values remain original:

- if `range_gcd(left, right) == 1`, it is already non-stable and needs no change;
- if its GCD is greater than 1, at least one position in it must be modified.

For an unhit bad window, the greedy choice is its right endpoint:

`last_changed = right`.

The change counter is incremented, and feasibility fails immediately if it exceeds `maxC`.

**Why choosing the right endpoint is optimal**

Consider the first bad window not already covered by an earlier choice. Any valid modification plan must select at least one position inside this window; otherwise its original common divisor remains and the window stays stable.

Suppose some optimal plan selects position `p` inside `[left, right]`. Replacing `p` by `right` cannot lose coverage of any future window relevant to the left-to-right scan. Every future window begins at or after `left`. If such a window contains `p <= right`, its right endpoint is at least `right` because all windows have the same length, so it also contains `right`. Choosing the latest possible position covers at least as far into the future as any other choice inside the current window.

Thus there exists an optimal plan making the greedy choice. Repeating this exchange argument at every unhit bad window proves that `feasible` counts the minimum number of modifications required for this `limit`.

**Why one marker is enough**

All windows have the same length and are scanned by increasing left endpoint. The chosen positions also increase. Therefore, only the most recent selected endpoint can possibly lie in the current or a future window; earlier selected positions lie even farther left. `last_changed` is sufficient, and no set of all changes is needed.

The condition `last_changed >= left` works because `last_changed` can never exceed the current window's `right` when reached through this scan. It therefore means exactly that the current fixed-length window contains the last changed position.

**Binary searching the minimum feasible limit**

The search begins with `low = 0` and `high = n`. Limit `n` is always feasible because there is no subarray longer than the entire array; in the check, its window length is `n + 1`, so the scan is empty.

For midpoint `middle`:

- if `feasible(middle)` is true, the answer may be `middle` or smaller, so `high = middle`;
- otherwise, every value at most `middle` is impossible, so `low = middle + 1`.

When the bounds meet, `low` is the smallest achievable stability factor.

Limit 0 is meaningful. Its windows have length 1. A one-element window is stable exactly when its value is greater than 1, because its GCD is the element itself. Feasibility at zero therefore counts how many such individual positions must be changed, matching the rule that the answer is 0 only when no stable subarray remains.

**A compact example of the greedy scan**

For `nums = [2, 4, 9, 6]` and `limit = 1`, the tested windows have length 2. Window `[0, 1]` has GCD 2, so the greedy choice changes index 1. Window `[1, 2]` contains that chosen index and is already broken. Window `[2, 3]` has GCD 3 and does not contain index 1, so it requires a second modification at index 3.

With only one allowed change, limit 1 is infeasible. Limit 2 tests length-3 windows; their GCDs are already 1, so it is feasible. The minimum answer is 2.

## Complexity detail

Let `n` be the array length. Building `logarithm` costs `O(n)` time and space. The sparse table has `O(\log n)` levels, with at most `n` entries per level, so it costs `O(n\log n)` time and `O(n\log n)` space.

One `range_gcd` call is `O(1)`. One `feasible(limit)` scan processes at most `n` window starts, so it takes `O(n)` time and `O(1)` additional space. Binary search performs `O(\log n)` feasibility checks, totaling `O(n\log n)` time.

Including preprocessing, total time is `O(n\log n)` and auxiliary space is `O(n\log n)`. The sparse table dominates memory; the binary search and greedy scan retain only scalar state.

## Alternatives and edge cases

- **Segment tree for range GCD:** It supports each query in `O(\log n)` and uses `O(n)` space, making all binary-search checks `O(n\log^2 n)` time but reducing memory.
- **Two-pointer GCD maintenance:** GCD does not have a simple inverse when removing the leftmost element, so an ordinary sliding window is not straightforward.
- **Recompute every window directly:** Scanning all elements per GCD query can make one feasibility check quadratic.
- **Store distinct GCDs of subarrays:** This can solve related longest-GCD problems, but the fixed-window greedy plus sparse table is direct and predictable.
- **Change selected elements to 1:** This conceptual choice guarantees every containing window has GCD 1, regardless of the other values.
- **Limit zero:** Every original element greater than 1 needs its own modification; original 1s are already non-stable singleton windows.
- **Limit `n`:** It is always feasible because no length-`n+1` window exists.
- **All values equal 1:** No stable subarray exists initially, so limit 0 is feasible with zero changes.
- **All values share a factor:** Bad windows are dense, and choosing each earliest unhit window's right endpoint spaces changes as far apart as correctness permits.
- **No modifications allowed:** `feasible` returns false on the first bad window because `changes > maxC` immediately.
- **More modifications than positions:** The constraints allow at most `n`; once every value greater than 1 can be changed, answer 0 is possible.
- **Overlapping bad windows:** One right-endpoint modification may break many of them, which is exactly why the interval-hitting greedy is necessary.
- **Disjoint bad windows:** Each requires a separate change because no single array position lies in both.
- **GCD exactly 1:** The window is not stable; the condition correctly checks `> 1` rather than `>= 1`.
- **Single-element array:** Binary search distinguishes an original 1, a changeable value above 1, and the case with no available modification.
- **No reconstruction:** The source returns the minimum factor only. `last_changed` represents a possible plan but the selected indices are not retained across feasibility calls.
- **Input preservation:** `nums` is copied into sparse-table level 0 and never modified.
