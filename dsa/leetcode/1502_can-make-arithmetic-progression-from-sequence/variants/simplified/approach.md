## General

**Sort to expose the only order that needs checking**

A valid arithmetic progression may have a positive, negative, or zero common
difference. Reversing a valid sequence only changes the sign of that
difference, so it is enough to ask whether the values form a progression in
non-decreasing order.

Create a sorted copy of `arr`. Sorting preserves every occurrence, including
duplicates, and produces the only non-decreasing arrangement of the multiset.
Consequently, if any rearrangement forms an arithmetic progression, this sorted
order must form one as well.

**Compare every adjacent gap**

The first two sorted values determine the only candidate common difference.
Scan the remaining positions and compare each adjacent difference with that
value. Return `false` as soon as one differs. If the scan finishes, the sorted
copy itself is a valid arithmetic progression.

The reasoning works in both directions. Equal sorted gaps directly provide the
required arrangement. Conversely, reverse any valid arrangement when needed so
its difference is nonnegative. It is then non-decreasing and must equal the
sorted order of the same occurrences, so the scan cannot find a mismatch.

## Complexity detail

Sorting the $n$ values takes $O(n\log n)$ time, and the adjacent-gap scan takes
$O(n)$ time. The overall time bound is therefore $O(n\log n)$. Using
`sorted(arr)` preserves the input and stores an $O(n)$ copy.

This is the expected interview solution for this low-Elo Easy problem. The
constraint $n\le 1000$ makes sorting comfortably fast enough for every legal
LeetCode input, while the proof and implementation remain short and direct.
The Optimal tab is available when the best expected asymptotic bound is
explicitly requested.

## Alternatives and edge cases

- **Endpoint arithmetic plus a hash set:** This is the Optimal branch. It achieves $O(n)$ expected time, but requires careful divisibility, duplicate, and zero-span reasoning.
- **In-place sorting:** Sorting `arr` itself avoids the separate copy, but mutates the caller's input and does not match the app-local contract.
- **Linear membership in the original array:** Searching the list separately for each forced term is correct but can take $O(n^2)$ time.
- **Two elements:** Any pair forms an arithmetic progression because it has only one adjacent difference.
- **All values equal:** Every sorted adjacent difference is zero, so the scan accepts.
- **Duplicates with a nonzero span:** At least one sorted gap is zero while another is nonzero, so the scan rejects.
- **Descending input:** The original order is irrelevant because the method checks a sorted copy.
