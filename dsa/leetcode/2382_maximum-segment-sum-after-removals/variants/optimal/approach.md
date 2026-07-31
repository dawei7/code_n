## General

Processing the queries forward destroys connectivity: removing one position can split a segment, which ordinary disjoint-set union cannot represent. Reverse the process instead. Begin with every position inactive, then restore positions in the opposite query order. A restoration can only create a singleton segment or join it to active neighbors, exactly the operations disjoint-set union handles efficiently.

**Align reverse states with forward answers.** Before restoring the position removed by query `i`, the active positions are precisely those that remain after forward query `i`. Store the current maximum at `answer[i]`, then activate `remove_queries[i]` for the next reverse step. This ordering also puts `0` in the final forward answer, because the reverse process initially has no active segment.

**Maintain one sum per component.** Each active connected component is one remaining segment. Store its sum at the component representative. When a position becomes active, initialize its component sum from `nums[index]`. If its left or right neighbor is active, union their representatives and add their component sums.

All values are positive, so merging active adjacent segments never decreases their sum. Consequently, the greatest segment sum seen during reverse activation can only stay unchanged or increase. After processing the possible unions, compare the restored position's component sum with the running maximum; no ordered multiset of all component sums is needed.

At every reverse step, disjoint-set components coincide exactly with maximal contiguous runs of active positions: activation creates the only new run, and unions merge it with each adjacent run that touches it. Their stored sums are therefore the corresponding segment sums, and the saved running maximum is the required answer for the matching forward state.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. There are $n$ activations and at most two union operations per activation. With path compression, the total time is $O(n\alpha(n))$, where $\alpha$ is the inverse Ackermann function. The parent array, component sums, active flags, and answer use $O(n)$ space.

## Alternatives and edge cases

- **Forward ordered intervals:** Maintain surviving intervals in an ordered set and their sums in a multiset. Each removal can split one interval in $O(\log n)$ time, but the bookkeeping is more involved.
- **Repeated full scan:** Mark each removal and rescan the whole array to recompute every segment sum. This is correct but takes $O(n^2)$ time.
- **Answer timing:** Save `answer[i]` before restoring `remove_queries[i]`; saving it afterward represents the state before that forward removal.
- **Two active neighbors:** A restored position can bridge two distinct segments, so both adjacent unions must occur before its component sum is compared with the maximum.
- **Single position:** The only answer is zero because the sole element is removed by the first query.
- **Large sums:** Up to $10^5$ values of $10^9$ may share a segment, so implementations in fixed-width languages need 64-bit sums.
