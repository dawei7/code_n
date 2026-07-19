## General
**Translate geometry into index order:** Two lines do not cross exactly when their matched indices increase in the same order in both arrays. Requiring equal endpoint values and forbidding shared endpoints therefore asks for the longest common subsequence.

**Define prefix states:** For prefixes ending before `i` and `j`, store the maximum number of lines. If the current values match, extend the diagonal prefix by one. Otherwise, skip one current value and keep the larger result from the prefix above or to the left.

**Keep only two rows:** Each new DP row depends only on the previous row and values already written in the current row. Make the shorter input the column dimension, so these two arrays use $O(\min(M,N))$ memory.

Every DP transition constructs legal increasing index pairs. Conversely, the last line of any optimal drawing either connects the current equal values or leaves at least one current endpoint unused, matching one of the recurrence branches. Induction over the two prefix lengths proves the final state is optimal.

## Complexity detail
The algorithm evaluates all $M\cdot N$ prefix pairs with constant work per pair, taking $O(MN)$ time. Two rows of length $min(M,N)+1$ use $O(\min(M,N))$ auxiliary space.

## Alternatives and edge cases
- **Full DP table:** Store every prefix state for the same $O(MN)$ time but $O(MN)$ space; this is useful only when reconstructing the actual lines.
- **Recursive memoization:** Express the same recurrence top-down, but recursion and memo entries can consume $O(MN)$ space.
- **Match-pair chain DP:** Create every equal index pair and find the longest chain increasing in both coordinates. A direct comparison of all match pairs can take $O(K^2)$ time for $K$ matches.
- **No shared values:** The answer is zero.
- **Repeated values:** Each occurrence remains a distinct endpoint and can be used at most once.
- **Reversed order:** Equal sets do not imply many lines when their index orders oppose one another.
- **Unequal lengths:** Using the shorter array for columns changes memory use, not the result.
