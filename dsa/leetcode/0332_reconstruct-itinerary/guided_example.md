# Guided Example: Reconstruct Itinerary

We trace the step-by-step Hierholzer algorithm for Eulerian paths, descending sorted adjacency list construction (`sorted(tickets, reverse=True)`), $O(1)$ lexical destination extraction (`g[f].pop()`), postorder dead-end accumulation, and reverse route reconstruction on representative flight ticket instances:

- **Input:**
  $$
  \text{tickets} = [[\text{"JFK"},\text{"SFO"}], [\text{"JFK"},\text{"ATL"}], [\text{"SFO"},\text{"ATL"}], [\text{"ATL"},\text{"JFK"}], [\text{"ATL"},\text{"SFO"}]]
  $$
- **Required output:** `["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]`
  - From `"JFK"`, valid destinations are `"ATL"` and `"SFO"`
  - Lexicographically choosing `"ATL"` first creates loop `"JFK" -> "ATL" -> "JFK"` before exploring `"SFO"`
  - All 5 tickets are used exactly once
- **Linear Path Instance:** `[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]` $\implies$ `["JFK", "MUC", "LHR", "SFO", "SJC"]`
- **Dead-End Suffix Trap:** On `[["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]`:
  - Greedily taking `"KUL"` first strands the traveler with 2 tickets unused
  - Hierholzer's postorder appends dead-end `"KUL"` first, which upon reversal becomes the final destination: `["JFK", "NRT", "JFK", "KUL"]`

This instance demonstrates Eulerian path discovery on directed multigraphs, mathematically proves why postorder traversal resolves premature dead ends without backtracking search trees, explains why reverse sorting permits $O(1)$ pop operations, and analyzes $O(E \log E)$ time and $O(E)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a collection of flight tickets:
$$
\text{tickets} = [[\text{"JFK"},\text{"SFO"}], [\text{"JFK"},\text{"ATL"}], [\text{"SFO"},\text{"ATL"}], [\text{"ATL"},\text{"JFK"}], [\text{"ATL"},\text{"SFO"}]]
$$
Construct a continuous flight itinerary that:
1. Begins at departure airport `"JFK"`.
2. Uses **every ticket exactly once** (an Eulerian trail).
3. If multiple valid itineraries exist, selects the one with the **smallest lexicographical order**.

```text
Flight Graph (Multigraph):
       +--- "SFO" <---+
       |     ^   |    |
       v     |   v    |
     "JFK" --+  "ATL"-+

Valid Sequences from "JFK":
Path A: JFK -> SFO -> ATL -> JFK -> ATL -> SFO
Path B: JFK -> ATL -> JFK -> SFO -> ATL -> SFO  (LEXICOGRAPHICALLY SMALLER!)

Output: ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
```

### Why Naive Left-to-Right Greed Fails
Consider tickets: `[["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]`.
- Alphabetically, `"KUL"` comes before `"NRT"`.
- If an agent greedily flies `JFK -> KUL`, it reaches `"KUL"` with no outgoing tickets, stranding the flight while tickets `JFK -> NRT` and `NRT -> JFK` remain unused!
- **Hierholzer's Algorithm:**
  - Instead of committing airports forward, it builds the path in **postorder** (bottom-up).
  - When a path hits a dead end (an airport with zero remaining outgoing flights), that airport is placed onto the postorder stack.
  - Reversing the postorder traversal at the end naturally places dead-end excursions at the **very end** of the journey!

---

## 2. Conceptual Foundation & Invariants

### 1. Reverse-Sorted Adjacency Lists
To always pop the lexicographically smallest destination in $O(1)$ time:
- Sort tickets in descending order: `sorted(tickets, reverse=True)`.
- For each `[from, to]` in sorted order, append `to` to `g[from]`.
- Because tickets were sorted descending, the smallest lexical airport is at the **end** of list `g[from]`.
- `g[from].pop()` extracts the smallest destination in $O(1)$ time!

### 2. Hierholzer's Postorder DFS
Define `dfs(f)`:
- While airport `f` has remaining outgoing flights in `g[f]`:
  $$
  \text{next\_airport} = g[f].\text{pop}()
  $$
  $$
  dfs(\text{next\_airport})
  $$
- Once all outgoing flights from `f` have been traversed:
  $$
  ans.\text{append}(f)
  $$
- Return $ans[::-1]$.

> **Invariant.** At every step, every flight ticket is traversed exactly once. An airport is appended to `ans` only after its entire forward Eulerian subgraph has been fully consumed.

---

## 3. Step-by-Step Worked Execution

We trace the execution on tickets between `JFK`, `ATL`, and `SFO`:
- Reverse sorted ticket insertions populate:
  - `g["JFK"] = ["SFO", "ATL"]` (Pop gives `"ATL"` first, then `"SFO"`)
  - `g["ATL"] = ["SFO", "JFK"]` (Pop gives `"JFK"` first, then `"SFO"`)
  - `g["SFO"] = ["ATL"]` (Pop gives `"ATL"`)
- Initialize `ans = []`. Call `dfs("JFK")`.

---

### Step 1: Forward Path Exploration
1. **At `dfs("JFK")`:**
   - Outgoing destinations: `["SFO", "ATL"]`.
   - Pop smallest: `"ATL"`.
   - Call $dfs(\text{"ATL"})$.
2. **At `dfs("ATL")`:**
   - Outgoing destinations: `["SFO", "JFK"]`.
   - Pop smallest: `"JFK"`.
   - Call $dfs(\text{"JFK"})$.
3. **At `dfs("JFK")` (Second visit):**
   - Outgoing destinations: `["SFO"]`.
   - Pop smallest: `"SFO"`.
   - Call $dfs(\text{"SFO"})$.
4. **At `dfs("SFO")`:**
   - Outgoing destinations: `["ATL"]`.
   - Pop smallest: `"ATL"`.
   - Call $dfs(\text{"ATL"})$.
5. **At `dfs("ATL")` (Second visit):**
   - Outgoing destinations: `["SFO"]`.
   - Pop smallest: `"SFO"`.
   - Call $dfs(\text{"SFO"})$.
6. **At `dfs("SFO")` (Second visit):**
   - Outgoing destinations: `g["SFO"]` is empty!

---

### Step 2: Postorder Backtracking Unroll
Now the recursion unrolls, appending airports to `ans`:
1. From `dfs("SFO")` (empty):
   - `ans.append("SFO")` $\implies ans = \text{["SFO"]}$.
   - Returns to `dfs("ATL")`.
2. From `dfs("ATL")` (empty):
   - `ans.append("ATL")` $\implies ans = \text{["SFO", "ATL"]}$.
   - Returns to `dfs("SFO")`.
3. From `dfs("SFO")` (empty):
   - `ans.append("SFO")` $\implies ans = \text{["SFO", "ATL", "SFO"]}$.
   - Returns to `dfs("JFK")`.
4. From `dfs("JFK")` (empty):
   - `ans.append("JFK")` $\implies ans = \text{["SFO", "ATL", "SFO", "JFK"]}$.
   - Returns to `dfs("ATL")`.
5. From `dfs("ATL")` (empty):
   - `ans.append("ATL")` $\implies ans = \text{["SFO", "ATL", "SFO", "JFK", "ATL"]}$.
   - Returns to `dfs("JFK")`.
6. From root `dfs("JFK")` (empty):
   - `ans.append("JFK")` $\implies ans = \text{["SFO", "ATL", "SFO", "JFK", "ATL", "JFK"]}$.

---

### Step 3: Reverse Postorder Route
Reversing `ans`:
$$
ans[::-1] = \mathbf{\text{["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]}}
$$

---

## 4. Complete Execution Trace

```text
Tickets: [JFK->SFO, JFK->ATL, SFO->ATL, ATL->JFK, ATL->SFO]
Adjacency:
  JFK: [SFO, ATL]
  ATL: [SFO, JFK]
  SFO: [ATL]

Traversal Tree:
dfs("JFK") -> pops "ATL"
  dfs("ATL") -> pops "JFK"
    dfs("JFK") -> pops "SFO"
      dfs("SFO") -> pops "ATL"
        dfs("ATL") -> pops "SFO"
          dfs("SFO") -> dead end! -> ans = ["SFO"]
        ans = ["SFO", "ATL"]
      ans = ["SFO", "ATL", "SFO"]
    ans = ["SFO", "ATL", "SFO", "JFK"]
  ans = ["SFO", "ATL", "SFO", "JFK", "ATL"]
ans = ["SFO", "ATL", "SFO", "JFK", "ATL", "JFK"]

Reversed: ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
```

| Traversal Depth | Active Airport | Edge Popped | Remaining Edges at Airport | Next Recursion | `ans` Snapshot (Postorder) |
|:---:|:---:|:---:|:---|:---:|:---|
| 1 | `"JFK"` | `"ATL"` | `["SFO"]` | `dfs("ATL")` | `[]` |
| 2 | `"ATL"` | `"JFK"` | `["SFO"]` | `dfs("JFK")` | `[]` |
| 3 | `"JFK"` | `"SFO"` | `[]` | `dfs("SFO")` | `[]` |
| 4 | `"SFO"` | `"ATL"` | `[]` | `dfs("ATL")` | `[]` |
| 5 | `"ATL"` | `"SFO"` | `[]` | `dfs("SFO")` | `[]` |
| 6 | `"SFO"` | None | `[]` (Dead end) | Returns | `["SFO"]` |
| 5 (unroll) | `"ATL"` | None | `[]` | Returns | `["SFO", "ATL"]` |
| 4 (unroll) | `"SFO"` | None | `[]` | Returns | `["SFO", "ATL", "SFO"]` |
| 3 (unroll) | `"JFK"` | None | `[]` | Returns | `["SFO", "ATL", "SFO", "JFK"]` |
| 2 (unroll) | `"ATL"` | None | `[]` | Returns | `["SFO", "ATL", "SFO", "JFK", "ATL"]` |
| 1 (unroll) | `"JFK"` | None | `[]` | Finish | `[..., "JFK"]` |
| **Reversed** | - | - | - | - | **`["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]`** |

---

## 5. Algorithmic Correctness

**Soundness.** Hierholzer's algorithm is mathematically proven to construct an Eulerian trail in any directed multigraph where one exists. Because edges are popped immediately upon traversal, each ticket is consumed exactly once. Appending airports only after their outgoing edges are exhausted guarantees that any branch terminating early is placed at the end of the reversed itinerary.

**Completeness.** By sorting tickets and popping the lexicographically smallest destination first, the algorithm attempts the lexicographically earliest valid branch at every opportunity. The Eulerian property ensures that all $E$ tickets are traversed, yielding an itinerary of length $E + 1$ without omitting any segment.

---

## 6. Traps This Instance Exposes

- **Greedy Trapping at Dead Ends:** Pushing airports forward during traversal strands the path at a premature terminal node. Hierholzer's postorder ensures dead ends correctly become the trail's conclusion.
- **Duplicate Tickets:** Multiple identical tickets (e.g. two `["JFK", "SFO"]` flights) must be preserved as distinct edge instances. Using a multiset or list rather than a hash set is essential.
- **Efficient Smallest-Element Extraction:** Removing the smallest element from the front of a list takes $O(N)$ due to shifting. Sorting descending and using `pop()` from the back runs in $O(1)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E \log E)$, where $E$ is the number of tickets.
  - Sorting all tickets takes $O(E \log E)$ time.
  - Constructing the adjacency list takes $O(E)$.
  - The DFS visits each edge exactly once, popping in $O(1)$ time, taking $O(E)$ total traversal time.
  - Reversing `ans` of length $E + 1$ takes $O(E)$ time.
- **Auxiliary Space Complexity:** $O(E)$ auxiliary memory to store adjacency lists, the recursive call stack, and the result array.
