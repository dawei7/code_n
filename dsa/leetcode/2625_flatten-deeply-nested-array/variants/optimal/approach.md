## General

Flattening is governed by the depth of an array boundary, not by the depth of an integer. Traverse the outer array from left to right while carrying the current boundary depth, initially zero.

**Expand only before the cutoff**

For each entry, there are two possibilities:

- If the entry is an array and the current depth is less than `n`, recursively visit that array at `depth + 1`.
- Otherwise, append the entry itself to the result. This includes every integer and every array encountered exactly at or below the cutoff.

The recursive calls are completed immediately before traversal continues with the next sibling. Therefore, all descendants of an expanded array occupy exactly the position previously held by that array, preserving the original left-to-right order.

At every visited boundary, the depth test matches the contract directly. A boundary above the cutoff is removed and its entries are processed; a boundary at the cutoff is appended unchanged and its contents are never inspected. Consequently, the output removes exactly the permitted array boundaries and retains every value or unexpanded subarray in its original order.

## Complexity detail

Let $V$ be the number of entries inspected before the cutoff and $D$ the greatest traversed nesting depth. Each inspected entry is handled once, so the running time is $O(V)$. The returned array can contain $O(V)$ entries, and recursion uses at most $O(D)$ stack frames, for $O(V + D)$ total space. Excluding the output, auxiliary space is $O(D)$.

## Alternatives and edge cases

- **Explicit stack:** Push entries in reverse order together with their depths, then pop them into the result. This is also $O(V)$ and avoids recursion, but it requires careful reversal to preserve order.
- **Repeated spread or concatenation:** Rebuilding the accumulated result after each entry is correct but repeatedly copies earlier entries, leading to $O(V^2)$ time on a wide array.
- **Built-in `Array.flat`:** It expresses the operation directly but is explicitly disallowed by the problem contract.
- **Zero depth:** No nested boundary is eligible for expansion, so the returned array preserves the top-level entries and their nested arrays.
- **Cutoff boundary:** An array encountered when `depth === n` is appended as one entry; nothing inside it should be traversed or copied separately.
- **Empty arrays:** An expanded empty array contributes no entries, while an empty array at the cutoff remains as an empty nested entry.
- **Large limits:** When `n` exceeds the input's maximum depth, every nested boundary is removed without requiring a special case.
