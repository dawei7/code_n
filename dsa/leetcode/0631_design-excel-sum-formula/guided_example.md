# Guided Example: Design Excel Sum Formula

We trace the step-by-step spreadsheet cell coordinate indexing (1-based row, 'A'-based column), range syntax expansion (`"A1:B2"` bounding box), multiset dependency graph construction ($dependents[source][target] \leftarrow multiplicity$), recursive delta change propagation ($\Delta \cdot multiplicity$), formula overwrite edge tearing, and dynamic reactive recalculation on representative spreadsheet sessions:

- **Input:**
  - Initialization: $height = 3, \quad width = \text{"C"}$ ($3 \times 3$ grid: rows $1 \dots 3$, columns $A, B, C$)
  - Operation sequence:
    ```text
    Excel excel = new Excel(3, "C");
    excel.set(1, "A", 2);                      // A1 = 2
    excel.sum(3, "C", ["A1", "A1:B2"]);        // C3 = sum(A1, A1:B2), returns 4
    excel.set(2, "B", 2);                      // B2 = 2, propagates change to C3
    excel.get(3, "C");                         // returns 6
    ```
- **Required outputs:**
  - `[null, null, 4, null, 6]`
  - Core spreadsheet mechanics:
    1. Cells can store constant literal integers or dynamic formulas.
    2. Formulas are defined over individual cell references (e.g. `"A1"`) or rectangular ranges (e.g. `"A1:B2"`).
    3. References can overlap: if `"A1"` appears as an individual term and also within `"A1:B2"`, its value is added **twice** (multiplicity 2).
    4. Changing any cell dynamically cascades through the dependency graph to update all dependent formulas.
    5. Setting a literal value on a formula cell **overwrites and deletes** its active formula and breaks its dependency edges.
- **Dependency Multi-Graph & Delta Propagation Architecture:**
  - **Coordinate Translation:**
    - Reference `"C3"` maps to row index $2$ ($3 - 1$) and column index $2$ ($'C' - 'A'$).
  - **Range Parsing ($references(numbers)$):**
    - A range token `"TopLeft:BottomRight"` expands to all cells $(r, c)$ satisfying:
      $$
      r \in [row_{top}, row_{bottom}], \quad c \in [col_{left}, col_{right}]
      $$
    - Accumulate all cell appearances into a multiset frequency map:
      $$
      formula = Counter(\text{cell} \to \text{multiplicity})
      $$
  - **Reactive Graph Links ($dependents$):**
    - For each cell $(r, c)$ in $formula$:
      $$
      dependents[source][target] += multiplicity
      $$
  - **Change Propagation ($\Delta$):**
    - When a cell value changes from $old$ to $new$, compute delta:
      $$
      \Delta = new - old
      $$
    - Recursively propagate to each dependent target:
      $$
      change = \Delta \times multiplicity
      $$
      $$
      values[target] \leftarrow values[target] + change
      $$
- **Step-by-Step Worked Execution Trace:**
  - **Init: `Excel(3, "C")`:**
    - Initialize $3 \times 3$ grid with 0s:
      ```text
          A  B  C
      1 [ 0, 0, 0 ]
      2 [ 0, 0, 0 ]
      3 [ 0, 0, 0 ]
      ```
    - $formulas = \{\}, \quad dependents = \{\}$.
  - **Op 1: `set(1, "A", 2)`:**
    - Target: $A1$ (row 0, col 0).
    - Previous value: $0$.
    - New value: $2$.
    - Delta: $\Delta = 2 - 0 = +2$.
    - $A1$ has no dependents yet $\implies$ No propagation.
    - Grid state: $A1 = 2$.
  - **Op 2: `sum(3, "C", ["A1", "A1:B2"])`:**
    - Target: $C3$ (row 2, col 2).
    - Parse references:
      - Term 1: `"A1"` $\implies$ cell $A1$ (count 1).
      - Term 2: `"A1:B2"` $\implies$ rectangular box spanning rows $1 \dots 2$ and cols $A \dots B$:
        - Cells: $A1, B1, A2, B2$ (count 1 each).
      - Multiplicity Counter:
        $$
        formula(C3) = \{A1: \mathbf{2}, \; B1: \mathbf{1}, \; A2: \mathbf{1}, \; B2: \mathbf{1}\}
        $$
    - Evaluate initial sum using current grid values:
      - $A1 = 2 \implies 2 \times 2 = 4$
      - $B1 = 0 \implies 0 \times 1 = 0$
      - $A2 = 0 \implies 0 \times 1 = 0$
      - $B2 = 0 \implies 0 \times 1 = 0$
      - Sum:
        $$
        value = 4 + 0 + 0 + 0 = \mathbf{4}
        $$
    - Register dependency edges:
      - $dependents[A1][C3] = 2$
      - $dependents[B1][C3] = 1$
      - $dependents[A2][C3] = 1$
      - $dependents[B2][C3] = 1$
    - Assign $C3 = 4$.
    - Returns: **`4`**.
  - **Op 3: `set(2, "B", 2)`:**
    - Target: $B2$ (row 1, col 1).
    - Previous value: $B2 = 0$.
    - New value: $B2 = 2$.
    - Delta:
      $$
      \Delta = 2 - 0 = \mathbf{+2}
      $$
    - Update $B2 \leftarrow 2$.
    - **Trigger Reactive Propagation from $B2$:**
      - Inspect $dependents[B2]$:
        - Target $C3$ is registered with multiplicity $1$!
      - Calculated change for $C3$:
        $$
        change = \Delta \times multiplicity = 2 \times 1 = \mathbf{+2}
        $$
      - Update $C3$:
        $$
        C3 \leftarrow 4 + 2 = \mathbf{6}
        $$
      - Recurse from $C3$: $C3$ has no further dependents $\implies$ Halts.
  - **Op 4: `get(3, "C")`:**
    - Read value of cell $C3$:
      $$
      \mathbf{6}
      $$
- **Formula Overwrite Edge-Tearing Instance:**
  - If we subsequently call `set(3, "C", 10)`:
    - $C3$ is assigned literal $10$.
    - Its formula is removed, and all incoming dependency edges from $A1, B1, A2, B2$ are severed.
    - Future changes to $B2$ will no longer affect $C3$.
- **Multi-Hop Dependency Chain (Diamond Topology):**
  - If $A1$ affects $B1$, and both $A1$ and $B1$ affect $C1$:
  - Updating $A1$ propagates directly to $B1$ and $C1$, and then $B1$'s updated value propagates further to $C1$, accumulating both paths correctly.

This instance demonstrates reactive dataflow programming and directed acyclic graph (DAG) dependency tracking, mathematically proves why multiplicity-weighted delta propagation updates dependent cells in topological order, and derives $O(E)$ update time and $O(V + E)$ space bounds.

---

## 1. Instance & Teaching Goal

Implement a spreadsheet supporting:
- `set(row, col, val)`: Sets literal value and updates dependents.
- `get(row, col)`: Returns current value.
- `sum(row, col, [ranges])`: Sets formula, calculates sum, registers dynamic dependencies, and returns value.

```text
Session Trace:
  set(A1, 2)
  sum(C3, ["A1", "A1:B2"]) -> A1 counted twice, others 0 -> C3 = 4
  set(B2, 2) -> B2 increases by +2 -> C3 increases by +2 -> C3 = 6
  get(C3) -> 6
```

### The Invariant of Multiplicity
- A cell can appear multiple times in a sum formula (e.g. individually and inside a range).
- The graph edge must store a **multiplicity weight** $W$:
  $$
  change(target) = \Delta(source) \times W
  $$

---

## 2. Conceptual Foundation & Invariants

### 1. The Multiset Dependency Relation:
For a formula defined on target cell $T$:
$$
formula[T] = \{(S_i, W_i)\}
$$
where $S_i$ is a source cell and $W_i$ is its occurrence count.
Invert to forward graph:
$$
dependents[S_i][T] = W_i
$$

### 2. Delta Propagation:
When cell $S$ changes by $\Delta = val_{new} - val_{old}$:
For each $(T, W) \in dependents[S]$:
$$
\Delta_T = \Delta \times W
$$
$$
val_T \leftarrow val_T + \Delta_T
$$
$$
\text{propagate}(T, \Delta_T)
$$

> **Linearity of Sum Invariant.** Since the sum formula is a linear combination $\sum W_i S_i$, any differential change $\Delta S_i$ induces a strictly linear change $W_i \Delta S_i$ on all downstream dependents.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: `set(1, "A", 2)`
- $A1 \leftarrow 2$. $\Delta = 2$.
- No dependents.

---

### Step 2: `sum(3, "C", ["A1", "A1:B2"])`
- Range `"A1:B2"` has cells: $A1, A2, B1, B2$.
- Term `"A1"` adds another $A1$.
- Total weights: $A1: 2, A2: 1, B1: 1, B2: 1$.
- Sum: $2 \times 2 + 0 + 0 + 0 = 4$.
- $C3 \leftarrow 4$.
- Register dependencies.

---

### Step 3: `set(2, "B", 2)`
- $B2$: from 0 to 2. $\Delta = +2$.
- Dependent $C3$ has weight 1.
- Propagate to $C3$: change $= 2 \times 1 = +2$.
- $C3 \leftarrow 4 + 2 = 6$.

---

### Step 4: `get(3, "C")`
- Returns **`6`**.

---

## 4. Complete Execution Trace

| Call | Cell | Previous Value | New Value | $\Delta$ | Graph Action | Downstream Effects | Return |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `set` | $A1$ | $0$ | $2$ | $+2$ | None | None | — |
| `sum` | $C3$ | $0$ | $4$ | $+4$ | Add 4 edges to $C3$ | None | **`4`** |
| `set` | $B2$ | $0$ | $2$ | $+2$ | None | $\Delta C3 = +2 \implies C3 = 6$ | — |
| `get` | $C3$ | $6$ | $6$ | $0$ | Query | None | **`6`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Cell Reference (`["A1"]`):** Weight is 1.
- **Overwriting Formula with Literal:** Must delete all incoming edges from $dependents$.
- **Multiple Overlapping Ranges:** Cell counts sum into total multiplicity.
- **Zero Delta ($\Delta = 0$):** Halts propagation early without traversal.

---

## 6. Traps & Common Anti-Patterns

- **Recalculating Formulas from Scratch on Every `get()`:** Re-evaluating large nested formula graphs on every get causes exponential slowdown. Delta propagation keeps cell values constantly up to date in $O(1)$ read time.
- **Ignoring Multiplicity:** Storing dependencies in a set (`set()`) drops duplicates, treating `"A1", "A1:B2"` as weight 1 instead of weight 2.
- **Cycles:** Problem guarantees no circular dependencies (DAG).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `get`: strictly $\mathcal{O}(1)$ direct array lookup.
  - `sum`: $\mathcal{O}(R \cdot C)$ to parse ranges, plus $\mathcal{O}(E)$ to register dependencies and propagate.
  - `set`: $\mathcal{O}(E_{sub})$ where $E_{sub}$ is the number of reachable downstream dependency edges.
  - Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H \cdot W + E)$ space to store grid values and the dependency graph.
