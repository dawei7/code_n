### 1. Description

You are given an undirected tree with `n` nodes labeled 0 to $n - 1$. This is represented by a 2D array `edges` of length $n - 1$, where $\text{edges}[i] = [u_{i}, v_{i}]$ indicates an undirected edge between nodes $u_{i}$ and $v_{i}$.

You are also given a string `s` of length `n` consisting of lowercase English letters, where $s[i]$ represents the character assigned to node `i`.

You are also given a string array `queries`, where each $\text{queries}[i]$ is either:

- $"update u_{i} c"$: Change the character at node $u_{i}$ to `c`. Formally, update $s[u_{i}] = c$.

- $"query u_{i} v_{i}"$: Determine whether the string formed by the characters on the **unique** path from $u_{i}$ to $v_{i}$ (inclusive) can be **rearranged** into a **palindrome**.

Return a boolean array `answer`, where $\text{answer}[j]$ is `true` if the $$j^{\text{th}}$$ query of type $"query u_{i} v_{i}"​​​​​​​$ can be rearranged into a **palindrome**, and `false` otherwise.

### 2. Function Contract

**Inputs**

- `n`: The number of labeled tree nodes.
- `edges`: The undirected edges of the tree.
- `s`: The initial lowercase character at every node.
- `queries`: The ordered update and path-query command strings.

Let $T=(V,E)$ be the tree with $V=\{0,\ldots,n-1\}$. For nodes $u$ and $v$, let $P(u,v)$ be the unique inclusive path between them. Operations are stateful: an `update` replaces one node's current character but produces no output, while a `query` observes every update that precedes it.

A multiset of letters can be rearranged into a palindrome exactly when at most one letter has an odd frequency. Therefore, a path query returns `true` precisely when

$$
\left\lvert
\left\{c\in\{\texttt{a},\ldots,\texttt{z}\}
\mid \operatorname{count}_{P(u,v)}(c)\equiv 1\pmod 2\right\}
\right\rvert \le 1.
$$

**Return value**

Return the query results in chronological order. The returned array has one boolean for each command beginning with `"query"` and no entry for an `"update"` command.

### 3. Examples

#### Example 1

- **Input:** n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]

- **Output:** [true,false]

- **Explanation:** 

- `"query 0 2"`: Path `0 → 1 → 2` gives `"aac"`, which can be rearranged to form `"aca"`, a palindrome. Thus, $\text{answer}[0] = true$.

- `"update 1 b"`: Update node 1 to `'b'`, now `s = "abc"`.

- `"query 0 2"`: Path characters are `"abc"`, which cannot be rearranged to form a palindrome. Thus, $\text{answer}[1] = false$.

Thus, $answer = [true, false]$.

#### Example 2

- **Input:** n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]

- **Output:** [false,false,true]

- **Explanation:** 

- `"query 1 2"`: Path `1 → 0 → 2` gives `"bac"`, which cannot be rearranged to form a palindrome. Thus, $\text{answer}[0] = false$.

- `"update 0 b"`: Update node 0 to `'b'`, now `s = "bbca"`.

- `"query 2 3"`: Path `2 → 0 → 3` gives `"cba"`, which cannot be rearranged to form a palindrome. Thus, $\text{answer}[1] = false$.

- `"update 3 a"`: Update node 3 to `'a'`, `s = "bbca"`.

- `"query 1 3"`: Path `1 → 0 → 3` gives `"bba"`, which can be rearranged to form `"bab"`, a palindrome. Thus, $\text{answer}[2] = true$.

Thus, $answer = [false, false, true]$.

### 4. Constraints

- $1 \le n = \text{s.length} \le 5 * 10^{4}$

- $\text{edges.length} = n - 1$

- $\text{edges}[i] = [u_{i}, v_{i}]$

- $0 \le u_{i}, v_{i} \le n - 1$

- `s` consists of lowercase English letters.

- The input is generated such that `edges` represents a valid tree.

- $1 \le \text{queries.length} \le 5 * 10^{4}$​​​​​​​

		- $\text{queries}[i] = "update u_{i} c"$ or

- $\text{queries}[i] = "query u_{i} v_{i}"$

- $0 \le u_{i}, v_{i} \le n - 1$

- `c` is a lowercase English letter.
