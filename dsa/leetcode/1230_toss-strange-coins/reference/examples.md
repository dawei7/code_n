## Examples

**Example 1**

- Input: `prob = [0.4], target = 1`
- Output: `0.40000`

**Example 2**

- Input: `prob = [0.5,0.5,0.5,0.5,0.5], target = 0`
- Output: `0.03125`

### Additional Examples

**Deterministic result**

- Input: `prob = [1.0,0.0,1.0], target = 2`
- Output: `1.0`

The two certain-head coins always produce exactly two heads, while the remaining coin always produces tails.

**Interior target with unequal probabilities**

- Input: `prob = [0.1,0.2,0.3,0.4], target = 2`
- Output: `0.2144`

Several different pairs of coins can supply the two heads, and their disjoint outcome probabilities add together.
