## General

**Represent every key by its coordinate**

The movement rule depends only on the two endpoints of each move. Build a fixed lookup from each lowercase letter to its row and column in the keyboard. The irregular row lengths are harmless: only actual keys enter the lookup, so unused cells can never become destinations.

**Accumulate consecutive Manhattan distances**

Initialize the current coordinate to the position of `a`, as required by the contract. Then scan `s` from left to right. For each character, obtain its coordinate, add the absolute row difference and the absolute column difference from the current coordinate, and replace the current coordinate with the destination.

Each loop iteration accounts for exactly the movement used to type one character. Before the iteration for `s[i]`, the stored coordinate is the finger's position after typing the preceding prefix, or `a` when $i=0$. The added Manhattan distance is therefore precisely the cost of the next required move, and the coordinate update establishes the same fact for the following iteration. Summing these per-character costs returns the distance of the complete typing sequence.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$. Constructing the 26-entry position map is constant work, and the scan performs constant work for each character, so the total time is $O(N)$. The map has exactly 26 entries and no storage grows with $N$, giving $O(1)$ auxiliary space.

The benchmark defines size as $N$ and alternates between distant keyboard positions. A one-pass implementation retains linear growth, while a correct prefix-recomputation control repeats all earlier movements for every endpoint and takes $O(N^2)$ time.

## Alternatives and edge cases

- **Arithmetic coordinate formulas:** A letter's location can be derived from its position in the three row strings instead of stored in a map. This still takes $O(N)$ time but makes the uneven row endings easier to mishandle.
- **Repeated prefix recomputation:** Recomputing the total for every prefix eventually obtains the correct full-string answer, but repeats earlier moves and requires $O(N^2)$ time.
- **Initial position:** The finger begins on `a`, not on the first character of `s`; omitting the first move is wrong unless `s[0]` is `a`.
- **Repeated characters:** Moving from a key to the same key costs zero, but the repeated character must still be processed so the current position remains well defined.
- **Uneven rows:** The absent cells after `l` and `m` do not change the column indices of existing keys.
- **Single-character input:** Even with one character, the answer is the distance from `a` to that character and is not always zero.
