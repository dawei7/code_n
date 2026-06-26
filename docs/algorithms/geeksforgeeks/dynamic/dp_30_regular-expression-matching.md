# Regular Expression Matching

| | |
|---|---|
| **ID** | `dp_30` |
| **Category** | dynamic |
| **Complexity (required)** | $O(M * N)$ Time, $O(M * N)$ Space |
| **Difficulty** | 9/10 |
| **Interview relevance** | 5/10 |
| **LeetCode Equivalent** | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) |

## Problem statement

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*` where:
- `.` Matches any single character.
- `*` Matches zero or more of the **preceding** element.
The matching should cover the entire input string (not partial).

**Input:** Two strings `s` and `p`.
**Output:** A boolean: `True` if `s` matches `p`, otherwise `False`.

## When to use it

- To showcase advanced string DP handling where the state transition looks BACKWARDS more than 1 step due to variable-length modifiers (like `*`).
- *Note:* Do not confuse this with Wildcard Matching (`dp_09`), where `*` matches *any sequence*. Here, `a*` specifically means zero or more `a`s!

## Approach

**1. Define the State:**
Let `dp[i][j]` be a boolean indicating whether the prefix `s[0...i-1]` matches the pattern prefix `p[0...j-1]`.

**2. Find the Base Cases:**
- `dp[0][0] = True`: Empty string matches empty pattern.
- `dp[i][0] = False`: Non-empty string NEVER matches an empty pattern.
- `dp[0][j]`: Empty string CAN match a non-empty pattern, but ONLY if the pattern is a sequence of optional characters (e.g., `a*b*c*`).
  For an empty string to match `p[0...j-1]`, the last character MUST be `*`, and if we ignore that `*` and its preceding character, the rest of the pattern must ALSO match the empty string!
  `dp[0][j] = dp[0][j-2]` (if `p[j-1] == '*'`).

**3. Find the Transition (The recurrence relation):**
We compare the current character `s[i-1]` and `p[j-1]`.
- **Case A (Direct Match):**
  If `p[j-1]` is a normal character and `p[j-1] == s[i-1]`, or if `p[j-1] == '.'`, it's a 1-to-1 match!
  The strings match if their remaining prefixes match.
  `dp[i][j] = dp[i-1][j-1]`
- **Case B (The tricky `*`):**
  If `p[j-1] == '*'`, we look at the character *preceding* the star: `p[j-2]`.
  We have two distinct choices to make the `*` valid:
  1. **Zero Occurrences (Ignore it):** We simply throw away the `*` and its preceding character.
     `dp[i][j] = dp[i][j-2]`
  2. **One or More Occurrences (Use it):** We can only use it IF the preceding character `p[j-2]` actually matches `s[i-1]` (or is a `.`). If it matches, we "consume" `s[i-1]`, but we KEEP the `*` active in the pattern so it can consume more characters!
     `dp[i][j] = dp[i-1][j]` (Only valid if `p[j-2] == s[i-1]` or `p[j-2] == '.'`)

  Since either choice is valid, we take the boolean `OR`!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_30: Coin Change (Count Ways).

dp[a] = number of ways to make a. For each coin c, walk
forward: dp[a] += dp[a - c].
"""


def solve(coins, n, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]
```

</details>

## Walk-through

`s = "aab"`, `p = "c*a*b"`. M=3, N=5.
Base Cases (i=0): `dp[0][0]=T`.
`j=2 ('*')`: `dp[0][2] = dp[0][0] = T` ("c*").
`j=4 ('*')`: `dp[0][4] = dp[0][2] = T` ("c*a*").

1. **i = 1 ('a'):**
   - `j=1 ('c')`: False.
   - `j=2 ('*')`: Zero occurrences (`dp[1][0]=F`).
   - `j=3 ('a')`: Direct match. `dp[1][3] = dp[0][2] = T`.
   - `j=4 ('*')`: Zero occurrences (`dp[1][2]=F`) OR Use it (`p[j-2]=='a' == s[i-1]`, so `dp[0][4]=T`). `dp[1][4] = T`.
2. **i = 2 ('a'):**
   - `j=4 ('*')`: Zero occurrences (`dp[2][2]=F`) OR Use it (`p[j-2]=='a' == s[i-1]`, so `dp[1][4]=T`). `dp[2][4] = T`.
3. **i = 3 ('b'):**
   - `j=4 ('*')`: Zero occurrences (`dp[3][2]=F`). Use it fails (`'a' != 'b'`). False.
   - `j=5 ('b')`: Direct match. `dp[3][5] = dp[2][4] = T`!

Result `dp[3][5]` is `True`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(M * N)$ | $O(M * N)$ |
| **Average** | $O(M * N)$ | $O(M * N)$ |
| **Worst** | $O(M * N)$ | $O(M * N)$ |

The nested loops unconditionally execute exactly M x N times. Time complexity is strictly $O(M \times N)$.
Space complexity is $O(M \times N)$ for the DP matrix. It can technically be reduced to $O(N)$ with a 1D rolling array, but because `*` requires looking back at `j-2`, the state management becomes highly error-prone in an interview setting. The 2D matrix is vastly preferred for clarity.

## Variants & optimizations

- **Top-Down Memoization:** Many find the recursive approach `is_match(i, j)` more intuitive because the branching (use `*` vs ignore `*`) visually maps perfectly to recursive calls, and you avoid building the empty-string base case loop.
- **NFA (Non-deterministic Finite Automata):** The mathematically pure way to solve this in industry (like the `re` module in Python or `grep` in Linux) is to compile the pattern `p` into a state-machine graph (NFA), and then traverse the graph with string `s`. It handles much more complex regex features without DP arrays!

## Real-world applications

- **Compilers & Lexers:** The foundation of tokenizing source code strings into discrete grammatical symbols based on RegEx syntax rules.

## Related algorithms in cOde(n)

- **[dp_09 - Wildcard Matching](dp_09_wildcard-matching.md)** — The simpler cousin where `*` matches any sequence unconditionally, rather than tying itself to the preceding character.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
