## General

**Membership matters, multiplicity does not**

The output asks whether each value occurs in an array, not how many times it occurs. Convert both arrays to hash sets so each distinct value is represented once and membership checks are expected constant time.

**Take both directional differences**

A value belongs in the first result exactly when it is in the first set and not in the second. The symmetric condition produces the second result. These are two separate directional differences: values shared by both sets appear in neither output, while a value unique to one side appears only in that side's list.

This construction matches the contract directly. Set conversion removes duplicates. Each directional difference then retains every and only value absent from the other array, so the two returned groups are complete and contain no duplicate entries.

## Complexity detail

Let $n=\lvert\texttt{nums1}\rvert$ and $m=\lvert\texttt{nums2}\rvert$. Building and comparing the hash sets takes expected $O(n+m)$ time.

The two sets and output values use $O(n+m)$ space in the worst case.

## Alternatives and edge cases

- **Repeated linear membership tests:** Checking every distinct value against the other list avoids hash storage but can require $O(nm)$ time.
- **Sort both arrays:** Sorting permits a two-pointer comparison in $O(n\log n+m\log m)$ time and may mutate the inputs unless copies are made.
- **Bounded-value bitmap:** The narrow numeric domain permits fixed indexed presence arrays, but a hash-set solution generalizes without depending on those bounds.
- **Duplicates:** Multiple copies of a value must contribute at most one result entry.
- **Complete overlap:** If both arrays have the same distinct values, both result groups are empty.
- **Disjoint arrays:** Every distinct value appears in its corresponding result group.
- **Output order:** Each inner list is order-independent, but the first and second groups themselves must retain their prescribed meanings.
