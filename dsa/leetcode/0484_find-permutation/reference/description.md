## Description

A permutation `perm` of `n` integers of all the integers in the range `[1, n]` can be represented as a string `s` of length $n - 1$ where:

- $s[i] = 'I'$ if $\text{perm}[i] < perm[i + 1]$, and

- $s[i] = 'D'$ if $\text{perm}[i] > perm[i + 1]$.

Given a string `s`, reconstruct the lexicographically smallest permutation `perm` and return it.
### Function Contract

**Inputs**

- `s`: a nonempty pattern whose characters are `"I"` or `"D"`

**Return value**

- Return the lexicographically smallest permutation of the integers from $1$ through $\lvert \texttt{s} \rvert + 1$
  whose adjacent comparisons match `s`.

The result has length $\lvert \texttt{s} \rvert + 1$ and uses every integer in that range exactly once.

### Examples

#### Example 1

- **Input:** `s = "I"`
- **Output:** `[1,2]`
- **Explanation:** [1,2] is the only legal permutation that can represented by s, where the number 1 and 2 construct an increasing relationship.
#### Example 2

- **Input:** `s = "DI"`
- **Output:** `[2,1,3]`
- **Explanation:** Both [2,1,3] and [3,1,2] can be represented as "DI", but since we want to find the smallest lexicographical permutation, you should return [2,1,3]
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- $s[i]$ is either `'I'` or `'D'`.