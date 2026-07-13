# Sort Colors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 75 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-colors/) |

## Problem Description
### Goal
An array `nums` contains only the values `0`, `1`, and `2`, representing red, white, and blue. Sort the colors so all zeroes come first, followed by all ones and then all twos, while preserving the number of occurrences of each value.

The native method must modify the array in place, make one pass, and avoid a library sorting routine; it returns no value. The app adapter returns the same mutated array for inspection. Inputs of one color or one element remain unchanged apart from satisfying the same ordering.

### Function Contract
**Inputs**

- `nums`: a nonempty `List[int]` containing only 0, 1, and 2

**Return value**

The sorted array in the app; LeetCode's `sortColors` method returns nothing.

### Examples
**Example 1**

- Input: `nums = [2,0,2,1,1,0]`
- Output: `[0,0,1,1,2,2]`

**Example 2**

- Input: `nums = [2,0,1]`
- Output: `[0,1,2]`

**Example 3**

- Input: `nums = [1]`
- Output: `[1]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Maintain three finalized color regions around one unknown region**

Maintain `low`, `current`, and `high`. Values in `[0, low)` are finalized zeroes, values in `[low, current)` are finalized ones, `[current, high]` is unclassified, and `(high, n)` contains finalized twos. Initially the first three regions are empty except for the full unknown interval.

**The pointer update depends on which side supplied the swap**

For `0`, swap with `low` and advance both `low` and `current`. The value arriving from `low` is known to be `1` when the pointers differ, or is the current value itself when they coincide, so it needs no reclassification. For `1`, leave it in the middle region and advance `current`.

For `2`, swap with `high` and decrement only `high`. The value arriving from the right belonged to the unknown region and may be `0`, `1`, or `2`, so advancing `current` would skip an unclassified value.

**Every iteration shrinks the unknown interval**

Every step expands one classified region while preserving the values assigned to all others. The unclassified interval strictly shrinks, so the loop terminates with consecutive 0, 1, and 2 regions.

**Trace why a swapped-in right value is inspected again**

For `[2,0,2,1,1,0]`, the first 2 swaps with the final 0, which is then processed and moved into the zero region. Later 2s move right and 1s remain in the center, yielding `[0,0,1,1,2,2]`.

**The unclassified region shrinks without disturbing final regions**

Values left of `low` are finalized zeroes, values between `low` and `current` are finalized ones, and values right of `high` are finalized twos. A current zero swaps into the zero region; a one extends the middle region; a two swaps into the high region while leaving the incoming value unclassified for the next check.

Each action preserves all finalized regions and reduces the unclassified interval by at least one position. When `current` passes `high`, the interval is empty and the three finalized regions cover the whole array in sorted color order.

#### Complexity detail

Each iteration classifies at least one position, so there are $O(n)$ operations. Three indices and swap temporaries use $O(1)$ space.

#### Alternatives and edge cases

- **Count values then overwrite:** is also linear and constant-space but requires two passes.
- **Comparison sorting:** works but takes $O(n \log n)$ time and ignores the three-value domain.
- **Allocate three buckets:** is simple but uses $O(n)$ extra space.
- Arrays containing one color already satisfy the partition invariant and remain unchanged apart from harmless self-swaps.
- The method depends on the closed domain `{0,1,2}`; additional values would require more partitions or a general sorting algorithm.

</details>
