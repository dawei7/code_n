## General
**Know whether a character is replaceable:** Record the last index of every character. If a character already chosen for the answer still occurs later, it may be removed now and restored from that later occurrence; otherwise removing it would violate the exactly-once coverage requirement.

**Maintain the smallest feasible prefix:** Scan `s` from left to right and skip a character already present in the stack. For a new character, repeatedly pop the stack while its top is lexicographically larger and the top's last occurrence lies after the current index. Each such pop makes the earliest differing answer position smaller without losing the ability to include the removed character later.

**Commit the current character once:** Push it and mark it present. Characters below a top that cannot be safely popped remain fixed because either they are no larger or this is their last available occurrence.

The stack always contains distinct characters in subsequence order. Safe pops preserve the possibility of covering every distinct character, and each pop produces a lexicographically smaller feasible prefix. When a top cannot be popped, every valid completion must retain it before the current character or lose it entirely, so the greedy choice is forced. The final stack is therefore feasible and lexicographically minimal.

## Complexity detail
The last-occurrence pass and main scan each process $n$ characters. Every character is pushed at most once after each removal and popped at most once per push, so total stack work is $O(n)$. Because the alphabet has 26 lowercase letters, the last-index map, membership set, and stack use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Rebuild suffix counts at each index:** It supports the same safe-pop test but repeatedly scans suffixes and can take $O(n^2)$ time.
- **Sort the distinct letters:** Alphabetic order alone may not be realizable as a subsequence and ignores last-occurrence constraints.
- **Pop every larger top:** Removing a character after its final occurrence makes it impossible to include that character in the result.
- **All characters equal:** Return that character once.
- **All characters distinct:** The input itself is the only valid subsequence.
- **Repeated opportunities:** A skipped duplicate can still be important as the future occurrence that permits an earlier stack pop.
