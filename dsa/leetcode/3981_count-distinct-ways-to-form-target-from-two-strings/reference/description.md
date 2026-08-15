### 1. Description

You are given three strings `word1`, `word2`, and `target`.

Your task is to count the number of ways to form `target` by choosing characters from `word1` and `word2` under the following conditions:

- For each character of `target`, choose one matching character from either `word1` or `word2`.

- The chosen indices from `word1` must be **strictly** increasing.

- The chosen indices from `word2` must be **strictly** increasing.

- **At least** one character must be chosen from **both** `word1` and `word2`.

Two ways are considered different if, for **at least** one position in `target`, the chosen character comes from a different string or a different index.

Return the number of ways. Since the answer may be very large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

`solve(word1, word2, target) -> int`

Let $n = \lvert\texttt{word1}\rvert$, $m = \lvert\texttt{word2}\rvert$, and $t = \lvert\texttt{target}\rvert$. Define the state-volume measure

$P = tnm.$

**Inputs**

- `word1`: The first lowercase source string.
- `word2`: The second lowercase source string.
- `target`: The lowercase string to form by ordered selections.

The selected indices must increase separately within each source. There is no ordering comparison between an index in `word1` and an index in `word2`.

**Output**

Return, modulo $10^9+7$, the number of distinct constructions that use at least one character from each source word.

### 3. Examples

#### Example 1

- **Input:** word1 = "abc", word2 = "bac", target = "abc"

- **Output:** 5

- **Explanation:** There are 5 ways to form `target`:

- $\text{word1}[0] = 'a'$, $\text{word1}[1] = 'b'$, $\text{word2}[2] = 'c'$

- $\text{word1}[0] = 'a'$, $\text{word2}[0] = 'b'$, $\text{word1}[2] = 'c'$

- $\text{word1}[0] = 'a'$, $\text{word2}[0] = 'b'$, $\text{word2}[2] = 'c'$

- $\text{word2}[1] = 'a'$, $\text{word1}[1] = 'b'$, $\text{word1}[2] = 'c'$

- $\text{word2}[1] = 'a'$, $\text{word1}[1] = 'b'$, $\text{word2}[2] = 'c'$

All ways preserve the increasing index order inside each string and choose at least one character from each string.

#### Example 2

- **Input:** word1 = "cd", word2 = "cd", target = "ccd"

- **Output:** 4

- **Explanation:** There are 4 ways to form `target`:

- $\text{word1}[0] = 'c'$, $\text{word2}[0] = 'c'$, $\text{word1}[1] = 'd'$

- $\text{word1}[0] = 'c'$, $\text{word2}[0] = 'c'$, $\text{word2}[1] = 'd'$

- $\text{word2}[0] = 'c'$, $\text{word1}[0] = 'c'$, $\text{word1}[1] = 'd'$

- $\text{word2}[0] = 'c'$, $\text{word1}[0] = 'c'$, $\text{word2}[1] = 'd'$

The first two `'c'` characters in `target` must come one from each string. The final `'d'` can be chosen from either string.

#### Example 3

- **Input:** word1 = "xy", word2 = "xy", target = "xyxy"

- **Output:** 2

- **Explanation:** There are 2 ways to form `target`:

- $\text{word1}[0] = 'x'$, $\text{word1}[1] = 'y'$, $\text{word2}[0] = 'x'$, $\text{word2}[1] = 'y'$

- $\text{word2}[0] = 'x'$, $\text{word2}[1] = 'y'$, $\text{word1}[0] = 'x'$, $\text{word1}[1] = 'y'$

Each `"xy"` part in `target` comes entirely from one string.

#### Example 4

- **Input:** word1 = "ab", word2 = "cde", target = "ace"

- **Output:** 1

- **Explanation:** The only way is to choose $\text{word1}[0] = 'a'$, $\text{word2}[0] = 'c'$, and $\text{word2}[2] = 'e'$. Thus, the answer is 1.

### 4. Constraints

- $1 \le \text{word1.length}, \text{word2.length}, \text{target.length} \le 100$

- `word1`, `word2`, and `target` consist of lowercase English letters only.
