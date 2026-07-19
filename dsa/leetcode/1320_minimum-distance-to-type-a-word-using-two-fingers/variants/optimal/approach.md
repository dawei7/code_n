## General
**Exploit the finger that typed the previous character**

After a prefix has been typed, at least one finger is on its final character. Call that the active finger. A state needs only the location of the other finger; its 26 possible keys plus one special `unplaced` position form a constant-size table. Store the minimum cost for each such state.

Initially, the active finger is placed on `word[0]` for free and the other finger is unplaced. To type the next target key, each state has two transitions. Moving the active finger from the previous character to the target preserves the other location and adds their Manhattan distance. Moving the other finger to the target makes the previous active location become the new other location; that move costs 0 if the other finger was still unplaced.

These two transitions cover which finger types the next character. Keeping the cheaper cost whenever transitions reach the same state discards no optimal continuation, because future costs depend only on the two current locations. Induction over the typed prefix therefore gives the minimum cost in every state, and the smallest final state cost is the answer.

## Complexity detail
Each of the $n-1$ transitions scans 27 states and performs constant work, so the time is $O(27n)=O(n)$. Two 27-element tables are sufficient, which is $O(27)=O(1)$ auxiliary space because the alphabet is fixed.

## Alternatives and edge cases
- **Three-dimensional dynamic programming:** Tracking both finger locations and the prefix index is direct but uses $O(26^2n)$ state storage; one finger's position is already determined by the last typed character.
- **Recursive assignment without memoization:** Trying both fingers for every letter is exact but takes $O(2^n)$ time.
- **Free initial placement:** The first use of either unplaced finger contributes zero distance, regardless of the key.
- **Repeated letters:** Pressing the same key again with the same finger costs 0.
- **Two-character word:** Each finger can start on one character, so the minimum is always 0.
- **Partial final row:** Coordinates still follow `index // 6` and `index % 6`; `Y` and `Z` occupy only the first two columns of row 4.
