## General
**Precompute every legal cut segment once**

Build `palindrome[left][right]` for every substring. It is true when `s[left] = s[right]` and either the length is at most two or the enclosed interval `[left+1,right-1]` is already true.

Fill `left` from right to left (or lengths from short to long) so the enclosed interval is known before the outer substring. This avoids rescanning the same characters for many backtracking branches.

**Backtracking chooses the next palindromic endpoint**

From `start`, try every `end >= start` whose table entry is true. Append `s[start:end+1]`, recurse from `end + 1`, and pop after return. When `start = len(s)`, the path covers the complete string and a copy is emitted.

**The path is a lossless partition of exactly one processed prefix**

The current path contains consecutive palindromic substrings whose concatenation is exactly the processed prefix. The recursion index is the first unprocessed character.

**Trace alternate first cuts in `aab`**

Choosing `a`, then `a`, then `b` yields one partition. Backtracking to index zero also permits `aa`, followed by `b`, yielding the second; substring `aab` is rejected.

**Cut endpoints uniquely describe each palindrome partition**

Every recursive choice uses a substring certified by the palindrome table, and a leaf is emitted only after choices cover the complete string. Every result is therefore a valid partition.

Conversely, any valid partition has a unique sequence of substring end positions. The search tries its first palindromic endpoint and then repeats on the remaining suffix, following that entire sequence. Different endpoint sequences describe different partitions, so all valid partitions are generated once.

## Complexity detail
The palindrome table takes $O(n^2)$ time and space. Beyond that, writing all returned substring values costs `L` total output work. The active path and recursion use $O(n)$ space excluding results.

## Alternatives and edge cases
- **Rescan every candidate substring:** can add an avoidable factor of `n`.
- **Generate arbitrary cuts then validate:** explores invalid partitions too late.
- **Return only the fewest cuts:** solves Problem 132 and discards required partitions.
- A one-character string has one partition containing itself. Highly repetitive strings can have exponentially many valid partitions, so output-sensitive work is unavoidable.
- Copy the path only at a complete partition; copying at every edge adds avoidable work.
