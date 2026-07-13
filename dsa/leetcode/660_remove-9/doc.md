# Remove 9

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 660 |
| Difficulty | Hard |
| Topics | Math |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-9/) |

## Problem Description
### Goal
Consider the positive integers in increasing numerical order after removing every integer whose decimal representation contains the digit `9`. The remaining sequence begins with the ordinary one-digit values `1` through `8` and then continues with larger numbers that also avoid `9` in every position.

Given a positive one-based index `n`, return the `n`th integer in this filtered sequence. The index counts valid integers rather than decimal digits, and an otherwise valid number is excluded if `9` appears anywhere in its representation.

### Function Contract
**Inputs**

- `n`: a positive 1-based position in the filtered integer sequence

**Return value**

- The integer at position `n` among positive decimal integers that do not contain `9`

### Examples
**Example 1**

- Input: `n = 9`
- Output: `10`

**Example 2**

- Input: `n = 1`
- Output: `1`

**Example 3**

- Input: `n = 18`
- Output: `20`

### Required Complexity

- **Time:** $O(\log N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count choices at each digit position**

A valid decimal position may contain exactly nine digits: `0` through `8`. Consequently, all valid strings of a fixed width are counted like base-9 numerals. Increasing a rank through the filtered sequence changes these allowed digits in precisely the same order as incrementing a base-9 number.

**Reinterpret the rank's base-9 digits as decimal digits**

Repeatedly divide `n` by nine. Each remainder is a digit from zero through eight, so it is also a legal decimal digit. Place successive remainders into decimal ones, tens, hundreds, and so on. For example, rank `18` is `20` in base nine, and decimal `20` is the eighteenth positive integer without a `9`.

**Why the mapping preserves rank and order**

Every positive base-9 numeral maps to one decimal numeral containing no `9`, and reading any no-`9` decimal numeral's digits as base nine reverses the mapping. Both numeral systems compare equal-length representations lexicographically by their most significant digit, and shorter positive representations precede longer ones. The bijection therefore preserves increasing order, making the image of base-9 `n` exactly the `n`-th retained integer.

#### Complexity detail

Each division removes one base-9 digit, so the algorithm performs $O(\log N)$ iterations. It stores only the remaining rank, result, digit, and decimal place multiplier, using $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Generate integers and reject those containing `9`:** follows the sequence definition directly, but examines every preceding candidate and takes time proportional to the answer rather than its digit count.
- **Build a base-9 string:** is concise and still takes $O(\log N)$ time, but allocates $O(\log N)$ temporary string space.
- **Digit dynamic programming plus binary search:** can count valid integers up to a bound, but is far more machinery than the direct order-preserving bijection.
- Ranks `1` through `8` map to themselves.
- Rank `9` is the first carry and maps to decimal `10`.
- Zero digits inside or at the end of the result are valid; only digit `9` is excluded.

</details>
