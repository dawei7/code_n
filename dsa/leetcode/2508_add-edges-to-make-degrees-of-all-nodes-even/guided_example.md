# Guided Example: Add Edges to Make Degrees of All Nodes Even

## 1. What a single added edge actually changes

The graph is undirected, may be disconnected, and may contain isolated nodes. The
only property under examination is *degree parity*: we want every node to end
with an even number of incident edges.

An added edge $\{u, v\}$ with $u \neq v$ increases $d(u)$ by one and $d(v)$ by
one. Every other node keeps its degree, and no edge ever touches a node twice.
So the entire effect of one added edge is:

$$
d(u) \bmod 2 \;\mapsto\; (d(u) + 1) \bmod 2, \qquad
d(v) \bmod 2 \;\mapsto\; (d(v) + 1) \bmod 2,
$$

with all other parities untouched. One edge therefore **flips exactly two node
parities**, and which two is exactly the choice we control. That single sentence
carries the whole case analysis:

- The set of odd-degree nodes must be fixed completely, so its size can only be
  $0$, $2$, or $4$ when at most two edges may be added.
- Any node that receives two new edges has both flips cancel, so it returns to
  its original parity.

Two structural facts follow. The handshake lemma (the degree sum is twice the
edge count) forces the number of odd-degree nodes to be **even**, so a count of
$5$ can never occur. And an isolated node, whose degree is $0$ and therefore
even, is a legitimate and often decisive middle node.

## 2. The representative instance: the official `n = 5` graph

Consider the statement's first example, with $n = 5$ and edges
`(1,2)`, `(2,3)`, `(3,4)`, `(4,2)`, `(1,4)`, `(2,5)`. Building the neighbour
sets gives the raw state on which every later decision depends.

| Node | Neighbours | Degree $d(v)$ | $d(v) \bmod 2$ | Classification |
|:---:|:---|:---:|:---:|:---|
| 1 | 2, 4 | 2 | 0 | even |
| 2 | 1, 3, 4, 5 | 4 | 0 | even |
| 3 | 2, 4 | 2 | 0 | even |
| 4 | 3, 2, 1 | 3 | 1 | odd |
| 5 | 2 | 1 | 1 | odd |

The odd set is $O = \{4, 5\}$. Two anomalies need two flips, which is the budget
of a single added edge. Node 4 is adjacent to 1, 2, 3, and node 5 is adjacent to
2; because `4` never appears in the neighbour set of 5, the pair is
non-adjacent and the edge `(4,5)` is legal. Adding it changes the table into:

| Node | Degree before | Flip from `(4,5)` | Degree after | Parity after |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 2 | 0 | 2 | even |
| 2 | 4 | 0 | 4 | even |
| 3 | 2 | 0 | 2 | even |
| 4 | 3 | $+1$ | 4 | even |
| 5 | 1 | $+1$ | 2 | even |

Every parity is even, only one of the two permitted edges was used, and the
instance is therefore answerable `true` — exactly the expected result for this
official input.

## 3. The two-odd case: one edge, or one intermediate node

With $O = \{a, b\}$ there are two ways to spend the budget.

**Direct repair.** If `(a,b)` is not already an edge, add it. Both odd nodes flip
and everything becomes even. This is the situation in the traced `n = 5` graph.

**Repair through a middle node.** If `(a,b)` already exists, it cannot be added
again. Instead pick any node $c \notin \{a, b\}$ such that neither `(a,c)` nor
`(c,b)` is an existing edge, and add both. Node $a$ and node $b$ each flip once;
node $c$ flips **twice**, so its parity is unchanged. Because only $a$ and $b$
were odd, $c$ was even before and stays even — the middle node is free of charge
parity-wise. This is why an isolated node is such a valuable candidate.

The authored case `trial-intermediate-node` (with $n = 5$ and edges `(1,2)`,
`(1,3)`, `(2,3)`, `(1,4)`, `(2,4)`) blocks the direct repair and forces exactly
this search. Its odd set is $\{1, 2\}$, and the candidate middle nodes are
checked one at a time:

| Candidate $c$ | `(1,c)` exists? | `(c,2)` exists? | Verdict | Reason |
|:---:|:---:|:---:|:---|:---|
| 3 | yes | yes | rejected | both proposed edges already exist |
| 4 | yes | yes | rejected | both proposed edges already exist |
| 5 | no | no | accepted | two legal edges, and node 5 is even with degree 0 |

Choosing $c = 5$ adds `(1,5)` and `(5,2)`: nodes 1 and 2 become even, node 5
rises from degree 0 to degree 2 and remains even, and nodes 3 and 4 are
untouched. The expected answer is `true`, and the decisive reason is that a
*degree-zero* node existed to absorb the second flip.

## 4. When even the middle node is impossible

Not every adjacent odd pair can be repaired. Take the authored case
`trial-adjacent-pair-blocked`: $n = 4$ with edges `(1,2)`, `(1,3)`, `(2,3)`,
`(1,4)`, `(2,4)`. Degrees are $d(1) = 3$, $d(2) = 3$, $d(3) = 2$, $d(4) = 2$, so
$O = \{1, 2\}$ and `(1,2)` already exists.

| Candidate $c$ | `(1,c)` exists? | `(c,2)` exists? | Verdict | Reason |
|:---:|:---:|:---:|:---|:---|
| 3 | yes | yes | rejected | edge `(1,3)` and edge `(3,2)` both present |
| 4 | yes | yes | rejected | edge `(1,4)` and edge `(4,2)` both present |

There is no other node: the graph has only four nodes, and every remaining
candidate touches an odd endpoint. Every legal edge incident to node 1 already
exists, and the same holds for node 2, so no pair of fresh edges can be
manufactured. The answer is `false`. The lesson is that the failure here is
*saturation*, not parity: the degrees are repairable in principle, but the graph
offers no free slot to repair them in.

## 5. The four-odd case: choose one of three pairings

With $O = \{a, b, c, d\}$ the budget must be spent as two disjoint pairs, and the
order of pairing is the only decision. There are exactly three ways to partition
four elements into two unordered pairs:

$$
\{a,b\}\{c,d\}, \qquad \{a,c\}\{b,d\}, \qquad \{a,d\}\{b,c\}.
$$

A pairing is feasible when **neither** of its two pairs is an existing edge. The
official third example ($n = 4$, edges `(1,2)`, `(1,3)`, `(1,4)`) is the failing
instance: all four nodes have odd degree, because node 1 has degree 3 and nodes
2, 3, 4 have degree 1 each.

| Pairing | First pair legal? | Second pair legal? | Outcome |
|:---|:---|:---|:---|
| $\{1,2\}$ and $\{3,4\}$ | no: `(1,2)` exists | yes, `(3,4)` is free | rejected |
| $\{1,3\}$ and $\{2,4\}$ | no: `(1,3)` exists | yes, `(2,4)` is free | rejected |
| $\{1,4\}$ and $\{2,3\}$ | no: `(1,4)` exists | yes, `(2,3)` is free | rejected |

Node 1 is joined to all three other nodes, so whichever pair it is placed in is
already an edge. All three partitions fail and the answer is `false`, matching
the official expectation. Note that the second pair in each row is always legal —
the obstruction is entirely caused by the hub node.

The authored case `trial-four-odd-alternate-pairing` shows the opposite outcome
for the same shape of odd set. With $n = 5$ and edges `(1,2)`, `(1,3)`, `(1,5)`,
`(5,4)`, the degrees are $d(1) = 3$, $d(2) = 1$, $d(3) = 1$, $d(4) = 1$, and
$d(5) = 2$, so $O = \{1, 2, 3, 4\}$:

| Pairing | First pair legal? | Second pair legal? | Outcome |
|:---|:---|:---|:---|
| $\{1,2\}$ and $\{3,4\}$ | no: `(1,2)` exists | yes, `(3,4)` is free | rejected |
| $\{1,3\}$ and $\{2,4\}$ | no: `(1,3)` exists | yes, `(2,4)` is free | rejected |
| $\{1,4\}$ and $\{2,3\}$ | yes, `(1,4)` is free | yes, `(2,3)` is free | **accepted** |

Only the third partition works, and the answer is `true`. Two instances with a
hub node in the odd set produce opposite verdicts, and the difference is whether
*some* pairing avoids the existing edges. A method that stops after the first
failed pairing returns the wrong verdict on this input, which is why all three
partitions must be tested.

## 6. Counting impossible configurations

| Odd-set size $\lvert O \rvert$ | Edges needed | Verdict | Reason |
|:---:|:---:|:---|:---|
| 0 | 0 | `true` | nothing to repair; the empty addition is always legal |
| 2 | 1 | case-dependent | direct edge if non-adjacent, otherwise a middle node must be free |
| 4 | 2 | case-dependent | some legal pairing must exist; the hub obstruction decides |
| 6 | 3 | `false` | three edges are needed but only two may be added |
| odd | — | impossible | the handshake lemma forbids an odd number of odd degrees |
| 5 | — | impossible | same parity argument, applied to the largest odd value |

The count alone never settles the answer for $\lvert O \rvert \in \{2, 4\}$:
adjacency structure decides. It settles the answer completely only for $0$
(always yes) and for any count of $6$ or more (always no), because the flip
budget is exhausted.

## 7. Correctness: the parity invariant and exhaustiveness of the cases

The method rests on a single invariant and a complete case split.

> **Parity invariant.** After any sequence of added edges, the parity vector of
> the graph equals the original parity vector with the multiset of endpoints of
> the added edges toggled once per incidence.

Because each added edge contributes exactly two endpoint incidences, and because
in every feasible construction the two endpoints are distinct nodes, the goal
"all parities even" is equivalent to: *the odd set $O$ is partitioned into pairs,
each pair being a legal (absent, loop-free, non-repeated) edge.* This equivalence
is exact in both directions, which is what makes the case analysis complete
rather than merely sufficient:

1. **Necessity.** If all degrees can be made even with at most two edges, then
   those edges toggle exactly the nodes of $O$ (any even node toggled an odd
   number of times would end odd), so $\lvert O \rvert \le 4$ and the edges pair
   up the members of $O$. Hence a "true" answer requires one of the enumerated
   pairings, or the direct/middle repair in the two-odd case.
2. **Sufficiency.** Each enumerated pairing consists of edges that are verified
   to be absent from the graph, loop-free by $a \neq b$ among distinct odd nodes,
   and distinct from each other; adding them pairs every odd node exactly once
   and leaves even nodes toggled either zero or two times. Every degree becomes
   even.
3. **Termination and coverage.** The three partitions of a four-element set are
   exhaustive, and the middle-node search ranges over all $n$ nodes, so no
   feasible construction is missed. If the enumeration fails, no construction of
   at most two edges exists.

The middle-node step is where the invariant does real work: node $c$ is toggled
twice, so its parity is preserved rather than repaired. That is why the search
never needs to ask whether $c$ was even — the construction guarantees it cannot
disturb an even node, and there are no odd nodes left besides $a$ and $b$.

## 8. Boundary and edge cases

| Instance | Input condition | Expected | Deciding reason |
|:---|:---|:---:|:---|
| already even | $n = 3$, triangle `(1,2)`,`(2,3)`,`(3,1)` | `true` | zero odd nodes; add nothing, which "at most two" permits |
| direct repair | $n = 4$, path `(1,2)`,`(2,3)` | `true` | odd set $\{1,4\}$, and `(1,4)` is absent |
| middle node | $n = 5$, isolated node 5 present | `true` | $c = 5$ has degree 0 and both proposed edges are free |
| blocked middle | $n = 4$, both odd nodes adjacent to 3 and 4 | `false` | every candidate middle node already touches an odd endpoint |
| hub in odd set | $n = 4$ star at node 1 | `false` | all three pairings include an existing edge at the hub |
| alternate pairing | $n = 5$ with hub node 1 | `true` | the third partition avoids every existing edge |
| six odd nodes | $n = 6$, three disjoint edges | `false` | three edges required, only two permitted |
| isolated nodes | any input with unused node numbers | — | contribute degree 0, hence even, and are prime middle-node candidates |

Two traps are worth naming explicitly. First, a node numbered between 1 and $n$
that appears in no edge is *not* missing from the problem — it exists with degree
0 and must remain even, and treating absent nodes as "not part of the graph"
loses the only viable middle node in the `n = 5` case above. Second, when the two
odd nodes are adjacent, "add the edge between them" is precisely the choice that
is forbidden by the no-repeated-edges rule, so the adjacent case must fall
through to the middle-node search instead of returning `false` immediately.

## 9. Alternatives and their failure modes

| Approach | How it works | Time | Auxiliary space | Failure mode |
|:---|:---|:---|:---|:---|
| Parity counting plus case analysis | compute degrees, then test the direct edge, the middle-node sweep, or the three pairings | $O(n + m)$ expected | $O(n + m)$ | none; this is the method traced above |
| Exhaustive search over edge pairs | try every pair of candidate edges and check all degrees | $O(n^2 m)$ or worse | $O(n + m)$ | far beyond the $10^{5}$ limits; rechecks degrees it could have inferred |
| General matching on the odd nodes | build a graph on $O$ where adjacency means "edge is free", then find a matching of size $\lvert O \rvert / 2$ | $O(\lvert O \rvert^3)$ | $O(\lvert O \rvert^2)$ | correct but needless: $\lvert O \rvert \le 4$, so three hand-written pairings are cheaper and simpler |
| Greedy first-two pairing | always pair the first two odd nodes, then the last two | $O(1)$ after degree counting | $O(n + m)$ | returns `false` on the alternate-pairing instance where only the third pairing succeeds |
| Count-only test | answer `true` whenever the odd count is 0, 2, or 4 | $O(n + m)$ | $O(n + m)$ | ignores adjacency: wrong on both the blocked-middle case and the star case |
| Queue-based flip simulation | repeatedly flip parities of an arbitrary odd pair | $O(\lvert O \rvert)$ | $O(\lvert O \rvert)$ | still needs an adjacency check per chosen pair; the "edge exists" test cannot be skipped |

## 10. Complexity: time and auxiliary space

Let $n$ be the node count and $m$ the number of given edges, with $n, m \le
10^{5}$.

**Building state.** One pass over `edges` inserts both endpoints into neighbour
sets, costing $O(m)$ time and $O(m)$ stored adjacencies; a second pass over the
$n$ nodes reads each degree and collects the odd set, costing $O(n + m)$ because
each neighbour set is visited once. Expected constant time per hash insertion is
what makes this linear.

**Deciding.** With $\lvert O \rvert = 0$ the answer is immediate. With
$\lvert O \rvert = 2$ the direct check is one membership test, and the
middle-node sweep performs at most $2n$ membership tests, so $O(n)$ expected.
With $\lvert O \rvert = 4$ the method runs a fixed three pairings, each with two
membership tests: $O(1)$. Larger counts return `false` at once.

**Total time.** $O(n + m)$ expected, dominated by building the neighbour sets and
the middle-node sweep, with hash lookups assumed constant on average. Under a
strict worst-case reading of the lookup cost the bound becomes $O((n + m) \log
n)$, which is precisely why a balanced structure would be the fallback if the
hash behaviour were adversarial.

**Auxiliary space.** The neighbour sets store each edge twice, at $O(n + m)$; the
odd set holds at most four relevant entries, but a naive collection can hold
$O(n)$ before the size check, so the honest bound is $O(n + m)$. The parity
verdicts themselves need no degree array beyond what the neighbour sets already
encode, and the pairing analysis is constant-size.
