## Examples

**Example 1**

- Input: `width = 3, height = 3, sideLength = 2, maxOnes = 1`
- Output: `4`
- Explanation: No `2 * 2` submatrix of a `3 * 3` matrix may contain more than one `1`. The following construction attains the optimal total of four:

    [1,0,1]
    [0,0,0]
    [1,0,1]

**Example 2**

- Input: `width = 3, height = 3, sideLength = 2, maxOnes = 2`
- Output: `6`
- Explanation: The following construction contains six ones while every `2 * 2` submatrix contains at most two:

    [1,0,1]
    [1,0,1]
    [1,0,1]
