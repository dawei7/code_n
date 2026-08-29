## General

**Group compatibility by decimal digit sum**

Two numbers may form a pair exactly when their decimal digits sum to the same value. The algorithm processes numbers from left to right and remembers the largest earlier number for each digit sum.

When a new number arrives, pairing it with the largest compatible earlier number produces the greatest pair ending at the current index. Comparing those candidates across all indices finds the global maximum.

**Compute one number's digit sum**

For current value `v`, the code copies it into `y` and initializes `x = 0`. Repeatedly:

- `y % 10` extracts the last decimal digit;
- that digit is added to `x`;
- `y //= 10` removes the last digit.

When `y` reaches zero, `x` is the sum of every digit in `v`. The original `v` remains intact for pair sums and dictionary storage.

All input values are positive, so the loop executes at least once. With `v <= 10^9`, there are at most ten decimal digits.

**Store only the largest previous value per group**

Dictionary `d` maps a digit sum to the greatest number with that sum among values processed earlier.

If `x in d`, at least one distinct earlier index is compatible with the current index. The best compatible pair ending here is `d[x] + v` because replacing `d[x]` by any smaller earlier group member cannot increase the sum.

The algorithm updates `ans` with that candidate, then sets

`d[x] = max(d[x], v)`.

Updating after evaluating the candidate is important. It ensures the current value is not paired with itself. Afterward it becomes available as the best previous value for later indices.

**Why one stored number is enough**

Suppose a digit-sum group has previous values `a_1, a_2, ..., a_r` and current value `v`. Every legal pair ending at `v` has sum `a_t + v`. Since `v` is fixed, the greatest is obtained with `max(a_t)`.

Smaller previous values can never become useful again: for any later compatible value `w`, the stored maximum plus `w` is at least their pair sum. Discarding them loses no optimal candidate.

Across the full scan, consider the two largest values in the globally optimal digit-sum group. Whichever of those two appears later is processed when the earlier one—or an even larger compatible value—is already stored. The algorithm evaluates a pair at least as large as the optimum, and every evaluated pair is legal, so it finds exactly the maximum.

**Preserve minus one when no group has two indices**

`ans` starts at `-1`. It changes only when a digit sum has already appeared. If every digit sum occurs once, no pair exists and the sentinel remains.

Duplicate numeric values are allowed at different indices. The second occurrence sees the first in `d` and may form a valid pair; index distinctness is guaranteed by processing order, not by value uniqueness.

**The digit-sum key universe is bounded**

For values up to `10^9`, the largest digit sum occurs near nine digits of 9 and is at most 81. The dictionary therefore contains at most a small fixed number of keys.

The source uses `defaultdict(int)`, but the explicit `if x in d` distinguishes an unseen group from a real stored value. This is appropriate because all actual numbers are positive.

## Complexity detail

Let `n` be the number of values and `D` the maximum number of decimal digits. Digit extraction costs `O(D)` per number, so total time is `O(nD)`. Under `nums[i] <= 10^9`, `D <= 10` is fixed and the manifest simplifies this to `O(n)`.

The mapping has at most 82 possible digit-sum keys, so auxiliary space is `O(1)` under the bounded numeric domain. In a generalized arbitrary-length-number setting, it would scale with the number of possible digit sums.

The input list is not changed. Python integers safely hold pair sums up to twice the maximum input.

## Alternatives and edge cases

- **Group all values then sort each group:** The top two in every group give candidates, but storing everything uses `O(n)` space and sorting adds `O(n \log n)` time.
- **Two-element heap per digit sum:** Retain each group's two largest values. This works but stores more state than the streaming maximum needs.
- **Fixed array indexed by digit sum:** Use 82 entries initialized to a sentinel instead of a dictionary. It provides the same bounded constant space.
- **Store the smallest prior value:** Pair sums require the largest compatible partner, so this would miss the optimum.
- **Update the mapping before forming a pair:** The current value could then pair with itself on its first group occurrence, violating distinct indices.
- **Only one number:** No prior group member exists, so the answer stays `-1`.
- **All digit sums distinct:** No pair is evaluated.
- **Duplicate values at different indices:** They are a valid pair and may produce the maximum sum.
- **Several values in one group:** Only the largest previous member matters for every new arrival.
- **Optimal two values in either order:** Whichever appears second forms a candidate with the best earlier member, so input order cannot hide the optimum.
- **Positive input guarantee:** It makes zero a safe default value internally, although membership is checked explicitly.
- **Value `10^9`:** Its digit sum is one and is processed normally.
- **No string conversion:** Arithmetic digit extraction avoids allocating decimal strings.
- **Input preservation:** `y` is a local copy, so neither `v` nor `nums` is modified.
