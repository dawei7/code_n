### 1. Description

You are given a **0-indexed** array of strings `words` and a 2D array of integers `queries`.

Each query $\text{queries}[i] = [l_{i}, r_{i}]$ asks us to find the number of strings present at the indices ranging from $l_{i}$ to $r_{i}$ (both **inclusive**) of `words` that start and end with a vowel.

Return *an array *`ans`* of size *`queries.length`*, where *$\text{ans}[i]$* is the answer to the *`i`^th* query*.

### 2. Function Contract

**Inputs**

- `words`: Input parameter (`List[str]`).
- `queries`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `List[int]`.

### 3. Note

that the vowel letters are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

### 4. Examples

#### Example 1

- **Input:** $words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]$
- **Output:** `[2,3,0]`
- **Explanation:** The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].

#### Example 2

- **Input:** $words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]$
- **Output:** `[3,2,1]`
- **Explanation:** Every string satisfies the conditions, so we return [3,2,1].

### 5. Constraints

- $1 \le \text{words.length} \le 10^{5}$

- $1 \le \text{words}[i].length \le 40$

- $\text{words}[i]$ consists only of lowercase English letters.

- $sum(\text{words}[i].length) \le 3 * 10^{5}$

- $1 \le \text{queries.length} \le 10^{5}$

- $0 \le l_{i} \le r_{i} < \text{words.length}$
