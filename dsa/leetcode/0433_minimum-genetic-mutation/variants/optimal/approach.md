## General

**Model valid genes as an unweighted graph**

Treat each gene string as a vertex. Two genes have an edge when they differ in exactly one character, because one mutation changes precisely one position. The starting gene is a valid initial vertex even if absent from `bank`; every later vertex must come from the bank.

Every edge represents one mutation and has equal cost. The requested minimum number of mutations is therefore an unweighted shortest-path distance from `startGene` to `endGene`. Breadth-first search is the appropriate traversal because it visits vertices in nondecreasing distance from the start.

**Queue each gene with its distance**

The queue begins with `(startGene, 0)`, and `vis` initially contains `startGene`. The integer `depth` is the exact number of edges in the discovered path to `gene`.

When a pair is removed with `popleft()`, the code first checks `gene == endGene`. If true, it returns `depth`. This correctly handles `startGene == endGene` with answer zero, even if the target is not listed in the bank.

Because the queue is first-in, first-out, all states at depth $d$ are removed before states first discovered at depth $d+1$. The first target removal therefore has the smallest possible depth.

**Discover neighbors by comparing against the bank**

For the current gene, the solution loops through every string `nxt` in `bank`. It computes

`diff = sum(a != b for a, b in zip(gene, nxt))`.

The paired positions have equal fixed length, so each unequal character contributes `True`, which Python sums as one. `diff` is exactly the Hamming distance between the two gene strings.

When `diff == 1`, one legal mutation transforms `gene` into `nxt`. If `nxt` has not been visited, it is appended with `depth + 1` and marked immediately.

Marking at enqueue time is important. If marking waited until dequeue, several current-level genes could enqueue the same neighbor, wasting work and potentially expanding it multiple times. Immediate marking keeps one queue entry per gene string.

The loop does not generate arbitrary strings. Every discovered next state comes directly from `bank`, automatically enforcing mutation validity. The starting gene is the sole allowed exception.

**Why comparing every bank entry is complete**

Every valid next mutation must be a bank string differing in exactly one position. Scanning the entire bank tests that exact condition for every possible valid destination, so no graph edge from the current gene is omitted.

Strings differing in zero positions are the same state and are either already visited; strings differing in two or more positions would require multiple mutations and cannot be one BFS edge.

**Shortest-path proof**

The start enters at distance zero. Whenever a state at distance $d$ discovers an unvisited neighbor, that neighbor receives a real path of length $d+1$. FIFO ordering ensures no longer-distance state is processed before all shorter-distance states.

Suppose the target is first dequeued at depth $D$. Any path shorter than $D$ would have caused the target to be discovered from a state at depth at most $D-2$ and enqueued for an earlier layer, contradicting this first dequeue. Thus $D$ is minimal.

If the queue empties without the target, every bank gene reachable through a sequence of one-character differences has been visited. No valid path exists, so returning `-1` is correct.

**Example path**

From `"AACCGGTT"`, bank gene `"AACCGGTA"` differs only at the last position and enters at depth one. If the target is `"AAACGGTA"`, it differs from that intermediate at one additional position and enters at depth two. BFS returns two, while an unrelated bank string with several differences is never treated as an immediate mutation.

## Complexity detail

Let $B$ be `len(bank)` and $L$ the gene length. At most $B$ bank strings, plus the start, are dequeued. For every dequeued state, the exact implementation scans all $B$ bank entries, and each `zip`/sum comparison costs $O(L)$. Its generalized worst-case time is therefore

$$
O(B^2L).
$$

The variant manifest lists $O(BL)$, which would require avoiding a full bank rescan per visited state—for example by generating the $3L$ one-character alternatives and checking a bank hash set, or by preprocessing wildcard buckets. The exact code shown here performs the nested visited-state-by-bank comparison, so $O(B^2L)$ is the faithful bound. With the stated constants $B\le10$ and $L=8$, it remains very small in practice.

The queue and visited set hold at most $O(B)$ distinct gene strings, so auxiliary space is $O(B)$. Each queued tuple also stores one distance integer.

## Alternatives and edge cases

- **Generate all one-character mutations:** For each of $L$ positions, try the other three bases and test membership in a bank set. This reaches $O(BL)$ expected time after set construction and matches the manifest bound.
- **Wildcard-pattern buckets:** Map patterns such as `AACCGGT*` to genes, then retrieve neighbors through shared patterns. This is useful for larger banks but adds preprocessing machinery.
- **Depth-first search:** It can determine reachability but does not naturally guarantee the first found path is shortest; it would need exhaustive distance tracking.
- **Bidirectional BFS:** Search simultaneously from start and target to reduce explored layers in larger graphs. The bank limit is tiny, so ordinary BFS is simpler.
- **Target equals start:** The dequeue check returns zero immediately, independent of bank membership.
- **Target absent from bank:** Unless it equals the start, it can never be enqueued because every mutation destination is selected from `bank`, so the result is `-1`.
- **Empty bank:** Only the start is processed; a distinct target is unreachable.
- **Duplicate bank strings:** `vis` prevents duplicate string states from being enqueued more than once.
- **Difference zero:** A gene is not a one-mutation neighbor of itself and is not enqueued by `diff == 1`.
- **Difference greater than one:** It cannot be traversed in a single step, though intermediate bank genes may eventually connect it.
- **Mark on enqueue:** This prevents multiple shortest-path parents from creating duplicate queue entries while preserving the first, minimal depth.
