# Reverse Only Letters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 917 |
| Difficulty | Easy |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-only-letters/) |

## Problem Description
### Goal

Given a string `s`, reverse the order of its English letters while preserving every other character at its original index. Both lowercase and uppercase English letters participate in the reversal, and their case travels with the character.

Characters that are not English letters must not move. Return the resulting string after the letters have been placed in reverse order around those fixed positions.

### Function Contract
**Inputs**

- `s`: a string of length $n$, where $1 \le n \le 100$.
- Every character has an ASCII value from $33$ through $122$. The string contains neither a double quote nor a backslash.

**Return value**

A string of the same length in which the subsequence of English letters is reversed and every non-letter remains at its original index.

### Examples
**Example 1**

- Input: `s = "ab-cd"`
- Output: `"dc-ba"`

**Example 2**

- Input: `s = "a-bC-dEf-ghIj"`
- Output: `"j-Ih-gfE-dCba"`

**Example 3**

- Input: `s = "Test1ng-Leet=code-Q!"`
- Output: `"Qedo1ct-eeLg=ntse-T!"`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Keep punctuation anchored with two pointers**

Convert the string to a mutable character list. Place one pointer at each end. If the left pointer is on a non-letter, advance it because that character must stay where it is. Likewise, move the right pointer leftward whenever it is on a non-letter.

When both pointers identify English letters, swap those characters and move both pointers inward. Each swap places the next letter from the original right end into the next available letter position on the left, and symmetrically places the left letter at the matching position from the right.

Non-letters are never assigned or swapped, so their indices remain unchanged. The letter positions are visited from the outside inward, pairing the first with the last, the second with the second-last, and so on; therefore the resulting letter subsequence is exactly the reverse of the original one.

#### Complexity detail

Let $n$ be the length of `s`. Each pointer moves in only one direction and crosses each index at most once, so the runtime is $O(n)$. The mutable character list and returned string require $O(n)$ space.

#### Alternatives and edge cases

- **Letter stack:** Collecting all letters and popping them while rebuilding the string is also $O(n)$ time and space, but stores the letter subsequence separately.
- **Rescan for every letter position:** Searching from the end again for each replacement letter is correct but takes $O(n^2)$ time.
- **All non-letters:** No swaps occur, and the original string is returned unchanged.
- **One or zero letters:** Reversing the letter subsequence has no visible effect.
- **Mixed case:** Uppercase and lowercase characters are letters and reverse by position without changing case.
- **Fixed symbols:** Digits, hyphens, equals signs, punctuation, and other non-letters stay at their exact original indices.

</details>
