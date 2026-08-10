## General

A directed edge `u -> v` says team $u$ is stronger than team $v$. Therefore every incoming edge to $v$ is direct evidence that some team is stronger than $v$. Such a team cannot be champion.

This reduces the problem to indegrees:

- indegree zero means no recorded stronger team points to this team, so it is a champion candidate;
- positive indegree means the team is definitely not champion;
- the answer is valid only when exactly one team has indegree zero.

The source allocates `indeg = [0] * n` and scans every edge. For `(_, v)` it increments `indeg[v]`. The starting endpoint is irrelevant to the count beyond establishing that an incoming edge exists at $v$.

**Why zero indegree matches the definition**

If a team has an incoming edge, the edge's source is stronger, so the team fails the champion condition immediately.

If a team has no incoming edge, no other team is declared stronger than it. The reference graph is a DAG representing the strength relations, including the stated transitive consistency. Thus it is a source of the strength ordering and satisfies the definition of a possible champion.

There can be several sources in a DAG. When that happens, none has a stronger incoming team, but the contract asks for a champion only if it is unique. The algorithm must count all zero entries rather than return the first.

**Exact final selection**

`indeg.count(0)` scans the array and obtains the number of source teams. If that number is not one, the source returns `-1`.

If it is exactly one, `indeg.index(0)` finds and returns that sole source's label. Calling `index` only in this branch is safe because existence and uniqueness have already been established.

For $n=4$ with edges `[[0,2],[1,3],[1,2]]`, indegrees are `[0,0,2,1]`. Teams $0$ and $1$ both have zero indegree, so there is no unique champion and the result is `-1`.

For edges `[[0,1],[1,2]]`, indegrees are `[0,1,1]`. Only team $0$ is unmarked and is returned.

**Why reachability does not need to be computed**

One might think a champion must reach every other node through directed paths. Under a unique-source DAG, every node is reachable from that source: if some node were unreachable, following its incoming predecessors backward within the finite DAG would eventually reach another zero-indegree source, contradicting uniqueness.

The local definition itself asks only that no stronger team exists, so incoming-edge marking is already direct. Transitive closure, topological sorting, and graph traversal are unnecessary for selecting the unique source.


Every returned team has indegree zero, so no edge identifies a stronger team. Uniqueness of the zero ensures there is no second champion candidate.

If a unique champion exists, it cannot have an incoming edge and therefore appears among the zero-indegree entries. Any other zero-indegree team would also have no stronger team and contradict uniqueness. Hence the count is exactly one and the algorithm returns the champion.

## Complexity detail

Let $m$ be number of edges. Initializing the indegree array takes $O(n)$ time. Scanning edges takes $O(m)$. `count` and, in the successful case, `index` each take $O(n)$. Total time is $O(n+m)$.

The indegree array contains $n$ integers, so auxiliary space is $O(n)$. The method does not build an adjacency list because edge destinations alone are sufficient.

## Alternatives and edge cases

- **Topological sort:** It also begins with indegrees but maintaining a queue and removing nodes is unnecessary when only the number of initial sources matters.
- **Build an adjacency list:** Useful for reachability questions, but redundant here; every required update is determined directly by an edge destination.
- **Transitive closure:** Computing all strength relationships would cost much more and does not change which vertices have incoming edges.
- **No edges:** Every team has indegree zero. Return the sole team only when $n=1$; otherwise return `-1`.
- **One team:** Its indegree is zero, so it is the unique champion.
- **Duplicate edges:** The declared graph data normally treats edges as entries; duplicates would raise an indegree further but would not change zero-versus-positive classification.
- **Multiple zero-indegree teams:** Do not arbitrarily pick one. The required answer is `-1`.
- **Positive indegree magnitude:** Only whether it is zero matters; counting rather than Boolean marking remains simple and standard.
- **DAG guarantee:** Cycles are excluded. The zero-indegree logic still rejects cycle vertices, but an all-cycle graph could have no source and returns `-1`.
- **Why outgoing edges are unnecessary:** A champion may be connected to weaker teams indirectly. Its defining feature is absence of a stronger predecessor, which incoming-edge marking captures without counting victories.
- **Disconnected components:** A DAG with multiple disconnected components has at least one source in each, so it cannot have a unique champion unless only one component supplies all nodes through reachability.
- **Two linear scans of indegree:** `count` followed by `index` is still $O(n)$; combining them in one loop would only improve a constant factor.
