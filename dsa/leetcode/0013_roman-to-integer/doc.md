# Roman to Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 13 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/roman-to-integer/) |

## Problem Description
### Goal
You are given a valid Roman numeral composed of `I`, `V`, `X`, `L`, `C`, `D`, and `M`, representing `1`, `5`, `10`, `50`, `100`, `500`, and `1000`. Most symbols contribute their values additively from left to right, and repeated symbols represent repeated contributions.

The notation also permits the standard subtractive pairs: `I` before `V` or `X`, `X` before `L` or `C`, and `C` before `D` or `M`. Convert the complete numeral to its integer value between `1` and `3999`. Because the input is guaranteed canonical, invalid or nonstandard symbol arrangements do not need to be diagnosed.

### Function Contract
**Inputs**

- `s`: non-empty `str` containing `I`, `V`, `X`, `L`, `C`, `D`, and `M`

**Return value**

An `int` equal to the value represented by `s`.

### Examples
**Example 1**

- Input: `s = "III"`
- Output: `3`

**Example 2**

- Input: `s = "LVIII"`
- Output: `58`

**Example 3**

- Input: `s = "MCMXCIV"`
- Output: `1994`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Let the next symbol determine addition or subtraction**

Roman symbols normally contribute positively. The only exception is a smaller symbol immediately before a larger one, where it is subtracted as part of a canonical subtractive pair. Therefore scan from left to right and compare each symbol's value with the next value.

Subtract the current value when it is smaller than its successor; otherwise add it. The final symbol always contributes positively.

**Why one-character lookahead is sufficient**

Before index `i` is processed, `total` equals the signed contribution of every symbol strictly before `i`. Comparing the current value to its successor uniquely determines whether it starts a subtractive pair or contributes additively. Even though the larger symbol in a subtractive pair is added on the following iteration, the two signed contributions combine to the pair's value: for example, $-100 + 1000 = 900$ for `CM`.

The input is guaranteed to be a valid canonical Roman numeral. Therefore any smaller-before-larger adjacency is one of the allowed subtractive forms; the algorithm is evaluating notation, not validating arbitrary Roman-like strings.

**Trace a representative input**

For `MCMXCIV`, process `M` as +1000, `C` as -100 before `M`, `M` as +1000, `X` as -10 before `C`, `C` as +100, `I` as -1 before `V`, and `V` as +5. Their sum is 1994.

**Why one-symbol lookahead captures every subtraction**

In a valid canonical numeral, a symbol is subtractive exactly when the immediately following symbol has greater value. The scan assigns a negative contribution to precisely that first symbol and a positive contribution to every other symbol. Thus `IV` becomes $-1 + 5$, while a descending pair such as `VI` remains $+5 + 1$.

Every allowed subtractive component has this adjacent smaller-before-larger form, and no additive component does. Replacing each component by these signed single-symbol contributions preserves its numeric value, so their total evaluates the entire numeral exactly.

#### Complexity detail

The scan performs one mapping lookup and at most one comparison per symbol, giving $O(n)$ time. The seven-symbol value mapping has fixed size, and no input-dependent auxiliary structure is created, so space is $O(1)$.

#### Alternatives and edge cases

- **Match six subtractive strings first:** correct, but needs explicit two-character branching before single-symbol handling.
- **Scan right to left:** maintain the greatest value seen and subtract smaller values. It is equally linear and constant-space.
- **Expand through repeated string replacement:** obscures ordering rules and allocates intermediate strings.
- The last symbol is always added because it has no successor that could make it subtractive.
- Validation of illegal forms such as `IC` or repeated `V` is outside the contract; supporting it would require additional grammar rules.

</details>
