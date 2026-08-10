## General

**First identify the largest possible AND value**

The phrase “maximum possible bitwise AND of any non-empty subarray” initially suggests examining many subarrays. The key simplification comes from a basic property of bitwise AND. For non-negative integers, AND can only keep a bit that is present in every operand. It cannot introduce a new 1-bit. Consequently, the AND of a subarray is less than or equal to every element in that subarray.

Let

`mx = max(nums)`.

The one-element subarray containing any occurrence of `mx` has bitwise AND exactly `mx`, so the maximum achievable AND is at least `mx`. On the other hand, every subarray's AND is no greater than each of its elements and therefore no greater than the array maximum `mx`. Combining the lower and upper bounds proves that the maximum possible AND value is exactly `mx`.

This reasoning depends on subarrays being non-empty and the values being positive as specified. A singleton is a legal subarray, and the bitwise AND of a singleton is simply its sole value.

**Which longer subarrays can still have AND equal to the maximum**

Knowing the target value is `mx` is only half of the problem; the algorithm must determine which multi-element subarrays have that AND. If a subarray contains a value `x < mx`, then its total AND is at most `x` and therefore strictly below `mx`. Such a subarray cannot qualify.

No array element can be larger than `mx` by definition. It follows that every element in a qualifying subarray must be exactly `mx`. Conversely, ANDing `mx` with itself any number of times leaves `mx` unchanged. Thus a subarray has the maximum possible AND if and only if it is a contiguous run consisting entirely of the array maximum.

The original bitwise problem has now become a simple sequence problem: find the longest consecutive run of `mx`.

**Measure one run at a time**

The solution initializes `ans = cnt = 0`. The variable `cnt` is the length of the run of maximum values ending at the element currently being processed. The variable `ans` is the largest such run seen anywhere in the processed prefix.

For each `x` in `nums`:

- When `x == mx`, the current maximum-only run extends by one, so `cnt` increases. The code then updates `ans` with `max(ans, cnt)`.
- When `x != mx`, this position cannot belong to a qualifying subarray. It breaks any run that ended immediately before it, so `cnt` resets to zero.

The reset is essential because the required object is a subarray, which must be contiguous. Two groups of maximum values separated by a smaller value cannot be combined.

For `nums = [1, 2, 3, 3, 2, 2]`, `mx` is 3. The counters remain zero for 1 and 2. The first 3 makes `cnt` equal 1 and `ans` equal 1; the next 3 makes both equal 2. The following 2 resets `cnt`, while `ans` stays 2. The returned length is therefore 2.

**The invariant behind the scan**

After processing position `i`, `cnt` equals the length of the longest suffix of `nums[0:i+1]` made only of `mx`. If `nums[i]` is `mx`, that suffix is the preceding maximum-only suffix plus the current element. If it is not `mx`, no non-empty suffix ending there can contain only `mx`, so its length is zero. This proves the statement about `cnt` by induction over the scan.

At the same moment, `ans` equals the greatest `cnt` value produced at any processed position. Every contiguous run has a unique last position, and at that position `cnt` equals the run's full length. Therefore taking the maximum of these suffix lengths considers every run. When the loop finishes, `ans` is the longest maximum-only run in the entire array.

Earlier, we proved that the qualifying subarrays are exactly the maximum-only runs and their non-empty subarrays. The longest qualifying subarray is therefore the longest complete run, whose length is `ans`. This connects the simple counter scan back to the original bitwise AND requirement.

**Why two passes are still optimal**

Python's `max(nums)` makes one pass, and the explicit loop makes a second. Both are linear, so the total is linear. It is possible to combine discovery of the maximum and streak counting into one pass by resetting all counters when a new maximum appears. However, the two-pass version separates the mathematical steps cleanly: first fix the global target, then measure its runs. It is less error-prone and has the same asymptotic cost.

Any correct algorithm must inspect every element in the worst case. An unexamined final value might be a new maximum or might extend the longest run. The $O(n)$ scan is therefore asymptotically optimal.

## Complexity detail

Let $n$ be the length of `nums`. Finding `mx` with `max` visits $n$ elements and takes $O(n)$ time. The following loop visits $n$ elements and performs constant-time comparisons, assignments, increments, and maximum updates. Total time is $O(n) + O(n) = O(n)$.

The variables `mx`, `ans`, `cnt`, and the loop variable occupy a fixed amount of extra storage independent of $n$, so auxiliary space is $O(1)$. The input is read but not modified, and the method returns a single integer rather than allocating an output collection.

Although integers up to $10^6$ use multiple binary bits, Python's operations here compare values rather than repeatedly applying bitwise AND. Under the standard word-RAM analysis used by the manifest, each supported integer operation is constant time. Even if bit width were written explicitly as $B$, finding and comparing values would cost $O(nB)$ at the bit level, with $B$ bounded by the constraints.

## Alternatives and edge cases

- **Enumerate all subarrays:** Compute an AND for every start and end position. Even with a running AND per start, this takes $O(n^2)$ time and ignores the decisive fact that a singleton maximum establishes the target immediately.
- **Track distinct subarray AND values:** A common technique maintains the small set of AND results for subarrays ending at each position. It is useful when the target or number of distinct results matters, but it is unnecessary here because the maximum target collapses to the array maximum.
- **One-pass maximum and streak tracking:** When a larger value appears, replace the known maximum and reset the best and current streaks; handle equal and smaller values appropriately. This remains $O(n)$ and $O(1)$, but the exact two-pass solution is easier to verify.
- **Binary search on a length:** Testing whether a qualifying subarray of length $L$ exists would still reduce to finding a run of `mx` and would add needless logarithmic searches.
- **One element:** Its singleton subarray is legal and has the maximum AND, so the result is 1. The scan increments `cnt` once and returns 1.
- **All values equal:** Every element is `mx`, `cnt` grows to $n$, and the whole array is correctly selected.
- **Maximum appears only once:** The longest run has length 1 even if many smaller values share bits with the maximum. Any smaller operand makes the AND no greater than that smaller value.
- **Separated maximum values:** Runs on opposite sides of a smaller element cannot be joined because a subarray must be contiguous. Resetting `cnt` at the separator enforces this.
- **Bit patterns that seem compatible:** A smaller number may contain many of the maximum's 1-bits, but it is still numerically below `mx`, and the subarray AND is at most that operand. It therefore cannot keep the target value.
- **Positive-value constraint:** The proof uses the ordinary ordering property of bitwise AND for non-negative integers. The given values are positive, so signed negative-integer behavior never enters the problem.
- **Maximum constraint size:** With up to $10^5$ elements, the linear scan is suitable, while quadratic subarray enumeration would be far too slow.
