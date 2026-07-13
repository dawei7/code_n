# Detect Capital

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 520 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/detect-capital/) |

## Problem Description
### Goal
Given a nonempty English word, its use of capitals is correct in exactly three forms: every letter is uppercase, every letter is lowercase, or only the first letter is uppercase while all later letters are lowercase.

Return `True` when the complete word matches one of those forms and `False` otherwise. A one-letter word is valid whether its sole letter is uppercase or lowercase. Mixed patterns such as a lowercase first letter followed by an uppercase letter, or several capitals after the first position, do not qualify; the function does not modify the word's spelling.

### Function Contract
**Inputs**

- `word`: a nonempty string of English letters

**Return value**

- `True` when the capitalization matches an accepted form; otherwise `False`

### Examples
**Example 1**

- Input: `word = "USA"`
- Output: `True`

**Example 2**

- Input: `word = "FlaG"`
- Output: `False`

**Example 3**

- Input: `word = "Google"`
- Output: `True`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count uppercase letters once**

Scan the word and count characters classified as uppercase. The all-uppercase form has count `n`; the all-lowercase form has count zero.

**Identify the one-capital form precisely**

When the count is one, the word is valid only if `word[0]` is uppercase. This distinguishes a title-style word such as `"Google"` from an interior capital such as `"gOogle"`.

**Why the three tests are exhaustive**

The accepted patterns contain respectively `n`, zero, or one uppercase character. In the one-character case, the stated position condition is both necessary and sufficient. Every other uppercase count, or a lone uppercase letter away from index zero, violates all three patterns.

#### Complexity detail

The scan examines each of `n` characters once, giving $O(n)$ time. The counter and length use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Built-in case predicates:** `isupper`, `islower`, and title-case checks express the three patterns concisely and still take linear time.
- **Regular expression:** can match the accepted forms but adds pattern-engine machinery to a simple scan.
- **Repeatedly recount capitals:** remains correct but can take $O(n^2)$ time.
- **One uppercase letter:** is valid as the all-uppercase form.
- **One lowercase letter:** is valid as the all-lowercase form.
- **Interior capital:** invalidates an otherwise lowercase word.
- **First capital plus later capital:** is neither title style nor all uppercase when lowercase letters also occur.

</details>
