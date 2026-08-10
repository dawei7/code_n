## General

**Encode every reachable total as one bit**

Integer `f` is a bitset. Bit $x$ is 1 exactly when total reward $x$ is reachable after processing some reward values.

Initially only total zero is reachable, so `f = 1` has bit 0 set.

For a reward $v$, it may be chosen only from an old total $x<v$. Mask

`(1 << v) - 1`

has ones at positions 0 through $v-1$. Thus `f & mask` keeps precisely eligible reachable totals.

Shifting that bitset left by $v$ maps each eligible bit $x$ to new total $x+v$. OR with original `f` preserves the option to skip $v$:

`f |= (f & ((1 << v) - 1)) << v`.

This performs all valid transitions for one reward simultaneously.

**Why distinct sorted values are enough**

`nums = sorted(set(rewardValues))` removes duplicates. Once reward $v$ is selected, total becomes $x+v\ge v$, so another equal reward is no longer strictly greater than total. At most one copy of any value can ever be selected; duplicates cannot create a new sequence.

Sorting is not strictly required for the one-step bitset transition's local legality, but processing ascending values ensures every reachable total represented before $v$ was built from smaller values. It gives the standard 0/1-DP interpretation and makes the strict-threshold mask sufficient.

**Example**

For distinct rewards `[1,3]`:

- start reachable set is $\{0\}$;
- value 1 uses old totals below 1, adding total 1, so set becomes $\{0,1\}$;
- value 3 uses both 0 and 1, adding totals 3 and 4.

Maximum is 4.

For value 2 after total 3, bit 3 is removed by the below-2 mask, so illegal transition 3→5 is never created.

**Why no marked-index state is needed**

Every selected reward becomes no greater than new total and can never be selected again. Any unselected value already no greater than total is also permanently unusable because totals only increase.

Processing each distinct value once exactly captures these facts. The bitset needs only total, not a history of chosen indices.


After processing the first $p$ distinct rewards, bit $x$ is set if and only if some legal sequence using only those values reaches total $x$.

For next value $v$, legal sequences either skip it, preserved by old `f`, or use it last. In the latter case their prior total must be a reachable $x<v$, exactly selected by the mask, and shifting creates $x+v$. These cases are exhaustive and valid, so the invariant holds inductively.

At the end, the highest set bit is the maximum reachable total. For a positive integer bitset, `f.bit_length() - 1` is exactly that index.

**Bounded bitset**

If $V$ is maximum reward, immediately before choosing a final reward $v\le V$, total satisfies $x<v$. Final total is $x+v<2v\le2V$. Therefore, the meaningful bitset has only $O(V)$ positions even though many subsets exist.

The integer may contain gaps: a zero bit means that total cannot be produced by any legal ordering, not merely that no ordinary subset has that sum. The threshold mask is what distinguishes legal reward sequences from unrestricted subset sum.

Because each update reads old `f` on the right before assigning the OR result, current reward is used at most once in that iteration.

## Complexity detail

Let $n$ be input length, $V$ maximum reward, and $w$ machine word size.

Creating a set and sorting distinct values costs expected $O(n+n\log n)$, summarized as $O(n\log n)$. Each big-integer mask, AND, shift, and OR touches $O(V/w)$ words in the worst case. Across at most $n$ distinct values, time is $O(n\log n+nV/w)$.

The distinct list uses $O(n)$ space and the bitset uses $O(V/w)$ machine words, giving $O(n+V/w)$.

In Python, big-integer operation constants and allocations matter, but this word-parallel method is far faster than iterating every total in Python.

The input list is not modified because `sorted(set(...))` creates a new list.

## Alternatives and edge cases

- **Boolean-array DP:** Apply the same transitions with an array of reachable totals, costing $O(nV)$ scalar work.
- **Memoized total search:** ID 3180's exact source explores totals recursively and is slower for the larger constraints.
- **Keep duplicates:** Correct but repeats an update that cannot add useful double selections; deduplication saves work.
- **Reward equal to total:** It is illegal; the mask stops at bit $v-1$.
- **Single reward:** Reachable totals are zero and that reward, so the reward is returned.
- **All rewards equal:** Deduplication leaves one value, which can be selected once.
- **Skip option:** OR with old `f` preserves totals that do not use current reward.
- **Zero total:** Bit zero remains set throughout and allows starting with any positive reward.
- **Highest set bit:** `bit_length - 1` returns maximum total, not number of reachable totals.
- **Strict positivity:** Rewards are positive, so transitions always increase totals.
- **Total below 2V:** This ensures pseudo-polynomial storage remains bounded.
- **Sorted distinct copy:** Caller ordering and duplicates remain unchanged in the original list.
