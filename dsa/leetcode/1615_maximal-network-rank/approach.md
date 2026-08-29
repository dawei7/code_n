## General

**Store each city’s direct neighbors**

The network is an undirected graph. The source builds `g` as a mapping from city ID to a set of adjacent city IDs.

For every road `[a,b]`, it inserts `b` into `g[a]` and `a` into `g[b]`. The size `len(g[a])` is then the degree of city `a`: the number of roads directly incident to it.

Sets also answer direct-connectivity membership in expected constant time. The constraint that each city pair has at most one road means degrees correspond directly to set sizes without duplicate-edge concerns.

**Network rank of one pair**

For two different cities `a` and `b`, adding their degrees counts every road incident to either city. If the cities are directly connected, their shared road appears once in `a`’s degree and once in `b`’s degree, so it has been counted twice.

The rank formula is:

`len(g[a]) + len(g[b]) - (a in g[b])`.

In Python, membership produces `True` or `False`, which behave numerically as one or zero. Therefore, exactly one is subtracted when the road `a-b` exists.

No other road can be directly connected to both distinct cities: an edge has two endpoints, so the only common incident edge is the road between the pair itself.

**Enumerate every unordered city pair**

The nested loops use `a in range(n)` and `b in range(a + 1, n)`. This visits every unordered pair exactly once:

- `a` and `b` are always different;
- pair `(b,a)` is not repeated after `(a,b)`.

The walrus expression computes and names the current rank `t` inside the comparison. If `t > ans`, `ans` is updated.

A tied rank does not require an update because only the maximum numeric value is returned.

**Isolated cities**

`g` is a `defaultdict(set)`. Accessing `g[a]` for a city with no roads creates and returns an empty set. Its length is zero and membership checks are false.

Thus isolated cities require no preprocessing entry and participate correctly in pair enumeration.

**A sample calculation**

Suppose city zero connects to one and three, so its degree is two. City one connects to zero, two, and three, so its degree is three.

Their degree sum is five. Because zero and one share a direct road, subtract one, giving rank four. The four distinct incident roads are zero-one, zero-three, one-two, and one-three.

For two high-degree cities that are not directly connected, no subtraction occurs. This can make a disconnected pair achieve the maximum, as allowed by the problem.

**Why the formula is exact**

Let $E_a$ be the set of roads incident to `a` and $E_b$ the set incident to `b`. The network rank is the size of their union.

By inclusion-exclusion:

$$
\lvert E_a\cup E_b\rvert
=\lvert E_a\rvert+\lvert E_b\rvert-\lvert E_a\cap E_b\rvert.
$$

The first two terms are the degrees. The intersection size is one exactly when road `a-b` exists, otherwise zero. This is exactly the source formula.

Since the loops evaluate this exact value for every pair of different cities, taking the maximum produces the infrastructure’s maximal network rank.

**Why no graph traversal is needed**

Rank concerns only directly incident roads. Whether a city can reach another through a path, whether the graph is connected, and component structure are irrelevant. Degree and one adjacency test contain all needed information.

## Complexity detail

Let $N$ be the number of cities and $M$ the number of roads.

Building adjacency sets takes $O(M)$ expected time. The loops examine $\binom{N}{2}$ pairs, with expected $O(1)$ degree and membership operations, taking $O(N^2)$ time. Total expected time is $O(M+N^2)$.

The adjacency sets store each undirected road twice, using $O(N+M)$ space including dictionary/set overhead and isolated keys created during pair checks. In the dense worst case $M=O(N^2)$, this is $O(N^2)$, matching the manifest.

Expected qualifications come from hash-set operations.

## Alternatives and edge cases

- **Degree array plus Boolean adjacency matrix:** It gives deterministic constant-time connectivity tests and $O(N^2)$ space. The checked-in sets use space proportional to actual roads.
- **Degree array plus encoded road set:** Store normalized pairs such as `(min(a,b), max(a,b))` for expected constant membership and $O(N+M)$ space.
- **Count incident roads separately for every pair:** Scanning all roads per pair costs $O(N^2M)$ and repeats degree work.
- **Run BFS or DFS:** Connectivity paths do not affect direct network rank, so traversal is irrelevant.
- **No roads:** Every degree and rank is zero, so the result remains zero.
- **One road:** Its endpoint pair has rank one, and pairs with one endpoint also have rank one.
- **Directly connected pair:** Subtract exactly one to correct double counting.
- **Not directly connected pair:** Degree sets are disjoint as edge identities, so no subtraction occurs.
- **Isolated city:** `defaultdict` supplies an empty neighbor set and degree zero.
- **Disconnected graph:** Pairs may come from different components; all are still evaluated.
- **Duplicate roads:** The contract excludes them. Sets would deduplicate them, which would not represent multiplicity if parallel roads were allowed.
- **Self-loops:** The contract excludes them; the rank formula assumes roads join two different cities.
- **Tied maximum pairs:** Only the numeric maximum is requested, so pair identities need not be stored.
- **Boolean subtraction:** Python converts membership truth to one or zero; another language may require an explicit conditional.
