## General

**Turn values into the relations that matter.** The pattern never depends on the magnitude of a number or on the difference between two neighbors. For each adjacent pair, compute `1` when the second value is larger, `0` when it is equal, and `-1` when it is smaller. A requested subarray matches exactly when its $m$ consecutive relation symbols equal `pattern`.

The relation sequence has length $n-1$, but it does not need to be stored. Generate one symbol at a time while scanning `nums`; this keeps the extra memory tied to the pattern length even when $n$ reaches $10^6$.

**Reuse partial matches with KMP.** Build the prefix-function array for `pattern`. At position $i$, the stored value is the length of the longest proper prefix of `pattern[0..i]` that is also its suffix. During the scan, `matched` records how many leading pattern symbols agree with the suffix of the relations processed so far.

If the next relation disagrees, repeatedly replace `matched` by the prefix value for the previous pattern position. Each fallback preserves the longest remaining suffix that could still extend into a match, without rereading any relation from `nums`. On agreement, advance `matched`. Reaching $m$ proves that the most recent $m$ relations equal the full pattern, so increment the answer and fall back once more. That final fallback is essential because it allows overlapping matches.

Every candidate window corresponds to one length-$m$ block of relation symbols, and KMP reports every occurrence of `pattern` in that sequence exactly once. Therefore the reported occurrence count is precisely the required subarray count.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and $m=\lvert\texttt{pattern}\rvert$. Building the prefix function costs $O(m)$. Across the scan, each increase and fallback of `matched` can be charged to linear KMP progress, so the $n-1$ generated relations cost $O(n)$. Total time is $O(n+m)$.

The prefix-function array uses $O(m)$ space. Relations are produced one at a time, so no $O(n)$ transformed array is retained.

## Alternatives and edge cases

- **Z-function matching:** Concatenate the pattern, a separator, and the relation sequence, then use Z-values to identify matches in $O(n+m)$ time. This is also asymptotically optimal but normally stores the entire transformed input and combined sequence, using $O(n+m)$ space.
- **Rolling hash:** Hashing relation windows can achieve expected linear time, but collision handling complicates an exact correctness guarantee; KMP is deterministic.
- **Direct window comparison:** Comparing all $m$ relations for every one of the $n-m$ starts costs $O((n-m)m)$ in the worst case, which is too slow for million-element inputs.
- **One relation:** When $m=1$, every adjacent pair is checked and overlapping is irrelevant; the same KMP logic applies without a special case.
- **Full-length pattern:** When $m=n-1$, there is exactly one candidate subarray, and the scan returns either zero or one.
- **Overlapping occurrences:** After a full match, falling back through the prefix function retains a valid border and permits the next match to share relations with the previous one.
- **Equal and extreme values:** Equality maps to `0`, while values as small as $1$ or as large as $10^9$ are only compared; subtraction and its overflow concerns are unnecessary.
