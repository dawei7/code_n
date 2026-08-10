## General

**Adding one edge toggles exactly two degree parities**

An undirected edge increases the degree of each endpoint by one. Therefore:

- an even endpoint becomes odd;
- an odd endpoint becomes even.

No other node changes parity.

The task is governed by the set of odd-degree nodes. Their exact degree values do not matter, except that existing adjacency determines which new edges are legal.

**Build adjacency sets and collect odd nodes**

For each edge `[a,b]`, the code inserts `b` into `g[a]` and `a` into `g[b]`. Sets serve two purposes:

- `len(g[v])` gives the degree;
- membership such as `a in g[b]` tells whether an edge already exists.

`vs` contains nodes whose adjacency-set length is odd.

Nodes absent from `g` have degree zero, which is already even, so omitting them from `vs` is correct. They remain available as possible intermediate nodes because `defaultdict(set)` supplies an empty adjacency set when accessed.

**Only zero, two, or four odd nodes can be repaired**

The handshaking lemma guarantees an even number of odd-degree vertices in every undirected graph. One added edge can toggle at most two odd nodes, and two edges can toggle at most four.

Consequently:

- zero odd nodes need no edges;
- two odd nodes may be fixable with one or two edges;
- four odd nodes require two edges;
- more than four cannot be fixed within the limit.

The code handles precisely these cases and returns false for every other count.

**Case zero: do nothing**

When `len(vs)==0`, every degree is already even. “At most two” permits adding no edges, so the method immediately returns true.

**Case two: connect directly or through one intermediate**

Let the odd nodes be `a` and `b`.

If they are not already adjacent, adding edge `(a,b)` toggles both from odd to even. No other parity changes, so one edge solves the graph.

If `a` and `b` are already adjacent, that edge cannot be added again. The alternative is to find a node `c` such that both missing edges `(a,c)` and `(c,b)` can be added.

Adding these two edges toggles `a` once and `b` once. Node `c` is toggled twice, so its original parity is restored. The test

`a not in g[c] and c not in g[b]`

checks exactly that both proposed edges are absent. Self-loop candidates cannot accidentally pass when `a-b` already exists: choosing `c=a` or `c=b` makes the other membership condition fail.

Scanning all node labels from 1 through `n` includes isolated nodes, which can be excellent intermediate choices because they have no existing edges.

**Case four: pair the odd nodes**

Let the odd nodes be `a,b,c,d`. Two added edges provide exactly four endpoint parity toggles. Each odd node must be used once; using an even intermediate twice would leave too few endpoint toggles to fix all four odds.

There are exactly three ways to partition four labeled nodes into two unordered pairs:

- $(a,b)$ with $(c,d)$;
- $(a,c)$ with $(b,d)$;
- $(a,d)$ with $(b,c)$.

The method tests all three. A pairing is valid only when both proposed edges are missing, because repeated edges are forbidden.

If any pairing passes, adding its two edges makes all four degrees even. If all fail, every parity-valid two-edge arrangement uses at least one existing edge, so the answer is false.

**Why no other arrangement is missing**

For two odd nodes, parity forces each to appear an odd number of times among added-edge endpoints. With at most two edges, the only possibilities are the direct edge or a two-edge path through a node toggled twice.

For four odd nodes, all four available endpoint occurrences must go to distinct odd nodes, forcing a pairing. Enumerating the three pairings is exhaustive.

This parity classification proves that every true return corresponds to legal edges that solve the graph, while every false return follows after all possible parity structures have been ruled out.

**Disconnected graphs require no special treatment**

New edges may connect nodes from different components. Degree parity is local to endpoints, and the goal does not require preserving or changing connectivity. Adjacency membership checks remain sufficient across disconnected components.

## Complexity detail

Let $m$ be the number of existing edges. Building two adjacency entries per edge takes expected $O(m)$ time. Collecting odd nodes is $O(n)$ worst case.

The zero- and four-odd cases use constant additional checks. The two-odd case may scan all `n` possible intermediate nodes, with expected $O(1)$ set membership per node. Total expected time is $O(n+m)$.

Adjacency sets store $O(n+m)$ structure and edge entries. The odd list holds at most $n$ nodes, so total auxiliary space is $O(n+m)$.

## Alternatives and edge cases

- **Degree array plus edge hash set:** Store degrees separately and encode edges in one global set; it gives the same asymptotic bounds.
- **Already all even:** Return true without adding anything.
- **Two nonadjacent odd nodes:** One direct edge is sufficient.
- **Two adjacent odd nodes:** A third node must be nonadjacent to both endpoints for the two-edge path.
- **Isolated intermediate:** It has even degree zero, receives two edges, and remains even.
- **Four odd nodes:** Test all three perfect matchings; there are no others.
- **More than four odd nodes:** Two edges cannot toggle enough endpoints.
- **Repeated edge restriction:** Every proposed pair must be absent from the adjacency sets.
- **Self-loops:** They are never proposed by a successful tested arrangement.
- **Disconnected input:** Component boundaries do not limit which legal new edges may be added.
