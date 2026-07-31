## General

**A champion is a source node.** An edge `[stronger, weaker]` is an incoming
edge for the weaker team and directly proves that team cannot be champion.
Mark the target of every edge. After this single pass, exactly the unmarked
nodes have indegree zero and therefore have no explicitly stronger team.

Because the graph is transitively consistent, any team stronger through a
longer chain is also represented by the relation; in any case, the first edge
on such a chain already gives the descendant positive indegree. Thus an
unmarked team satisfies the champion definition, while every marked team
fails it. Scan the marks and return the only unmarked index. Encountering a
second one proves that the champion is not unique, so return `-1`.

## Complexity detail

Let $n$ be the number of teams and
$m=\lvert\texttt{edges}\rvert$. Initializing and scanning the mark array
takes $O(n)$ time, and processing the edges takes $O(m)$ time, for
$O(n+m)$ total. The indegree-status array uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Rescan all edges for each team:** Testing whether each team appears as a target is correct but costs $O(nm)$ time instead of one edge pass.
- **Full topological sort:** Kahn's algorithm also identifies zero-indegree nodes in $O(n+m)$ time, but removing the rest of the DAG is unnecessary once the initial source count is known.
- **Reachability search:** Computing which teams can reach others does extra work; the champion definition depends only on whether an incoming stronger edge exists.
- **Single team:** With no possible incoming edge, team 0 is the unique champion.
- **No edges with multiple teams:** Every team is a source, so return `-1`.
- **Disconnected DAG:** A unique source may still exist, but two source components necessarily make the result `-1`.
- **Redundant transitive edges:** Repeatedly marking an already weaker team does not change the answer.

