## Examples

**Example 1**

- Input: `balance = [-1, 2, -1]`
- Output: `2`
- **Explanation:** Transfer one unit from person `1` to person `0`, producing `[0, 1, -1]`. Then transfer one unit from person `1` to person `2`, producing `[0, 0, 0]`. This uses the minimum two moves.

**Example 2**

- Input: `balance = [4, -1, -2]`
- Output: `3`
- **Explanation:** Transfer one unit from person `0` to person `1`, giving `[3, 0, -2]`. Because indices `0` and `2` are also neighbors, transfer one unit from person `0` to person `2` twice. The intermediate state is `[2, 0, -1]`, and the final state is `[1, 0, 0]`. Three moves are sufficient and optimal.

**Example 3**

- Input: `balance = [-3, -3, 5]`
- Output: `-1`
- **Explanation:** The entries sum to $-1$, so the available positive balance cannot cover all deficits. Making every entry non-negative is impossible.
