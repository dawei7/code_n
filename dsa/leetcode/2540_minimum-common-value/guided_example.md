# Guided Example: Minimum Common Value

## 1. The instance and what "common" means

Take the second official instance, `nums1 = [1,2,3,6]` and
`nums2 = [2,3,4,5]`, whose declared answer is $2$. An integer is **common** to the
two arrays when each array contains at least one occurrence of it, and the task is
to return the *minimum* common integer, or `-1` when the arrays share nothing.

This instance is the instructive one because it has two common values: $2$ and
$3$ both occur in each array. Returning "a common value" is therefore not enough;
the method must be able to certify that no smaller value is shared. The arrays are
given in **non-decreasing** order — `nums1` holds $1, 2, 3, 6$ and `nums2` holds
$2, 3, 4, 5$ — and that ordering is the resource the method spends.

| Common value | Present in `nums1`? | Present in `nums2`? | Eligible as the answer? |
|---|---|---|---|
| $1$ | yes, at index 0 | no, all of `nums2` is at least $2$ | no |
| $2$ | yes, at index 1 | yes, at index 0 | yes, and minimal |
| $3$ | yes, at index 2 | yes, at index 1 | yes, but not minimal |
| $6$ | yes, at index 3 | no, `nums2` stops at $5$ | no |

## 2. The state: two frontiers into two sorted arrays

Keep one index into each array, `i` for `nums1` and `j` for `nums2`, both starting
at $0$. The claim that makes two indices sufficient is an invariant:

> **Elimination invariant.** At the start of every iteration, no common value lies
> in `nums1` before index `i` or in `nums2` before index `j`.

The invariant holds trivially at the start, because both prefixes are empty. It is
maintained by comparing the two frontier values and discarding the smaller one:

- if `nums1[i] < nums2[j]`, then `nums1[i]` is not common. Every element of
  `nums2` from index `j` to the end is at least `nums2[j]`, hence greater than
  `nums1[i]`; and no element of `nums2` before index `j` can equal `nums1[i]`,
  because by the invariant nothing before index `j` is common to the arrays at
  all, while `nums1[i]` certainly does occur in `nums1`. So advancing `i` is safe.
- if `nums2[j] < nums1[i]`, the same reasoning with the roles swapped justifies
  advancing `j`.
- if the two frontier values are equal, that shared value is common, and the scan
  ends by returning it.

| State component | Meaning at the start of an iteration | Maintained how |
|---|---|---|
| `i` | everything in `nums1` before `i` has been proved not common | advanced when `nums1[i]` is the smaller frontier value |
| `j` | everything in `nums2` before `j` has been proved not common | advanced when `nums2[j]` is the smaller frontier value |
| frontier pair | the two smallest not-yet-eliminated values of the two arrays | recomputed by the comparison, in $O(1)$ |

```mermaid
flowchart TD
    accTitle: One iteration of the two-frontier scan
    accDescr: The two frontier values are compared; equality returns the value, and a strict inequality advances the pointer of the smaller side because that value cannot occur in the other array.
    A["compare nums1[i] with nums2[j]"] -->|equal| B["return nums1[i] as the minimum common value"]
    A -->|nums1[i] smaller| C["advance i: that value is absent from nums2"]
    A -->|nums2[j] smaller| D["advance j: that value is absent from nums1"]
    C --> E["repeat while both pointers are in range"]
    D --> E
    E -->|a pointer leaves its array| F["return -1: no common value exists"]
```

## 3. Executing the scan on `nums1 = [1,2,3,6]`, `nums2 = [2,3,4,5]`

| Step | `i` | `j` | `nums1[i]` | `nums2[j]` | Comparison | Action | Value eliminated, and why it is not common |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 1 | 2 | $1 < 2$ | advance `i` to 1 | $1$: every element of `nums2` from index 0 on is at least $2$ |
| 2 | 1 | 0 | 2 | 2 | $2 = 2$ | stop and return 2 | none — the frontiers agree |

The scan finds the answer in a single elimination. That is the point of the
method: it does not examine $3$, $4$, $5$, or $6$ at all, because once the
frontiers agree at $2$, the elimination invariant already certifies that no value
below $2$ is common. The value $3$ is common but *cannot* be returned, since the
scan stops at the first agreement, and the first agreement is necessarily the
smallest: a value can only be passed over by an elimination step, and every
eliminated value is provably absent from the other array.

## 4. A longer run: `nums1 = [1,5,9]`, `nums2 = [2,6,9]`

When the arrays interleave, the scan alternates sides and the accumulated
eliminations do the real work. Only the final entries $9$ and $9$ agree.

| Step | `i` | `j` | `nums1[i]` | `nums2[j]` | Comparison | Action | Elimination justification |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 1 | 2 | $1 < 2$ | advance `i` to 1 | `nums2` from index 0 onward is at least $2$ |
| 2 | 1 | 0 | 5 | 2 | $5 > 2$ | advance `j` to 1 | `nums1` from index 1 onward is at least $5$ |
| 3 | 1 | 1 | 5 | 6 | $5 < 6$ | advance `i` to 2 | `nums2` from index 1 onward is at least $6$ |
| 4 | 2 | 1 | 9 | 6 | $9 > 6$ | advance `j` to 2 | `nums1` from index 2 onward is at least $9$ |
| 5 | 2 | 2 | 9 | 9 | $9 = 9$ | stop and return 9 | none — the frontiers agree |

Four eliminations, then the answer. Note that the two pointers together advanced
exactly as far as needed and never beyond: each advancement discards one element
and never revises a decision, so the total number of comparisons is bounded by
`m + n - 1` for arrays of lengths `m` and `n`.

The opposite outcome has the same shape. For `nums1 = [1,2]` and
`nums2 = [3,4]`, step 1 eliminates $1$ (both `nums2` entries exceed it), step 2
eliminates $2$, and then `i` has left `nums1` entirely; the scan returns `-1`,
correctly reporting that the arrays are disjoint. Exhausting either array is
conclusive, because the elimination invariant then says that no common value
exists anywhere.

| Step | `i` | `j` | `nums1[i]` | `nums2[j]` | Comparison | Action |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 1 | 3 | $1 < 3$ | advance `i` to 1 |
| 2 | 1 | 0 | 2 | 3 | $2 < 3$ | advance `i` to 2 |
| 3 | 2 | 0 | out of range | 3 | — | `nums1` is exhausted, so return `-1` |

## 5. Why the first agreement is the minimum

Two claims together prove correctness.

**Every returned value is common.** The scan returns only when `nums1[i]` and
`nums2[j]` are equal, and those are genuine occurrences in their arrays, so the
returned integer occurs in both.

**No smaller common value is skipped.** Suppose $x$ is the smallest common value,
let $i^\*$ be its first occurrence in `nums1` and $j^\*$ its first occurrence in
`nums2`. All elements of `nums1` before $i^\*$ are strictly less than $x$, and
likewise for `nums2` before $j^\*$. While `i` is at most $i^\*$ and `j` at most
$j^\*$, both frontier values are at most $x$, so an advancement of `i` can only
happen when `nums1[i] < nums2[j] <= x`, which means `nums1[i] < x`, and an
advancement of `j` happens only when `nums2[j] < nums1[i] <= x`, which means
`nums2[j] < x`. Neither pointer can jump past its target occurrence, and the only
way the scan stops early is the equality at $(i^\*, j^\*)$, which returns exactly
$x$. If no common value exists, then every comparison eliminates a value and the
shorter array must be exhausted, so the `-1` branch is reached rather than an
infinite scan.

The invariant during the sweep is therefore: *the discarded prefixes contain no
common value, and the surviving frontiers are the smallest candidates left in
each array.* Since the answer is the smallest common value and the scan returns
the first agreement, the returned integer is the minimum.

## 6. Alternative designs, and what each one gives up

| Method | Time | Auxiliary space | Trade-off |
|---|---|---|---|
| Two frontiers on the sorted arrays | $O(m + n)$ worst case, and it stops at the answer | $O(1)$ | exploits both orderings and exits early at the minimum |
| Hash one array, scan the other for the minimum hit | $O(m + n)$ expected | $O(m)$ | works on unsorted input but always reads all of `nums2`, so it cannot stop early and pays for the set |
| Binary search each element of the shorter array | $O(m \log n)$ | $O(1)$ | better when one array is tiny, but ignores the early-exit structure and can be slower when both are large |
| Merge both arrays and inspect the run of equal neighbours | $O(m + n)$ | $O(m + n)$ | materializes a merged array to answer a question that needs only two indices |
| Sort first, then scan | $O(m \log m + n \log n)$ | depends on the sort | pure waste here, since the inputs are already in non-decreasing order |

The two-frontier scan is the only entry in that table that is simultaneously
linear, constant-space, and able to stop the moment the minimum is found.

## 7. Traps and boundary behaviour

| Instance | Situation | Behaviour | Answer |
|---|---|---|---|
| `[1,2,3]`, `[2,4]` | the common value sits in the middle of `nums1` | one elimination of $1$, then agreement at $2$ | 2 |
| `[1,2,3,6]`, `[2,3,4,5]` | two common values | the scan returns the first agreement, which is the smaller one | 2 |
| `[1,1,2,5]`, `[1,1,3]` | duplicates on both sides | duplicates are adjacent in sorted order, so the first occurrence is reached without any de-duplication | 1 |
| `[1,5,9]`, `[2,6,9]` | only the final entries agree | four alternations, then agreement at the last index pair | 9 |
| `[1000000000]`, `[1000000000]` | the largest allowed value, single entries | immediate agreement; no arithmetic is performed on the values, so no overflow is possible | 1000000000 |
| `[1]`, `[2,4]` | `nums1` is exhausted first | the elimination invariant plus exhaustion proves no common value | `-1` |
| `[1,1]`, `[2,4]` | repeated elements with no match | both copies are eliminated in turn, then `nums1` is exhausted | `-1` |

Conditions worth stating explicitly:

- **Minimum, not any match.** `[1,2,3,6]` and `[2,3,4,5]` share both $2$ and $3$;
  a method that collects all common values and then takes a maximum, or that
  returns the last agreement, answers $3$ and is wrong.
- **Equality must be tested before any advancement.** Advancing the smaller side
  first and only then comparing loses the agreement and drifts past the answer.
- **Exhaustion is an answer, not an error.** Reaching the end of either array
  proves no common value remains, and the required report is `-1`.
- **Only one pointer moves per comparison.** Advancing both on inequality is a
  common slip that skips past a value that the other array still holds.
- **Duplicates need no special handling.** Because the arrays are sorted, equal
  values are contiguous, so the first occurrence of the minimum is encountered at
  the frontiers without de-duplication, and the elimination argument never depends
  on values being distinct.
- **Both arrays are non-decreasing, not strictly increasing.** Reading the
  ordering as strict would wrongly justify skipping repeated values.
- **The values are never combined arithmetically.** Comparisons only, so the
  bound `nums1[i], nums2[j] <= 10^9` raises no overflow concern in any language.

## 8. Time and auxiliary space

Let $m$ and $n$ be the array lengths. Each iteration performs one comparison and
advances exactly one pointer, so the number of iterations is at most `m + n - 1`
before either an agreement or an exhaustion occurs. The running time is $O(m+n)$,
and on instances with a small common value it is far below that, because the scan
halts at the first agreement. Since no step can be skipped — a value must be
compared before it can be eliminated — the bound is tight in the worst case, so
the method is $\Theta(m+n)$ on inputs without early agreement.

Auxiliary space is $O(1)$: the two indices are the entire working state, and the
input arrays are read but never copied or rewritten. The output is a single
integer, so nothing proportional to the input size is allocated.