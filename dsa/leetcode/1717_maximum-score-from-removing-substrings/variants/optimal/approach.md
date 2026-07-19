## General
**Remove the more valuable pair first**

Suppose `ab` is worth at least as much as `ba`; otherwise exchange the roles of the two patterns and their scores. Process `s` from left to right with a stack. Whenever the stack top and current character form `ab`, remove that pair immediately and add `x`; otherwise push the character. This single pass removes every possible occurrence of the higher-valued pattern, including occurrences created by earlier removals.

**Resolve every competing deletion in the profitable direction**

The only local competition between the two operations occurs around three alternating characters: deleting one adjacent pair can destroy the opportunity to delete the other. Giving that choice to the higher-valued pair never lowers the score. Any sequence that takes the cheaper pair at such a conflict can be exchanged for one that takes the expensive pair, while preserving all removals outside that local `a`/`b` region. Consequently, some optimal sequence removes all possible higher-valued pairs before using the cheaper operation.

**Collect the remaining lower-value pairs**

Run the same stack procedure over the remaining characters for the other pattern. The first pass has left no higher-valued pair, and the second pass extracts every remaining cheaper pair. Characters other than `a` and `b` are simply pushed and can never match either pattern, so the procedure also respects the independent-region boundaries automatically.

## Complexity detail
Let $n = \lvert \texttt{s} \rvert$. Each pass pushes and pops every character at most once, so the two passes take $O(n)$ time. The stacks and the intermediate remaining string contain at most $n$ characters, requiring $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Count within `a`/`b` blocks:** The same greedy order can be implemented by counting unmatched endpoint characters in each block, but the stack version makes newly adjacent pairs and separators more direct.
- **Repeated substring search and deletion:** Searching for one occurrence and rebuilding the string after every removal is correct when the valuable pattern is exhausted first, but it can require $O(n^2)$ time.
- **Equal scores:** When $x = y$, either pair may be processed first because every removal contributes the same value.
- **Separating characters:** Any character other than `a` or `b` prevents a removable pair from crossing it, even after all possible deletions on either side.
- **No removable pair:** A one-character string or a region containing only one of `a` and `b` contributes zero.
