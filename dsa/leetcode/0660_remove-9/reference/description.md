## Description

Start from integer `1`, remove any integer that contains `9` such as `9`, `19`, `29`...

Now, you will have a new integer sequence `[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...]`.

Given an integer `n`, return *the* $$n^{\text{th}}$$ (**1-indexed**) integer in the new sequence.
### Function Contract

`solve(n: int) -> int`

**Inputs**

- `n`: a one-based position in the increasing sequence of positive integers whose decimal representations do not contain `9`.

**Return value**

Return the positive integer at sequence position `n`. The returned integer must contain no decimal digit `9`.

### Examples
#### Example 1

- **Input:** $n = 9$
- **Output:** `10`
#### Example 2

- **Input:** $n = 10$
- **Output:** `11`
### Constraints

- $1 \le n \le 8 * 10^{8}$