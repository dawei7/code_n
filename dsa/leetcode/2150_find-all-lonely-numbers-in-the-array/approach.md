## General

Loneliness is a property of a value’s frequency and its two neighboring values:

1. the value itself must occur exactly once;
2. one less than it must not occur;
3. one more than it must not occur.

A frequency map answers all three questions directly.

**Count every distinct value once**

The source constructs `cnt = Counter(nums)`. For every value `x`, `cnt[x]` is its number of occurrences.

This first pass is necessary because seeing a value once during a left-to-right scan does not prove it will not appear again later. It also gives constant-time expected checks for neighboring values without searching the array repeatedly.

**Iterate over distinct value-frequency pairs**

The comprehension loops through `cnt.items()`, so each distinct value `x` is considered exactly once with its frequency `v`. Its filter is

`v == 1 and cnt[x - 1] == 0 and cnt[x + 1] == 0`.

The first comparison enforces uniqueness. A frequency of two or more immediately makes the value non-lonely, even if neither adjacent numeric value occurs.

The second and third comparisons require both adjacent values to be absent. Logical `and` short-circuits from left to right. If `v != 1`, Python does not need to evaluate the neighbor checks, though this affects only constant factors.

**Understand missing Counter keys**

For a normal dictionary, reading a missing key with square brackets raises `KeyError`. A `Counter` is different: a missing key reads as count zero.

Therefore `cnt[x - 1] == 0` means precisely that `x - 1` does not occur, and `cnt[x + 1] == 0` means `x + 1` does not occur. These missing-key reads do not insert new entries into the counter, so iterating through `cnt.items()` remains safe.

**Return values, not occurrences**

Only values with frequency one pass, so adding `x` once to the result is exactly right. A duplicate value is rejected entirely rather than emitted once.

The problem permits any output order. In modern Python, `Counter` preserves first-insertion order, so the result commonly follows the order in which distinct values first appeared. Correctness does not rely on that behavior.

For `[10,6,5,8]`, every value has frequency one. Ten passes because neither nine nor eleven occurs. Eight passes because neither seven nor nine occurs. Six fails because five occurs, and five fails because six occurs.

For `[1,3,5,3]`, the frequency of three is two, so it is rejected before neighbor absence could matter. One and five are unique and have no adjacent values.

**Why the filter is necessary and sufficient**

If the code includes `x`, then its stored frequency is one and both neighboring frequencies are zero. These are exactly the three parts of the lonely definition.

If `x` is lonely, its frequency must be one and neither adjacent value appears. The counter values tested by the comprehension are therefore one, zero, and zero, so `x` is included. No lonely number can be missed and no non-lonely number can pass.

**Why numeric adjacency is different from array adjacency**

The word “adjacent” in the problem means values `x-1` and `x+1`, not elements next to `x` in the input order. The frequency map intentionally discards positions because only membership of those neighboring numbers matters.

## Complexity detail

Let $n$ be the array length and $d$ the number of distinct values. Building the counter takes $O(n)$ expected time. The comprehension examines $d \le n$ entries and performs expected $O(1)$ counter lookups for each, taking $O(d)$ expected time. Total expected time is $O(n)$.

The counter stores $d$ key-count pairs, using $O(d)$ space, which is $O(n)$ in the worst case. The returned list can also contain up to $d$ values. Temporary comprehension state is constant beyond the counter and output.

The input is only read. Counter construction and result creation do not modify `nums`.

## Alternatives and edge cases

- **Sort the array:** After sorting, a value is lonely if it occurs once and differs by more than one from its immediate sorted neighbors. This costs $O(n\log n)$ time and needs careful boundary and duplicate handling.
- **Use a set plus a separate count:** A set handles neighbor membership, but uniqueness still requires counts. `Counter` supplies both in one structure.
- **Search the list for every value:** Repeated calls to count or membership can make the algorithm $O(n^2)$.
- **One element:** Its frequency is one and neither numeric neighbor occurs, so it is lonely.
- **Duplicate with absent neighbors:** It is not lonely because `v == 1` fails.
- **Unique value with one adjacent neighbor:** Either neighbor check failing is enough to reject it.
- **Both neighbors present:** The value is non-lonely regardless of all three frequencies.
- **Zero value:** The check for `-1` safely returns zero because negative numbers need not be legal input values to be queried as absent keys.
- **Maximum value one million:** Querying one million plus one is equally safe.
- **Consecutive chain:** In values such as `[4,5,6]`, none is lonely: endpoints each have one neighbor and the middle has two.
- **Gaps of two:** Values `x` and `x+2` do not disqualify one another because only differences of exactly one matter.
- **Any output order:** The comprehension’s order is acceptable; no sorting step is required.
- **Missing-key behavior:** Counter lookup returns zero and does not grow the mapping, avoiding mutation during `items()` iteration.
- **Input preservation:** All frequency and output storage is separate from `nums`.
