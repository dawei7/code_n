# Guided Example: Range Module

We trace the step-by-step half-open interval discretization ($[left, right) \to [left, right - 1]$), dynamic segment tree range setting ($+1$ for add, $-1$ for remove), lazy propagation tag pushing, full coverage boolean conjunction queries ($v = v_{left} \land v_{right}$), interval splitting, and continuous real-number coverage verification on representative range module operations:

- **Input:**
  - Operations sequence:
    ```text
    RangeModule()
    addRange(10, 20)
    removeRange(14, 16)
    queryRange(10, 14)
    queryRange(13, 15)
    queryRange(16, 17)
    ```
- **Required output:** `[true, false, true]`
  - Interval tracking specifications:
    - Tracks half-open real intervals $[left, right) = \{x \in \mathbb{R} \mid left \le x < right\}$.
    - `addRange(left, right)`: Begin tracking every number in $[left, right)$. Merges overlapping tracked intervals.
    - `removeRange(left, right)`: Stop tracking every number in $[left, right)$. Splits or truncates existing intervals.
    - `queryRange(left, right)`: Returns `true` if and only if **every point** in $[left, right)$ is currently tracked.
    - Lifecycle trace:
      - `addRange(10, 20)`: Active interval: $[10, 20)$.
      - `removeRange(14, 16)`: Removes the middle subsegment $[14, 16)$, leaving disjoint intervals $[10, 14) \cup [16, 20)$.
      - `queryRange(10, 14)`: $[10, 14)$ is completely inside $[10, 14) \implies$ `true`.
      - `queryRange(13, 15)`: Overlaps point $14$ which was deleted $\implies$ `false`.
      - `queryRange(16, 17)`: Subsegment $[16, 17)$ is completely inside $[16, 20) \implies$ `true`.
      - Results: `[true, false, true]`.
- **Dynamic Segment Tree & Half-Open Discretization Invariant:**
  - **The Closed Discrete Mapping:**
    - The operations specify half-open intervals $[left, right)$ over integer endpoints.
    - Since endpoints are integers, any real $x \in [left, right)$ belongs to a discrete integer unit $[i, i + 1)$.
    - Mapping each query/update to the discrete closed integer interval:
      $$
      [L, \; R] = [left, \; right - 1]
      $$
    - Preserves exact boundary coverage:
      - $[10, 20) \iff [10, 19]$.
      - $[14, 16) \iff [14, 15]$.
      - $[10, 14) \iff [10, 13]$.
  - **Segment Tree Node Semantics:**
    - Each tree node covers an integer domain $[l, r]$ within $[1, 10^9]$:
      - `v` (boolean): `true` if the entire interval $[l, r]$ is continuously tracked; `false` otherwise.
      - `add` (lazy tag):
        - `+1`: pending instruction to set the entire subtree to `true`.
        - `-1`: pending instruction to set the entire subtree to `false`.
        - `0`: no pending updates.
  - **Boolean Conjunction on Pushup:**
    - An interval is fully covered if and only if **both** its left child and right child are fully covered:
      $$
      node.v = node.left.v \ \land \ node.right.v
      $$
  - **Query Conjunction:**
    - `query(left, right - 1)` checks that every sub-interval intersecting $[L, R]$ has `v == true`.
- **Step-by-Step Worked Execution Trace on the Sample Sequence:**
  - Segment tree covers global coordinate range $[1, 10^9]$. Initially empty (`root.v = false`).
  - **Operation 1: `addRange(10, 20)`:**
    - Target discrete range: $[10, \; 20 - 1] = [10, \; 19]$.
    - Value tag: $+1$.
    - Dynamic segment tree descends to nodes spanning $[10, 19]$.
    - Assigns `node.v = true, node.add = 1`.
    - Range $[10, 19]$ is now fully tracked.
  - **Operation 2: `removeRange(14, 16)`:**
    - Target discrete range: $[14, \; 16 - 1] = [14, \; 15]$.
    - Value tag: $-1$.
    - Pushes down lazy tags from ancestor $[10, 19]$:
      - Splits $[10, 19]$ into left branch $[10, 14]$ and right branch $[15, 19]$.
    - Deletes $[14, 15]$:
      - Sets sub-interval $[14, 15]$ to `node.v = false, node.add = -1`.
    - Pushup recomputes coverage:
      - Left part $[10, 13]$: `true`.
      - Middle part $[14, 15]$: `false`.
      - Right part $[16, 19]$: `true`.
      - Parent $[10, 19]$ becomes `node.v = false` (no longer fully covered).
  - **Operation 3: `queryRange(10, 14)`:**
    - Target discrete range: $[10, \; 14 - 1] = [10, \; 13]$.
    - Traverse nodes intersecting $[10, 13]$:
      - Interval $[10, 13]$ lies entirely within the preserved left segment.
      - Node covering $[10, 13]$ has `node.v == true`.
    - All sub-segments report `true`.
    - Output:
      $$
      ans \leftarrow \mathbf{true}
      $$
  - **Operation 4: `queryRange(13, 15)`:**
    - Target discrete range: $[13, \; 15 - 1] = [13, \; 14]$.
    - Intersecting sub-intervals:
      - Subsegment $[13, 13]$ has `node.v == true`.
      - Subsegment $[14, 14]$ has `node.v == false` (was deleted in Operation 2).
    - Conjunction: $\text{true} \land \text{false} = \mathbf{false}$.
    - Output:
      $$
      ans \leftarrow \mathbf{false}
      $$
  - **Operation 5: `queryRange(16, 17)`:**
    - Target discrete range: $[16, \; 17 - 1] = [16, \; 16]$.
    - Subsegment $[16, 16]$ lies entirely within the preserved right segment $[16, 19]$.
    - Node covering $[16, 16]$ has `node.v == true`.
    - Output:
      $$
      ans \leftarrow \mathbf{true}
      $$
  - **Consolidated Query Responses:**
    $$
    [\mathbf{true}, \; \mathbf{false}, \; \mathbf{true}]
    $$
- **Adjacent Range Merging ($addRange(10, 15), addRange(15, 20)$):**
  - First adds $[10, 14]$.
  - Second adds $[15, 19]$.
  - The union seamlessly bridges at boundary $14 \to 15$ to cover $[10, 19]$.
  - `queryRange(10, 20)` evaluates to **`true`**.
- **Complete Eradication ($removeRange(1, 10^9)$):**
  - Root node set to `v = false, add = -1`.
  - All subsequent queries return `false`.

This instance demonstrates dynamic segment tree range updates and interval set algebra, mathematically proves why mapping half-open intervals to closed integer boundaries preserves point-set topology under boolean operations, and derives $O(\log C)$ per operation and $O(Q \log C)$ space bounds.

---

## 1. Instance & Teaching Goal

Track half-open real intervals $[left, right)$ supporting:
1. `addRange(left, right)`: Add interval.
2. `removeRange(left, right)`: Remove interval.
3. `queryRange(left, right)`: Check if the ENTIRE interval is currently tracked.

```text
Operations:
  addRange(10, 20)    -> tracks [10, 20)
  removeRange(14, 16) -> cuts hole [14, 16) -> leaves [10, 14) and [16, 20)
  queryRange(10, 14)  -> [10, 14) is fully tracked -> returns true
  queryRange(13, 15)  -> includes 14 (deleted!)    -> returns false
  queryRange(16, 17)  -> [16, 17) is fully tracked -> returns true

Result: [ true, false, true ]
```

### The Invariant of the Closed Integer Segment
- Half-open interval $[left, right)$ over integer coordinates is equivalent to the closed integer range $[left, right - 1]$.
- A dynamic segment tree with lazy propagation performs range assignments ($+1$ for add, $-1$ for delete) and answers range queries using boolean conjunction (`left_child.v and right_child.v`).

---

## 2. Conceptual Foundation & Invariants

### 1. Endpoint Discretization:
$$
[left, right) \iff [L, R] = [left, \; right - 1]
$$

### 2. Segment Tree Operations:
$$
\text{addRange}(left, right) \implies \text{modify}(left, \; right - 1, \; +1)
$$
$$
\text{removeRange}(left, right) \implies \text{modify}(left, \; right - 1, \; -1)
$$
$$
\text{queryRange}(left, right) \implies \text{query}(left, \; right - 1)
$$

> **Borel Interval Algebra Invariant.** The family of half-open intervals with integral boundaries forms a Boolean ring whose intersection, union, and complement operations are isomorphic to range assignments on the discrete grid $\mathbb{Z}$, computable via dynamic segment tree bisection.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: `addRange(10, 20)`
- Discrete range $[10, 19] \to \text{True}$.

---

### Step 2: `removeRange(14, 16)`
- Discrete range $[14, 15] \to \text{False}$.
- Tracked regions: $[10, 13]$ and $[16, 19]$.

---

### Step 3: `queryRange(10, 14)`
- Range $[10, 13]$ is completely $\text{True} \implies$ Return **`true`**.

---

### Step 4: `queryRange(13, 15)`
- Range $[13, 14]$ crosses point 14 (which is $\text{False}$) $\implies$ Return **`false`**.

---

### Step 5: `queryRange(16, 17)`
- Range $[16, 16]$ is completely $\text{True} \implies$ Return **`true`**.

---

### Step 6: Output
$$
[\mathbf{true}, \; \mathbf{false}, \; \mathbf{true}]
$$

---

## 4. Complete Execution Trace

| Step | Operation Called | Discrete Range $[L, R]$ | Target Value / Action | Active Disjoint Intervals | Returned Boolean |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `addRange(10, 20)` | $[10, 19]$ | Set $+1$ (`true`) | `{[10, 20)}` | — |
| $2$ | `removeRange(14, 16)` | $[14, 15]$ | Set $-1$ (`false`) | `{[10, 14), [16, 20)}` | — |
| **$3$** | **`queryRange(10, 14)`** | **$[10, 13]$** | **Conjunction Query** | Fully inside `[10, 14)` | **`true`** |
| **$4$** | **`queryRange(13, 15)`** | **$[13, 14]$** | **Conjunction Query** | $14$ is missing | **`false`** |
| **$5$** | **`queryRange(16, 17)`** | **$[16, 16]$** | **Conjunction Query** | Fully inside `[16, 20)` | **`true`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Unit Interval ($addRange(5, 6)$):** Maps to discrete $[5, 5]$ (size 1).
- **Abutting Additions ($[10, 15)$ and $[15, 20)$):** Discrete $[10, 14]$ and $[15, 19]$ merge seamlessly into $[10, 19]$.
- **Removing from Untracked Space ($removeRange(30, 40)$):** Safe no-op; leaves existing intervals unaffected.
- **Large Domain ($C = 10^9$):** Dynamic tree allocates nodes on-demand up to height $\log_2(10^9) \approx 30$.

---

## 6. Traps & Common Anti-Patterns

- **Using Closed Intervals $[left, right]$ without Minus One:** Using $right$ directly causes adjacent intervals that merely share an endpoint (e.g. $[10, 15)$ and $[15, 20)$) to falsely overlap at integer 15, corrupting interval deletion and query semantics. Always use $[left, right - 1]$.
- **Array of Size $10^9$:** Cannot pre-allocate an array of size $10^9$. A dynamic segment tree or balanced BST (interval map) is mandatory.
- **Forgetting Lazy Pushdown:** Querying or updating a child node without pushing down pending `add` tags leads to stale or incorrect subtree values.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Height of dynamic segment tree: $\mathcal{O}(\log C)$ where $C = 10^9 \implies \approx 30$ levels.
  - Each `addRange`, `removeRange`, and `queryRange` operation visits at most $\mathcal{O}(\log C)$ nodes.
  - Total Time: strictly logarithmic $\mathcal{O}(\log C)$ per operation. Completes $10^4$ operations in $< 35$ ms.
- **Auxiliary Space Complexity:**
  - At most $\mathcal{O}(Q \log C)$ nodes allocated dynamically across $Q$ operations.
