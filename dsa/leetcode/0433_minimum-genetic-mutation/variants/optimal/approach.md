## General
**Treat valid genes as an unweighted graph**

Each bank gene is a vertex. Two genes are adjacent when they differ at exactly one position, and the start is an additional source vertex. Every edge represents one mutation, so the required answer is an unweighted shortest-path distance.

**Generate the bounded set of possible neighbors**

For a dequeued gene, try each of its `L` positions and each of the four alphabet characters. A candidate is a usable neighbor only when it is still in the unvisited-bank set. Remove it immediately when enqueuing so no later path repeats its work.

**Use breadth-first levels as mutation counts**

Store each queued gene with its distance, or process the queue one level at a time. The first time `endGene` is generated, BFS has used the fewest possible edges because every earlier queue level contains strictly shorter mutation sequences.

**Why rejecting absent targets is safe**

Except for the already-equal zero-step case, the final mutated gene must itself be allowed. If `endGene` is absent from the bank, no valid path can finish there, so return `-1` before searching.

## Complexity detail
Let `B` be the bank size and `L` the gene length. Each bank gene is visited at most once and generates at most `4L` candidates, with $O(L)$ string construction under the fixed eight-character contract, conventionally written $O(BL)$ because $L = 8$. The unvisited set and queue use $O(B)$ space.

## Alternatives and edge cases
- **Scan the entire bank for every visited gene:** comparing Hamming distances is correct but takes $O(B^2L)$ time.
- **Prebuild every adjacency:** comparing all gene pairs before BFS also takes $O(B^2L)$ time and stores up to $O(B^2)$ edges.
- **Bidirectional BFS:** expands from both endpoints and can reduce the explored frontier while preserving the same worst-case class here.
- **Start equals target:** return zero without requiring a mutation.
- **Target absent from bank:** return `-1` unless no mutation is needed.
- **Cycles in the bank graph:** removing a gene when enqueued prevents repeated exploration.
- **Unreachable target:** exhaust the queue and return `-1`.
