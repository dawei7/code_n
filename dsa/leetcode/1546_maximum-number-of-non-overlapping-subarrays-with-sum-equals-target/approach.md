## General

**Greedily choose the earliest finishing target-sum subarray**

Every desired object is an interval. For maximizing the number of non-overlapping intervals, an interval that finishes earlier leaves at least as much room for all future choices as one that finishes later.

The stored solution scans from left to right. Starting immediately after the last selected subarray, it finds the first possible ending index of any target-sum subarray. It selects that subarray, increments the answer, discards all prefix-sum history, and begins a fresh search after the selected end.

This is the standard earliest-finish greedy principle specialized to subarrays discovered through prefix sums.

**Detect a target sum with prefix differences**

For the current search segment, `s` is the running sum through the current index. Set `vis` contains prefix sums observed before the current position, relative to the segment start.

A subarray ending at the current index has sum `target` exactly when an earlier prefix sum equals `s - target`:

$$
s-\text{earlier prefix}=\texttt{target}.
$$

The set begins as `{0}`, representing the empty prefix before the segment starts. This allows a target-sum subarray that begins exactly at the current segment's first index to be detected.

Negative array values cause no problem. Prefix sums need not be increasing because the algorithm asks only whether the required difference has appeared.

**Understand the exact index movement**

At a nonmatching index, the inner loop increments `i` and then inserts the updated running sum into `vis`. That prefix can serve as the beginning boundary for a later subarray.

At a matching index, the source increments `ans` and breaks before incrementing `i` or inserting the current prefix. The outer code then executes one `i += 1`, moving directly to the element after the chosen subarray's end.

Thus no index is processed twice, and the next search cannot overlap the selected interval.

If the scan reaches the array end without finding another match, the inner loop has already advanced `i` to `n`. The outer increment makes it `n+1`, and the outer condition stops. That harmless extra increment does not access the array.

**Why resetting the prefix set is necessary**

After choosing a subarray ending at index `i`, future subarrays must begin after `i`. Prefix sums from before or inside the chosen interval represent starts that would overlap it.

Creating `s = 0` and `vis = {0}` for the next outer iteration discards those forbidden boundaries. This reset enforces non-overlap directly rather than recording interval endpoints separately.

**Why the earliest ending choice is optimal**

Consider the current unprocessed suffix. Let the algorithm choose a target-sum interval $A$ with the smallest possible ending position.

Take any optimal collection for this suffix. If it contains no interval, selecting $A$ is plainly better. Otherwise, let $B$ be its first interval. Because $A$ ends no later than $B$, replace $B$ with $A$.

Every later interval in that optimal collection begins after $B$ ends, so it also begins after $A$ ends. The replacement preserves non-overlap and the number of selected intervals. Therefore, some optimal solution begins with the greedy interval.

After selecting it, the remaining problem is exactly the same task on the suffix after its end. Repeating the exchange argument proves every greedy selection is compatible with a global optimum.

**Tracing the first example**

For five ones and target two, the first segment starts with prefix set containing zero. Running sums become one, then two. At sum two, `s-target` is zero, so indices zero and one form the earliest target-sum subarray.

The search resets at index two. Sums again become one and two, selecting indices two and three. Only the final element remains, so the answer is two.

**Why the final count is correct**

Within each search segment, prefix-sum membership detects exactly whether some target-sum subarray ends at the current position. Stopping at the first detected end selects the globally earliest feasible finish.

Resetting begins the independent suffix problem and prevents overlap. The interval-scheduling exchange argument proves this repeated choice maximizes the count, so `ans` is the required maximum.

## Complexity detail

Let $N$ be array length. Although the source has nested `while` loops, index `i` only moves forward. Each array element is added to a running sum once and causes constant expected-time set work. Total expected time is $O(N)$.

The prefix set can contain $O(N)$ distinct sums if a long segment has no selected target interval. Its worst-case auxiliary space is $O(N)$, matching the manifest. Each reset releases the previous segment's set for reuse or garbage collection.

Hash-set operations are expected $O(1)$; adversarial collision behavior is a language-runtime caveat rather than the intended bound.

## Alternatives and edge cases

- **Dynamic programming over all intervals:** It can solve the problem but is unnecessary once earliest finishing is recognized.
- **Store every target-sum interval:** Generating and sorting intervals uses more time and space than selecting during the scan.
- **Global prefix set without reset:** It can detect overlapping intervals and overcount, so history must be cleared after a selection.
- **Sliding window:** It is invalid with negative numbers because expanding or shrinking does not change sums monotonically.
- **Target zero:** Repeated prefix sums detect nonempty zero-sum subarrays correctly.
- **Negative values:** Prefix differences remain valid without any ordering assumption.
- **Single matching element:** The empty-prefix zero allows it to be selected as a one-element subarray.
- **No matching subarray:** The scan reaches the end and returns zero for that suffix or the whole array.
- **Adjacent selected intervals:** They are allowed because the next search begins exactly one index after the previous end.
- **Nested candidate intervals:** The earliest ending one is selected, leaving the largest possible suffix.
- **Duplicate prefix sums:** A set is enough because only existence, not which starting index, matters for earliest-end selection.
- **Nonempty requirement:** The lookup uses a previously stored prefix, so a detected difference corresponds to at least one processed element.
- **Nested loops:** Their total work is linear because `i` never resets backward.
