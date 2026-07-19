## General
**Track how many child slots remain available**

Before reading the root, exactly one slot is available. Every token consumes one slot. A null marker creates no replacements, while a real node creates two child slots, for a net change of minus one for `#` and plus one for an integer token.

Scan tokens from left to right. Before consuming any token, the slot count must be positive; reaching zero early means a complete tree has already ended, so any further token is extra. After the final token, the slot count must be exactly zero. A positive remainder means required children were never serialized.

**Scan token boundaries without building a token array**

Only the first character of a token matters for the slot update: `#` is null and every other valid token is an integer, including a negative one beginning with `-`. After processing that distinction, advance to the next comma or the end of the string.

For `"1,#"`, the root changes one slot into two, and the null consumes only one, leaving one missing child slot. For `"9,#,#,1"`, the first three tokens reduce the count to zero; the final `1` is rejected before it can consume a nonexistent slot.

**Slot balance is equivalent to a valid preorder tree**

Every serialized node must occupy exactly one slot provided by its parent, except the root, whose initial slot is supplied explicitly. Real nodes introduce exactly their two ordered child positions, and null markers close one position. Therefore a scan that never runs out early can attach every processed token in preorder order.

Ending at zero proves all introduced positions were closed. Ending above zero leaves missing children, while reaching zero before the end leaves extra tokens. These are the only possible structural failures, so the condition is both necessary and sufficient.

## Complexity detail
Each character is advanced over once while locating token boundaries, giving $O(L)$ time for serialization length `L`. The scan stores only indices and the slot counter, using $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Split into tokens and use the same slot rule:** remains linear but uses $O(L)$ extra storage.
- **Recursively parse left and right subtrees:** is correct, but repeated list or string slicing can become $O(L^2)$ on a skewed serialization and recursion can overflow.
- **Count only total nodes and nulls:** misses invalid prefixes that finish a tree before later tokens.
- `"#"` is a valid empty-tree serialization. Negative node values behave like all other non-null tokens.
