# Verify Preorder Serialization of a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 331 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack, Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/) |

## Problem Description
### Goal
Given a comma-separated preorder serialization, integer tokens represent non-null binary-tree nodes and `#` tokens represent null child positions. Preorder records a node first, then the complete serialization of its left subtree, followed by its right subtree.

Return `True` only when every token fills one valid pending position and the final token completes exactly one whole tree. Missing null markers leave unfinished children, while extra tokens after all positions are filled are invalid. A lone `#` correctly represents an empty tree. Validate the sequence without constructing node objects or treating a numeric token as a leaf unless its two children are also represented.

### Function Contract
**Inputs**

- `preorder`: comma-separated integer and `#` tokens in preorder order

**Return value**

`True` when every token fills a valid child position and the serialization finishes with no missing or extra tokens; otherwise `False`.

### Examples
**Example 1**

- Input: `preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"`
- Output: `True`

**Example 2**

- Input: `preorder = "1,#"`
- Output: `False`

**Example 3**

- Input: `preorder = "9,#,#,1"`
- Output: `False`

### Required Complexity

- **Time:** $O(L)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track how many child slots remain available**

Before reading the root, exactly one slot is available. Every token consumes one slot. A null marker creates no replacements, while a real node creates two child slots, for a net change of minus one for `#` and plus one for an integer token.

Scan tokens from left to right. Before consuming any token, the slot count must be positive; reaching zero early means a complete tree has already ended, so any further token is extra. After the final token, the slot count must be exactly zero. A positive remainder means required children were never serialized.

**Scan token boundaries without building a token array**

Only the first character of a token matters for the slot update: `#` is null and every other valid token is an integer, including a negative one beginning with `-`. After processing that distinction, advance to the next comma or the end of the string.

For `"1,#"`, the root changes one slot into two, and the null consumes only one, leaving one missing child slot. For `"9,#,#,1"`, the first three tokens reduce the count to zero; the final `1` is rejected before it can consume a nonexistent slot.

**Slot balance is equivalent to a valid preorder tree**

Every serialized node must occupy exactly one slot provided by its parent, except the root, whose initial slot is supplied explicitly. Real nodes introduce exactly their two ordered child positions, and null markers close one position. Therefore a scan that never runs out early can attach every processed token in preorder order.

Ending at zero proves all introduced positions were closed. Ending above zero leaves missing children, while reaching zero before the end leaves extra tokens. These are the only possible structural failures, so the condition is both necessary and sufficient.

#### Complexity detail

Each character is advanced over once while locating token boundaries, giving $O(L)$ time for serialization length `L`. The scan stores only indices and the slot counter, using $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Split into tokens and use the same slot rule:** remains linear but uses $O(L)$ extra storage.
- **Recursively parse left and right subtrees:** is correct, but repeated list or string slicing can become $O(L^2)$ on a skewed serialization and recursion can overflow.
- **Count only total nodes and nulls:** misses invalid prefixes that finish a tree before later tokens.
- `"#"` is a valid empty-tree serialization. Negative node values behave like all other non-null tokens.

</details>
