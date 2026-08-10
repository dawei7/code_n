## General

**Split nesting levels rather than contiguous pieces**

A deeply nested parentheses string has several simultaneously open pairs. To minimize the maximum depth of two subsequences, those nesting levels should be divided as evenly as possible between group zero and group one.

The solution assigns alternating depth levels by parity. Pairs opened from even current depth go to one group, and pairs opened from odd current depth go to the other. This makes each group contain roughly half of the original nesting layers.

**Track the current depth**

Variable `x` is the number of unmatched opening parentheses seen before the current character, except that a closing parenthesis first decreases it to the depth of its matching opening context.

For an opening parenthesis, `ans[i] = x & 1` records the parity of the depth before entering the new pair, then `x += 1` increases the active depth.

For a closing parenthesis, `x -= 1` first returns to the depth that existed before its matching opening, and `ans[i] = x & 1` assigns that same parity.

This order difference is essential. If both characters used depth before updating, a matched opening and closing could receive different groups.

**Matched pairs receive the same group**

Suppose an opening parenthesis is encountered while current depth is $d$. It receives group $d\bmod 2$, and depth becomes $d+1$. Because the input is valid, its matching closing parenthesis is reached after every nested pair inside it has closed. Just before processing that close, active depth is $d+1$; decrementing returns it to $d$, so the close receives the same parity.

Therefore, the algorithm never separates the two endpoints of a matched pair.

**Each selected subsequence remains valid**

Within either group, opening and closing parentheses preserve their original order. Every chosen close belongs to a matched pair whose chosen open occurs earlier in the same group. Nested pairs assigned to the other group may disappear from this subsequence, but removing complete matched pairs does not invalidate the remaining matching structure.

Thus neither group’s running balance becomes negative, and every chosen opening eventually has its chosen closing. Both subsequences are valid parentheses strings.

**Why parity minimizes maximum depth**

Let the original maximum nesting depth be $D$. At a position attaining that depth, there are $D$ simultaneously open pairs. Those pairs must be divided between two groups. By the pigeonhole principle, one group must contain at least $\lceil D/2\rceil$ of them. No split can have maximum group depth below that lower bound.

Parity assignment alternates consecutive nested levels. Among any $D$ active levels, group zero receives at most $\lceil D/2\rceil$ and group one receives at most $\lceil D/2\rceil$. Therefore, the achieved maximum depth is exactly the best possible bound.

The algorithm does not need to know $D$ in advance. Online parity decisions automatically balance every prefix and every nested region.

**Interpret the output**

`ans[i] = 0` assigns `seq[i]` to subsequence A, and one assigns it to B. The result need not match the examples because multiple optimal splits may exist. What matters is validity of both subsequences and the minimized maximum depth.

## Complexity detail

The loop visits every character once and performs constant-time arithmetic and assignment, so time is $O(n)$.

The answer array has one entry per input character and therefore uses $O(n)$ space, matching the manifest. Apart from this required output, `x` and loop variables use $O(1)$ auxiliary space.

No stack is necessary because the input is guaranteed valid and only current depth parity, not explicit pair indices, is needed.

## Alternatives and edge cases

- **Assign by depth after opening:** One may increment first and use the new depth parity, provided closing characters use parity before decrementing. This swaps group labels but remains optimal.
- **Explicit stack of pair indices:** Match every pair, then assign by nesting depth. It works but uses extra stack state that the running depth already summarizes.
- **Split contiguous halves:** Contiguous division does not generally balance nested levels and may not even produce two valid parentheses strings.
- **Put complete primitive components alternately:** This balances separate top-level pieces but fails to divide depth inside one deeply nested component.
- **Depth one:** All pairs can go to one group, and the maximum depth is one; parity may leave the other group empty.
- **Empty subsequence:** An empty group is a valid parentheses string under the definition.
- **Sequential pairs:** Depth repeatedly returns to zero, so all top-level pairs may receive the same group without hurting optimality.
- **Deep single nesting:** Alternating levels gives the two groups depths differing by at most one.
- **Matched endpoint order:** Updating depth after an opening but before a closing is what guarantees equal assignments.
- **Valid-input guarantee:** The algorithm assumes depth never becomes negative and finishes at zero; it does not validate malformed parentheses.
- **Multiple optimal answers:** Swapping every zero and one yields another equally good split.
- **Output length:** Every original character is assigned exactly once, so the two subsequence lengths sum to the input length.
