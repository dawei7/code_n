# Guided Example: Keys and Rooms

We trace the step-by-step directed graph reachability search from source room 0, visited set membership tracking ($vis \subset \{0, \dots, n-1\}$), depth-first search recursive key exploration, locked component discovery, and full vertex set coverage verification ($|vis| == n$) on representative room key distributions:

- **Input:**
  $$
  rooms = [[1, 3], [3, 0, 1], [2], [0]]
  $$
- **Required output:** `false`
  - Room unlocking rules:
    - There are $n$ rooms numbered $0 \dots n - 1$.
    - Initially, **only Room 0 is unlocked**. All other rooms $1 \dots n - 1$ are locked.
    - Inside room $i$, there is a collection of keys $rooms[i]$. A key with value $j$ unlocks Room $j$.
    - Once unlocked, a room can be visited at any subsequent time.
    - Objective: Return `true` if and only if every single room $0 \dots n - 1$ can eventually be visited.
    - For $rooms = [[1, 3], [3, 0, 1], [2], [0]]$ ($n = 4$):
      - Start in Room 0 (unlocked). Keys collected: $\{1, 3\}$.
      - Visit Room 1 (using key 1). Keys collected: $\{3, 0, 1\}$.
      - Visit Room 3 (using key 3). Keys collected: $\{0\}$.
      - All accessible keys lead only to rooms in $\{0, 1, 3\}$.
      - Room 2 remains locked with key 2 trapped inside itself!
      - Visited rooms count is $3 < 4$.
      - Result: **`false`**.
- **Directed Graph Reachability & Component Coverage Invariant:**
  - **The Directed Key Digraph $G = (V, E)$:**
    - Vertices: $V = \{0, 1, \dots, n - 1\}$.
    - Directed edge $u \to v$ exists if $v \in rooms[u]$ (room $u$ contains the key to room $v$).
    - Root: Source vertex $s = 0$.
  - **The Reachable Subgraph:**
    - A room $v$ can be visited if and only if there exists a directed path from $0$ to $v$:
      $$
      0 \rightsquigarrow v
      $$
    - The set of all visited rooms is the transitive out-component of 0:
      $$
      vis = \text{Reach}(0) = \{ v \in V \mid 0 \rightsquigarrow v \}
      $$
  - **Global Solvability Criterion:**
    $$
    \text{CanVisitAll} \iff |vis| = n
    $$
    - If $|vis| = n$, every room is reachable.
    - If $|vis| < n$, at least one room belongs to an unreachable component.
- **Step-by-Step Worked Execution Trace on $rooms = [[1, 3], [3, 0, 1], [2], [0]]$ ($n = 4$):**
  - Initialize visited set: $vis = \emptyset$.
  - **Call `dfs(0)`:**
    - Mark Room 0: $vis \leftarrow \{0\}$.
    - Keys in Room 0: $[1, 3]$.
    - Explore Key 1:
      - $1 \notin vis \implies$ call `dfs(1)`.
  - **Call `dfs(1)`:**
    - Mark Room 1: $vis \leftarrow \{0, 1\}$.
    - Keys in Room 1: $[3, 0, 1]$.
    - Explore Key 3:
      - $3 \notin vis \implies$ call `dfs(3)`.
  - **Call `dfs(3)`:**
    - Mark Room 3: $vis \leftarrow \{0, 1, 3\}$.
    - Keys in Room 3: $[0]$.
    - Explore Key 0:
      - $0 \in vis \implies \mathbf{Already\ Visited\ (Cycle\ Detected).}$
    - Room 3 traversal finishes.
  - **Resume `dfs(1)`:**
    - Next keys in Room 1:
      - Key 0: $0 \in vis \implies$ skip.
      - Key 1: $1 \in vis \implies$ skip.
    - Room 1 traversal finishes.
  - **Resume `dfs(0)`:**
    - Next key in Room 0:
      - Key 3: $3 \in vis \implies$ skip.
    - Room 0 traversal finishes.
  - **Termination & Size Check:**
    - Total visited rooms:
      $$
      vis = \{0, 1, 3\} \implies |vis| = 3
      $$
    - Compare with total rooms:
      $$
      |vis| = 3 \ne 4 = n \implies \mathbf{Unreachable\ Room\ 2\ Discovered!}
      $$
    - Final Output:
      $$
      \mathbf{\text{false}}
      $$
- **Linear Chain Trace ($rooms = [[1], [2], [3], []]$):**
  - $0 \to 1 \to 2 \to 3$.
  - Visited set: $\{0, 1, 2, 3\}$.
  - $|vis| = 4 == 4 \implies \mathbf{\text{true}}.$
- **Disconnected Island Trace ($rooms = [[], [0]]$):**
  - Room 0 has no keys. Traversal terminates immediately.
  - $vis = \{0\} \implies |vis| = 1 \ne 2 \implies \mathbf{\text{false}}.$

This instance demonstrates directed connectivity in finite graph models and out-component reachability from designated source vertices, mathematically proves why a standard DFS or BFS traversal from root 0 decides universal reachability in optimal linear time, and derives $O(V + E)$ execution time and $O(V)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given $n$ rooms where room 0 is unlocked and each room contains keys to other rooms:
Return `true` if we can visit **all rooms**, and `false` otherwise.

```text
rooms = [ [1, 3], [3, 0, 1], [2], [0] ]

Start at Room 0:
  Collect keys: 1, 3
Visit Room 1:
  Collect keys: 3, 0, 1
Visit Room 3:
  Collect keys: 0

Visited so far: { 0, 1, 3 }
Room 2 is NEVER reached (its key is locked inside itself!).
Result: false
```

### The Invariant of Directed Reachability
- The problem is standard graph reachability from source node 0.
- A DFS or BFS collects all reachable nodes into a set $vis$.
- If $|vis| == n$, all rooms were unlocked.

---

## 2. Conceptual Foundation & Invariants

### 1. Reachability Set:
$$
\text{Reach}(0) = \{ v \in V \mid \exists \text{ directed path } 0 \to \dots \to v \}
$$

### 2. Universal Coverage Decision:
$$
\text{canVisitAllRooms}(rooms) \iff |\text{Reach}(0)| = n
$$

> **Reachability Closure Invariant.** Let $G = (V, E)$ be the key digraph with $E = \{(u, v) \mid v \in rooms[u]\}$. The set of accessible rooms is the smallest subset $S \subseteq V$ containing $0$ that is closed under the forward neighbor operator $\Gamma^+(S) \subseteq S$.

---

## 3. Step-by-Step Worked Execution

We trace $rooms = [[1, 3], [3, 0, 1], [2], [0]]$:

---

### Step 1: Start at Room 0
- $vis = \{0\}$. Keys: $1, 3$.

---

### Step 2: Visit Room 1
- $vis = \{0, 1\}$. Keys: $3, 0, 1$.

---

### Step 3: Visit Room 3
- $vis = \{0, 1, 3\}$. Key: $0$ (already visited).

---

### Step 4: Check Unvisited Rooms
- Room 2 is not in $vis$.

---

### Step 5: Output
$$
|vis| = 3 \ne 4 \implies \mathbf{\text{false}}
$$

---

## 4. Complete Execution Trace

| DFS Step | Current Room $i$ | Keys Found in Room | Unvisited Keys Enqueued | Cumulative Visited Set $vis$ | $\lvert vis \rvert$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Initial | $0$ | $[1, 3]$ | $1, 3$ | $\{0\}$ | $1$ |
| Step 1 | $1$ | $[3, 0, 1]$ | $3$ | $\{0, 1\}$ | $2$ |
| Step 2 | $3$ | $[0]$ | None | $\{0, 1, 3\}$ | $3$ |
| **Complete** | **Trapped** | **Room $2$ Unreachable** | **None** | **$\{0, 1, 3\}$** | **`3 < 4`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Room ($rooms = [[]]$):** Room 0 is already unlocked $\implies |vis| = 1 == 1 \implies \text{true}$.
- **Isolated Self-Loop ($rooms = [[], [1]]$):** Room 1 holds its own key, but cannot be reached from 0 $\implies \text{false}$.
- **Complete Graph (Every room has all keys):** Every room visited on first layer $\implies \text{true}$.
- **Cycles in Keys:** Visited set prevents infinite loops.

---

## 6. Traps & Common Anti-Patterns

- **Searching for Missing Keys Backwards:** Trying to find which room holds key 2 is unnecessary; simply run a forward traversal from 0 and test $|vis| == n$.
- **Not Handling Graph Cycles:** Rooms can contain keys to previously visited rooms (e.g. room 1 has key 0); always check `if i in vis: return`.
- **Counting Key Frequencies Instead of Unique Rooms:** Multiple copies of the same key can appear across rooms; track visited rooms via a set or boolean array.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Standard DFS / BFS visits each room at most once: $\mathcal{O}(V)$.
  - Each key (edge) is examined at most once: $\mathcal{O}(E)$.
  - Total Time: strictly linear in graph size $\mathcal{O}(V + E)$ where $V \le 1000, E \le 3000$. Completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(V)$ memory for the visited set and recursion call stack.
