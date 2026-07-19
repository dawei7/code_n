# Check if Numbers Are Ascending in a Sentence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2042 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/) |

## Problem Description

### Goal

A sentence consists of tokens separated by single spaces, with no space at
either end. Every token is either a lowercase English word or the decimal
representation of a positive integer. Numeric tokens have no leading zeros.

Read only the numeric tokens from left to right, ignoring the words. Return
whether every number is strictly smaller than the next numeric token in the
sentence. Equality does not count as increasing.

### Function Contract

Let $L$ be the length of `s`.

**Inputs**

- `s`: a valid sentence with $3 \le L \le 200$, between `2` and `100` tokens,
  and at least two numeric tokens.
- Every numeric token represents an integer from $1$ through $99$.

**Return value**

- `true` when the numeric tokens are strictly increasing from left to right;
  otherwise `false`.

### Examples

**Example 1**

- Input: `s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"`
- Output: `true`
- Explanation: The numeric sequence is `1, 3, 4, 6, 12`.

**Example 2**

- Input: `s = "hello world 5 x 5"`
- Output: `false`
- Explanation: Equal consecutive numeric values are not strictly increasing.

**Example 3**

- Input: `s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"`
- Output: `false`
- Explanation: The numeric sequence decreases from `51` to `50`.

### Required Complexity

- **Time:** $O(L)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

**Recognize complete numeric tokens**

Split the sentence at its single-space separators. A token is numeric exactly
when all of its characters are digits; word tokens are ignored. Convert each
numeric token to an integer so comparisons use numeric value rather than
lexicographic text order. For example, `2` is less than `10` numerically even
though `"2"` sorts after `"10"` as text.

**Compare only with the previous number**

Maintain the most recently encountered numeric value. Since all input numbers
are positive, initialize it to `0`. For each new number, return `false`
immediately if it is less than or equal to the previous value; otherwise
replace the previous value and continue.

Strict increase is a local adjacent property: a finite sequence is strictly
increasing exactly when every element after the first exceeds its predecessor.
The scan checks each such pair once. If it finds a violation, the full sequence
cannot be valid; if it finishes, all adjacent inequalities hold and
transitivity establishes the required order.

#### Complexity detail

Splitting, classifying, and converting tokens examines $O(L)$ characters in
total, so time is $O(L)$. The token list and substrings created by splitting
occupy $O(L)$ auxiliary space.

#### Alternatives and edge cases

- **Manual character scan:** Parse each number directly from the sentence to
  retain $O(L)$ time while reducing auxiliary space to $O(1)$.
- **Extract every number first:** Building a numeric list and comparing adjacent
  entries is also linear but stores information the streaming comparison does
  not need.
- Equal numeric tokens must return `false` because the order is strict.
- A violation may occur only at the final numeric token and must still be
  detected.
- Multi-digit values require integer comparison, not string comparison.
- Words between numbers have no effect on ordering.
- The positive-number guarantee makes `0` a safe initial sentinel.

</details>
