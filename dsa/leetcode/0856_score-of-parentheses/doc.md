# Score of Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 856 |
| Difficulty | Medium |
| Topics | String, Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/score-of-parentheses/) |

## Problem Description
### Goal
A balanced parentheses string receives a recursive score. The primitive string `"()"` has score $1$. Concatenating balanced strings adds their scores, so `AB` scores as the score of $A$ plus the score of $B$. Wrapping a balanced string doubles its score, so `(A)` scores twice the score of $A$.

Given a guaranteed balanced string `s` containing only `(` and `)`, evaluate and return its score under those rules.

### Function Contract
**Inputs**

- `s`: a balanced parentheses string of length $n$, where $2 \leq n \leq 50$.

**Return value**

Return the integer score obtained from the primitive, concatenation, and wrapping rules.

### Examples
**Example 1**

- Input: `s = "()"`
- Output: `1`

**Example 2**

- Input: `s = "(())"`
- Output: `2`

**Example 3**

- Input: `s = "()()"`
- Output: `2`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Decompose the score into primitive pairs**

Every balanced string can be viewed as primitive `()` pairs nested at various depths and concatenated together. A primitive pair at outer depth $0$ contributes $1$. Each surrounding pair doubles that contribution, so a primitive pair enclosed by $d$ other pairs contributes $2^d$.

For example, the only primitive pair in `"(())"` lies at depth $1$ and contributes $2$, while the two outer-depth primitives in `"()()"` each contribute $1$.

**Track depth while scanning**

Increase `depth` for an opening parenthesis. For a closing parenthesis, decrease it first; if the previous character was `(`, the two characters form a primitive pair, and the new depth is exactly its number of enclosing pairs. Add `1 << depth` to the score.

Non-primitive closing parentheses add nothing directly because their doubling effect is already present in the depth-weighted contributions of the primitive pairs inside them. Concatenation is also handled automatically by summing every primitive contribution. Thus the scan implements all three recursive score rules.

#### Complexity detail

The scan examines each of the $n$ characters once, taking $O(n)$ time. The running depth, score, and previous character use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Stack of partial scores:** Push the outer subtotal on `(`, then combine it with `max(2 * inner, 1)` on `)`; this takes $O(n)$ time and $O(n)$ space.
- **Recursive parsing:** Split top-level concatenations and recurse through wrappers; it mirrors the definition but substring scans and copies can take $O(n^2)$ time.
- **Rescan each primitive prefix:** Computing every primitive's depth from scratch is correct but quadratic.
- **Single primitive:** `"()"` is detected after depth returns to zero and contributes one.
- **Pure nesting:** Each extra wrapper doubles the sole primitive contribution.
- **Pure concatenation:** Every primitive appears at depth zero, so the score equals the number of pairs.
- **Mixed structure:** Only adjacent `()` pairs contribute directly; their depths encode all wrappers.
- **Balanced guarantee:** Depth never becomes negative and finishes at zero, so no validation path is required.
- **Maximum nesting:** With at most 25 pairs, the resulting power of two fits comfortably in the required integer range.

</details>
