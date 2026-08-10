## General

**Enumerate combinations as numbers in a mixed-radix system**

If each digit had exactly ten choices, an integer's decimal digits could select those choices. Phone digits instead provide either three or four letters, so each position has its own radix. The selected competitive method numbers all combinations from `0` through `total - 1` and decodes each number into one letter choice per input position.

`lookup[int(digit)]` gives the choice string directly because `lookup` has empty placeholders at indices `0` and `1`.

**Count the exact number of outputs first**

The product

```python
total *= len(lookup[int(digit)])
```

multiplies the choice counts. For `"23"`, `total = 3 * 3 = 9`; for `"79"`, it is `4 * 4 = 16`. This is the number of leaves in the implicit choice tree and the exact number of required result strings.

**Decode one combination index from left to right**

For each output number `i`, begin with `base = total`. At a digit with `c` choices, divide `base` by `c`. The new `base` equals the number of full combinations associated with each choice at this position among the still-unprocessed suffixes.

The selected letter index is

```python
(i // base) % len(choices)
```

Integer division identifies which block of size `base` contains `i`; modulo restricts it to this position's range. `curr.append(...)` stores the selected letter. After the last digit, `base` is `1`, so the final choice changes on every consecutive `i`.

**Why the division order matters**

At the beginning of a position, `base` still counts all combinations covered by the current choice and every choice to its right. Dividing by `c` first removes the current position's factor. The resulting number is therefore precisely the number of suffix combinations beneath one letter at this position. If the code selected a letter before performing `base //= len(choices)`, the blocks would be too large and several legal letters would never be reached.

The modulo operation is equally important after integer division. For the leftmost position, `i // base` already lies in its legal index range. At later positions, however, that quotient also contains contributions from positions to the left. Taking the remainder modulo `c` discards those completed cycles and leaves only the current mixed-radix digit.

**Trace indices for `"23"`**

`total = 9`.

- For digit `2`, divide `base` to `3`. Choice `(i // 3) % 3` is `0` for `i = 0..2`, `1` for `3..5`, and `2` for `6..8`, producing blocks beginning with `a`, `b`, and `c`.
- For digit `3`, divide `base` to `1`. Choice `i % 3` cycles through `d`, `e`, and `f` inside each block.

The resulting order is `ad, ae, af, bd, be, bf, cd, ce, cf`.

For a mixed example such as `"27"`, the first position has radix three and the second has radix four. `total` is twelve. After the first division, `base` is four, so `a`, `b`, and `c` each own a consecutive block of four results. After the second division, `base` is one, so `p`, `q`, `r`, and `s` cycle within each block. This example shows why the method is genuinely mixed-radix rather than secretly assuming three letters per digit.

**Why every combination appears once**

The mixed-radix digits of integers `0` through `total - 1` form every tuple of legal choice indices exactly once. Two different integers differ in at least one decoded position, producing different letter strings. Conversely, every tuple has a unique mixed-radix numerical encoding in that range.

Joining `curr` after all positions produces one complete string. The outer loop covers the full numerical range, proving completeness and uniqueness.

**Empty input behavior**

The early return gives `[]`. Without it, `total` would stay one and the method would generate one empty string, which is not the desired API result for no phone digits. Legal problem input is non-empty, but the guard makes this convention explicit.

## Complexity detail

Let $n$ be the digit count and $P$ the product of their choice counts.

- **Time complexity: $O(nP)$, at most $O(n\cdot4^n)$.** Each of `P` output indices decodes all `n` positions and joins an `n`-character list.
- **Space complexity: $O(nP)$ including output and $O(n)$ transient auxiliary space.** `result` stores every output string. For one iteration, `curr` contains `n` characters. The fixed lookup and scalar arithmetic use constant space. The source comment's $O(1)$ excludes both output and the per-result construction buffer, whereas the manifest's $O(n)$ captures the transient buffer.

## Alternatives and edge cases

- **Optimal variant list expansion:** Repeatedly form the Cartesian product of existing prefixes and current letters. It is shorter code but holds whole prefix layers.
- **Backtracking (`Solution3`):** Mirrors the choice tree and uses an $O(n)$ mutable path plus recursion stack.
- **In-place breadth expansion (`Solution2`):** Grows and rewrites one result list from rightmost digit to leftmost; its index arithmetic is different but output-equivalent.
- **One digit:** `total` is three or four, and `base` becomes one immediately.
- **Mixed three/four choice digits:** Per-position division handles different radices without padding.
- **Repeated digits:** Each position is decoded independently, so repeated letters across positions are allowed.
- **Maximum branching:** Four digits chosen from `7` or `9` generate 256 strings, each length four.
- **Integer safety:** `base` remains positive and ends at one because `total` contains every position's factor exactly once.
- **Output order:** Mixed-radix order is deterministic, but any order is permitted.
- **Fresh per-result buffer:** `curr` is recreated for every value of `i`; otherwise letters from the preceding combination would leak into the next joined string.
