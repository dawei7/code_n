# Minimum Length of String After Deleting Similar Ends

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1750 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/) |

## Problem Description

### Goal

You are given a string `s` containing only `a`, `b`, and `c`. In one operation, choose a nonempty prefix whose characters are all equal and a nonempty suffix whose characters are all equal. The two chosen parts must contain the same character and must not overlap at any index.

Delete both chosen parts simultaneously. You may repeat this operation any number of times, including zero. Return the minimum length that can remain. Prefix and suffix lengths are chosen independently, so equal boundary runs do not need to have the same size, but neither side may consume a character also selected by the other.

### Function Contract

**Inputs**

- `s`: a nonempty string over the alphabet `{a, b, c}`, with $1 \le \lvert s\rvert \le 10^5$.

Let $n=\lvert s\rvert$.

**Return value**

- Return the smallest possible length after repeatedly deleting legal equal-character prefix and suffix pairs.

### Examples

**Example 1**

- Input: `s = "ca"`
- Output: `2`
- Explanation: The endpoint characters differ, so no operation is available.

**Example 2**

- Input: `s = "cabaabac"`
- Output: `0`
- Explanation: Successive matching boundary runs can remove `c`, then `a`, then `b`, and finally the remaining `a` characters.

**Example 3**

- Input: `s = "aabccabba"`
- Output: `3`
- Explanation: Removing the outer `a` runs and then the outer `b` runs leaves `"cca"`, whose endpoints differ.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Only matching endpoint characters permit progress**

At any stage, every legal prefix begins with the current leftmost character and every legal suffix ends with the current rightmost character. If those characters differ, no pair can satisfy the same-character rule, so the current length is already minimal.

**Discard both complete boundary runs**

When the endpoints share character $c$, advance the left pointer past every consecutive $c$ and retreat the right pointer past every consecutive $c$. Removing less cannot produce a better outcome: any surviving boundary $c$ still has to be paired with $c$ from the other side before a different inner character can become exposed. Therefore an optimal sequence may remove both maximal boundary runs immediately.

**Stop safely when the pointers meet or cross**

Repeat while at least two characters remain and the endpoint characters match. Each pointer moves only inward. If the runs consume the entire remaining interval, the pointers cross and the result is zero; if one character remains, its length is one because nonempty prefix and suffix selections may not overlap. Otherwise, differing endpoints prove that no further operation exists.

#### Complexity detail

Each character is passed by the left or right pointer at most once, so the total time is $O(n)$. The algorithm keeps only two indices and the current removable character, using $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Repeated string slicing:** Applying the same maximal-run logic by constructing a new substring after every operation is correct, but nested boundary layers can make the copied work $O(n^2)$.
- **Run-length encoding:** Compressing the string into character-count runs makes the boundary process explicit, but uses $O(n)$ additional space in the worst case.
- **Different endpoints initially:** Zero operations are possible, so the original length remains.
- **One character:** Prefix and suffix cannot be disjoint, leaving length one.
- **Uniform string:** Equal boundary runs consume the entire string, leaving zero.
- **Unequal run sizes:** Remove each complete boundary run independently; their lengths need not match.
- **Pointers meet:** The remaining middle character cannot be selected by both sides and therefore survives.
- **Pointers cross:** The final pair of runs was disjoint before deletion, so an empty result is legal.

</details>
