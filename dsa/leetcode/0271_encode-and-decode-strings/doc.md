# Encode and Decode Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 271 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/encode-and-decode-strings/) |

## Problem Description
### Goal
Design a codec that converts a list of arbitrary strings into one transport string and later reconstructs the exact original list. Individual strings may be empty or contain digits, delimiter characters, spaces, and other content, so ordinary separator joining is not sufficient.

`encode(strs)` must preserve every string boundary, value, and list order, distinguishing an empty list from a list containing an empty string. `decode(s)` must invert every valid encoded result without ambiguity. The encoded representation may use any reversible format, but decoding must not depend on a delimiter being absent from the original strings. Return the reconstructed strings with exactly the same values and ordering as the input list.

### Function Contract
**Inputs**

- `operation`: either `"encode"` or `"decode"`
- `value`: a string list for encoding, or an encoded string for decoding

**Return value**

Encoding uses consecutive `<decimal length>#<content>` fields; decoding returns the represented list. The native interface exposes `Codec.encode(strs)` and `Codec.decode(s)`.

### Examples
**Example 1**

- Input: `operation = "encode", value = ["lint","code"]`
- Output: `"4#lint4#code"`

**Example 2**

- Input: `operation = "decode", value = "5#hello0#"`
- Output: `["hello",""]`

**Example 3**

- Input: `operation = "encode", value = ["","a#b"]`
- Output: `"0#3#a#b"`
