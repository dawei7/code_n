# Making File Names Unique

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1487 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String |
| Official Link | [LeetCode](https://leetcode.com/problems/making-file-names-unique/) |

## Problem Description
### Goal

A file system receives `n` folder-name requests in chronological order. At minute `i`, it tries to create a folder named `names[i]`. If that exact name has not already been assigned, the system uses it unchanged.

When the requested name is already occupied, append a suffix of the form `(k)`, where `k` is the smallest positive integer that makes the complete resulting string unused. Assign that name immediately, so it participates in all later collision checks. Return the actual assigned name for every request in the original order.

### Function Contract
**Inputs**

Let $N$ be the length of `names`.

- `names`: an array of strings with $1 \le N \le 5 \cdot 10^4$.
- Every requested name has length from $1$ through $20$.
- Each character is a lowercase English letter, digit, opening parenthesis, or closing parenthesis.
- A string that already looks like a suffixed name is still an ordinary literal request; its parentheses have no special parsing rule.

**Return value**

Return an array `assigned` of length $N$. For each index `i`:

- `assigned[i]` is unused before request `i`;
- it equals `names[i]` if that name is free;
- otherwise it equals `names[i] + "(" + k + ")"` for the smallest positive integer `k` that makes it free.

### Examples
**Example 1**

- Input: `names = ["pes","fifa","gta","pes(2019)"]`
- Output: `["pes","fifa","gta","pes(2019)"]`
- Explanation: Every requested string is new, including the literal name `"pes(2019)"`.

**Example 2**

- Input: `names = ["gta","gta(1)","gta","avalon"]`
- Output: `["gta","gta(1)","gta(2)","avalon"]`
- Explanation: The second request already occupies `"gta(1)"`, so the later duplicate of `"gta"` must skip to suffix two.

**Example 3**

- Input: `names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]`
- Output: `["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]`
- Explanation: Suffixes one through three are occupied when the final base-name request arrives.
