## General

**Interpret every pair as a directed edge**

A pair `[start, end]` can precede another pair exactly when the first edge's destination equals the next edge's source. Using every pair once in one continuous arrangement is therefore the problem of finding an Eulerian trail in a directed multigraph.

`adjacency[start]` stores all destinations of outgoing edges. `balance` stores out-degree minus in-degree: it increases for each start and decreases for each end.

The existence guarantee implies the graph has either an Eulerian circuit, where all balances are zero, or an open Eulerian trail, where one start vertex has balance 1 and one end vertex has balance -1.

**Choose the required trail start**

The default is `pairs[0][0]`. That is valid for an Eulerian circuit because any vertex with an edge can start the cycle.

If a vertex with `difference == 1` exists, it has one extra outgoing edge and must start an open Eulerian trail. The loop finds it and replaces the default.

No sorting is needed because any valid arrangement may be returned.

**Consume edges with iterative Hierholzer traversal**

The stack holds the current unfinished walk. At its top vertex:

- if an outgoing edge remains, `pop()` consumes one edge and pushes its destination;
- if no edge remains, the vertex is popped from the stack and appended to `reversed_vertices`.

Appending only after all outgoing edges are consumed is the key. A locally chosen edge can enter a dead end before every edge has been placed. Postorder recording puts that dead end at the proper end of the eventual trail, while the stack resumes earlier branching points.

Each adjacency entry is popped exactly once, so every input pair is used exactly once.

**Reverse the postorder vertex sequence**

Vertices are finalized from the end of the Euler trail backward. Reversing `reversed_vertices` produces the forward vertex walk.

If there are $P$ edges, a complete Euler trail contains $P+1$ vertices. The final comprehension emits `[vertices[index], vertices[index + 1]]` for every index from 0 through $P-1$.

Consecutive output pairs connect automatically because the end of one is the shared vertex used as the start of the next.

**Why the algorithm is correct**

Every stack extension consumes a real unused input edge. Hierholzer's postorder construction splices closed detours into the surrounding trail implicitly: a vertex is finalized only when nothing remains to leave from it.

Starting at the balance-1 vertex when necessary satisfies the only possible open-trail endpoint condition. Under the promised existence conditions, traversal reaches and consumes every edge in the relevant graph.

After reversal, adjacent vertices correspond to consumed edges, all $P$ edges appear once, and every consecutive edge endpoint matches. The returned pairs therefore form a valid arrangement.

The adjacency lists are internal copies of destinations; popping them does not modify the input `pairs`.

**Trace how postorder avoids a premature dead end**

Consider edges `[1, 2]`, `[1, 3]`, and `[2, 1]`. Vertex 1 has one extra outgoing edge, so it is the trail start. If `pop()` first chooses edge `1 -> 3`, vertex 3 immediately has no outgoing edge and is appended to the reversed sequence. This does not incorrectly finish the whole answer. The stack still contains vertex 1, whose remaining edge can be consumed.

Traversal can then follow `1 -> 2 -> 1`. As those vertices run out of edges, they are appended. The recorded order is backward; reversing it places the earlier dead end at the final position and yields the connected trail `1 -> 2 -> 1 -> 3`.

This example shows why arbitrary edge choice is safe only together with postorder finalization. The algorithm does not claim the first walked sequence is already the answer. It builds a stack of unfinished trail fragments and fixes their order while unwinding.

**Relate degree balance to endpoints**

Every time an Euler trail enters an internal vertex, it must later leave through another unused edge, so incoming and outgoing usages balance. The trail start has one departure without a matching earlier arrival, giving balance 1. The trail end has one arrival without a later departure, giving balance -1.

All other vertices have balance zero. The source needs to search only for the balance-1 start; the guaranteed valid input ensures the corresponding end and connectivity conditions hold.

## Complexity detail

Let $P$ be the number of pairs.

Building maps, finding the start, consuming every edge, reversing the $P+1$ vertices, and constructing $P$ output pairs each take $O(P)$ total time.

The adjacency lists hold $P$ destinations. Degree maps, the stack, and the reversed vertex list also use at most $O(P)$ space. Auxiliary space is $O(P)$, and the required result is another $O(P)$.

Large vertex labels do not affect complexity because hash maps store only labels that occur.

## Alternatives and edge cases

- **Greedy output without postorder:** Committing edges directly can get trapped at a dead end before all edges are used. Hierholzer's postorder repairs branching choices.
- **Recursive Hierholzer:** It has the same logic and complexity but can overflow Python's recursion limit for $10^5$ edges.
- **Backtracking over permutations:** Exploring edge orders is exponential and ignores Eulerian structure.
- **Eulerian circuit:** No balance-1 vertex exists, so the first pair's start is a valid arbitrary start.
- **Open trail:** The unique balance-1 vertex must be selected.
- **One pair:** The walk has two vertices and reconstructs that pair directly.
- **Repeated endpoints:** Different pairs may share starts or ends; adjacency lists retain every edge occurrence.
- **Arbitrary pop order:** Any outgoing edge order is acceptable because any valid arrangement may be returned and existence is guaranteed.
- **Large sparse labels:** No array indexed by values is needed.
- **Input preservation:** Only constructed adjacency lists are consumed.
- **Output edge identity:** Reconstructing consecutive vertex pairs preserves edge multiplicity. Even when several edges share endpoints, each popped adjacency entry supplies one occurrence in the trail.
