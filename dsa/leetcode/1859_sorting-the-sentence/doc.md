# Sorting the Sentence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1859 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sorting-the-sentence/) |

## Problem Description
### Goal
A sentence consists of words separated by single spaces, with no space before
the first word or after the last. Each word contains only lowercase and
uppercase English letters. To shuffle such a sentence, append the word's
1-indexed original position to it, then rearrange the resulting marked words.

Given one shuffled sentence `s` containing at most nine words, restore the
original order. Remove the appended position digit from every word and return
the reconstructed words joined by single spaces.

### Function Contract
**Inputs**

- `s`: a shuffled sentence of length from $2$ through $200$. It contains one
  to nine space-separated marked words. Every marked word consists of English
  letters followed by its digit from `1` through `9`.

Let $S = \lvert s \rvert$ be the number of characters in the shuffled sentence.

**Return value**

The original sentence as a string, with position digits removed and words
separated by one space.

### Examples
**Example 1**

- Input: `s = "is2 sentence4 This1 a3"`
- Output: `"This is a sentence"`

**Example 2**

- Input: `s = "Myself2 Me1 I4 and3"`
- Output: `"Me Myself and I"`

**Example 3**

- Input: `s = "Hello1"`
- Output: `"Hello"`

### Required Complexity
- **Time:** $O(S)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

Split `s` at its spaces. The final character of each resulting token is its
original 1-based position, while every earlier character belongs to the word.
Because there are at most nine words, one decimal digit always contains the
entire position.

Allocate nine result slots. For each token, convert its final digit to a
zero-based index and store `token[:-1]` in that slot. If the sentence contains
$m$ tokens, the contract guarantees that positions $1$ through $m$ occur
exactly once, so those first $m$ slots become the original word sequence.
Joining them with single spaces restores precisely the requested sentence.

#### Complexity detail

Splitting, slicing the marked words, and joining the answer process $O(S)$
characters in total. The result slots, split tokens, and returned string store
$O(S)$ characters. The fixed nine-element slot array itself is $O(1)$.

#### Alternatives and edge cases

- **Sort marked words by their suffix:** sorting the tokens by the final digit
  is concise, but it adds comparison work that direct indexed placement does
  not need.
- **Repeated search by position:** scanning all tokens once for each expected
  digit reconstructs the same answer but performs redundant searches.
- A one-word sentence still carries the suffix `1`; remove it and return the
  remaining word without adding spaces.
- Uppercase and lowercase letters are word content and must be preserved
  exactly.
- The position is always one digit because the contract permits at most nine
  words; stripping more trailing characters would corrupt the word.

</details>
