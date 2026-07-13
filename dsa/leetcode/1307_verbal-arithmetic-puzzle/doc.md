# Verbal Arithmetic Puzzle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1307 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, String, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [verbal-arithmetic-puzzle](https://leetcode.com/problems/verbal-arithmetic-puzzle/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/verbal-arithmetic-puzzle/).

### Goal
Assign a distinct digit to every letter so that the sum of the word numbers equals the result number. No multi-letter number may start with zero.

### Function Contract
**Inputs**

- `words`: addend words.
- `result`: target sum word.

**Return value**

`true` if a valid digit assignment exists, otherwise `false`.

### Examples
**Example 1**

- Input: `words = ["SEND","MORE"]`, `result = "MONEY"`
- Output: `true`

**Example 2**

- Input: `words = ["SIX","SEVEN","SEVEN"]`, `result = "TWENTY"`
- Output: `true`

**Example 3**

- Input: `words = ["LEET","CODE"]`, `result = "POINT"`
- Output: `false`

---

## Solution
### Approach
Column-wise backtracking with carry propagation.

### Complexity Analysis
- **Time Complexity**: Exponential in the number of distinct letters, bounded by `10!` assignments.
- **Space Complexity**: `O(U)` for `U` unique letters plus recursion depth.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(words, result):
    words = words[:]
    max_len = max(map(len, words + [result]))
    leading = {word[0] for word in words + [result] if len(word) > 1}
    assignment = {}
    used = [False] * 10

    def dfs(pos, row, carry):
        if pos == max_len:
            return carry == 0

        if row == len(words):
            ch = result[-1 - pos] if pos < len(result) else None
            digit = carry % 10
            next_carry = carry // 10
            if ch is None:
                return digit == 0 and dfs(pos + 1, 0, next_carry)
            if ch in assignment:
                return assignment[ch] == digit and dfs(pos + 1, 0, next_carry)
            if used[digit] or (digit == 0 and ch in leading):
                return False
            assignment[ch] = digit
            used[digit] = True
            if dfs(pos + 1, 0, next_carry):
                return True
            used[digit] = False
            del assignment[ch]
            return False

        word = words[row]
        if pos >= len(word):
            return dfs(pos, row + 1, carry)
        ch = word[-1 - pos]
        if ch in assignment:
            return dfs(pos, row + 1, carry + assignment[ch])
        for digit in range(10):
            if used[digit] or (digit == 0 and ch in leading):
                continue
            assignment[ch] = digit
            used[digit] = True
            if dfs(pos, row + 1, carry + digit):
                return True
            used[digit] = False
            del assignment[ch]
        return False

    if len(result) < max(map(len, words)) or len(set("".join(words) + result)) > 10:
        return False
    return dfs(0, 0, 0)
```
</details>
