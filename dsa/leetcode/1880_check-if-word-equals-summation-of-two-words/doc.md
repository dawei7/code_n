# Check if Word Equals Summation of Two Words

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/) |
| Frontend ID | 1880 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Assign each letter its zero-based alphabet position: `'a'` is digit `0`, `'b'` is `1`, through `'j'` as `9`. The numerical value of a word is formed by concatenating those digits in letter order and interpreting the resulting digit string as an integer. Leading zero digits therefore do not affect the integer value; for example, `"acb"` becomes `"021"`, then $21$.

Given `firstWord`, `secondWord`, and `targetWord`, determine whether the numerical values of the first two words add exactly to the numerical value of the target.

### Function Contract

**Inputs**

- `firstWord`, `secondWord`, `targetWord`: nonempty strings of length at most $8$, containing only letters from `'a'` through `'j'`.

**Return value**

- Return `true` exactly when `value(firstWord) + value(secondWord) = value(targetWord)`; otherwise return `false`.

### Examples

**Example 1**

- Input: `firstWord = "acb", secondWord = "cba", targetWord = "cdb"`
- Output: `true`

The values are $21$, $210$, and $231$.

**Example 2**

- Input: `firstWord = "aaa", secondWord = "a", targetWord = "aab"`
- Output: `false`

The comparison is $0+0\ne1$.

**Example 3**

- Input: `firstWord = "aaa", secondWord = "a", targetWord = "aaaa"`
- Output: `true`

All three words have numerical value zero.

### Required Complexity

- **Time:** $O(S)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Read each word as a decimal number**

Let $S$ be the total number of characters across the three words. Convert a word from left to right. If the accumulated prefix has value $v$ and the next letter represents digit $d$, the extended prefix has value $10v+d$. This is ordinary decimal place-value evaluation and naturally discards leading zeros.

**Compare the three values**

Apply the conversion independently to the two addends and the target, then test their integer equality after addition. Every character contributes its exact prescribed digit once, so induction over the word length shows the conversion equals the stated concatenation. The final Boolean comparison is therefore true exactly for the required equation.

#### Complexity detail

Each of the $S$ characters is processed once, giving $O(S)$ time. The conversion keeps only three integers plus loop variables, so it uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Build digit strings:** Joining mapped digits and parsing them is correct but allocates $O(S)$ temporary space.
- **Repeated place-value powers:** Computing a fresh power of ten for every character is correct but costs $O(S^2)$ time.
- **Leading `'a'` letters:** They represent leading zeros and do not change a word's integer value.
- **All `'a'` letters:** Words of different lengths can all represent zero.
- **Carry between addends:** Compare integer values; digitwise concatenation alone is not addition.
- **Single letters:** They map directly to digits from $0$ through $9$.

</details>
