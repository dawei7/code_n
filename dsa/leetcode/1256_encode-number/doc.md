# Encode Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1256 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/encode-number/) |

## Problem Description

### Goal

Nonnegative integers are encoded in groups of binary strings ordered first by length and then by binary value. The number `0` is encoded as the empty string; `1` and `2` are encoded as `"0"` and `"1"`; `3` through `6` are encoded as `"00"`, `"01"`, `"10"`, and `"11"`; subsequent groups continue in the same pattern.

Given a nonnegative integer `num`, return its encoding under this scheme. The result contains only the characters `"0"` and `"1"`, except that the encoding of zero contains no characters.

### Function Contract

**Inputs**

- `num`: an integer satisfying $0 \le \texttt{num} \le 10^9$.
- Let $q=\texttt{num}+1$.

**Return value**

- Return the binary encoding assigned to `num` by the stated length-grouped sequence.

### Examples

**Example 1**

- Input: `num = 23`
- Output: `"1000"`
- Explanation: `num + 1` is `24`, whose binary form is `"11000"`; removing its leading `"1"` leaves `"1000"`.

**Example 2**

- Input: `num = 107`
- Output: `"101100"`

**Example 3**

- Input: `num = 0`
- Output: `""`

### Required Complexity

- **Time:** $O(\log q)$
- **Space:** $O(\log q)$

<details>
<summary>Approach</summary>

#### General

There is one encoding of length zero, two encodings of length one, four of length two, and generally $2^k$ encodings of length $k$. Those group sizes are exactly the counts represented by the leading `"1"` in ordinary positive binary numbers.

**Relating the sequence to binary representation**

Shift the input by one. The binary strings for $q=1,2,3,\ldots$ are `"1"`, `"10"`, `"11"`, `"100"`, and so forth. Removing the leading `"1"` yields `""`, `"0"`, `"1"`, `"00"`, exactly the required encoding sequence. The leading bit identifies the length group, while the remaining bits identify the position within that group.

Therefore compute the ordinary binary representation of `num + 1` and return every bit after its leading `"1"`. This also handles zero naturally because the binary form of one consists only of the removed leading bit.

#### Complexity detail

The binary representation of $q$ contains $\lfloor\log_2 q\rfloor+1$ bits. Producing and slicing it therefore takes $O(\log q)$ time, and the returned string occupies $O(\log q)$ space.

#### Alternatives and edge cases

- **Generate every preceding code:** Enumerating encodings from zero through `num` eventually finds the result but takes $O(q\log q)$ time instead of jumping directly to it.
- **Locate the length group by subtraction:** Repeatedly subtract powers of two, then format the remaining offset with leading zeros; this is correct but more elaborate than the shifted-binary identity.
- **Zero:** `bin(1)` has no suffix after its leading data bit, producing the required empty string.
- **Power-of-two boundary:** When `num + 1` is a power of two, the encoding begins a new group and consists entirely of zeros.
- **Leading zeros:** They are meaningful encoding characters and must not be stripped from the returned suffix.

</details>
