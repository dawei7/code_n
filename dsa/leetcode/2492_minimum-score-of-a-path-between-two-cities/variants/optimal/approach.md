## General

**The objective is unusual: make the minimum edge as small as possible**

The score of a path is its smallest road distance. Unlike a shortest-path problem, a large total distance is irrelevant, and taking detours can improve the answer by introducing one very small road.

Paths may revisit cities and even traverse the same road multiple times. That permission changes the problem fundamentally. If cities 1 and `n` lie in the same connected component, a walk can leave the direct route, travel to any road in that component, cross that road, and then travel onward to city `n`. Repeated vertices and edges make such a detour legal.

The test guarantee says at least one path connects 1 to `n`, so city `n` belongs to city 1's connected component.

**Why the answer is the lightest road in that component**

Let $w_{\min}$ be the minimum distance among all roads in the connected component containing city 1.

Every path from 1 to `n` uses only roads from that component. No road on any such path can have distance below $w_{\min}$, so the path's minimum road distance cannot be smaller than $w_{\min}$. This gives a lower bound on the best possible score.

Now choose a road $(u,v)$ whose distance is $w_{\min}$. Since `u` is in city 1's component, there is a route from 1 to `u`. Cross the chosen road to `v`. Because `v` and `n` are in the same component, there is also a route from `v` to `n`. Concatenating these routes creates a legal walk from 1 to `n` that contains the lightest road. Its score is exactly $w_{\min}$, since no component road is lighter.

The lower bound is achievable, so $w_{\min}$ is the required answer.

This proof also explains the second example: the path can travel from city 1 to city 2 along the distance-two road, return along that road, and then continue toward city `n`. A simple path restriction would prevent that detour, but this problem explicitly allows it.

**Build the undirected graph**

The adjacency list `g` has `n+1` entries so city numbers can be used directly as indices. For every input `[a,b,w]`, the code appends `(b,w)` to `g[a]` and `(a,w)` to `g[b]`.

Both insertions are necessary because roads are bidirectional. Omitting either direction could make depth-first search miss cities or roads that are reachable only by traversing the input edge opposite its listed order.

**Traverse exactly city 1's component**

The recursive `dfs(a)` marks city `a` visited, then examines every adjacent road `(b,w)`. Before deciding whether to recurse, it updates

`ans = min(ans,w)`.

Therefore, every road incident to every reached city contributes its distance. Even when neighbor `b` was already visited, the road's weight is still considered. Visitation controls recursion, not whether an edge can influence the minimum.

If `b` is unvisited, DFS enters it. By the standard reachability property of DFS, the traversal eventually visits every city reachable from 1 and no city outside that component. Since every component road touches a reached city, every relevant road is examined.

`ans` starts at positive infinity, so the first examined road replaces it. The connectivity guarantee and `n>=2` ensure city 1's component contains a route to another city and hence at least one road.

**Why disconnected components are ignored**

A road in a component not containing city 1 cannot occur on any walk beginning at city 1. There is no connecting road by the definition of components. Even if such an unrelated road has a smaller distance, it cannot affect a path between 1 and `n`.

Starting DFS only at city 1 naturally excludes these irrelevant roads.

**A useful invariant**

After DFS has finished processing some reached vertices, `ans` is the smallest weight among all adjacency entries examined so far. The update with `min` preserves this invariant for each new edge. At traversal completion, the examined entries cover all component roads, so `ans` is their global minimum. Combined with the detour proof, returning it is correct.

## Complexity detail

Let $m$ be the number of roads. Building the adjacency list costs $O(n+m)$ initialization and insertion time. DFS visits each city in city 1's component once and examines each of its undirected road entries, for $O(n+m)$ worst-case time. Total time is $O(n+m)$.

The adjacency list stores two entries per road and $n+1$ list headers, using $O(n+m)$ space. The visited array uses $O(n)$, and recursive DFS can use $O(n)$ call-stack frames on a deep component. Total auxiliary space is $O(n+m)$.

With up to $10^5$ cities, a path-shaped graph can exceed Python's default recursion limit. The algorithmic idea is correct, but an iterative traversal would be more robust for the full constraint range.

## Alternatives and edge cases

- **Iterative DFS:** Use an explicit stack to avoid Python recursion-depth failure while preserving the same $O(n+m)$ bounds.
- **Breadth-first search:** A queue visits the same component and can update the same minimum.
- **Union-find:** Unite road endpoints and then inspect roads whose endpoint belongs to city 1's component. It works but is more machinery than a traversal.
- **Shortest-path algorithms:** Dijkstra minimizes total distance, which is not this path score and can produce the wrong objective.
- **Disconnected graph:** Only the component containing city 1 matters; city `n` is guaranteed to be inside it.
- **Tiny road on a detour:** It still determines the answer because repeated cities and roads are legal.
- **Visited neighbor:** Its connecting edge must still update `ans` even though recursion is skipped.
- **Parallel direction storage:** Each bidirectional road must be inserted for both endpoints.
- **Single connecting route:** The minimum road on that component's edges is attainable even if reaching it requires backtracking.
- **Recursion limit:** Prefer an iterative queue or stack in production Python for $n=10^5$.
