## General

**There are only two possible answers**

If every element is already equal, no operation is needed and the answer is zero.

Otherwise, choose the entire array as one subarray. Compute the bitwise AND of all its values, then replace every element in that same whole-array interval with the result. Since every position receives one identical value, the array becomes equal in exactly one operation.

Therefore:

- Already equal `-> 0` operations.
- Not already equal `-> 1` operation.

No input can require two or more operations.

**Why the whole-array operation is always legal**

The allowed subarray may be any nonempty contiguous interval `[l, r]`. The full interval `[0, n - 1]` is contiguous and nonempty because `n >= 1`.

Bitwise AND is well-defined for every positive input value. Whether the result is zero or positive does not matter; the operation assigns that one result to every selected position.

The goal asks only that all values become equal, not that they equal an original value or a specific target. Thus the global AND is always a valid common target.

**Detect whether the zero-operation case applies**

The source evaluates

`any(x != nums[0] for x in nums)`.

The generator compares each value with the first element.

If any comparison is true, at least one element differs and the array is not equal. If every comparison is false, every element equals `nums[0]` and therefore every pair of elements is equal through that common value.

The array is guaranteed nonempty, so accessing `nums[0]` is safe.

**Convert the Boolean directly to the answer**

Python converts `False` to integer zero and `True` to integer one. The source returns

`int(any(...))`.

This compactly implements the complete case distinction:

- `any` returns false for an already equal array, giving zero.
- `any` returns true for a non-equal array, giving one.

The conversion is not a heuristic. The full-array construction proves that the Boolean exactly equals the minimum operation count.

**Why zero is minimal for an equal array**

Operation counts cannot be negative. If the initial array already satisfies the goal, doing nothing achieves it with zero, which is therefore optimal.

Performing an operation would be unnecessary even though selecting any subarray of equal values might leave the array equal.

**Why one is minimal for a non-equal array**

A non-equal initial array does not satisfy the target before any operation, so zero operations are impossible.

The full-array operation supplies a one-operation solution. Combining the lower bound of at least one with the construction of at most one proves the minimum is exactly one.

**Trace the examples**

For `[1, 2]`, the generator sees that two differs from the first value one. It returns true, and the method returns one. Selecting the whole array computes `1 AND 2 = 0` and produces `[0, 0]`.

For `[5, 5, 5]`, every comparison with the first five is false. The array is already equal, so the method returns zero.

**Why smaller subarrays do not need analysis**

There may be many ways to equalize an array through one or more local operations, but the existence of a universal one-operation solution makes them irrelevant to the minimum.

Once the zero-operation case is checked, no optimization over interval choices remains.

**Short-circuit behavior**

`any` stops at the first true comparison. If an early value differs from `nums[0]`, the source does not scan the remainder.

Worst-case time remains linear because an equal array or a difference only at the end requires checking all values. Best-case time can be constant after the first mismatch.

The generator is lazy and does not allocate a list of Booleans.

## Complexity detail

Let `n` be the number of elements. In the worst case, the generator examines all `n` values, so time is `O(n)`.

Only a generator iterator, the current element, and the first-element reference are needed. Auxiliary space is `O(1)`.

The source does not compute the global AND because only the minimum count is returned. Computing it would still be `O(n)` but would perform unnecessary work after the one-operation proof.

The input list is read but not modified.

## Alternatives and edge cases

- **Use `len(set(nums))`:** Returning whether the set size exceeds one is correct but allocates `O(n)` space.
- **Compare adjacent elements:** Checking whether every `nums[i] == nums[i-1]` also works in `O(n)` time and `O(1)` space.
- **Compute the whole-array AND:** It can construct the eventual common value but is not needed to return the operation count.
- **Simulate interval operations:** This solves a harder problem than required because one global interval always suffices.
- **Single element:** It is already equal to itself, so `any` finds no mismatch and returns zero.
- **All values equal:** Return zero even if their shared value is not zero.
- **Global AND equals an existing value:** This does not change the count; a non-equal array still needs one operation.
- **Global AND equals zero:** Zero is a valid common result.
- **Difference at the second element:** `any` short-circuits quickly and returns one.
- **Difference only at the end:** The source scans the full array, still within `O(n)`.
- **Nonempty guarantee:** It makes `nums[0]` safe. An empty-array variant would need a separate convention.
- **Input preservation:** The source only tests values and never applies the conceptual operation.
- **Missing import:** The stored source uses `List` without importing it. Standalone Python needs `from typing import List` unless the harness provides the name.
