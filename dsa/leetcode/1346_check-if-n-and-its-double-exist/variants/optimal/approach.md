## General

The task asks for two **different indices**, not merely a numeric identity. A one-pass hash set handles both requirements: it remembers only values from earlier indices, and it checks whether the current value forms the double relationship with any of them before inserting itself.

Let the current value be `x`. A valid pair with an earlier value can have either orientation:

- The earlier value is twice `x`, so look for `x * 2`.
- The current value is twice the earlier value, so, when `x` is even, look for `x // 2`.

The condition
`x * 2 in s or (x % 2 == 0 and x // 2 in s)` checks both orientations.

**Why the parity guard is necessary**

If `x` is odd, it cannot be exactly twice an integer. Using floor division without checking parity would be wrong. For example, `3 // 2` is one, but three is not twice one. The test `x % 2 == 0` ensures the half lookup is performed only when an exact integer half exists.

The double lookup needs no corresponding guard because multiplying any integer by two remains an integer. Negative values also work. If the pair is negative five and negative ten, encountering either value second triggers one of the two checks.

**Why one pass covers every input order**

Suppose a valid pair has values `a` and `2a`. Whichever occurrence appears later becomes the current `x`:

- If `a` appears later, `x * 2` finds the earlier `2a`.
- If `2a` appears later, `x // 2` finds the earlier `a` because `2a` is even.

Thus no sorting or second pass is needed. The set contains exactly the distinct values at earlier indices, so the two possible arrival orders are both covered.

**Distinct indices and the special role of zero**

The current value is added with `s.add(x)` only after the pair checks. Therefore, an element can never match itself during its own iteration. Any match found in `s` came from an earlier, distinct index.

This also handles zero correctly. Numerically, zero is twice zero. On the first zero, the set does not yet contain zero, so neither lookup succeeds; the value is then added. On the second zero, `x * 2` is zero and is already in the set, so the method returns true. Exactly one zero does not produce a false match.

If the loop finishes, every element has been checked against all earlier distinct values in both orientations. Any valid pair would have been detected when its later endpoint was processed. Therefore, returning false after the loop proves that no required pair exists.

The input array is not modified. Duplicate nonzero values alone do not automatically form a pair because `x` generally differs from `2x`; zero is the only value equal to its own double.

## Complexity detail

Let $n$ be the array length.

The loop examines each element once. It performs a constant number of arithmetic operations, set membership tests, and one insertion. Python hash-set lookup and insertion take expected $O(1)$ time, so total expected time is $O(n)$.

In the theoretical worst case of pathological hash collisions, set operations can degrade, but standard analysis uses the expected hash-table model for integer keys.

The set contains at most one copy of each distinct value and at most $n$ values. Auxiliary space is $O(n)$ in the worst case. Scalar `x` and the arithmetic results need constant additional space.

## Alternatives and edge cases

- **Frequency map:** Count all values first, then check whether each double exists. It is also $O(n)$ expected time and naturally handles zero by requiring its frequency to be at least two.
- **Sorting and binary search:** Sort the array and search for each doubled value. It takes $O(n\log n)$ time and needs careful index handling for zero and duplicates.
- **Brute-force pairs:** Check every pair of distinct indices directly. This uses $O(1)$ extra space but $O(n^2)$ time.
- **Only checking the double:** A one-pass method that checks only `2 * x` misses the order where the smaller value appeared earlier and its double appears later. Both orientations are required.
- **Floor division without parity:** This creates false matches for odd values, such as treating one as half of three.
- **Single zero:** It must not satisfy the condition because two distinct indices are required. Insertion after lookup prevents self-matching.
- **Two zeros:** The second zero finds the first and correctly returns true.
- **Negative pair:** Values such as negative four and negative eight satisfy the same doubling relationship and are handled without a special case.
- **Duplicate nonzero values:** Two copies of five do not form a valid pair with each other because five is not twice five.
- **Values at either order:** The double and exact-half checks make the algorithm independent of which member appears first.
- **Input preservation:** The solution builds a separate set and leaves the original array unchanged.
- **Early return:** Once a matching earlier value is found, no later element can invalidate the pair. Returning immediately is safe and can avoid scanning the rest of the array while preserving the $O(n)$ worst-case bound.
