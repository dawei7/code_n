## General

**Change the rightmost possible position**

Lexicographic order compares arrays from left to right. To obtain the smallest arrangement that is still greater than the current one, the algorithm should preserve the longest possible prefix. It therefore searches from the right for the first index `i` satisfying

```python
nums[i] < nums[i + 1]
```

This `i` is the pivot. Everything after it is non-increasing: if an ascent had existed farther right, the reverse scan would have found that position first.

A non-increasing suffix is already the greatest lexicographic arrangement of its own multiset. Rearranging only that suffix cannot make the whole array larger. The pivot is consequently the rightmost position that must change.

**Read the generator-based pivot search carefully**

The exact source uses

```python
i = next(
    (i for i in range(n - 2, -1, -1) if nums[i] < nums[i + 1]),
    -1,
)
```

`range(n - 2, -1, -1)` visits candidate indices from right to left, ending at zero. The generator yields only indices containing an ascent, and `next` takes the first yielded one. If none exists, the supplied default `-1` is returned instead of raising `StopIteration`.

For a one-element array, the range is empty and `i` is also `-1`, which correctly indicates that no larger permutation exists.

**Understand the unusual `if ~i` test**

The condition is not a logical negation. `~i` is the bitwise complement, equal to `-i - 1` for Python integers. Therefore:

- when `i == -1`, `~i == 0`, which is false; and
- when `i >= 0`, `~i` is a nonzero negative integer, which is true.

So `if ~i:` is a compact but less beginner-friendly spelling of `if i != -1:`. The swap block runs only when a pivot exists.

**Replace the pivot with the smallest value that makes an increase**

Once the pivot is fixed, the next permutation must put a value strictly greater than `nums[i]` at index `i`. Choosing a much larger value would skip valid permutations. The source scans from the final index leftward and takes the first `j` with `nums[j] > nums[i]`.

Because the suffix is non-increasing from left to right, its rightmost value greater than the pivot is the smallest suffix value that is still greater. The strict `>` is important with duplicates: swapping with an equal value would not increase the permutation.

The pair assignment

```python
nums[i], nums[j] = nums[j], nums[i]
```

evaluates both old values before writing either destination, so no temporary variable is required.

**Why the suffix remains non-increasing after the swap**

Before the swap, values before `j` in the suffix are at least `nums[j]`. Values after `j` are no greater than the old pivot, because `j` was the rightmost element strictly greater than it. Placing the old pivot at `j` therefore keeps it no greater than the part before and no smaller than the part after. The entire suffix remains non-increasing.

This fact allows the smallest possible suffix to be obtained by reversal rather than general sorting.

**Reverse the suffix into its minimum arrangement**

The exact statement is

```python
nums[i + 1 :] = nums[i + 1 :][::-1]
```

The right-hand slice copies the suffix, and `[::-1]` produces it in reverse order. Assigning it back replaces the original suffix in place from the caller's perspective. Since the suffix was non-increasing, its reversal is non-decreasing—the lexicographically smallest arrangement of those remaining values.

The pivot has been increased by the smallest possible amount, and the remainder has been minimized. No lexicographically greater permutation can lie between the old array and this result.

**Handle the maximum permutation by the same final line**

If no pivot exists, the complete array is non-increasing and is the greatest permutation of its multiset. The contract requires wrapping to the lowest permutation. With `i = -1`, `i + 1` is zero, so the final slice assignment reverses the entire array into non-decreasing order.

The false `if ~i` condition skips the nonexistent swap. Thus `[3,2,1]` becomes `[1,2,3]` without a separate reversal branch.

**Trace `[1, 3, 5, 4, 2]`**

Scanning from the right finds no ascent at `4,2` or `5,4`, but finds `3 < 5`, so pivot index one holds `3`. The suffix `[5,4,2]` is non-increasing. From the right, `2` is not greater than `3`; `4` is, so `j = 3`. Swapping gives `[1,4,5,3,2]`. Reversing the suffix `[5,3,2]` produces `[2,3,5]`, yielding `[1,4,2,3,5]`.

Every permutation still beginning with `1,3` is no greater than the original because its suffix was already maximal. Among permutations beginning with a value greater than `3`, choosing `4` is the smallest pivot increase, and `[2,3,5]` is the smallest possible remainder.

**Why the transformation is correct**

The pivot choice proves no change strictly to its right can increase the array. The rightmost-greater choice gives the least possible increase at the first changed position. Reversing the remaining non-increasing suffix gives the least arrangement after that position. These three facts establish that the result is greater and that no intermediate permutation exists. If there is no pivot, the input is globally maximal and full reversal gives the required global minimum.

## Complexity detail

Let $n$ be `len(nums)`.

- **Time complexity: $O(n)$.** The pivot generator scans at most $n-1$ adjacent pairs, the successor generator scans at most the suffix length, and reversal copies and writes at most $n$ values. These are sequential linear operations, not nested scans.
- **Auxiliary space of the exact Python source: $O(n)$ in the worst case.** `nums[i + 1 :]` and its reversed slice create temporary list objects proportional to the suffix length. The generator expressions themselves use constant iterator state. The manifest's $O(1)$ claim describes an implementation that reverses the suffix with two indices and swaps; it does not describe this slice-based line's peak allocation.

The mutation is still in place in the API sense because the original `nums` object is updated and no replacement list is returned.

## Alternatives and edge cases

- **Two-pointer suffix reversal:** Swap suffix endpoints while moving inward. It preserves $O(n)$ time and achieves genuine $O(1)$ auxiliary space.
- **Sort the suffix:** Correct after the pivot swap but costs $O(n\log n)$ rather than exploiting its known reverse order.
- **Generate all permutations:** Factorial time and large storage are unnecessary.
- **Single element:** No pivot exists; reversing the length-one slice leaves it unchanged.
- **Entirely non-increasing input:** Full reversal wraps to the smallest permutation.
- **Entirely increasing input:** The pivot is the penultimate index, so only the final two values swap.
- **Duplicate values:** Strict pivot and successor comparisons avoid treating equal swaps as an increase.
- **Repeated maximum suffix:** The rightmost greater successor remains the smallest legal replacement.
- **No return value:** The function's result is communicated solely through mutation of `nums`.
- **`~i` readability:** It works because only `-1` and nonnegative indices are possible; `i != -1` would express the intent more directly.
