## General

**Understand what "largest but smaller" demands**

Lexicographic comparison examines arrays from left to right. At the first index where two arrays differ, the array with the smaller value at that index is lexicographically smaller; later positions cannot reverse that decision.

We need an array smaller than `arr`, so the first position changed by the swap must receive a smaller value. Among all arrays satisfying that requirement, we want the largest one. This creates three priorities in order:

1. Preserve the original prefix for as long as possible.
2. At the first changed position, place the largest available value that is still smaller than the original value.
3. If duplicate copies of that chosen value exist, swap with the copy that leaves the suffix as large as possible.

The code realizes these priorities using two right-to-left scans and one swap.

**Locate the rightmost position that can be decreased**

The outer loop is:

```python
for i in range(n - 1, 0, -1):
    if arr[i - 1] > arr[i]:
```

The loop begins at the final index and moves left. It looks for the first adjacent descent `arr[i - 1] > arr[i]`.

At such a descent, the value at `i - 1` can certainly be decreased: `arr[i]` is to its right and is strictly smaller, so those two positions could be swapped to make the array lexicographically smaller.

Because the scan starts at the right, `i - 1` is the rightmost index that can serve as the first changed position. Choosing it preserves more of the original prefix than choosing any earlier index. Since lexicographic order prioritizes that unchanged prefix before all later values, no solution whose first change occurs earlier can be larger.

The absence of a descent to the right also tells us something important about the suffix. Once the loop finds the rightmost descent, every adjacent pair inside `arr[i:]` is non-decreasing. If a later pair descended, the loop would have found it first. Thus:

```text
arr[i] <= arr[i + 1] <= ... <= arr[n - 1]
```

This ordered suffix lets the second right-to-left scan identify the best swap partner without sorting.

**Why a swap cannot first decrease a later index**

Suppose one tries to preserve the prefix through an index later than `i - 1`. The suffix beginning at `i` is already non-decreasing. At any suffix position `p`, every value to its right is at least `arr[p]`. Swapping `arr[p]` with a later value therefore cannot put a strictly smaller number at `p`.

So no one-swap permutation can have its first decrease strictly to the right of the found pivot. The pivot at `i - 1` is not merely a convenient choice; it is the latest possible first difference.

**Choose the largest value below the pivot**

The inner loop scans candidate indices from the end back through `i`:

```python
for j in range(n - 1, i - 1, -1):
    if arr[j] < arr[i - 1] and arr[j] != arr[j - 1]:
```

Let the pivot value be `arr[i - 1]`. A candidate must be strictly smaller. An equal value would leave the pivot unchanged, so the first actual difference might occur later and would not necessarily make the result smaller. A larger value would make the result lexicographically larger than the original, which is forbidden.

Because `arr[i:]` is non-decreasing from left to right, scanning it from right to left visits values from largest to smallest. The first candidate satisfying `arr[j] < arr[i - 1]` therefore has the greatest value that can legally replace the pivot.

That choice is optimal at the first differing index. Every candidate keeps the same prefix ending just before the pivot, so the candidate with the largest smaller pivot replacement produces the lexicographically largest result, regardless of what happens farther right.

**Handle duplicate candidate values correctly**

The condition `arr[j] != arr[j - 1]` is easy to overlook. Its purpose is to select the leftmost occurrence within a block of duplicate candidate values.

Imagine the pivot is three and the sorted suffix begins with two copies of one. Swapping with either copy puts one at the pivot, so both results have the same first difference. The tie is decided later: the original pivot value three should be inserted at the earlier duplicate position, because placing that larger value earlier makes the suffix lexicographically larger.

Since the inner loop moves right to left, it first reaches the rightmost copy of a duplicate block. For that copy, `arr[j] == arr[j - 1]`, so it is skipped. The scan continues until it reaches the leftmost copy, whose preceding value is different. That is the copy selected.

For example, consider `[3, 1, 1, 3]`. The pivot is the first three, and the best smaller value is one. Swapping with the leftmost one produces `[1, 3, 1, 3]`. Swapping with the rightmost one produces `[1, 1, 3, 3]`. Both are smaller than the input, but the former is larger because its value at index one is three instead of one.

When `j == i`, `j - 1` is the pivot index. A legal candidate already satisfies `arr[j] < arr[i - 1]`, so the duplicate guard is automatically true. There is no out-of-range access.

**Perform exactly the chosen exchange**

Once the best partner is found, Python's simultaneous assignment swaps the two values:

```python
arr[i - 1], arr[j] = arr[j], arr[i - 1]
return arr
```

The function returns immediately because the globally optimal one-swap result has been determined. Continuing to search could only consider an earlier pivot, which would create a smaller lexicographic result.

The swap mutates the input list. The returned object is the same list object in its new order.

**Why the complete choice is optimal**

The outer scan chooses the latest index at which a first decrease is possible, maximizing the unchanged prefix. The ordered suffix then allows the inner scan to choose the largest value strictly below the pivot, maximizing the value at the first changed index. Finally, the duplicate guard chooses the leftmost occurrence of that value, placing the displaced larger pivot as early as possible in the remaining suffix.

These decisions optimize lexicographic order in exactly the order lexicographic comparison uses. Therefore no other single swap can produce an array that is both smaller than the input and larger than the returned array.

**When no descent exists**

If the outer loop finishes without finding `arr[i - 1] > arr[i]`, the entire array is non-decreasing. It is then the lexicographically smallest ordering of its multiset.

Any swap of distinct values would move a larger value to the first changed position and make the array larger, not smaller. Swapping equal values would leave the array unchanged rather than create a smaller permutation. Hence no valid smaller permutation exists, and the final `return arr` correctly returns the original array.

## Complexity detail

Let `N` be the length of `arr`.

The outer scan examines at most `N - 1` adjacent pairs. Once it finds the pivot, the inner scan examines at most the remaining suffix, also bounded by `N - 1` elements. The scans are sequential rather than nested over every pivot: the inner loop runs only once, for the first descent found. Total time is therefore `O(N)`.

The algorithm stores only `n`, the two indices, and temporary values used by the swap. It creates no auxiliary array or map, so auxiliary space is `O(1)`.

The output is produced by modifying `arr` in place. If a caller needs the original order preserved, copying the array before calling this logic would add `O(N)` space, but that copy is not part of the exact implementation.

## Alternatives and edge cases

- **Generate all swaps:** Trying every pair, keeping only smaller results, and selecting the largest takes `O(N^3)` time if every candidate array is copied and compared naively. It ignores the strong lexicographic structure used by the two scans.
- **Sort candidate permutations:** Materializing all one-swap results also requires quadratic candidate count and substantial memory. The pivot argument identifies the winner directly in linear time.
- **Choose the first smaller suffix value:** Scanning the suffix from left to right and accepting the first smaller value can place a value much smaller than necessary at the pivot. The result is valid but not lexicographically largest.
- **Choose the rightmost duplicate blindly:** When the best candidate value appears more than once, using its rightmost occurrence puts the displaced pivot later. Choosing the leftmost duplicate makes the suffix larger.
- **Strictly increasing input:** A strictly increasing array has no descent and is already its multiset's smallest permutation. The function returns it unchanged.
- **All values equal:** Every possible swap leaves the array identical. There is no smaller permutation, so returning the same array is correct.
- **Single element:** There is no pair of positions to swap. The outer range is empty and the original one-element list is returned.
- **Strictly decreasing input:** The rightmost adjacent pair is immediately a descent. Swapping the final two values makes the smallest possible change near the end and gives the largest smaller permutation.
- **Duplicates around the pivot:** The strict candidate test rejects values equal to the pivot, while the neighboring-value guard walks across duplicates of the selected smaller value to their leftmost occurrence.
- **Exactly one swap wording:** When a smaller permutation exists, the code performs exactly one swap. When none exists, the contract explicitly permits returning the unchanged array.
- **Input mutation:** The solution changes `arr` in place. This matches the returned-array contract, but callers retaining the old order must pass a copy.
- **Positive-value constraint:** The reasoning depends only on comparisons, so it would also work for zero or negative integers. Positivity does not require special handling.
