# Guided Example: Apply Operations to an Array

## 1. The representative instance and the two phases

Take the instance

$$\texttt{nums} = [1,\,2,\,2,\,1,\,1,\,0], \qquad n = 6 .$$

Every entry is a non-negative integer. The task has two distinct phases that must not be
mixed up.

**Phase 1 — the sequential scan.** For $i = 0, 1, \dots, n-2$ in that exact order, inspect
the pair at positions $i$ and $i+1$ of the array *as it currently stands*. If the two
values are equal, double the value at position $i$ and set position $i+1$ to `0`;
otherwise do nothing at all. The qualifier "as it currently stands" is the whole
difficulty: the operation at index $i$ changes what index $i+1$ will later compare.

**Phase 2 — the shift.** Move every `0` to the end of the array while preserving the
relative order of the non-zero values. The array keeps its length; only the positions of
its entries change.

For this instance the required output is

$$[1,\,4,\,2,\,0,\,0,\,0].$$

## 2. What the scan can do at one index

At index $i$ the scan reads two values and takes exactly one of three actions. The action
is determined only by the pair, never by the history of earlier steps.

| Case at index $i$ | Condition | Action | Effect on the count of zeros |
|:---|:---|:---|:---|
| Equal non-zero values | $\texttt{nums}[i] = \texttt{nums}[i+1] > 0$ | double the left value, zero the right one | increases by exactly $1$ |
| Equal zeros | $\texttt{nums}[i] = \texttt{nums}[i+1] = 0$ | double `0` and zero the right one — no visible change | unchanged |
| Different values | $\texttt{nums}[i] \ne \texttt{nums}[i+1]$ | skip | unchanged |

The second row is easy to overlook: it looks like a merge but rewrites `0` as `0`, so
existing zeros simply survive the scan. The list below makes the arithmetic explicit —
doubling is applied to the left member of the pair and the right member is overwritten:

- `nums[i] = 2 * nums[i]` when the pair matches, and `nums[i + 1] = 0` always in that case;
- nonzero values are never destroyed, only doubled in place;
- a doubled value is never examined again, because the scan moves strictly rightwards.

## 3. Worked trace of the scan

The instance `[1,2,2,1,1,0]` is chosen because it exercises a skip, two real merges, and a
no-op merge of two zeros in one pass.

| Index $i$ | Pair examined | Equal? | Action | Array afterwards | Zeros present |
|:---:|:---|:---:|:---|:---|:---:|
| start | — | — | — | `[1,2,2,1,1,0]` | `1` |
| 0 | `nums[0] = 1`, `nums[1] = 2` | no | skip | `[1,2,2,1,1,0]` | `1` |
| 1 | `nums[1] = 2`, `nums[2] = 2` | yes | `nums[1] = 4`, `nums[2] = 0` | `[1,4,0,1,1,0]` | `2` |
| 2 | `nums[2] = 0`, `nums[3] = 1` | no | skip | `[1,4,0,1,1,0]` | `2` |
| 3 | `nums[3] = 1`, `nums[4] = 1` | yes | `nums[3] = 2`, `nums[4] = 0` | `[1,4,0,2,0,0]` | `3` |
| 4 | `nums[4] = 0`, `nums[5] = 0` | yes | `nums[4] = 0`, `nums[5] = 0` | `[1,4,0,2,0,0]` | `3` |

Three details in this table carry the lesson.

1. The merge at index `1` writes a `0` at position `2`, so the very next step compares
   `0` with `1` and must skip. A new zero shields the following comparison.
2. The merge at index `3` doubles the value `1` into `2` at position `3`, and every
   later step works only with positions `4` and `5`, so the new `2` is frozen even though
   the equal value `2` that started at position `1` has already been doubled elsewhere.
3. The step at index `4` matches two zeros. It performs the doubling `0` and the
   assignment `nums[5] = 0`, yet nothing observable changes. Counting this step as a
   merge would wrongly predict a fourth zero.

After the scan the array is `[1,4,0,2,0,0]`; only the zero count grew, from one to three.

## 4. Why a run of equal non-zero values only merges pairwise

Sequentiality has a sharp consequence for a *run* of $k$ equal non-zero values occupying
consecutive positions. Let the run start at position $s$ with common value $v > 0$.

At index $s$ the pair matches, so position $s$ holds $2v$ and position $s+1$ holds `0`.
At index $s+1$ the scan compares that `0` with the run's third member $v$ and skips. At
index $s+2$ two run members meet again, and the pattern repeats every two indices. The run
therefore produces $\lfloor k/2 \rfloor$ doubled values, followed by one untouched copy of
$v$ if $k$ is odd, and the doubled values keep the run's original relative order.

| Run length $k$ | Merges $\lfloor k/2 \rfloor$ | Scan result for value `3` | After shifting zeros |
|:---:|:---:|:---|:---|
| 1 | 0 | `[3]` | `[3]` |
| 2 | 1 | `[6,0]` | `[6,0]` |
| 3 | 1 | `[6,0,3]` | `[6,3,0]` |
| 4 | 2 | `[6,0,6,0]` | `[6,6,0,0]` |
| 5 | 2 | `[6,0,6,0,3]` | `[6,6,3,0,0]` |

The tempting alternative is a *cascading* rule in which a doubled value may merge again
with its neighbour, as in a sliding-tile game.

| Instance | Result of the required sequential scan | Cascading rule (incorrect here) | Why they differ |
|:---|:---|:---|:---|
| `[2,2,2]` | `[4,2,0]` | `[4,4,0]` would need position `1` to hold two values at once | the pairs $(0,1)$ and $(1,2)$ overlap |
| `[2,2,2,2]` | `[4,4,0,0]` | `[8,0,0,0]` | the scan never revisits the doubled `4` |
| `[3,3,3,3]` | `[6,6,0,0]` | `[6,6,0,0]` | pairs $(0,1)$ and $(2,3)$ are disjoint, so the rules agree |

The middle row is the decisive trap: the doubled value sitting at position `0` is never
compared with the run again, so no carry propagates.

## 5. Shifting zeros: a stable filter, not a sort

Phase 2 does not order or compare values. It walks the post-scan array once from left to
right and keeps each non-zero value in the next free slot of the output, which leaves all
zeros at the far end. Stability is what makes the result well defined: the non-zero values
keep exactly the relative order they had after the scan.

| Source index | Value | Kept? | Destination index | Output so far |
|:---:|:---:|:---:|:---:|:---|
| `0` | `1` | yes | `0` | `[1,0,0,0,0,0]` |
| `1` | `4` | yes | `1` | `[1,4,0,0,0,0]` |
| `2` | `0` | no | — | `[1,4,0,0,0,0]` |
| `3` | `2` | yes | `2` | `[1,4,2,0,0,0]` |
| `4` | `0` | no | — | `[1,4,2,0,0,0]` |
| `5` | `0` | no | — | `[1,4,2,0,0,0]` |

Because a kept value always lands at a destination index no larger than its source index,
the filter can even be run inside the array it reads, writing each survivor just behind
the last one written. The number of trailing zeros is exactly the number of zeros present
after the scan — three for this instance — so the output is fully determined by the scan's
zero count and the surviving values in order.

## 6. Why the result is correct

Two claims together pin the answer down.

**The scan performs a left-to-right greedy pairing.** At each index the pair is examined
once, in increasing index order; a merge consumes both positions, immediately converts the
right one into a zero, and freezes the doubled left value because the scan never returns to
an index. The process is therefore deterministic and depends only on the array as it
evolves: every surviving non-zero value is either an original entry that never matched its
right neighbour, or a doubling of such an entry. Since the rule "double the left, zero the
right" is applied exactly when the *current* values are equal, no pair that the rule
requires is ever missed: the scan visits every index from $0$ to $n-2$.

**Shifting zeros preserves every non-zero value.** The filter copies each non-zero entry
exactly once, in order, into distinct slots, and fills the remaining
$n - (\text{number of non-zero entries})$ slots with zeros. The multiset of values is
therefore unchanged by Phase 2, and the relative order of the non-zero entries is
unchanged as well. Hence the output is the unique stable arrangement of the scanned array
with all zeros at the end.

A useful invariant to state explicitly: **after index $i$ has been processed, positions
$0$ through $i$ never change again.** The scan examines index $i$ and then index $i+1$,
and a merge at index $i$ touches only positions $i$ and $i+1$. This invariant is what
lets the whole first phase run in a single forward pass with no backtracking, and it is
also what forbids cascading merges.

## 7. Boundary cases and the traps they expose

The authored cases probe each row of the case table above; every entry below was checked
against the required output.

| Instance | Output | What it exposes |
|:---|:---|:---|
| `[1,2,2,1,1,0]` | `[1,4,2,0,0,0]` | one skip, two real merges, one no-op merge of zeros |
| `[0,1]` | `[1,0]` | the leading `0` has no equal neighbour, so only the shift acts |
| `[2,2,2]` | `[4,2,0]` | a run of three merges only once; the third value survives |
| `[3,3,3,3]` | `[6,6,0,0]` | disjoint pairs merge independently |
| `[8,4,7,0,0,6]` | `[8,4,7,6,0,0]` | the match `nums[3] = nums[4] = 0` changes nothing |
| `[0,0,1,1,1]` | `[2,1,0,0,0]` | existing zeros pass through the scan untouched |
| `[0,0,0,0]` | `[0,0,0,0]` | an all-zero array is already shifted |
| `[1,2,3,4,5]` | `[1,2,3,4,5]` | with no matches the array is returned unchanged |
| `[1]` | `[1]` | the shortest legal input has no pair to examine |
| `[1,1]` | `[2,0]` | the shortest possible merge |

Four traps are worth naming.

- **Presuming carries.** Doubling `2` into `4` does not license a further merge with a
  neighbouring `4`; the scan has already moved past that position.
- **Counting a zero-zero match as a merge.** It writes `0` over `0`; the number of zeros
  is unchanged, and the shifted output must show no extra zero.
- **Matching against the original array instead of the evolving one.** After a merge at
  index $i$, index $i+1$ holds `0`, so a comparison that ignores the write will believe a
  merge is available where the scan must skip.
- **Treating the shift as a sort.** The non-zero values `4` and `2` stay in the order
  `4, 2`; sorting them would break the required output.

## 8. Time and auxiliary-space complexity

**Time: $\mathcal{O}(n)$.** Phase 1 examines exactly $n-1$ index pairs, one comparison and
at most two assignments each, so it is $\Theta(n)$. Phase 2 reads all $n$ entries once and
writes each surviving value once, so it is $\Theta(n)$ as well. The two phases are
sequential and neither sorts nor searches, giving a total of $\Theta(n)$ elementary
operations with a small constant; for $n \le 2000$ this is trivially fast.

**Auxiliary space: $\mathcal{O}(n)$ for the returned array.** The canonical result is built
in a fresh buffer of $n$ slots — one write per kept value plus zero-initialised trailing
slots — so the extra working memory is linear in $n$ and is dominated by the output itself.
The scan phase needs only a single running index and two values, that is $\mathcal{O}(1)$
extra memory. A strict in-place variant of the shift exists because each survivor's
destination index is at most its source index; it needs no second buffer and therefore only
$\mathcal{O}(1)$ auxiliary space beyond the returned array.