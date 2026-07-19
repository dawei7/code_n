## General
**Separate equality from actual mismatches**

Strings of different lengths cannot become equal through a swap. For equally long strings, scan paired characters once and record the indices where they differ. A single swap changes at most two positions, so more than two mismatches makes the transformation impossible. Exactly one mismatch is also impossible because exchanging two positions cannot repair just one changed position.

While scanning, track which of the 26 lowercase letters have appeared and whether any letter is duplicated. This information handles the case with no mismatches: because the operation must choose distinct indices, an unchanged result is possible exactly when two equal occurrences can be exchanged.

**Character crossings characterize two mismatches**

Suppose the only mismatching indices are `i` and `j`. Swapping them works precisely when `s[i] == goal[j]` and `s[j] == goal[i]`. These two crossed equalities are necessary because no other positions change, and they are sufficient because every position outside the pair already matches.

The scan therefore covers all possible cases: zero mismatches uses the duplicate flag, two mismatches uses the crossed comparison, and every other mismatch count returns `false`. No possible one-swap transformation is omitted.

## Complexity detail
The paired scan examines $n$ positions once, so it takes $O(n)$ time. The mismatch list is capped at two indices, and the seen-letter table has exactly 26 entries because the alphabet is fixed. Auxiliary space is therefore $O(1)$.

## Alternatives and edge cases
- **Try every pair of indices:** Performing each possible swap is correct, but there are $O(n^2)$ pairs and materializing each result can add another linear factor.
- **Sort both strings:** Equal sorted forms verify that the character multisets match, but they do not enforce that exactly one swap suffices and sorting costs $O(n\log n)$ time.
- **Frequency counting alone:** Matching counts is necessary but not sufficient; `"abcd"` and `"badc"` have the same counts yet require two swaps.
- **Different lengths:** A swap preserves length, so the answer is immediately `false`.
- **Already equal strings:** The answer is `true` only if some letter appears at least twice.
- **One-character strings:** Distinct swap indices do not exist, so the answer is `false`.
- **Exactly one mismatch:** A swap affects two positions and cannot repair only one.
- **More than two mismatches:** One exchange cannot change enough positions.
