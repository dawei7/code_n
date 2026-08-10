## General

**Why sorting reduces the problem to one fixed order**

An arithmetic progression has the same difference between every pair of consecutive values. Its common difference may be positive, negative, or zero. If a valid arrangement has a negative difference, reversing that arrangement produces the same values with a positive difference. Therefore, it is enough to determine whether the values form an arithmetic progression in non-decreasing order.

The simplified solution creates `ordered = sorted(arr)`. This preserves the original input while arranging all values from smallest to largest. For a given multiset of values, this non-decreasing order is fixed except for swapping equal values, which makes no observable difference. Consequently, if any rearrangement forms an arithmetic progression, the sorted arrangement must form one too.

**How the adjacent-difference check works**

The first two sorted values determine the only possible common difference:

`difference = ordered[1] - ordered[0]`

The constraints guarantee at least two elements, so both indices are valid. The generator then visits every index from `2` through `len(ordered) - 1`. At each position, it computes the new adjacent gap and compares it with `difference`:

`ordered[index] - ordered[index - 1] == difference`

Python's `all` returns `False` as soon as one comparison fails. If every comparison succeeds, it returns `True`. With exactly two elements, the range is empty; `all` returns `True`, which is correct because any two numbers define one common difference.

For `[3, 5, 1]`, sorting produces `[1, 3, 5]`. The first gap is `2`, and the remaining gap is also `2`, so the method accepts. For `[1, 2, 4]`, the first gap is `1`, while the next gap is `2`, so the method rejects.

**Why the result is correct**

If the method returns `True`, every adjacent pair in `ordered` has the same difference. Thus `ordered` itself is a valid rearrangement into an arithmetic progression.

Conversely, suppose some rearrangement is an arithmetic progression. Reverse it when its difference is negative. The resulting progression is non-decreasing and contains exactly the same values as `arr`, so it must match the sorted order. Its adjacent differences are all equal, which means the solution's scan cannot reject it. Therefore, returning `False` proves that no valid rearrangement exists.

## Complexity detail

Let $n$ be the number of elements in `arr`. Creating the sorted copy costs $O(n\log n)$ time. Checking its adjacent differences costs another $O(n)$ time, so the total time complexity is $O(n\log n)$.

The sorted copy contains $n$ elements and therefore uses $O(n)$ auxiliary space. The generator consumed by `all` uses only constant additional state beyond that copy.

## Alternatives and edge cases

- **Endpoint arithmetic plus a hash set:** The Optimal branch derives the required gap from the minimum and maximum values and checks the forced terms in expected $O(n)$ time using $O(n)$ space. It is asymptotically faster but requires explicit handling of divisibility, duplicates, and a zero span.
- **Sort the input in place:** Calling `arr.sort()` avoids a separate full copy in the source code, but mutates the caller's list. Python's sorting implementation may still use $O(n)$ temporary memory.
- **Repeated linear searches:** Deriving the expected terms and searching for each one directly in the list can take $O(n^2)$ time and is strictly worse than either published branch.
- **Exactly two values:** Any two values form an arithmetic progression, and the empty sequence of remaining comparisons makes `all` return `True`.
- **All values equal:** Every adjacent difference is zero, so the method accepts.
- **Mixed duplicates and distinct values:** Sorting places equal values together, creating a zero gap alongside a nonzero gap; the mismatch makes the method reject.
- **Negative values:** Sorting and subtraction handle negative integers without any special case.
- **Descending input:** The original order is irrelevant because the method checks a sorted copy.
- **Input preservation:** `sorted(arr)` leaves `arr` unchanged, which distinguishes this branch from an in-place sort.
