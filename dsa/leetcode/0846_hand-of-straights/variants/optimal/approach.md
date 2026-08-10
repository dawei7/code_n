## General

**A necessary divisibility check**

Every group must contain exactly `groupSize` cards, and every card must belong to one group. If `len(hand)` is not divisible by `groupSize`, a complete partition is impossible.

The solution returns false immediately in that case.

**Count copies of every card value**

`cnt = Counter(hand)` records how many unused copies of each value remain. Multiple identical cards may be needed in different consecutive groups, so a set alone would lose essential multiplicity.

The algorithm iterates through `sorted(hand)`, which includes duplicates in nondecreasing order.

**The smallest remaining card must start a group**

When current value `x` has `cnt[x] > 0`, at least one copy remains unassigned. Because the traversal is sorted, there is no smaller remaining card that could start a group containing `x` later.

Could `x` appear in the middle of a group starting at `x-1` or lower? If such a group were still needed, its smaller starting card would also remain and would have been encountered earlier. All groups starting below `x` have already been formed.

Therefore, the smallest remaining `x` is forced to be the first value of a new group:

$$
x,x+1,\ldots,x+\texttt{groupSize}-1.
$$

This forced-choice property is the greedy proof.

**Consume one copy of every required consecutive value**

For `y` in `range(x, x + groupSize)`:

- if `cnt[y] == 0`, the required group cannot be completed, so return false;
- otherwise, decrement `cnt[y]` by one.

Counter returns zero for a missing key, so gaps in card values are detected without a separate dictionary-membership test.

After the inner loop, one valid group beginning at `x` has been removed from the multiset.

**Why duplicate entries in `sorted(hand)` are harmless**

The sorted list still contains original occurrences whose Counter count may already have been consumed by earlier groups. At such an occurrence, `if cnt[x]` is false, so the loop skips it.

If several copies of `x` remain, separate visits to duplicate `x` entries will each start another required group. There are exactly as many original sorted occurrences as copies, so every needed start is eventually processed.

**Trace the successful example**

For `[1,2,3,6,2,3,4,7,8]` with group size three, counts include two copies each of 2 and 3.

- The first remaining value 1 forces group `[1,2,3]`.
- The next remaining value 2 forces `[2,3,4]`.
- Values 2, 3, 3, and 4 encountered later have zero remaining counts and are skipped.
- The next remaining value 6 forces `[6,7,8]`.

All cards are consumed, so the function returns true.

**Why failure is conclusive**

Suppose the smallest remaining value is `x` and some required `y` from `x` through `x+groupSize-1` is unavailable. Every valid grouping must place `x` in a consecutive group. Since no smaller card remains, that group cannot start below `x`; it must start at `x` and therefore requires `y`.

Because `y` is missing, no alternative rearrangement can succeed. Returning false is safe.

**Why successful completion proves a partition**

Each inner-loop execution removes exactly one copy of each of `groupSize` consecutive values, constructing a legitimate group. No count becomes negative because availability is checked first.

If the outer scan finishes without failure, every original card occurrence has either started a group or was already consumed in a previous group. Divisibility and the count decrements mean all counts are zero, and the constructed groups form a full valid partition.

## Complexity detail

Let `n = len(hand)`. Building the Counter takes `O(n)` time. Sorting the hand takes `O(n\log n)`.

Although an inner loop appears inside the sorted traversal, each successful inner iteration decrements one actual card count. Across all formed groups, exactly `n` decrements occur. Skipped sorted entries take constant time. Work after sorting is therefore `O(n)`, and total time is `O(n\log n)`.

The Counter stores up to `O(n)` distinct keys, and `sorted(hand)` creates a length-`n` list. Total auxiliary space is `O(n)`.

## Alternatives and edge cases

- **Min-heap of distinct values:** Repeatedly take the smallest remaining key and consume a group. It avoids sorting all duplicate occurrences but requires heap cleanup and logarithmic operations.

- **Ordered map:** Process counts by ascending key and propagate required group starts. It can be efficient but is more involved than the direct greedy scan.

- **Backtracking over group assignments:** The smallest-card argument makes choices forced, so exponential search is unnecessary.

- **Hand length not divisible by group size:** Return false before counting or sorting.

- **`groupSize = 1`:** Every card forms its own one-value consecutive group, so divisibility holds and all groups succeed.

- **Missing middle value:** The first forced group that needs it returns false.

- **Duplicate values:** Counter multiplicity assigns copies to different groups correctly.

- **Large gaps:** They are acceptable between completed groups, but not inside one forced consecutive range.

- **Several groups with the same start:** Multiple copies of the start create multiple identical value ranges, provided all required multiplicities exist.

- **Card value zero:** It is a valid smallest start; `range` handles it normally.

- **Values near `10^9`:** Python integer ranges and Counter keys handle them without an array indexed by value.

- **Input immutability:** `sorted(hand)` returns a new list, and the original `hand` ordering is unchanged.
