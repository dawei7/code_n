### 1. Description

You are given an array of equal-length strings `words`. Assume that the length of each string is `n`.

Each string $\text{words}[i]$ can be converted into a **difference integer array** $\text{difference}[i]$ of length $n - 1$ where $\text{difference}[i][j] = \text{words}[i][j+1] - \text{words}[i][j]$ where $0 \le j \le n - 2$. Note that the difference between two letters is the difference between their **positions** in the alphabet i.e. the position of `'a'` is `0`, `'b'` is `1`, and `'z'` is `25`.

- For example, for the string `"acb"`, the difference integer array is `[2 - 0, 1 - 2] = [2, -1]`.

All the strings in words have the same difference integer array, **except one**. You should find that string.

Return* the string in *`words`* that has different **difference integer array**.*

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $words = ["adc","wzy","abc"]$
- **Output:** `"abc"`
- **Explanation:**
- The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
- The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
- The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1].
The odd array out is [1, 1], so we return the corresponding string, "abc".
#### Example 2

- **Input:** $words = ["aaa","bob","ccc","ddd"]$
- **Output:** `"bob"`
- **Explanation:** All the integer arrays are [0, 0] except for "bob", which corresponds to [13, -13].

### 4. Constraints

- $3 \le \text{words.length} \le 100$

- $n = \text{words}[i].length$

- $2 \le n \le 20$

- $\text{words}[i]$ consists of lowercase English letters.