## General

**Represent indirect friendship as connected components**

Once successful requests are accepted, direct friendship links form an undirected graph. Two people are indirectly friends exactly when a path connects them, so the algorithm does not need the complete path structure. It needs to know only which people currently belong to the same connected component.

A disjoint-set union structure, also called DSU or union-find, stores this partition. The parent array `p` initially satisfies `p[x] = x` for every person `x` because nobody is connected to anybody else. A root represents one entire current friendship component.

The nested `find(x)` function follows parent pointers to the root of `x`. Its recursive assignment

`p[x] = find(p[x])`

also performs path compression: after the root is discovered, `x` points directly to it. Future searches from that part of the structure become shorter.

The requests must be processed in their given order because every accepted request changes the components seen by later requests. For a request `[u, v]`, the code first computes `pu = find(u)` and `pv = find(v)`.

**Accept requests already inside one component**

If `pu == pv`, the two people are already directly or indirectly connected. Accepting their request does not merge different components and therefore cannot create a newly forbidden connection.

This matches the explicit note that a request between people who are already direct friends remains successful. The same reasoning extends to people already connected indirectly: the request adds a redundant direct edge, but the DSU partition does not change. Because all earlier accepted requests preserved every restriction, the existing component is already valid.

The code appends `True` and performs no union in this case.

**Test exactly what a component merge would change**

When `pu != pv`, accepting the request would merge the whole component rooted at `pu` with the whole component rooted at `pv`. A restriction `[x, y]` is violated after that merge precisely when one endpoint currently lies in the first component and the other lies in the second.

For every restriction, the code finds the current roots `px = find(x)` and `py = find(y)`. It rejects the request if either orientation matches:

- `pu == px and pv == py`, or
- `pu == py and pv == px`.

Both orientations are required because a restriction is an unordered relationship. Restriction `[x, y]` means the same forbidden pairing as `[y, x]`, while the two requested components may happen to be held in either root order.

If a restriction has both endpoints somewhere else, merging `pu` and `pv` cannot affect it. If both endpoints were already in the same current component, the invariant would already have been broken, which accepted requests never allow. The only new cross-component paths created by a union are paths between one member of `pu`'s component and one member of `pv`'s component. The scan tests exactly those possible new violations.

For example, suppose restriction `[0, 3]` exists and earlier successful requests have connected 0 with 1 and 3 with 4. A new request `[1, 4]` has component roots equal to the current roots of 0 and 3. Even though neither requested endpoint is literally an endpoint in the stored restriction, the root comparison detects that accepting the request would indirectly connect 0 and 3, so it rejects it.

**Commit only a request that passes every restriction**

The flag `ok` begins as `True`. Finding one conflicting restriction is sufficient to set it to `False` and break the scan because the request must satisfy all restrictions. The result for this request is appended immediately with `ans.append(ok)`.

If `ok` remains true, the code performs `p[pu] = pv`. Both values are roots, so this joins the two entire components. The code does not need to add a graph edge or update every member explicitly; future `find` calls follow parent links and observe the new common root.

If the request is rejected, the parent array receives no union. Path compression may still have shortened some parent chains during the checks, but it never changes which component a person belongs to, so it does not alter friendship semantics.

**Why checking original restrictions repeatedly is sufficient**

Restrictions do not disappear or transform after a request. Their endpoints stay the same, but their current components may grow. This is why the code retains the original pairs and recomputes their roots for each potential merge.

Assume before a request that no restriction's endpoints lie in the same component. This is true initially because every person is alone and restriction endpoints are distinct.

- If the requested people are already in one component, the partition does not change, so the assumption remains true.
- If their components differ and the scan finds a restriction crossing those two components, the request is rejected and the partition again remains unchanged.
- If no restriction crosses the two components, merging them cannot place any restricted pair together. Restrictions internal to either component were already absent by the assumption, and restrictions involving other components remain separated.

By induction over the requests, all accepted component states obey every restriction. The scan rejects exactly the merges that would violate that property, so every Boolean appended to `ans` is correct.

The union uses no rank or size heuristic. That does not affect correctness: any root may safely become the parent of another root. Path compression still reduces repeated lookup cost in practice.

## Complexity detail

Let $n$ be the number of people, $R$ the number of restrictions, and $Q$ the number of requests. Let $S=\max(n,R,Q)$.

Every request performs two initial `find` operations. A request between distinct components may scan all $R$ restrictions, performing two more `find` operations for each restriction. Thus the dominant operation count is $O(QR)$ disjoint-set lookups. Under the standard near-constant amortized DSU model represented by the manifest, these lookups contribute an inverse-Ackermann factor, giving $O(QR\alpha(n))$, or $O(S^2\alpha(S))$ in the manifest's single-parameter form.

The exact implementation has path compression but does not use union by rank or union by size. The strongest textbook $\alpha(n)$ guarantee is normally stated when both techniques are combined; without a balancing rule, a more conservative theoretical analysis may be weaker even though path compression keeps the operations fast for these constraints. The nested request-by-restriction scan remains the dominant structural cost.

The parent array uses $O(n)$ space, and the returned Boolean list uses $O(Q)$ space. Apart from the recursion stack used by `find`, the remaining variables are constant-size. The manifest summarizes storage as $O(n+Q)$. Parent chains can transiently determine recursion depth, while path compression shortens paths after visits.

## Alternatives and edge cases

- **Rebuilding a friendship graph for every request:** A graph search could test whether a proposed edge causes a forbidden connection, but repeating reachability work is more cumbersome. DSU directly represents the only property needed: current component membership.
- **Checking only the requested people against restrictions:** This is incorrect because a request can connect restricted people indirectly through their existing components. Root comparisons detect restrictions involving any members of the two components.
- **Checking restrictions only once at the beginning:** Component membership changes after successful requests. The original endpoint pair remains fixed, but its roots must be recomputed against the current DSU before each possible merge.
- **Storing forbidden component pairs dynamically:** One can maintain restriction relationships between components and merge those sets during union, potentially avoiding a full restriction scan. That design is more complex because all references to merged roots must remain consistent.
- **Union by size or rank:** Adding a balancing array would strengthen the conventional DSU amortized guarantee and keep trees shallow before compression. The exact source links `pu` directly under `pv` and remains semantically correct.
- **Already connected request:** The answer is `True` because no new component merge occurs. This includes directly connected people and people connected only through a longer path.
- **No restrictions:** Every request is accepted. DSU still merges new components and recognizes later redundant requests.
- **One conflicting restriction:** The scan can stop immediately after finding it because a successful request must violate none of the restrictions.
- **Restriction orientation:** Both root orderings must be checked. Treating `[x, y]` as directional would miss half of the forbidden merges.
- **Rejected request state:** No union is performed. Only harmless path compression may occur, so later requests see the same component partition they should see.
- **Result order:** A Boolean is appended while each request is processed, preserving the exact input order in the returned list.
