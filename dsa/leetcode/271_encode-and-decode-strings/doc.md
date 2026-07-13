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

### Required Complexity

- **Time:** $O(c)$
- **Space:** $O(c)$

<details>
<summary>Approach</summary>

#### General

**A length prefix makes arbitrary content self-delimiting**

Write the decimal character length, a `#` separator, then exactly that many content characters. Lengths make content self-delimiting even when it contains digits, separators, or empty strings.

**Decode headers and payloads with one cursor**

Find the next separator, parse the preceding length, then slice exactly that many characters. Advance the cursor to the next header and repeat.

At each decoding iteration, the cursor points to the first digit of the next length header. Consuming the header and its declared payload moves it to precisely the following header.

**Declared length removes every delimiter ambiguity**

The first `#` after a header start terminates a decimal length, and that length—not any character inside the payload—determines the next boundary. The decoder therefore recovers the exact payload even when it contains `#`, digits, or is empty. Advancing by the declared size restores the header-start position for the next field, so all strings are reconstructed in order.

#### Complexity detail

Every content and header character is produced or scanned a constant number of times, for $O(c)$ time and output-sized $O(c)$ space.

#### Alternatives and edge cases

- **Join with a sentinel:** fails when content contains the sentinel unless escaping is carefully defined.
- Empty lists, empty strings, separator characters, digits, and Unicode content are all handled by lengths.

</details>
