# Tag Validator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 591 |
| Difficulty | Hard |
| Topics | String, Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/tag-validator/) |

## Problem Description
### Goal
Given a string representing a code snippet, implement a tag validator that determines whether the code is valid under the specified grammar. The entire code must be wrapped in one valid closed tag. Every start tag must have a matching end tag in the correct nesting order, and each tag name must contain only upper-case English letters with a length from `1` through `9`.

Tag content may contain ordinary characters, other valid closed tags, or CDATA sections of the form `<![CDATA[...]]>`. Text and CDATA are allowed only inside an open tag; CDATA content is treated as opaque text and ends at the first `]]>`. Reject unmatched angle brackets, invalid names, mismatched or unclosed tags, text outside the single root element, and any second top-level element.

### Function Contract
**Inputs**

- `code: str`: the complete candidate code string

**Return value**

- `True` only when the entire string is enclosed by one matching root tag
- Tag names must contain 1 through 9 uppercase English letters
- Nested start and end tags must match in stack order
- CDATA sections may appear only inside an open tag and end at the first `]]>`

### Examples
**Example 1**

- Input: `"<DIV>This is <![CDATA[<raw>]]></DIV>"`
- Output: `True`

**Example 2**

- Input: `"<A><B></B></A>"`
- Output: `True`

**Example 3**

- Input: `"<A><B></A></B>"`
- Output: `False`
