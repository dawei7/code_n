# Design Bitset

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2166 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-bitset/) |

## Problem Description

### Goal

Implement a fixed-size `Bitset` whose bits are initially zero. Individual
indices can be fixed to `1` or unfixed to `0`; applying either operation to a
bit that already has the requested value changes nothing. A global `flip`
operation must exchange every logical zero and one.

The structure must also report whether all bits are one, whether at least one
bit is one, and how many one bits exist. Its string representation lists bits
in index order, so character $i$ is the logical value at bit index $i$.

### Function Contract

**Inputs**

- `Bitset(size)` creates `size` zero bits, where $1\le\texttt{size}\le10^5$.
- `fix(idx)` sets the bit at valid zero-based index `idx` to one.
- `unfix(idx)` sets the bit at valid zero-based index `idx` to zero.
- `flip()` complements every bit.
- `all()` tests whether every bit is one.
- `one()` tests whether at least one bit is one.
- `count()` reports the number of one bits.
- `toString()` returns the bit values in increasing index order.

At most $Q=10^5$ method calls occur, including at most five `toString()` calls.

**Return value**

Construction and mutating methods return no value. The three queries return
booleans or an integer as described, and `toString()` returns a binary string
of length `size`. The app-local trace returns one result per operation, using
`null` for construction and mutating calls.

### Examples

#### Example 1

- **Input:** `operations = ["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"]`
- Arguments: `[[5], [3], [1], [], [], [0], [], [], [0], [], []]`
- **Output:** `[null, null, null, null, false, null, null, true, null, 2, "01010"]`

The two flips are represented logically; the final one bits are at indices
`1` and `3`.

#### Example 2

- **Input:** construct size `1`, call `flip()`, then `all()`, `count()`, and `toString()`
- **Output:** `true`, `1`, and `"1"`

#### Example 3

- **Input:** construct size `4`, call `fix(1)` twice, then `unfix(1)` twice
- **Output:** final count `0` and string `"0000"`

Repeated idempotent updates do not change the maintained count.
