## General

**Search for the first strictly greater position**

The letters are already sorted in non-decreasing order, so all values less than or equal to `target` form a prefix. Any letters strictly greater than `target` form the suffix after that prefix.

The required ordinary answer is the first element of that greater suffix. This is exactly an upper-bound binary search: find the insertion position after all elements equal to the target.

**Why `bisect_right` matches strict comparison**

`bisect_right` returns the insertion index that would place a searched value after existing equal values. Therefore, when letters include duplicates of `target`, the returned position skips all of them and lands on the first genuinely greater character.

Using `bisect_left` would be wrong because it lands before equal values and could return the target itself, which is not strictly greater.

**Understand the key-function call**

The exact source calls

`bisect_right(letters, ord(target), key=lambda c: ord(c))`.

With Python’s keyed bisection, the key function is applied to array elements, not to the searched value. Each letter `c` is transformed to its integer character code, so the searched value must also be supplied as an integer, `ord(target)`.

The numeric character codes preserve lexicographic order for lowercase English letters. The result `i` is the first index whose keyed letter value is greater than the target’s code.

Passing `target` itself while keying elements to integers would compare incompatible types. Passing `ord(target)` is an intentional part of the implementation.

**Implement circular wraparound**

If at least one greater letter exists, `i < len(letters)` and the answer is `letters[i]`.

If no letter is greater, the upper bound is exactly `len(letters)`. The problem then asks for the first letter, as though the sorted array wraps around. The expression

`letters[i % len(letters)]`

handles both situations:

- A normal index remains unchanged because it is smaller than the length.
- The end position becomes `0` because `len(letters) % len(letters) == 0`.

No explicit conditional branch is needed.

**Trace duplicate targets**

For `letters = ["c", "f", "f", "j"]` and `target = "f"`, the upper-bound search places the target code after both copies of `"f"`. It returns index 3, whose letter is `"j"`.

For target `"z"`, every array letter is less than or equal to the target. The insertion position is 4, and modulo 4 produces index zero, returning `"c"`.

For target `"a"`, the insertion position is zero because even the first letter is greater. Modulo leaves zero unchanged.

**Why sorting makes binary search valid**

At any probe, comparing the middle letter with the target tells which half can contain the first greater value:

- If the middle letter is less than or equal to the target, the boundary lies to its right.
- If it is greater, that position may be the answer, but an earlier greater value may exist, so search left.

The non-decreasing guarantee creates one monotone boundary. Duplicate letters do not disturb it.

**Why the result is correct**

Upper-bound bisection returns the smallest index after every letter less than or equal to `target`. If that index is within the array, its letter is strictly greater, and no earlier letter can qualify. If the index equals the length, no greater letter exists and modulo selects the contractually required first letter.

These cases are exhaustive, so the returned character is always correct.

## Complexity detail

Let `n` be the number of letters. Binary search halves the remaining interval after each comparison, requiring `O(log n)` time.

The method stores only the returned index and uses the input array in place, so auxiliary space is `O(1)`. The lambda and integer character values do not allocate storage proportional to `n`.

The modulo and final indexing are constant-time operations.

## Alternatives and edge cases

- **Manual upper-bound binary search:** Maintain left and right boundaries, move left past values `<= target`, and return the final boundary modulo `n`. This avoids reliance on keyed `bisect` semantics and has the same bounds.

- **Linear scan:** Return the first letter greater than the target, otherwise the first letter. It is simple but costs `O(n)` instead of using the sorted order.

- **Use `bisect_left`:** This is incorrect when the target appears in the array because it may return an equal character. Strictly greater requires an upper bound.

- **Forget to convert the search value:** With `key=lambda c: ord(c)`, keyed array values are integers. The search argument must be `ord(target)`.

- **Several copies of the target:** `bisect_right` skips all of them.

- **Target below the first letter:** The insertion index is zero, directly returning the first letter.

- **Target at or above the last letter:** The insertion index is the array length, and modulo wraps to index zero.

- **Repeated non-target letters:** Non-decreasing order, not strict order, is sufficient for upper-bound search.

- **At least two distinct letters:** This guarantee supports the problem’s circular-next interpretation, though the implementation would also return the sole letter in a one-value array.
