## General

Let $n$ be the length of `s`.

**Process consecutive fixed-size groups**

Visit group starts `0, k, 2k, ...`. For one group, scan exactly the next `k` characters and add `ord(character) - ord('a')` for each. This expression is the required zero-based alphabet index.

Reduce the completed sum modulo 26, add it to `ord('a')`, convert that code point back to a character, and append it to the result. Joining the emitted characters preserves group order.

The divisibility guarantee partitions all string indices into exactly one group each. Every group accumulator therefore contains precisely its required character values, and the modulo conversion emits precisely that group's hash. Concatenating those independent hashes produces the specified result.

## Complexity detail

Each of the $n$ characters is visited once, giving $O(n)$ time. The result contains $n/k$ characters and uses $O(n/k)$ output space; excluding the required output, the group sum and indices use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Slice and sum each group:** This is also linear but creates temporary substring objects.
- **Build prefix sums:** Range sums make each group query constant time but require $O(n)$ extra storage for a one-pass task.
- **Rescan from the string start for every group:** Correctly filtering the current group can take $O(n^2/k)$ time.
- With `k = 1`, each character hashes to itself.
- With `k = n`, the result contains exactly one character.
- A group of only `a` characters hashes to `a` because every value is zero.
- Sums greater than 25 wrap around through modulo 26.
- Group boundaries are consecutive; characters are neither skipped nor shared.
- The output length is exactly the number of groups, $n/k$.
