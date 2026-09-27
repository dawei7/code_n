# Guided Example: Design Memory Allocator

A memory allocator of size $n$ owns a 0-indexed array of $n$ units. Every unit
is either free or carries an owner label `mID`. Two operations act on that
array:

- an allocation request asks for the **leftmost** run of `size` consecutive free
  units, claims the whole run for one `mID`, and reports the run's first index,
  or reports $-1$ when no run that long exists;
- a release request returns every unit carrying a given `mID` to the free state
  and reports how many units changed owner.

The whole difficulty of this Medium problem lives in two places: the allocation
must be the leftmost qualifying run rather than merely *some* qualifying run,
and it must be a run of consecutive units rather than that many free units
scattered anywhere. The trace below makes both requirements concrete and shows
exactly why a single sweep with a counter is enough.

## 1. The array of ownership labels

Model the allocator as a function

$$
\text{owner}: \{0, 1, \dots, n-1\} \to \{\bot\} \cup \mathbb{Z},
$$

where $\bot$ marks a free unit and an integer value is the `mID` currently
holding that unit. The two operations are then pure transformations of
`owner`.

For the allocation, define the **trailing free run length** at position $i$ as

$$
c(i) = \#\{k : 0 \le k \le i,\ \text{owner}(j) = \bot \text{ for all } j \in \{i-k, \dots, i\}\}.
$$

That is, $c(i)$ counts how many free units sit immediately to the left of $i$
in an unbroken chain ending at $i$. It satisfies a one-line recurrence:

$$
c(i) = \begin{cases} 0 & \text{if } \text{owner}(i) \neq \bot,\\ c(i-1) + 1 & \text{if } \text{owner}(i) = \bot. \end{cases}
$$

A run of `size` consecutive free units ends at the first index $i$ with
$c(i) = \text{size}$, and that run begins at $i - \text{size} + 1$. Because the
sweep visits indices in increasing order, this first hit is automatically the
**leftmost** qualifying run.

## 2. The representative command stream

Use the official example: an allocator over $n = 10$ units driven by eleven
commands. It exercises single-unit allocations, a release, a multi-unit
allocation into a hole, repeated blocks under one identifier, a release that
returns non-adjacent units, and finally a request that must fail.

| Call | Command | Argument(s) | Required return |
|:---:|:---|:---|:---:|
| 0 | construct | `n = 10` | none |
| 1 | observe | `allocate(1, 1)` | 0 |
| 2 | observe | `allocate(1, 2)` | 1 |
| 3 | observe | `allocate(1, 3)` | 2 |
| 4 | release | `freeMemory(2)` | 1 |
| 5 | observe | `allocate(3, 4)` | 3 |
| 6 | observe | `allocate(1, 1)` | 1 |
| 7 | observe | `allocate(1, 1)` | 6 |
| 8 | release | `freeMemory(1)` | 3 |
| 9 | observe | `allocate(10, 2)` | −1 |
| 10 | release | `freeMemory(7)` | 0 |

## 3. State evolution, call by call

Each column is one memory unit; `free` means $\bot$, and a number is the `mID`
holding that unit.

| After call | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 construct | free | free | free | free | free | free | free | free | free | free |
| 1 | 1 | free | free | free | free | free | free | free | free | free |
| 2 | 1 | 2 | free | free | free | free | free | free | free | free |
| 3 | 1 | 2 | 3 | free | free | free | free | free | free | free |
| 4 | 1 | free | 3 | free | free | free | free | free | free | free |
| 5 | 1 | free | 3 | 4 | 4 | 4 | free | free | free | free |
| 6 | 1 | 1 | 3 | 4 | 4 | 4 | free | free | free | free |
| 7 | 1 | 1 | 3 | 4 | 4 | 4 | 1 | free | free | free |
| 8 | free | free | 3 | 4 | 4 | 4 | free | free | free | free |
| 9 | free | free | 3 | 4 | 4 | 4 | free | free | free | free |
| 10 | free | free | 3 | 4 | 4 | 4 | free | free | free | free |

The counter trace that produced these results is worth reading field by field
for the two most interesting calls.

**Call 5, `allocate(3, 4)`, on the state `[1, free, 3, free, free, free, free, free, free, free]`:**

| Index $i$ | `owner(i)` | Counter before | Counter after | `c(i) = size`? |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 0 | 0 | no |
| 1 | free | 0 | 1 | no |
| 2 | 3 | 1 | 0 | no |
| 3 | free | 0 | 1 | no |
| 4 | free | 1 | 2 | no |
| 5 | free | 2 | 3 | yes, first hit |

The block ends at index 5, so it starts at $5 - 3 + 1 = 3$ and covers indices
3, 4, 5. Scanning further would be unnecessary: the sweep order guarantees that
no earlier run of length 3 exists, because index 3 is the first place the
counter reached 3.

**Call 8, `freeMemory(1)`, on the state `[1, 1, 3, 4, 4, 4, 1, free, free, free]`:**

| Index $i$ | `owner(i)` before | Equals `mID = 1`? | `owner(i)` after | Released so far |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | yes | free | 1 |
| 1 | 1 | yes | free | 2 |
| 2 | 3 | no | 3 | 2 |
| 3 | 4 | no | 4 | 2 |
| 4 | 4 | no | 4 | 2 |
| 5 | 4 | no | 4 | 2 |
| 6 | 1 | yes | free | 3 |
| 7 | free | no | free | 3 |
| 8 | free | no | free | 3 |
| 9 | free | no | free | 3 |

The released units at indices 0, 1 and 6 form two disjoint runs, but the release
does not care about adjacency: it returns the count $3$. This is the defining
difference between the two operations — allocation reasons about *runs*, release
reasons about *labels*.

## 4. The invariant that makes the sweep correct

State the claim precisely. Let $c(i)$ be the trailing free run length defined in
Section 1, and let $i^{*}$ be the smallest index with $c(i^{*}) = \text{size}$.

- **Soundness.** By induction on $i$, $c(i)$ equals the length of the maximal
  free run ending at $i$. The base case is $i = 0$; the recurrence in Section 1
  is exactly the induction step, since a free unit extends the previous run and
  an occupied unit terminates it. Hence $c(i^{*}) = \text{size}$ means indices
  $i^{*} - \text{size} + 1$ through $i^{*}$ are all free and consecutive, so
  claiming them is legal.
- **Leftmost.** If some qualifying run started at $s < i^{*} - \text{size} + 1$,
  then its last index $s + \text{size} - 1$ would satisfy
  $c(s + \text{size} - 1) = \text{size}$ and would be strictly smaller than
  $i^{*}$, contradicting minimality. So no legal run is skipped, and the reported
  offset is the smallest possible one.
- **Completeness of failure.** The sweep runs to the last index before reporting
  $-1$. If it ends without a hit, then $c(i) < \text{size}$ for every $i$, so no
  window of `size` consecutive free units exists anywhere and $-1$ is the only
  correct answer.

The recurrence also gives the section's invariant: throughout the sweep, the
counter holds exactly the length of the maximal free run ending at the current
index. Nothing about earlier indices needs to be remembered, which is why the
search needs $O(1)$ working memory.

## 5. The fragmentation trap

Call 9 asks for `allocate(10, 2)` when the state is
`[free, free, 3, 4, 4, 4, free, free, free, free]`. Counting free units gives 6,
and a tempting shortcut — "is the number of free units at least `size`?" — would
wrongly claim success. The requirement is a single consecutive run.

| Free run | Start index | Length | Adequate for `size = 10`? |
|:---|:---:|:---:|:---:|
| $R_1$ | 0 | 2 | no |
| $R_2$ | 6 | 4 | no |
| total free units | — | 6 | still no: two runs cannot be joined |

The longest run has length $4 < 10$, so the correct return is $-1$. The final
call, `freeMemory(7)`, finds no unit labelled 7 and therefore returns 0 while
leaving the array untouched — releasing an identifier that was never allocated is
legal and must not be treated as an error.

## 6. Boundaries worth remembering

| Situation | Correct behaviour | Why it is easy to get wrong |
|:---|:---|:---|
| Several blocks share one `mID` | one release frees every such block | a bookkeeping structure that maps each `mID` to a single block would leak the other blocks |
| A block is requested at index 0 | the run starts at 0 and the return value is 0 | 0 is a valid offset, so a sentinel test like "no position recorded" must not use 0 |
| `size` equals $n$ on an empty allocator | allocate the whole array and return 0 | the counter reaches `size` only at the final index $n-1$; an early-exit loop bound of $n - \text{size}$ misses it |
| `size` exceeds $n$ | return −1 immediately | the counter can never reach `size`, so the sweep must terminate cleanly rather than index past the end |
| A release of an unknown `mID` | return 0, change nothing | there is no error channel in the contract, so absence is a normal outcome |
| Free units split by an intervening block | they are separate runs | the counter must reset to 0 on an occupied unit rather than accumulate across it |

Two authored boundary cases follow directly from these rules. For $n = 4$, an
`allocate(4, 7)` claims the whole array and returns 0; the following
`allocate(1, 8)` returns −1 because nothing is free; `freeMemory(7)` returns 4
and reopens the array; `allocate(4, 8)` then returns 0 again. For $n = 6$,
`allocate(2, 1)` at 0 and `allocate(2, 2)` at 2 leave two free units at the tail,
and freeing `mID = 1` returns 2 while leaving 4 free units in two disjoint runs,
so the trailing `allocate(3, 3)` correctly returns −1.

## 7. Complexity: time and auxiliary space

Let $n$ be the number of memory units and $q$ the number of operations invoked.
One `allocate` call sweeps at most all $n$ units once and writes at most `size`
labels, so it costs $O(n)$ time. One `freeMemory` call inspects all $n$ units and
writes at most $n$ of them, so it also costs $O(n)$ time. Over the whole command
stream the time is $O(q \cdot n)$ worst case, which for the stated limits
$n \le 1000$ and $q \le 1000$ is at most about $10^6$ unit inspections.

The allocator itself must store one label per unit, so the state occupies
$\Theta(n)$ space; this is the data structure, not a cost of any single call.
The additional working memory of a call is $O(1)$: one running counter for
`allocate` and one running count for `freeMemory`, with no auxiliary array,
stack, or recursion. The primary time is therefore $O(q n)$ and the auxiliary
space per operation is $O(1)$, on top of the $\Theta(n)$ state.

| Design | `allocate` | `freeMemory` | Memory | Trade-off |
|:---|:---:|:---:|:---:|:---|
| Label array with a sweep and a counter | $O(n)$ | $O(n)$ | $\Theta(n)$ | smallest constant factor and the least code; every call pays a full scan |
| Sorted free-interval list | $O(\log n)$ to locate plus $O(n)$ to split and rewrite | $O(n)$ to find the blocks of that `mID` | $O(n)$ | fast placement but needs careful interval merging when neighbours are released |
| Balanced tree of free runs keyed by start | $O(\log n)$ amortised | $O(n \log n)$ | $O(n)$ | best asymptotics for placement, worst bookkeeping and bug surface |
| Free lists bucketed by run length | $O(1)$ amortised for an exact-fit bucket | $O(n)$ | $O(n)$ | does not naturally return the *leftmost* run, so it needs an extra ordering key |

Because the limits are small and the leftmost-run requirement is a first-hit
search, the label array with a single counter is the design whose cost matches
the problem's actual demands; the interval structures only start to pay when
$n$ is large and allocations are far more frequent than releases.