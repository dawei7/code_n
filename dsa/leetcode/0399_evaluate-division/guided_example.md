# Guided Example: Evaluate Division

We trace the step-by-step Weighted Disjoint Set Union (Union-Find with multiplicative weights), path compression weight scaling ($w[x] \leftarrow w[x] \times w[origin]$), root bridge formula derivation ($w[pa] = w[b] \times v / w[a]$), and ratio quotient evaluation ($w[c] / w[d]$) on representative variable division systems:

- **Input:** $equations = [[\text{"a"}, \text{"b"}], [\text{"b"}, \text{"c"}]], \; values = [2.0, 3.0]$, queries:
  - $q_1 = [\text{"a"}, \text{"c"}]$
  - $q_2 = [\text{"b"}, \text{"a"}]$
  - $q_3 = [\text{"a"}, \text{"e"}]$
  - $q_4 = [\text{"a"}, \text{"a"}]$
  - $q_5 = [\text{"x"}, \text{"x"}]$
- **Required output:** `[6.0, 0.5, -1.0, 1.0, -1.0]`
  - Step 1 (Union $a / b = 2.0$):
    - $p[a] \leftarrow b, \; w[a] \leftarrow 2.0$
  - Step 2 (Union $b / c = 3.0$):
    - $p[b] \leftarrow c, \; w[b] \leftarrow 3.0$
  - Step 3 (Query $a / c$ with path compression):
    - $\text{find}(a) \implies origin = b, \; p[a] = c, \; w[a] = 2.0 \times 3.0 = 6.0$
    - Ratio: $w[a] / w[c] = 6.0 / 1.0 = \mathbf{6.0}$
  - Step 4 (Query $b / a$):
    - Same root $c$: $w[b] / w[a] = 3.0 / 6.0 = \mathbf{0.5}$
  - Step 5 (Query $a / e$):
    - Variable `"e"` unseen in equations $\implies \mathbf{-1.0}$
  - Step 6 (Query $a / a$):
    - Variable `"a"` exists $\implies w[a] / w[a] = \mathbf{1.0}$
  - Step 7 (Query $x / x$):
    - Variable `"x"` unseen in equations $\implies \mathbf{-1.0}$
- **Disconnected Components:** $a/b = 2.0, c/d = 3.0 \implies a/d$ has different roots $\implies -1.0$

This instance demonstrates modeling multiplicative relational graphs via weighted union-find, mathematically proves why telescoping path compression preserves transitive ratios, and achieves nearly linear $O((E + Q) \alpha(V))$ runtime and $O(V)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a list of equations $A_i / B_i = values[i]$:
- $a / b = 2.0$
- $b / c = 3.0$
Evaluate queries of the form $C / D$:

```text
Relational Graph:
   a ----(2.0)----> b ----(3.0)----> c
 (a/b=2)          (b/c=3)

Transitive Relations:
  a / c = (a / b) * (b / c) = 2.0 * 3.0 = 6.0
  b / a = 1 / (a / b) = 1 / 2.0 = 0.5
  a / e = Unconnected / Unknown variable 'e' -> -1.0
  a / a = Known variable 'a' -> 1.0
  x / x = Unknown variable 'x' -> -1.0
```

### Why Weighted Union-Find Outperforms Per-Query BFS/DFS
- A graph traversal (BFS/DFS) across $E$ equations for each of the $Q$ queries costs $O(E \cdot Q)$ worst-case time.
- **Weighted DSU (Disjoint Set Union):**
  - Each node $x$ stores its parent $p[x]$ and a weight ratio $w[x] = \frac{x}{p[x]}$.
  - Path compression flattens the tree, setting $p[x] = root$ and $w[x] = \frac{x}{root}$.
  - Any valid query $c / d$ evaluates in $O(\alpha(V)) \approx O(1)$ time via:
    $$
    \frac{c}{d} = \frac{c / root}{d / root} = \frac{w[c]}{w[d]}
    $$

---

## 2. Conceptual Foundation & Invariants

### 1. Data Structures:
- `p`: Dictionary mapping each variable $x$ to its parent $p[x]$.
- `w`: Dictionary where $w[x]$ represents the relative ratio $\frac{x}{p[x]}$. (For a root, $w[r] = 1.0$).

### 2. Path Compression in `find(x)`:
When $x \ne p[x]$:
1. Save intermediate parent: $origin = p[x]$.
2. Recursively find component root: $p[x] = \text{find}(p[x])$.
3. Multiply weights along the path:
   $$
   w[x] \leftarrow w[x] \times w[origin]
   $$
   *Proof:* Since $w[x] = \frac{x}{origin}$ and $w[origin] = \frac{origin}{root}$, their product is $\frac{x}{origin} \times \frac{origin}{root} = \frac{x}{root}$.

### 3. Union Operation on $a / b = v$:
Let $pa = \text{find}(a)$ and $pb = \text{find}(b)$:
If $pa \ne pb$, link root $pa$ to $pb$:
$$
p[pa] \leftarrow pb
$$
What is the new weight $w[pa] = \frac{pa}{pb}$?
$$
\frac{pa}{pb} = \frac{a / w[a]}{b / w[b]} = \frac{a}{b} \times \frac{w[b]}{w[a]} = v \times \frac{w[b]}{w[a]}
$$
Therefore:
$$
w[pa] \leftarrow \frac{w[b] \cdot v}{w[a]}
$$

> **Invariant.** For any variable $x$, after `find(x)`, $p[x]$ is the component root, and $w[x] = \frac{x}{p[x]}$.

---

## 3. Step-by-Step Worked Execution

We trace $equations = [[\text{"a"}, \text{"b"}], [\text{"b"}, \text{"c"}]], values = [2.0, 3.0]$:

---

### Step 1: Initialize Nodes
Initialize every variable as its own root with weight 1.0:
- $p[\text{"a"}] = \text{"a"}, \; w[\text{"a"}] = 1.0$
- $p[\text{"b"}] = \text{"b"}, \; w[\text{"b"}] = 1.0$
- $p[\text{"c"}] = \text{"c"}, \; w[\text{"c"}] = 1.0$

---

### Step 2: Union Equation 1: $a / b = 2.0$
- Find roots:
  - $pa = \text{find}(\text{"a"}) = \text{"a"}, \quad w[\text{"a"}] = 1.0$
  - $pb = \text{find}(\text{"b"}) = \text{"b"}, \quad w[\text{"b"}] = 1.0$
- Connect roots:
  $$
  p[\text{"a"}] \leftarrow \text{"b"}
  $$
- Compute root weight:
  $$
  w[\text{"a"}] \leftarrow \frac{w[\text{"b"}] \cdot 2.0}{w[\text{"a"}]} = \frac{1.0 \times 2.0}{1.0} = \mathbf{2.0}
  $$
- State: $a \to b$ ($w[a] = 2.0$), $b \to b$ ($w[b] = 1.0$).

---

### Step 3: Union Equation 2: $b / c = 3.0$
- Find roots:
  - $pa = \text{find}(\text{"b"}) = \text{"b"}, \quad w[\text{"b"}] = 1.0$
  - $pb = \text{find}(\text{"c"}) = \text{"c"}, \quad w[\text{"c"}] = 1.0$
- Connect roots:
  $$
  p[\text{"b"}] \leftarrow \text{"c"}
  $$
- Compute root weight:
  $$
  w[\text{"b"}] \leftarrow \frac{w[\text{"c"}] \cdot 3.0}{w[\text{"b"}]} = \frac{1.0 \times 3.0}{1.0} = \mathbf{3.0}
  $$
- State: $a \to b$ ($w[a] = 2.0$), $b \to c$ ($w[b] = 3.0$), $c \to c$ ($w[c] = 1.0$).

---

### Step 4: Evaluate Queries

- **Query 1: $a / c$:**
  - $\text{find}(a)$: $p[a] = b \ne a \implies origin = b$.
    - Recurse: $\text{find}(b) \implies p[b] = c, w[b] = 3.0$.
    - Compress: $p[a] \leftarrow c$.
    - Scale weight: $w[a] \leftarrow w[a] \times w[b] = 2.0 \times 3.0 = \mathbf{6.0}$.
  - $\text{find}(c)$: returns $c, w[c] = 1.0$.
  - Same root $c \implies$ quotient is:
    $$
    \frac{w[a]}{w[c]} = \frac{6.0}{1.0} = \mathbf{6.0}
    $$

- **Query 2: $b / a$:**
  - $\text{find}(b) = c, w[b] = 3.0$.
  - $\text{find}(a) = c, w[a] = 6.0$.
  - Same root $c \implies$ quotient is:
    $$
    \frac{w[b]}{w[a]} = \frac{3.0}{6.0} = \mathbf{0.5}
    $$

- **Query 3: $a / e$:**
  - Variable `"e"` not in $p \implies$ return $\mathbf{-1.0}$.

- **Query 4: $a / a$:**
  - Variable `"a"` exists in $p$. $\text{find}(a) == \text{find}(a) \implies$ return:
    $$
    \frac{w[a]}{w[a]} = \mathbf{1.0}
    $$

- **Query 5: $x / x$:**
  - Variable `"x"` not in $p \implies$ return $\mathbf{-1.0}$.

---

## 4. Complete Execution Trace

```text
Equations: [["a","b"]: 2.0, ["b","c"]: 3.0]

Union ("a", "b", 2.0): p["a"] = "b", w["a"] = 2.0
Union ("b", "c", 3.0): p["b"] = "c", w["b"] = 3.0

Queries:
["a", "c"]: find(a) -> compresses to c, w["a"] = 6.0 -> 6.0 / 1.0 = 6.0
["b", "a"]: w["b"] / w["a"] = 3.0 / 6.0 = 0.5
["a", "e"]: "e" not in p -> -1.0
["a", "a"]: w["a"] / w["a"] = 1.0
["x", "x"]: "x" not in p -> -1.0

Output: [6.0, 0.5, -1.0, 1.0, -1.0]
```

| Query $[c, d]$ | $c \in p \land d \in p$? | $\text{find}(c)$ Root | $\text{find}(d)$ Root | Connected ($\text{root}_c == \text{root}_d$)? | Weight $w[c]$ | Weight $w[d]$ | Result $\frac{w[c]}{w[d]}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `["a", "c"]` | True | `"c"` | `"c"` | True | 6.0 | 1.0 | **`6.0`** |
| `["b", "a"]` | True | `"c"` | `"c"` | True | 3.0 | 6.0 | **`0.5`** |
| `["a", "e"]` | False (`"e" \notin p`) | - | - | - | - | - | **`-1.0`** |
| `["a", "a"]` | True | `"c"` | `"c"` | True | 6.0 | 6.0 | **`1.0`** |
| **`["x", "x"]`**| **False (`"x" \notin p`)** | - | - | - | - | - | **`-1.0`** |

---

## 5. Algorithmic Correctness

**Soundness.** Because path compression recursively updates $w[x] = w[x] \times w[origin]$, $w[x]$ always satisfies $w[x] = x / root$. For any two variables $c$ and $d$ sharing the same root $r$, the ratio $c / d = (c / r) / (d / r) = w[c] / w[d]$. If $c$ and $d$ belong to different components, no chain of equations connects them, making the answer undefined (returning $-1.0$).

**Completeness.** Every given equation is merged. If a chain of equalities exists between $c$ and $d$, they will share the same root in the DSU. Unknown variables are caught by checking membership in $p$, ensuring all possible query categories are handled correctly.

---

## 6. Traps This Instance Exposes

- **Undefined Self-Query ($x / x$):** If variable `x` never appeared in any equation, $x / x$ cannot be assumed to be $1.0$ because $x$ is completely undefined in the system. It must return $-1.0$.
- **Path Compression Weight Multiplication Order:** Saving `origin = p[x]` before calling `p[x] = find(p[x])` is mandatory. Calling `find` mutates `p[x]`, so without caching `origin`, the previous parent's weight cannot be fetched.
- **Union Weight Formula Derivation:** Setting $p[pa] = pb$ requires $w[pa] = w[b] \times v / w[a]$. Inverting or misaligning this formula corrupts component ratios.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((E + Q) \alpha(V))$, where $E = \text{len}(equations)$, $Q = \text{len}(queries)$, and $V$ is the number of unique variables.
  - Adding $E$ equations performs $E$ union operations.
  - Processing $Q$ queries performs $2Q$ find operations.
  - With path compression, DSU operations run in amortized inverse-Ackermann time $O(\alpha(V)) \approx O(1)$.
- **Auxiliary Space Complexity:** $O(V)$ auxiliary space to store parent pointers and weights for the $V$ distinct variables in hash maps $p$ and $w$.
