## Description

You are given a string `s` and array `queries` where $\text{queries}[i] = [\text{left}_{i}, \text{right}_{i}, k_{i}]$. We may rearrange the substring $s[\text{left}_{i}...\text{right}_{i}]$ for each query and then choose up to $k_{i}$ of them to replace with any lowercase English letter.

If the substring is possible to be a palindrome string after the operations above, the result of the query is `true`. Otherwise, the result is `false`.

Return a boolean array `answer` where $\text{answer}[i]$ is the result of the $$i^{\text{th}}$$query$\text{queries}[i]$.

Note that each letter is counted individually for replacement, so if, for example $s[\text{left}_{i}...\text{right}_{i}] = "aaa"$, and $k_{i} = 2$, we can only replace two of the letters. Also, note that no query modifies the initial string `s`.

**Example :**

- **Input:** `s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]`
- **Output:** `[true,false,false,true,true]`
- **Explanation:**
queries[0]: substring = "d", is palidrome.
queries[1]: substring = "bc", is not palidrome.
queries[2]: substring = "abcd", is not palidrome after replacing only 1 character.
queries[3]: substring = "abcd", could be changed to "abba" which is palidrome. Also this can be changed to "baab" first rearrange it "bacd" then replace "cd" with "ab".
queries[4]: substring = "abcda", could be changed to "abcba" which is palidrome.
#### Example 2

- **Input:** `s = "lyb", queries = [[0,1,0],[2,2,1]]`
- **Output:** `[false,true]`
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Constraints

- $1 \le \text{s.length}, \text{queries.length} \le 10^{5}$

- $0 \le \text{left}_{i} \le \text{right}_{i} < \text{s.length}$

- $0 \le k_{i} \le \text{s.length}$

- `s` consists of lowercase English letters.