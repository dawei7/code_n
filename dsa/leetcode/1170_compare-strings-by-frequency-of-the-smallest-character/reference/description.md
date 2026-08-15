### 1. Description

Let the function `f(s)` be the **frequency of the lexicographically smallest character** in a non-empty string `s`. For example, if `s = "dcce"` then $f(s) = 2$ because the lexicographically smallest character is `'c'`, which has a frequency of 2.

You are given an array of strings `words` and another array of query strings `queries`. For each query $\text{queries}[i]$, count the **number of words** in `words` such that $f(\text{queries}[i])$ < `f(W)` for each `W` in `words`.

Return *an integer array *`answer`*, where each *$\text{answer}[i]$* is the answer to the *$$i^{\text{th}}$$* query*.

### 2. Function Contract

**Inputs**

- `queries`: Input parameter (`List[str]`).
- `words`: Input parameter (`List[str]`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** $queries = ["cbd"], words = ["zaaaz"]$
- **Output:** `[1]`
- **Explanation:** On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").

#### Example 2

- **Input:** $queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]$
- **Output:** `[1,2]`
- **Explanation:** On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").

### 4. Constraints

- $1 \le \text{queries.length} \le 2000$

- $1 \le \text{words.length} \le 2000$

- $1 \le \text{queries}[i].length, \text{words}[i].length \le 10$

- $\text{queries}[i][j]$, $\text{words}[i][j]$ consist of lowercase English letters.
