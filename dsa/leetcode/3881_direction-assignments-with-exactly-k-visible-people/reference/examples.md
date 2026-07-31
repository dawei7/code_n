## Examples

**Example 1**

- Input: `n = 3, pos = 1, k = 0`
- Output: `2`
- Explanation:

  - Index `0` is left of `pos`, and index `2` is right of it.
  - To keep both invisible, index `0` must choose `R` and index `2` must choose `L`.
  - The observer at index `1` may choose either direction without changing the visible count, giving two assignments.

**Example 2**

- Input: `n = 3, pos = 2, k = 1`
- Output: `4`
- Explanation:

  - Indices `0` and `1` are both left of the observer, with nobody to its right.
  - Exactly one of those two indices must choose `L`, while the other chooses `R`.
  - Either index can be the visible one, giving two choices.
  - The observer also has two direction choices, so the two cases contribute `2 + 2 = 4` complete assignments.

**Example 3**

- Input: `n = 1, pos = 0, k = 0`
- Output: `2`
- Explanation:

  - No index lies to either side of the observer, so no additional visibility condition is needed.
  - The sole person may choose `L` or `R`, producing two assignments.
