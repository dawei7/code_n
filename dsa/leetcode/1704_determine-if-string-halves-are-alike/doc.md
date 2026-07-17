# Determine if String Halves Are Alike

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1704 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/determine-if-string-halves-are-alike/) |

## Problem Description
### Goal

You are given an even-length string `s` containing uppercase and lowercase English letters. Split it exactly in the middle: `a` is the first half and `b` is the second half, so both halves contain the same number of characters.

Two strings are considered alike when they contain the same number of vowels. The vowels are `a`, `e`, `i`, `o`, and `u` in either letter case; repeated occurrences are counted separately. Return whether the two fixed halves of `s` are alike.

### Function Contract
**Inputs**

- `s`: an even-length string of uppercase and lowercase English letters
- Its length $n$ satisfies $2 \le n \le 1000$.

**Return value**

`True` when `s[:n // 2]` and `s[n // 2:]` contain equal numbers of vowels, and `False` otherwise.

### Examples
**Example 1**

- Input: `s = "book"`
- Output: `True`

The halves `bo` and `ok` each contain one vowel.

**Example 2**

- Input: `s = "textbook"`
- Output: `False`

The first half `text` contains one vowel, while `book` contains two occurrences of `o`.

**Example 3**

- Input: `s = "AAee"`
- Output: `True`

Uppercase vowels count as vowels, so both halves contain two.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Represent the comparison as one balance**

Store the ten valid vowel characters in a fixed membership set. Let `middle = len(s) // 2` and initialize `balance` to zero. Scan the string once. For every vowel in the first half, increment the balance; for every vowel in the second half, decrement it. Consonants do not affect either count.

After any processed prefix, `balance` equals the number of first-half vowels seen minus the number of second-half vowels seen. Once the entire string has been inspected, that difference is zero exactly when the two vowel counts are equal. Returning whether `balance == 0` therefore implements the definition directly without creating substring copies.

**Preserve case coverage without normalizing the input**

The fixed set contains both uppercase and lowercase forms, so membership recognizes every specified vowel while leaving consonants unchanged. This avoids allocating a lowercase copy and ensures that repeated vowels, including repeated copies of the same letter, each contribute once.

#### Complexity detail

The scan examines all $n$ characters once, taking $O(n)$ time. The vowel set has a fixed size of ten and the algorithm stores only a midpoint and counter, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Count two slices separately:** counting vowels in `s[:middle]` and `s[middle:]` is also linear, but substring creation uses additional space in languages with copying slices.
- **Lowercase the whole string:** normalization simplifies membership but may allocate an $O(n)$ copy; listing both cases keeps auxiliary space constant.
- **Repeated `count` calls:** summing counts for each vowel is correct and still linear because the vowel alphabet is fixed, but it scans each half several times.
- **No vowels:** both counts are zero, so the halves are alike.
- **Repeated vowels:** every occurrence counts; do not compare distinct vowel sets.
- **Uppercase letters:** `A`, `E`, `I`, `O`, and `U` must be recognized alongside lowercase forms.
- **Minimum length:** two characters form one-character halves and are compared by the same balance rule.
- **Fixed split:** the only permitted halves are the two equal substrings divided at the midpoint.

</details>
