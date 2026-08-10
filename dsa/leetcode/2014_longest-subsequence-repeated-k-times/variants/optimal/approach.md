## General

**Discard characters that cannot appear once in the answer**

If character `c` occurs fewer than $k$ times in `s`, a candidate repeated $k$ times cannot contain even one `c`. `Counter(s)` finds frequencies, and `cs` retains only letters with count at least $k$.

Letters come from `ascii_lowercase`, so `cs` is in ascending lexicographic order.

The constraints give $n<8k$. Any valid candidate of length $L$ requires $kL$ selected characters, so $L\le\lfloor n/k\rfloor\le7$. The number of qualifying distinct letters is bounded by the same ratio, keeping candidate generation small.

**Check repeated subsequence membership greedily**

`check(t,k)` scans `s` once. Pointer `i` tracks the next character needed in one copy of `t`.

When a source character matches `t[i]`, the pointer advances. Completing one copy decrements `k` and resets `i` to zero for the next copy. Reaching zero copies returns true.

Greedily taking the earliest possible match is correct for subsequence testing: an earlier matched position leaves at least as much suffix for the remaining characters as any later choice.

If the scan ends first, `t * k` is not a subsequence and check returns false.

**Generate only extensions of valid prefixes**

The queue starts with the empty string. For each valid queued `cur`, the method appends every qualifying character to form `nxt`.

Only candidates passing `check` are saved as `ans` and enqueued for further extension.

This pruning is safe. If `nxt * k` is not a subsequence, no longer string beginning with `nxt` can be repeated $k$ times, because deleting its added suffix would imply that `nxt * k` was a subsequence.

**Why breadth-first search finds maximum length**

Every queue edge adds one character. FIFO traversal processes all valid candidates of length $L$ before candidates of length $L+1$.

`ans` is overwritten whenever a valid extension is found. Consequently, candidates found later at greater depth replace shorter ones, and the final answer has maximum length.

No explicit length bound is needed: once extensions require more than the available $n$ characters across $k$ copies, `check` rejects them and the queue stops growing.

Repeated letters do not make the search unbounded. If a candidate contains a character $r$ times, repeating the candidate $k$ times requires at least $rk$ copies of that character in `s`. Its finite frequency therefore caps $r$. More generally, every added candidate character consumes at least $k$ source positions across all repetitions, which is the same resource argument behind the seven-character maximum.

**Why the final tie is lexicographically largest**

Parents at each BFS depth are processed in lexicographic order, and `cs` is iterated from a through z. Their children are therefore generated in lexicographic order within the next depth, after invalid candidates are removed without changing relative order.

Because `ans` is assigned on every valid candidate, the last valid candidate at the deepest reachable level is the lexicographically largest among maximum-length answers.

**Trace a tiny example**

For `s="bb"` and $k=2$, only b qualifies. Candidate `"b"` passes because `"bb"` is a subsequence and is enqueued. Extension `"bb"` would require four b characters and fails. The final answer is b.

For `s="ab"` and $k=2$, no character occurs twice, `cs` is empty, and the queue produces no extension. The initial empty answer is returned.

For a tie such as two valid length-three candidates, BFS finishes every valid length-three string before exploring length four. Ascending child generation places the lexicographically greater length-three candidate later, so the overwrite policy retains it unless a longer valid string is subsequently found.

**Why the check does not index an empty candidate**

The helper is called only for `nxt = cur + c`, which always has at least one character. Although the queue begins with an empty string, `check` never receives it, so `t[i]` is safe.

## Complexity detail

Let $C$ be the number of candidate extensions tested, $L\le7$ maximum candidate length, and $N=\lvert s\rvert$. Each check scans at most $N$ characters, so time is $O(NC)$, with the qualifying alphabet size absorbed into $C$ as in the manifest.

The queue can hold candidate strings totaling $O(CL)$ character space. The frequency counter and qualifying-character list are bounded by 26.

## Alternatives and edge cases

- **Enumerate every string over 26 letters:** Vastly larger; frequency filtering and valid-prefix pruning are essential.
- **Generate candidates in descending order and stop:** Possible with careful depth handling, but the ascending overwrite policy is straightforward.
- **Materialize `t * k`:** Simpler subsequence checking but allocates up to $kL$ characters; the helper cycles through `t` instead.
- **Character frequency below `k`:** Cannot appear in any valid answer.
- **Repeated character in candidate:** Allowed when its total source frequency supports all $k$ copies.
- **Empty result:** Returned when no one-character candidate passes.
- **Multiple longest answers:** BFS order plus overwriting selects the lexicographically largest.
- **Greedy subsequence matching:** Earliest matches never reduce feasibility.
- **Maximum candidate length:** At most seven from $n<8k$.
- **Valid-prefix pruning:** Any invalid prefix makes every extension invalid.
- **Queue initialization:** Empty string seeds all one-letter candidates but is not itself checked.
- **Environment imports:** The source assumes `Counter`, `ascii_lowercase`, and `deque` are available.
