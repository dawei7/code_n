# Guided Example: Cracking the Safe

We trace the step-by-step de Bruijn sequence formulation, state space condensation to $(n-1)$-length prefix vertices, Eulerian circuit construction on balanced directed graphs ($in\text{-}degree = out\text{-}degree = k$), Hierholzer backtracking edge traversal, and minimal overlapping sequence generation on representative safe combinations:

- **Input:** $n = 2, \quad k = 2$
- **Required output:** `"01100"` (or any valid de Bruijn sequence)
  - Safe unlocking criteria:
    - The safe password consists of $n$ digits, each chosen from $\{0, 1, \dots, k - 1\}$.
    - Total possible passwords:
      $$
      k^n = 2^2 = \mathbf{4\ combinations:}\quad \{\text{"00"}, \; \text{"01"}, \; \text{"10"}, \; \text{"11"}\}
      $$
    - The safe continuously tracks the most recent $n$ digits entered.
    - If those $n$ digits match the password, the safe immediately unlocks.
    - Objective: Generate the **shortest possible string** that contains all $k^n$ distinct passwords as contiguous substrings.
    - Theoretical Lower Bound:
      - Each new character appended can introduce at most 1 new $n$-length substring.
      - The absolute minimum length required to embed $k^n$ distinct $n$-tuples is:
        $$
        L_{\min} = k^n + n - 1 = 2^2 + 2 - 1 = \mathbf{5\ characters}
        $$
    - For `"01100"`:
      - Substring at index $0 \dots 1$: `"01"`
      - Substring at index $1 \dots 2$: `"11"`
      - Substring at index $2 \dots 3$: `"10"`
      - Substring at index $3 \dots 4$: `"00"`
      - All 4 passwords are contained within exactly 5 characters!
- **De Bruijn Graph & Eulerian Circuit Invariant:**
  - **Graph Construction:**
    - Vertices ($V$): All strings of length $n - 1$ over alphabet $\{0, \dots, k - 1\}$.
      - For $n = 2, k = 2$: $V = \{\text{"0"}, \text{"1"}\}$.
    - Directed Edges ($E$): For each vertex $u$ and each digit $x \in \{0, \dots, k - 1\}$, draw a directed edge with label $x$ to vertex:
      $$
      v = (u \times 10 + x) \pmod{10^{n - 1}}
      $$
    - Every directed edge corresponds bijectively to a complete $n$-digit password: the prefix $u$ followed by $x$.
    - Total edges: $|E| = k^{n - 1} \times k = k^n$.
  - **The Eulerian Condition:**
    - Every vertex $u$ has exactly $k$ outgoing edges and $k$ incoming edges:
      $$
      in(u) = out(u) = k
      $$
    - The directed graph is strongly connected and balanced $\implies$ an **Eulerian circuit** traversing every edge exactly once is guaranteed to exist!
  - **Hierholzer's Algorithm Protocol:**
    - Perform DFS from vertex $0$:
      - For each available edge $x \in \{0, \dots, k - 1\}$:
        - If edge $(u \to v, x)$ has not been visited:
          - Mark edge visited.
          - Recurse into vertex $v$.
          - Post-order append label $x$ to the sequence!
    - After unwinding, prepend $(n - 1)$ zeros for the starting prefix.
- **Step-by-Step Worked Execution Trace on $n = 2, k = 2$:**
  - Vertices (length $n - 1 = 1$): Node `0`, Node `1`.
  - Modulo factor: $mod = 10^{2 - 1} = 10$.
  - Visited edge set: $vis = \emptyset$, result stack: $ans = []$.
  - Start DFS at root: $u = 0$.
  - **Call 1: `dfs(0)`:**
    - Edge choice $x = 0$:
      - Edge code: $e = 0 \times 10 + 0 = \mathbf{00}$.
      - $00 \notin vis \implies vis.\text{add}(00)$.
      - Target vertex: $v = 00 \pmod{10} = 0$.
      - Recurse `dfs(0)`.
  - **Call 2: `dfs(0)` (Second visit to Node 0):**
    - Edge choice $x = 0$: $00 \in vis$ (already used).
    - Edge choice $x = 1$:
      - Edge code: $e = 0 \times 10 + 1 = \mathbf{01}$.
      - $01 \notin vis \implies vis.\text{add}(01)$.
      - Target vertex: $v = 01 \pmod{10} = 1$.
      - Recurse `dfs(1)`.
  - **Call 3: `dfs(1)`:**
    - Edge choice $x = 0$:
      - Edge code: $e = 1 \times 10 + 0 = \mathbf{10}$.
      - $10 \notin vis \implies vis.\text{add}(10)$.
      - Target vertex: $v = 10 \pmod{10} = 0$.
      - Recurse `dfs(0)`.
  - **Call 4: `dfs(0)` (Third visit to Node 0):**
    - Edge choice $x = 0$: $00 \in vis$.
    - Edge choice $x = 1$: $01 \in vis$.
    - Both outgoing edges exhausted from Node 0! Backtrack begins.
  - **Backtrack Unwinds & Post-Order Append:**
    - Unwind to Call 3 (Edge was $x = 0$):
      $$
      ans.\text{append}(\text{"0"}) \implies ans = [\text{"0"}]
      $$
    - Resume Call 3 at Node 1:
      - Edge choice $x = 1$:
        - Edge code: $e = 1 \times 10 + 1 = \mathbf{11}$.
        - $11 \notin vis \implies vis.\text{add}(11)$.
        - Target vertex: $v = 11 \pmod{10} = 1$.
        - Recurse `dfs(1)` (all outgoing from 1 now used; unwinds immediately).
      - Append label $x = 1$:
        $$
        ans.\text{append}(\text{"1"}) \implies ans = [\text{"0"}, \; \text{"1"}]
        $$
    - Unwind to Call 2 (Edge was $x = 1$):
      $$
      ans.\text{append}(\text{"1"}) \implies ans = [\text{"0"}, \; \text{"1"}, \; \text{"1"}]
      $$
    - Unwind to Call 1 (Edge was $x = 0$):
      $$
      ans.\text{append}(\text{"0"}) \implies ans = [\text{"0"}, \; \text{"1"}, \; \text{"1"}, \; \text{"0"}]
      $$
  - **Final Base Prefix Padding:**
    - Prepend initial $(n - 1) = 1$ zero:
      $$
      ans.\text{append}(\text{"0"}) \implies [\text{"0"}, \text{"1"}, \text{"1"}, \text{"0"}, \mathbf{\text{"0"}}]
      $$
    - Joined string:
      $$
      ans = \mathbf{\text{"01100"}}
      $$
- **Single-Digit Passwords ($n = 1, k = 2$):**
  - Passwords: `"0"`, `"1"`.
  - Node is empty string (length 0).
  - Traverses digits 0 and 1.
  - Returns `"10"` (or `"01"`). Length $= 2^1 + 1 - 1 = 2$.

This instance demonstrates de Bruijn sequence generation and Eulerian trail synthesis on de Bruijn digraphs via Hierholzer's post-order depth-first traversal, mathematically proves why in-degree equality guarantees complete edge factorability, and derives $O(k^n)$ execution time and $O(k^n)$ space bounds.

---

## 1. Instance & Teaching Goal

Given password length $n$ and alphabet size $k$ (digits $0 \dots k - 1$):
Find the **shortest string containing all $k^n$ possible passwords** as contiguous substrings.

```text
n = 2, k = 2
All 4 passwords: "00", "01", "10", "11"

Minimal string: "01100" (length 5)
  "01" at [0..1]
  "11" at [1..2]
  "10" at [2..3]
  "00" at [3..4]

All passwords covered in 5 characters!
Result: "01100"
```

### The Invariant of the de Bruijn Eulerian Circuit
- Vertices represent prefixes of length $n - 1$.
- Directed edges represent appending digit $x$, forming an $n$-length password.
- Because each node has equal in-degree and out-degree ($k$), an **Eulerian circuit** visits every edge (password) exactly once.
- Total length is optimal: $k^n + n - 1$.

---

## 2. Conceptual Foundation & Invariants

### 1. De Bruijn Digraph Definition:
$$
V = \{0, \dots, k - 1\}^{n - 1}, \quad E = \{ (u, (u \cdot 10 + x) \bmod 10^{n - 1}) \mid x \in \{0, \dots, k - 1\} \}
$$

### 2. Hierholzer's Circuit Assembly:
$$
\text{dfs}(u): \quad \forall x \in [0, k - 1]: \quad \text{if } (u, x) \notin vis \implies vis.\text{add}((u, x)), \; \text{dfs}(v), \; ans.\text{append}(x)
$$
$$
\text{output} = \text{reverse}(ans) + \text{"0"}^{n - 1}
$$

> **De Bruijn Cycle Theorem.** For any alphabet size $k$ and dimension $n$, the de Bruijn digraph $B(k, n-1)$ is Eulerian, whose Eulerian paths correspond bijectively to universal cycles of minimal length $k^n + n - 1$.

---

## 3. Step-by-Step Worked Execution

We trace $n = 2, k = 2$:

---

### Step 1: Start at Node 0
- Traverse edges:
  - $0 \to 0$ via 0 (edge `00`).
  - $0 \to 1$ via 1 (edge `01`).
  - $1 \to 0$ via 0 (edge `10`).
  - $1 \to 1$ via 1 (edge `11`).

---

### Step 2: Unwind and Append
- Backtracking appends edge labels in post-order.
- Yields sequence `"0110"`.

---

### Step 3: Add Starting Prefix
- Add `"0"` prefix $\implies \mathbf{\text{"01100"}}$.

---

### Step 4: Output
$$
\mathbf{\text{"01100"}}
$$

---

## 4. Complete Execution Trace

| Step | Current Node $u$ | Digit Appended $x$ | Directed Edge Formed | Target Node $v$ | Edge Used Status | Backtrack Post-Order Append |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `0` | `0` | `"00"` | `0` | Visited | — |
| $2$ | `0` | `1` | `"01"` | `1` | Visited | — |
| $3$ | `1` | `0` | `"10"` | `0` | Visited | — |
| $4$ | `0` | — | All used | — | Dead end | Append `'0'` |
| $5$ | `1` | `1` | `"11"` | `1` | Visited | Append `'1'` |
| $6$ | — | — | — | — | Unwinding | Append `'1'`, `'0'` |
| **Final**| — | — | — | — | Prefix added | **`"01100"`** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 1$:** Single digit passwords $\implies$ length is $k^1 + 1 - 1 = k$ (e.g. `"10"`).
- **$k = 1$:** Alphabet of size 1 $\implies$ only one password `"00...0"` of length $n$.
- **Large Inputs ($n = 4, k = 10$):** $10^4 = 10,000$ combinations $\implies$ recursion depth $10^4$ handled smoothly by DFS.
- **Multiple Valid Circuits:** Any valid Eulerian circuit is acceptable.

---

## 6. Traps & Common Anti-Patterns

- **Appending Labels Pre-Order:** Appending edge labels when traversing forward instead of during post-order unwinding can trap the DFS in premature dead ends before all cycles are explored. Hierholzer requires **post-order** collection.
- **Overlapping Window Off-By-One:** Forgetting to add the initial $(n - 1)$ characters produces a string that misses the first password prefix.
- **Brute Force Concatenation ($k^n \times n$):** Concatenating passwords naively (e.g. `"00011011"`) produces a string of length $4 \times 2 = 8$, far exceeding the minimal 5-character bound.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Total edges in the de Bruijn graph: $|E| = k^n$.
  - Each edge is visited and marked exactly once during DFS: $\mathcal{O}(k^n)$.
  - Total Time: strictly optimal linear $\mathcal{O}(k^n)$. For $k^n \le 4096$, completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(k^n)$ space for the visited edge set, call stack, and result list.
