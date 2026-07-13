# Reverse Words in a String II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 186 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-words-in-a-string-ii/) |

## Problem Description
### Goal
Given a mutable array of characters containing words separated by exactly one space, reverse the order of the words. The input has no leading or trailing spaces, and each word is a contiguous sequence of non-space characters.

Modify the supplied character array in place so the last original word becomes first and the first becomes last, while every word's internal spelling remains unchanged. Keep exactly one separator between adjacent words and preserve the array's total length. Return nothing and do not allocate another character array to hold the rearranged result. An input containing one word remains unchanged.

### Function Contract
**Inputs**

- `s`: a character list containing words separated by single spaces, with no leading or trailing space

**Return value**

Return nothing. Mutate `s` in place so its words appear in reverse order while every word's spelling remains unchanged.

### Examples
**Example 1**

- Input: characters of `"the sky is blue"`
- Mutated value: characters of `"blue is sky the"`

**Example 2**

- Input: `['a']`
- Mutated value: `['a']`

**Example 3**

- Input: characters of `"hello world"`
- Mutated value: characters of `"world hello"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

The in-place constraint rules out splitting into a list of words. Instead, use two layers of reversal.

First reverse the entire character array. This places the words in the desired order, but each word is spelled backward. For example,

`"the sky is blue" -> "eulb si yks eht"`.

Now scan the reversed array for maximal ranges of non-space characters. Reverse each such range in place:

`"eulb" -> "blue"`, `"si" -> "is"`, `"yks" -> "sky"`, and `"eht" -> "the"`.

The spaces remain separators throughout, so no character has to be inserted or removed. Treat the end of the array like a delimiter to ensure the final word is processed even though no trailing space exists.

The reason the transformation composes correctly is that reversing the whole sequence changes both the order of word blocks and the direction inside each block. The local reversals undo only the second effect; they cannot move a word across a separator, so the reversed block order remains.

After the whole-array reversal, the word blocks occur in reverse original order, and every block's characters occur in reverse order. Reversing each maximal non-space block restores that word's original spelling without changing its position among the blocks. Once every block has been restored, the array contains exactly the original words in reverse order. All operations are swaps within the original array, so the mutation is in place.

#### Complexity detail

The first reversal touches each character at most once. The second phase scans the array once and each character participates in at most one word-range reversal, so total time is $O(n)$. Only indices and a temporary swap value are stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- Splitting, reversing the word list, and joining is concise but allocates $O(n)$ additional storage and does not satisfy the in-place requirement.
- Moving complete words to their final positions by repeated shifts can degrade to $O(n^2)$ time.
- A stack of words remains linear but also uses $O(n)$ extra space.
- A one-character or one-word input returns to its original spelling after the two reversals.
- The contract guarantees single separators with no leading or trailing spaces; a more permissive whitespace contract would need decisions about preserving or normalizing runs.

</details>
