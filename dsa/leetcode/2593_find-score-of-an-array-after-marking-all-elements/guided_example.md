# Guided Example: Find Score of an Array After Marking All Elements

## 1. The rules are a simulation, not a search

Take `nums = [2,1,3,4,5,2]`. Nothing about the process is up to us: a round always takes the smallest unmarked value, ties are settled by the smaller index, that value is added to the score, and the chosen index together with its immediate neighbours becomes marked forever. The process repeats until every index is marked. Because each round is fully prescribed, the final score is a function of the input alone — there is no optimum to search for, only a simulation to run faithfully and quickly.

| Index $i$ | 0 | 1 | 2 | 3 | 4 | 5 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `nums[i]` | 2 | 1 | 3 | 4 | 5 | 2 |
| Note | ties with index 5 | current minimum | neighbour of index 1 | — | neighbour of index 5 | ties with index 0 |

Two features of this instance decide the whole lesson: the value 2 appears twice, at indices 0 and 5, and the array is *not* sorted, so the order in which values are consumed has nothing to do with position order.

## 2. What a single choice consumes

Choosing index $i$ marks the set $\{i-1, i, i+1\} \cap [0, n-1]$. The chosen element itself always joins the score; the neighbours never do, because a marked index is never chosen again.

| Candidate index $i$ | `nums[i]` | Indices marked if $i$ is chosen | Value added to the score |
|:---:|:---:|:---:|:---:|
| 0 | 2 | {0, 1} | 2 |
| 1 | 1 | {0, 1, 2} | 1 |
| 2 | 3 | {1, 2, 3} | 3 |
| 3 | 4 | {2, 3, 4} | 4 |
| 4 | 5 | {3, 4, 5} | 5 |
| 5 | 2 | {4, 5} | 2 |

Three facts follow immediately and are used constantly below.

- **Marking is permanent.** A marked index never returns to the unmarked pool, so the unmarked set only shrinks.
- **Chosen indices are non-adjacent.** If $i$ is chosen, $i \pm 1$ is marked at once, so no later round can choose a neighbour of $i$. The chosen indices form an independent set in the path graph on $0, \dots, n-1$.
- **The minimum is non-decreasing.** Successive rounds see a subset of the previous unmarked values, so the sequence of chosen values is non-decreasing — here $1, 2, 4$.

## 3. Maintaining "smallest unmarked" with a min-heap

Recomputing the minimum with a linear scan costs $O(n)$ per round and $O(n^2)$ in total, which is far too slow for $n = 10^{5}$. Instead, load every pair `(value, index)` into a min-heap once, ordered by value and then by index, and treat the heap as a **superset** of the unmarked indices:

- every unmarked index still has its pair somewhere in the heap, and
- a marked index may also still have its pair in the heap, in which case that entry is *stale*.

| Heap rank | 1 | 2 | 3 | 4 | 5 | 6 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Key `(value, index)` | (1, 1) | (2, 0) | (2, 5) | (3, 2) | (4, 3) | (5, 4) |

The heap order compares value first and index second, so the two copies of 2 sort as `(2, 0)` before `(2, 5)`. That is exactly the tie rule the problem states, provided the entry at the top is still unmarked. This is why the heap alone is never trusted: the top key is the smallest *heap* entry, and only after checking the marked array do we know whether it is the smallest *unmarked* element.

## 4. The trace on `[2,1,3,4,5,2]`

Each loop iteration looks at the top entry. A stale key is discarded and the next key is examined; the first entry whose index is unmarked is chosen and popped.

| Round | Heap top examined | Index already marked? | Action | Score after | Marked set after |
|:---:|:---:|:---:|:---|:---:|:---|
| 1 | (1, 1) | no | Choose index 1, add 1, mark indices 0, 1, 2 | 1 | {0, 1, 2} |
| 2 | (2, 0) | yes | Discard the stale entry without touching the score | 1 | {0, 1, 2} |
| 2 | (2, 5) | no | Choose index 5, add 2, mark indices 4, 5 | 3 | {0, 1, 2, 4, 5} |
| 3 | (3, 2) | yes | Discard the stale entry | 3 | {0, 1, 2, 4, 5} |
| 3 | (4, 3) | no | Choose index 3, add 4, mark indices 2, 3, 4 | 7 | {0, 1, 2, 3, 4, 5} |
| 4 | (5, 4) | yes | Discard the stale entry; the heap is now empty | 7 | all indices |

The simulation stops after round 3, because every index is marked even though the heap still holds entries. The final score is $1 + 2 + 4 = 7$.

Round 2 is the heart of the lesson. The smallest key overall is `(2, 0)`, but index 0 was consumed as a neighbour in round 1. A simulation that popped the smallest key unconditionally would add 2 a second time and report 9 for this input. The equal-valued entry `(2, 5)` is the one that actually satisfies the rules, and it is reachable only after the stale key is removed.

## 5. Where the score comes from, index by index

| Index $i$ | `nums[i]` | Marked in round | Marked as | Added to the score |
|:---:|:---:|:---:|:---|:---:|
| 0 | 2 | 1 | neighbour of chosen index 1 | no |
| 1 | 1 | 1 | the chosen element itself | yes, $+1$ |
| 2 | 3 | 1 | neighbour of chosen index 1 | no |
| 3 | 4 | 3 | the chosen element itself | yes, $+4$ |
| 4 | 5 | 2 | neighbour of chosen index 5 | no |
| 5 | 2 | 2 | the chosen element itself | yes, $+2$ |

Since marking is permanent and choosing an index marks it, no index can contribute twice: the score is precisely the sum of `nums[i]` over the indices chosen during the simulation. Note how much value the neighbourhoods swallow here — the 5 is destroyed by the 2 at index 5, and the 3 is destroyed by the 1 at index 1 — so the score 7 is far below the sum of the array, which is 17.

## 6. Invariant and correctness of the heap simulation

**Invariant.** At the start of every round: (a) each unmarked index has exactly one entry in the heap; (b) the marked set only grows; (c) the accumulated score equals the sum of `nums[i]` over the indices chosen so far.

**Lazy deletion is sound.** An entry whose index is marked can be dropped, because marking is permanent and that index can never be chosen again. Dropping it cannot remove a candidate the rules would ever accept.

**The top unmarked entry is the prescribed choice.** Suppose the first non-stale entry is `(x, i)`. Every entry ahead of it in heap order was stale, and every remaining entry is compared against it by value first: an unmarked index $j$ with `nums[j] < x` would sort strictly before `(x, i)` and would not be stale, contradicting that `(x, i)` comes first. If some unmarked $j$ had `nums[j] = x` and $j < i$, that entry would sort before `(x, i)` as well. So `x` is the smallest unmarked value and $i$ is the smallest index carrying it — exactly the tie-broken choice the problem prescribes.

**Termination.** Every loop iteration pops one entry. A round either discards one stale entry or marks at least one previously unmarked index, so at most $n$ choices and $n$ discards occur before the heap empties and all indices are marked. The simulation therefore always finishes, and since no step offers a decision, the score it produces is the unique score the process defines.

## 7. Traps, tie-breaks and boundaries

| Strategy | Score on `[2,1,3,4,5,2]` | Verdict |
|:---|:---:|:---|
| Pop the smallest key without consulting the marked array | 9 | Wrong: it selects index 0 in round 2, which the rules already marked |
| Rescan the array for the minimum each round | 7 | Correct but $O(n^2)$, roughly $10^{10}$ comparisons at $n = 10^{5}$ |
| Sort indices by `(value, index)` once and sweep with a marked array | 7 | Correct; logically the heap without the heap, and it needs the same staleness check |
| Delete both neighbours from the heap eagerly when marking | 7 | Correct, but positional deletion from a binary heap is not free; lazy marking is cheaper |
| Take the $\lceil n/2 \rceil$ smallest values of the array | 5 | Wrong: neighbourhoods swallow values by position, so which values count depends on adjacency |

A second trap is the tie rule itself. On `[2,3,5,1,3,2]` the two trailing 2s tie: the leftmost unmarked one, index 0, is chosen in the second round and marks index 1, after which only index 5 remains and contributes 2. Choosing the other 2 first would leave index 0 to be chosen later and would change the score. The order $(\text{value}, \text{index})$ is part of the contract, not an implementation detail.

| Instance | Score | What it teaches |
|:---|:---:|:---|
| `[1]` | 1 | A single index has no neighbours, so it is always chosen |
| `[1,2]` | 1 | Choosing index 0 marks index 1; the larger value never counts |
| `[2,1]` | 1 | The right-hand minimum marks its left neighbour and reaches the same total |
| `[1,1,1]` | 2 | Ties resolve left to right: index 0 is chosen, index 1 is marked, index 2 survives and is chosen |
| `[4,4,4,4,4,4]` | 12 | Equal values are consumed every other index; index 5 is never chosen |
| `[3,1,2,1,3]` | 2 | An earlier equal valley suppresses a later one because their neighbourhoods overlap |
| `[1000000,1,1000000]` | 1 | Even the largest legal value adds nothing when a neighbour is chosen first |

One more boundary deserves attention in languages with fixed-width integers: with $n \le 10^{5}$ and `nums[i]` $\le 10^{6}$, the score can reach $10^{11}$, which does not fit in a 32-bit signed accumulator even though every input value does.

## 8. Time and auxiliary space complexity

Let $n = \texttt{nums.length}$.

- **Building the structure** costs $O(n)$ to materialize the pairs plus $O(n)$ to heapify them.
- **The simulation** pops each entry at most once: at most $n$ choices and at most $n$ stale discards, and each pop or push costs $O(\log n)$. The total running time is $O(n \log n)$.
- **Auxiliary space** is $O(n)$: the heap holds one pair per index plus the marked flags, and the score is a single accumulator. No recursion or graph structure is involved.

The bounds are driven by $n$ alone; the value range $1 \le \texttt{nums}[i] \le 10^{6}$ affects only the magnitude of the answer, not the cost of computing it.
