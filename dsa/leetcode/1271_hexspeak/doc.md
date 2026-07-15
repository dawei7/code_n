# Hexspeak

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1271 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/hexspeak/) |

## Problem Description

### Goal

A positive decimal integer can be written in Hexspeak by first converting it to an uppercase hexadecimal string. In that string, hexadecimal digit `0` is pronounced as the letter `O`, and digit `1` is pronounced as the letter `I`. The ordinary hexadecimal letters `A` through `F` remain unchanged.

A representation is valid only when every converted character belongs to `A`, `B`, `C`, `D`, `E`, `F`, `I`, or `O`. Given the decimal integer as the string `num`, return its valid Hexspeak form. If its hexadecimal expansion contains any digit from `2` through `9`, return `"ERROR"` instead. The returned letters must be uppercase.

### Function Contract

**Inputs**

- `num`: a decimal string with no leading zeros representing an integer $n$ where $1 \le n \le 10^{12}$.
- Let $d=\lfloor\log_{16}n\rfloor+1$ be the number of hexadecimal digits. The source constraint guarantees $1 \le d \le 10$.

**Return value**

- Return the uppercase Hexspeak representation, or `"ERROR"` if any hexadecimal digit is between `2` and `9`.

### Examples

**Example 1**

- Input: `num = "257"`
- Output: `"IOI"`

**Example 2**

- Input: `num = "3"`
- Output: `"ERROR"`

**Example 3**

- Input: `num = "2827"`
- Output: `"BOB"`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(\log n)$

<details>
<summary>Approach</summary>

#### General

**Read the hexadecimal digits from least significant to most significant**

Parse `num` as an integer. Repeatedly apply `divmod(value, 16)`: the remainder is the next hexadecimal digit and the quotient contains the digits still to process. A remainder of `0` contributes `O`, `1` contributes `I`, and a remainder from `10` through `15` contributes `A` through `F`.

If a remainder lies from `2` through `9`, no replacement can make that digit pronounceable, so return `"ERROR"` immediately. Otherwise append the mapped letter to a buffer. Division discovers digits in reverse order, so reverse the buffer after the quotient reaches zero.

Each iteration consumes exactly one hexadecimal digit. Therefore every character in a returned string is the prescribed image of the corresponding digit and belongs to the valid alphabet. Conversely, the method rejects exactly when the hexadecimal expansion contains a forbidden digit, which is precisely the condition for having no valid Hexspeak representation.

#### Complexity detail

The loop processes the $d=\Theta(\log n)$ hexadecimal digits once, giving $O(\log n)$ time. The output buffer holds $d$ characters, so auxiliary space including the returned string is $O(\log n)$. Under the legal source bound, $d$ is at most ten; the package records this fixed domain with a validated non-scaling certificate rather than claiming measured runtime scaling.

#### Alternatives and edge cases

- **Built-in hexadecimal formatting:** Converting with `hex(...)`, uppercasing, and translating `0` and `1` is concise, but the remaining decimal characters must still be detected.
- **String replacement before validation:** Replacing `0` and `1` first is safe only if every leftover digit from `2` through `9` is then rejected.
- **Single hexadecimal digit:** Values `1` and `10` through `15` produce one valid letter; values `2` through `9` return `"ERROR"`.
- **Internal zeros and ones:** Every occurrence maps independently, as in hexadecimal `B0B` becoming `BOB`.
- **Maximum input:** $10^{12}$ still has only ten hexadecimal digits, but its forbidden digits make the result `"ERROR"`.
- **Letter case:** Hexadecimal letters must be emitted as uppercase `A` through `F`.

</details>
