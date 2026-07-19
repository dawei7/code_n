## General
**Generate only rotatable numbers:** Use depth-first search to append one digit from `0`, `1`, `6`, `8`, and `9`. Skip zero as the first digit, and stop a branch as soon as its numeric value would exceed `n`. This avoids inspecting integers that contain an invalid digit.

**Carry the rotation without rescanning digits:** Suppose the current number has $k$ digits, rotated value `rotated`, and place value `10 ** k`. Appending `digit` to the original number places its rotated mapping at the front, so update with `mapped_digit * place + rotated`. Then multiply `place` by 10 for descendants.

**Count only changed values:** Every generated positive candidate is valid under rotation. Increment the answer precisely when `candidate != rotated_candidate`, then continue extending it.

Every rotatable positive integer at most `n` has a unique sequence of valid digits and is reached by exactly one DFS path. The carried formula reverses that sequence while applying the required digit map, so the comparison classifies the candidate correctly. Invalid-digit integers are never generated and cannot contribute.

## Complexity detail
The search visits each of the $C$ valid-digit candidates once and performs constant work per edge, for $O(C)$ time. Its depth is at most $D$, so recursion uses $O(D)$ auxiliary space. The algorithm does not store all candidates.

## Alternatives and edge cases
- **Scan every integer:** Test each value from 1 through `n` digit by digit. It is correct but takes $O(nD)$ time and spends most work rejecting invalid digits.
- **Generate then rotate from text:** Enumerating only valid candidates remains efficient, but rebuilding a reversed mapped string adds an extra $O(D)$ factor per candidate.
- **Strobogrammatic subtraction:** Count all valid-digit numbers and subtract those unchanged by rotation. It can be efficient but requires careful bounded combinatorics.
- **Leading zero:** Never generate one; zero may appear only after a nonzero first digit.
- **Unchanged rotation:** Values such as 1, 8, 11, and 69 are valid but not confusing.
- **Digit 6 or 9:** Rotation swaps the two digits rather than preserving them.
- **Inclusive bound:** Count `n` itself when it is confusing.
