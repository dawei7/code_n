## General

Fix every possible left endpoint. While extending the right endpoint one position at a time, maintain separate hash sets for the distinct even and distinct odd values in that current subarray. Adding the new value updates exactly one set; comparing their sizes then reveals whether the current subarray is balanced.

Whenever the two sizes match, use the endpoint distance to update the longest length. For a fixed left endpoint, the sets contain precisely the distinct values in every successively extended subarray. Since every pair of endpoints is visited, every possible non-empty subarray is tested. Therefore the largest recorded balanced length is the requested answer.

Duplicates need no special counter: inserting the same value into a set again leaves its distinct count unchanged, which is exactly the source definition.

## Complexity detail

Let $n$ be `nums.length`. There are $O(n^2)$ endpoint pairs, and each expected hash-set insertion and size comparison is $O(1)$, for $O(n^2)$ expected time. The two sets can together hold $O(n)$ distinct values, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Rebuild sets for every subarray:** Computing both distinct sets from scratch for every endpoint pair is correct but costs $O(n^3)$ expected time.
- **Compare parity frequencies:** Equal numbers of even and odd elements do not imply equal numbers of distinct even and odd values when duplicates occur.
- **One-element array:** Its only subarray has one distinct value of one parity and zero of the other, so the answer is `0`.
- **No balanced subarray:** Keeping the initial result `0` represents this case.
- **Repeated values:** Repetition can lengthen a balanced subarray without changing either distinct count.
- **Whole array versus interior:** The best subarray may be the entire input or a proper contiguous segment, as the examples demonstrate.
