# Guided Example: Minimum Index Sum of Two Lists

We trace the step-by-step secondary list index mapping ($d[s] = j$), intersection element discovery ($s \in d$), index sum evaluation ($i + j$), minimum sum tracking with dynamic result array flushing ($i + j < mi \implies ans = [s]$), tie collection ($i + j == mi \implies ans.\text{append}(s)$), and optimal common interest extraction on representative restaurant preference lists:

- **Input:**
  - $list_1 = [\text{"Shogun"}, \; \text{"Tapioca Express"}, \; \text{"Burger King"}, \; \text{"KFC"}]$
  - $list_2 = [\text{"KFC"}, \; \text{"Shogun"}, \; \text{"Burger King"}]$
- **Required output:** `["Shogun"]` (order of tied outputs does not matter)
  - Objective: Identify the shared string(s) that minimize the sum of their indices:
    $$
    \text{Index Sum}(s) = \text{index}_1(s) + \text{index}_2(s)
    $$
  - If multiple common strings achieve the exact same minimum index sum, return all of them.
- **Hash Table Indexing & Dynamic Minimum Tracking:**
  - Build a hash map $d$ from the second list mapping each restaurant name to its 0-based index:
    $$
    d[s] = j
    $$
  - Iterate through the first list with index $i$ and name $s$:
    - If $s$ exists in $d$:
      - Calculate index sum: $current\_sum = i + d[s]$.
      - **Case 1: Strictly smaller sum found ($current\_sum < mi$):**
        - A new global minimum is achieved!
        - Update minimum: $mi \leftarrow current\_sum$.
        - Reset result list to contain only this restaurant: $ans = [s]$.
      - **Case 2: Tie with active minimum ($current\_sum == mi$):**
        - This restaurant matches the current best score!
        - Append to result list: $ans.\text{append}(s)$.
      - **Case 3: Inferior sum ($current\_sum > mi$):**
        - Ignore.
- **Step-by-Step Worked Trace on Sample Data:**
  - **Step 1: Index $list_2$ into Hash Map $d$:**
    - `"KFC"` $\to$ index $0$
    - `"Shogun"` $\to$ index $1$
    - `"Burger King"` $\to$ index $2$
    - Hash map:
      $$
      d = \{\text{"KFC"}: 0, \; \text{"Shogun"}: 1, \; \text{"Burger King"}: 2\}
      $$
  - **Step 2: Initialize Minimum and Output:**
    $$
    mi = \infty, \quad ans = []
    $$
  - **Step 3: Scan $list_1$ with Index $i$:**
    - **Item 0 ($i = 0, \; s = \text{"Shogun"}$):**
      - In $d$? Yes! $j = d[\text{"Shogun"}] = 1$.
      - Index sum:
        $$
        i + j = 0 + 1 = \mathbf{1}
        $$
      - Compare with $mi = \infty$:
        $$
        1 < \infty \implies mi \leftarrow \mathbf{1}, \quad ans = [\text{"Shogun"}]
        $$
    - **Item 1 ($i = 1, \; s = \text{"Tapioca Express"}$):**
      - In $d$? No. Skip.
    - **Item 2 ($i = 2, \; s = \text{"Burger King"}$):**
      - In $d$? Yes! $j = d[\text{"Burger King"}] = 2$.
      - Index sum:
        $$
        i + j = 2 + 2 = \mathbf{4}
        $$
      - Compare with $mi = 1$:
        $$
        4 > 1 \implies \text{Inferior. Skip.}
        $$
    - **Item 3 ($i = 3, \; s = \text{"KFC"}$):**
      - In $d$? Yes! $j = d[\text{"KFC"}] = 0$.
      - Index sum:
        $$
        i + j = 3 + 0 = \mathbf{3}
        $$
      - Compare with $mi = 1$:
        $$
        3 > 1 \implies \text{Inferior. Skip.}
        $$
  - **Step 4: Final Output Collection:**
    - Smallest index sum achieved: $mi = 1$.
    - Common restaurant(s) achieving $1$:
      $$
      ans = \mathbf{[\text{"Shogun"}]}
      $$
- **Tied Minimum Instance ($list_1 = [\text{"A"}, \text{"B"}], list_2 = [\text{"B"}, \text{"A"}]$):**
  - For `"A"`: $i + j = 0 + 1 = 1 \implies mi = 1, ans = [\text{"A"}]$.
  - For `"B"`: $i + j = 1 + 0 = 1 \implies i + j == mi \implies ans.\text{append}(\text{"B"})$.
  - Output contains both: `["A", "B"]`.
- **Early Exit / Pruning Insight:**
  - Since $j \ge 0$, any index $i$ in $list_1$ where $i > mi$ can never achieve an index sum smaller than $mi$ (because $i + j \ge i > mi$).
  - Once $i > mi$, the scan can safely terminate early!

This instance demonstrates indexed intersection filtering over ordered string domains, mathematically proves why single-pass hash lookups with dynamic list flushing maintain optimal tie sets, and derives $O(N_1 + N_2)$ runtime and $O(N_2)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two lists of strings $list_1$ and $list_2$:
Find all shared strings that have the **minimum index sum** $i + j$.
Return all candidates if there is a tie.

```text
list1: ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2: ["KFC", "Shogun", "Burger King"]

Common elements:
  "Shogun":      0 + 1 = 1  <-- Minimum!
  "Burger King": 2 + 2 = 4
  "KFC":         3 + 0 = 3

Minimum sum = 1
Result: ["Shogun"]
```

### Avoiding Quadratic Searches
- Checking every element in $list_1$ against every element in $list_2$ takes $O(|list_1| \cdot |list_2|)$ string comparisons.
- By pre-hashing $list_2$ into a hash map `{string: index}`:
  - Looking up whether $s \in list_2$ takes $O(1)$ time.
  - Total time drops from quadratic to strictly linear $O(|list_1| + |list_2|)$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Dynamic Tie Maintenance Protocol:
- Initialize $mi = \infty, \; ans = []$.
- For each shared item with index sum $S = i + j$:
  - If $S < mi$:
    - $mi \leftarrow S$
    - $ans \leftarrow [item]$  (flush stale candidates).
  - Else if $S == mi$:
    - $ans.\text{append}(item)$  (collect tied candidate).

> **Monotonic Minimum Invariant.** The tracker variable $mi$ never increases, and the list $ans$ contains exclusively items whose index sum equals the current global minimum $mi$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Pre-hash $list_2$
- $d[\text{"KFC"}] = 0$
- $d[\text{"Shogun"}] = 1$
- $d[\text{"Burger King"}] = 2$

---

### Step 2: Iterate over $list_1$
- $i = 0$ (`"Shogun"`):
  - $j = 1 \implies S = 0 + 1 = 1$.
  - $1 < \infty \implies mi = 1, \; ans = [\text{"Shogun"}]$.
- $i = 1$ (`"Tapioca Express"`):
  - Not in $d$.
- $i = 2$ (`"Burger King"`):
  - $j = 2 \implies S = 2 + 2 = 4$.
  - $4 > 1 \implies$ Ignored.
- $i = 3$ (`"KFC"`):
  - $j = 0 \implies S = 3 + 0 = 3$.
  - $3 > 1 \implies$ Ignored.

---

### Step 3: Final Output
$$
ans = \mathbf{[\text{"Shogun"}]}
$$

---

## 4. Complete Execution Trace

| $list_1$ Index $i$ | Restaurant | In $list_2$? | $list_2$ Index $j$ | Index Sum $i + j$ | Comparison with $mi$ | Active Result $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | `"Shogun"` | **Yes** | $1$ | **$1$** | $1 < \infty$ (New min) | `["Shogun"]` |
| $1$ | `"Tapioca Express"` | No | — | — | — | `["Shogun"]` |
| $2$ | `"Burger King"` | **Yes** | $2$ | $4$ | $4 > 1$ (Skip) | `["Shogun"]` |
| $3$ | `"KFC"` | **Yes** | $0$ | $3$ | $3 > 1$ (Skip) | `["Shogun"]` |
| **Final** | — | — | — | **$mi = 1$** | — | **`["Shogun"]`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Shared Element:** Discovered and returned as a 1-element list.
- **Multiple Ties:** All elements achieving the exact minimum index sum are collected in $ans$.
- **Lists Identical:** Element at index 0 has sum $0 + 0 = 0 \implies$ returns `[list1[0]]`.
- **Shared Element at Last Position ($i = n-1, j = m-1$):** Still correctly evaluated and returned if it is the only common element.

---

## 6. Traps & Common Anti-Patterns

- **Not Clearing the List When a Smaller Sum is Found:** Appending new minimums without resetting $ans$ leaves previously discovered larger index sums in the output.
- **Nested Loops Without Hashing ($O(N_1 \cdot N_2)$):** Iterating through both arrays with nested loops causes quadratic slowdown on large lists ($1000 \times 1000$).
- **Assuming Strings Are Single Words:** Restaurant names can contain spaces (e.g. `"Tapioca Express"`). Store complete raw string tokens.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Building the hash map of $list_2$: $\mathcal{O}(N_2 \cdot L)$ where $L$ is average string length.
  - Scanning $list_1$ and performing hash lookups: $\mathcal{O}(N_1 \cdot L)$.
  - Total Time: strictly linear $\mathcal{O}((N_1 + N_2) \cdot L)$. For $N \le 1000$, completes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N_2 \cdot L)$ space to store the hash map $d$.
