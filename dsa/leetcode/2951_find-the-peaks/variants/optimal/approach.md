## General

An index $i$ is a peak only when it has two neighbors and its value is strictly greater than both:

$$
\texttt{mountain}[i-1]
<
\texttt{mountain}[i]
>
\texttt{mountain}[i+1].
$$

The first and last indices are excluded by definition, so the source examines exactly `range(1, len(mountain) - 1)`.

**List-comprehension structure**

For every interior index `i`, the condition

`mountain[i - 1] < mountain[i] > mountain[i + 1]`

is Python's chained comparison. It is equivalent to:

`mountain[i - 1] < mountain[i] and mountain[i] > mountain[i + 1]`.

The middle value is evaluated as the shared peak candidate. Both comparisons are strict.

If the condition succeeds, `i` is placed in the returned list. Otherwise it contributes nothing.

**Why local checks are enough**

The definition depends only on immediate neighbors, not on whether the value is a global maximum or whether the entire array rises and falls like one mountain. Therefore each interior position can be decided independently with two comparisons.

Take any returned index. Both strict relations passed, so it is a peak by definition.

Conversely, any genuine peak lies between indices $1$ and $n-2$ and satisfies those exact relations. The range visits it, and the condition includes it. Hence the result contains all and only peaks.

**Plateaus are not peaks**

If the candidate equals either neighbor, one strict comparison fails. For `[2,4,4]`, index one is not a peak because $4$ is not greater than the right neighbor $4$.

This differs from a non-strict local maximum definition. Replacing either comparison with `<=` in the wrong direction would incorrectly accept flat areas.

**Multiple peaks**

Peaks need not be separated by a long distance. In `[1,4,3,8,5]`, indices one and three independently satisfy the condition and are both returned.

Two adjacent interior indices cannot both be strict peaks because each would need to be greater than the other. The method does not need to enforce this explicitly; the comparisons make it automatic.

**Output order**

The problem allows any order. The range visits indices from left to right, and list comprehensions preserve iteration order, so the exact source returns peaks in increasing index order without sorting.

## Complexity detail

For an array of length $n$, the method checks $n-2$ interior positions. Each performs two constant-time comparisons, so time complexity is $O(n)$.

The comprehension allocates the required result list. Excluding output, auxiliary space is $O(1)$. If output storage is included, it is $O(p)$ for $p$ peaks and at most $O(n)$, matching the manifest's space bound.

An algorithm must inspect every interior value in the worst case because changing one unseen value could create or remove a peak.

## Alternatives and edge cases

- **Compare with the global maximum:** Incorrect; a local peak need not be globally greatest.
- **Track rising and falling trends:** It can find peaks, but direct neighbor comparisons are simpler and equally linear.
- **Sort values:** Sorting destroys index adjacency and cannot answer the question.
- **First index:** Never a peak because it lacks a left neighbor, even if greater than index one.
- **Last index:** Never a peak because it lacks a right neighbor.
- **Minimum length three:** Exactly one interior candidate is tested.
- **All equal values:** Strict comparisons fail everywhere, returning an empty list.
- **Strictly increasing array:** Every interior element has a larger right neighbor, so none is a peak.
- **Strictly decreasing array:** Every interior element has a larger left neighbor, so none is a peak.
- **Plateau beside a high value:** Equality on either side disqualifies the candidate.
- **Negative values would also work:** The proof uses only ordering, though the contract supplies positive integers.
- **Output order:** Increasing order is a deterministic bonus, not a requirement.
- **Chained-comparison evaluation:** Python evaluates the shared middle expression once conceptually and short-circuits if the left comparison fails, while preserving the exact two-inequality meaning.
- **Neighbor equality on one side:** Even if the candidate exceeds the other neighbor by a large amount, one equality is enough to disqualify it.
- **Valley detection is different:** Reversing both comparisons would find local minima. The source's directions point upward toward the middle from both sides.
- **No need to remember a previous trend:** Direct indexed access supplies both neighbors at once, so the list comprehension uses no rolling state.
- **Peak count bound:** Strict peaks cannot be adjacent, so output contains at most roughly half the interior indices, although $O(n)$ remains the appropriate bound.
- **Changing one endpoint value:** It may affect whether index one or $n-2$ is a peak, but endpoints themselves remain excluded; the scan still checks the affected interior candidate.
- **Any-order contract:** Returning sorted indices makes testing and reading deterministic without paying a sorting cost because traversal already has that order.
- **No mutation:** Comparisons leave the mountain array intact.
- **Why one pass is optimal:** An unexamined interior position could be changed to exceed both neighbors without affecting distant checks, so worst-case correctness requires considering every candidate index.
