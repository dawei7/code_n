# Guided Example: Get Watched Videos by Your Friends

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"watchedVideos": [["A"], ["B"], ["C"]], "friends": [[1], [0], []], "id": 0, "level": 2}`
- **Required output:** `[]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` people, each person has a unique *id* between `0` and `n-1`. Given the arrays `watchedVideos` and `friends`, where $\text{watchedVideos}[i]$ and $\text{friends}[i]$ contain the list of watched videos and the list of friends respectively for the person with $id = i$.

The objective is to compute `[]` from `{"watchedVideos": [["A"], ["B"], ["C"]], "friends": [[1], [0], []], "id": 0, "level": 2}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Starting at distance zero

`q = deque([id])` places the starting person in the queue. `vis = {id}` immediately marks that person discovered.

At this point, the queue is exactly distance zero. Marking on discovery is important in an undirected friendship graph. Without it, two people in one layer could both enqueue the same friend, and edges back to already processed people could create cycles.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"watchedVideos": [["A"], ["B"], ["C"]], "friends": [[1], [0], []], "id": 0, "level": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Advancing one complete friendship level

The outer loop runs `level` times. Each iteration represents one edge of distance.

Inside it, `range(len(q))` captures the number of people in the current layer before new friends are appended. Each current person is removed, and every identifier in `friends[i]` is examined. An unvisited friend is marked immediately and appended.

Because newly appended people are not processed during the same frozen inner loop, they form the next layer. After the first outer iteration, the queue holds shortest-distance-one friends. After the second, it holds shortest-distance-two people, and so on.

The visited set is what makes the distance exact. Suppose a person is reachable through both a short path and a longer path. BFS discovers and marks that person along the shortest path first. A later longer route cannot enqueue the person into a deeper layer. Thus, the final queue excludes anyone whose true shortest distance is less than `level`.

The graph is undirected according to the contract, but the BFS logic would also find directed shortest distances if `friends` were interpreted as outgoing adjacency lists.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The outer loop runs `level` times.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the queue itself is the target layer

The solution does not copy the queue after the BFS. Once the outer loop has run exactly `level` times, every person from smaller distances has been popped, and people at greater distances have not yet been expanded or even necessarily discovered beyond the current frontier.

Therefore, iterating `for i in q` directly visits exactly the desired people.

If the connected component ends before the requested level, the queue becomes empty. Later outer iterations process zero people, and video counting produces an empty result, which is correct because nobody exists at that exact distance.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"watchedVideos": [["A"], ["B"], ["C"]], "friends": [[1], [0], []], "id": 0, "level": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Depth-first search with stored distances:** DF:** - **Depth-first search with stored distances:** DFS can traverse the graph while maintaining best known distances, but BFS obtains unweighted shortest layers directly and more simply.
- **Repeated frontier sets:** Replacing the queue with a set of the next layer can work, but a global visited set is still required to enforce shortest-distance semantics.
- **Count everyone within the level:** That is incorrect. The task asks for shortest path exactly equal to `level`, so smaller layers must be removed before counting.
- **No people at the requested level:** The queue is empty and the sorted key list is empty.
- **Several shortest paths to one person:** Immediate `vis.add(j)` ensures the person appears only once in the layer and their videos are not double-counted.
- **Cycles and friendship back-edges:** The visited set prevents returning to the starting person or looping between friends.
- **Disconnected graph:** Only the starting person's connected component can enter the queue; unreachable people correctly contribute nothing.
- **Same video watched by several target friends:** Every entry increments the shared counter, raising that title's frequency.
- **Frequency tie:** The second tuple component, the title itself, orders tied videos alphabetically.
- **No frequency in output:** `sorted(cnt.keys(), ...)` returns titles only, as required.
- **Level one:** One outer expansion removes `id` and leaves exactly direct friends.
- **Large level beyond component depth:** Empty frontiers remain empty through the remaining fixed iterations and produce an empty answer.
- **Duplicate friendship entries outside the usual graph representation:** Immediate visited marking prevents duplicate person insertion even if an adjacency list repeats an ID.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+E+S+V\log V)$. Let $n$ be the number of people, $E$ the total number of friendship adjacency entries scanned during BFS, $S$ the number of watched-video entries belonging to people in the selected layer, and $V$ the number of distinct titles among those entries.
- **Auxiliary Space Complexity:** $O(n+V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
