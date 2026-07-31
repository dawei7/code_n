## General

Each character is unique and appears in both strings, so it has exactly one position in `s` and exactly one position in `t`. The answer can be accumulated independently for each character.

Build a map from every character in `t` to its index. Then scan `s`; at index `i` with character `c`, add `abs(i - positions[c])`. Every required character contributes once, and the permutation guarantee means every lookup exists.

This sum is exactly the definition of permutation difference. No interaction between characters changes an individual displacement, so adding all mapped absolute differences produces the requested total.

## Complexity detail

Let $n$ be the common string length. Building the index map and scanning `s` each take $O(n)$ time, so the total is $O(n)$.

The map stores one entry per character, requiring $O(n)$ auxiliary space. The source domain caps $n$ at 26, but the bound states the data-structure growth directly.

## Alternatives and edge cases

- **Search `t` repeatedly:** Calling a linear index search for every character is concise but takes $O(n^2)$ time.
- **Fixed 26-entry array:** Converting letters to offsets avoids hashing and uses fixed space, while retaining the same $O(n)$ time.
- **Update signed positions in one joint scan:** Recording one string's index and subtracting the other can also work, but the explicit position map makes the absolute displacement clearer.
- A one-character permutation has difference zero.
- Identical strings produce zero because no character changes position.
- A reversed string and an end-to-end swap exercise the largest possible individual displacements.
- The strings contain no duplicates, so there is never an ambiguity about which occurrence to match.
