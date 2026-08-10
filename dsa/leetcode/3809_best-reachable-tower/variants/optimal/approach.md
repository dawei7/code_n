## General

**Separate eligibility from ranking**

Every tower has three values: coordinates `x` and `y`, followed by quality `q`. A tower can win only if it is reachable from `center = [cx, cy]`. Reachability uses Manhattan distance:

$$
d = \lvert x-cx\rvert+\lvert y-cy\rvert.
$$

The radius is inclusive, so a tower is reachable when $d\le\texttt{radius}$. The source computes this distance once for each tower. If `dist > radius`, it immediately executes `continue`. That rejected tower never participates in any quality or coordinate comparison. This ordering makes the selection logic easier to reason about: every candidate reaching the comparison is already known to satisfy the geographic condition.

There is no need to sort all towers. The output needs only the single best reachable tower, and “best” defines a total priority:

1. greater quality is better;
2. when qualities are equal, lexicographically smaller coordinates are better.

Because only the current winner matters, a one-pass scan can maintain the best candidate seen so far.

**Store the winner's index**

The variable `idx` starts at -1. It is a sentinel meaning that no reachable tower has appeared yet. The loop uses `enumerate(towers)`, so `i` identifies the current tower while `x`, `y`, and `q` expose its three fields.

For every reachable tower, the source replaces `idx` when any one of three conditions holds:

- `idx == -1`: this is the first reachable tower, so it must provisionally win;
- `towers[idx][2] < q`: the current tower has strictly greater quality;
- `towers[idx][2] == q and towers[i][:2] < towers[idx][:2]`: quality ties, but the current coordinate is lexicographically smaller.

Python compares two lists lexicographically. For coordinates `[x, y]` and `[best_x, best_y]`, the expression first compares `x` with `best_x`. It consults `y` only if the two x-coordinates are equal. That is exactly the tie rule in the contract. Slicing with `[:2]` excludes quality from this comparison, so a tied quality cannot accidentally be compared a second time.

Storing an index instead of a separate quality and coordinate keeps the state compact. The current winning quality is always available as `towers[idx][2]`, and its coordinate is `towers[idx][:2]`. The input is not modified.

**Why discarding every nonwinner is safe**

After processing the first $k$ towers, `idx` is either -1 when none of those towers is reachable, or it identifies the highest-priority reachable tower among exactly those $k$ entries. Consider the next tower.

If it is unreachable, adding it to the inspected prefix cannot change the best reachable tower. If it is reachable and no winner exists, it becomes the winner. If its quality is greater than the winner's, it outranks the winner and replaces it. If quality ties and its coordinate is smaller, it also replaces the winner. In every remaining case, the current winner is at least as good: it has greater quality, or it has equal quality and a coordinate no larger than the newcomer's. The newcomer can therefore be forgotten permanently.

This argument repeats for every entry. Once the loop finishes, the maintained winner is the best reachable tower over the entire array. Notice that the result does not depend on input order. Input order determines when the provisional winner changes, but the quality-and-coordinate priority determines the final answer.

For the second example, both `[1,3,4]` and `[2,2,4]` are reachable and have quality 4. The first is initially stored. When the second is examined, `[2,2] < [1,3]` is false because 2 is greater than 1 in the first coordinate, so `[1,3]` remains the winner. The quality-7 tower is unreachable and is skipped before its quality can influence the result.

**Finish the sentinel case cleanly**

After the scan, `idx == -1` still means that every tower had distance greater than the radius. The source then returns `[-1, -1]`. Otherwise, `towers[idx][:2]` returns a new two-element list containing only the winning coordinates. A reachable tower at the literal coordinate `[-1, -1]` could make a sentinel ambiguous in some problems, but all coordinates here are nonnegative, so the prescribed result is unambiguous.

The algorithm uses the required order of decisions precisely. It never chooses high quality before checking reachability, never minimizes distance among reachable towers, and never applies the lexicographic rule across different qualities. Distance is only an admission test; it is not part of the ranking after admission.

## Complexity detail

Let $N=\lvert\texttt{towers}\rvert$. The loop visits every tower exactly once. Computing a Manhattan distance takes a constant number of subtractions, absolute-value operations, and additions. Each winner comparison is also constant time because the coordinate lists have exactly two elements. Therefore the total running time is $O(N)$.

The linear bound is optimal for an unsorted input. In the worst case, any unseen tower could be reachable and have a quality larger than every earlier tower, so a correct algorithm cannot safely stop before inspecting all $N$ entries. This gives an $\Omega(N)$ information requirement and makes the source's $O(N)$ time asymptotically tight.

The maintained state consists of `cx`, `cy`, `idx`, the loop variables, and `dist`. All have constant size independent of $N$, so auxiliary space is $O(1)$. The returned two-element coordinate list is also constant-sized. Python's loop unpacking and the temporary two-element slices used by a tie comparison allocate only bounded temporary objects; they do not accumulate across iterations.

## Alternatives and edge cases

- **Sort all reachable towers:** Filtering and sorting with a key such as `(-q, x, y)` gives the same winner, but sorting costs $O(N\log N)$ time and stores up to $O(N)$ candidates when only one is needed.
- **Use a heap:** A priority queue can encode maximum quality and lexicographic coordinates, but inserting all reachable towers costs $O(N\log N)$ time and additional space. A heap is useful for repeated extraction, not for one best item.
- **Use a tuple ranking key:** The one-pass idea can compare a constructed key such as `(-q, x, y)` and retain its minimum. That is equivalent to the explicit branches; the source's conditions expose the problem's priority rules more directly.
- **Radius zero:** Only towers exactly at `center` are reachable because Manhattan distance must be zero. Quality and lexicographic ordering still decide among multiple towers at that coordinate, although all such coordinates are identical.
- **Exactly on the boundary:** A tower whose distance equals `radius` is reachable. The source skips only when `dist > radius`, correctly preserving the inclusive boundary.
- **No reachable tower:** The sentinel remains -1, and the function returns `[-1, -1]` rather than coordinates from an arbitrary input entry.
- **All qualities equal:** The scan reduces to finding the lexicographically smallest coordinate among reachable towers. Each smaller coordinate replaces the current winner.
- **Duplicate coordinates:** The constraints do not state that coordinates are unique. If two reachable entries have identical coordinates and quality, keeping the earlier index is harmless because both yield the same requested coordinate. If their qualities differ, the higher-quality entry wins.
- **Quality zero:** Zero is a valid quality. The -1 sentinel tracks absence separately, so a reachable zero-quality tower is accepted correctly instead of being confused with “no candidate.”
- **Large coordinates:** The maximum coordinate differences and their sum fit comfortably in Python integers. Manhattan distance must use absolute differences; omitting either absolute value would incorrectly classify towers lying left of or below the center.
- **Input remains untouched:** The source only reads `towers` and returns a slice of the selected entry, so it does not reorder or mutate the caller's array.
