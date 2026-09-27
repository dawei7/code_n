# Guided Example: Find Smallest Letter Greater Than Target

We trace the step-by-step lexicographical character comparison, upper-bound binary search bisection ($bisect\_right$), strict greater-than inequality evaluation ($c > target$), circular modular wraparound ($i \pmod n$), and boundary condition resolution on representative sorted character arrays:

- **Input:** $letters = [\text{"c"}, \; \text{"f"}, \; \text{"j"}], \quad target = \text{"c"}$
- **Required output:** `"f"`
  - Search criteria:
    - $letters$ is a non-empty array of characters sorted in **non-decreasing order**.
    - Find the lexicographically smallest character in $letters$ that is **strictly greater** than $target$.
    - **Circular Wraparound Rule:**
      - If no character in $letters$ is strictly greater than $target$ (i.e. all characters are $\le target$), wrap around and return the **very first character** $letters[0]$.
    - For the input:
      - Comparing each character against $target = \text{"c"}$:
        - $letters[0] = \text{"c"}$: not strictly greater ($\text{"c"} \le \text{"c"}$).
        - $letters[1] = \text{"f"}$: strictly greater ($\text{"f"} > \text{"c"}$).
      - The first strictly greater character is `"f"`.
      - Output is `"f"`.
- **Binary Search & Circular Modulo Invariant:**
  - **The Upper Bound Specification:**
    - We seek the earliest index $i \in [0, n - 1]$ such that:
      $$
      letters[i] > target
      $$
    - In standard binary search semantics, this corresponds precisely to the **upper bound** insertion index ($bisect\_right$):
      $$
      i = \min \{ j \in [0, n] \mid \forall k < j, \; letters[k] \le target \}
      $$
  - **The Circular Wraparound Identity:**
    - Two outcomes are possible:
      1. $i < n$: At least one character is strictly greater than $target$. The answer is $letters[i]$.
      2. $i == n$: Every character in $letters$ is $\le target$. By the circular rule, wrap to the start: $letters[0]$.
    - Both cases are unified into a single modulo expression:
      $$
      ans = letters[i \pmod n]
      $$
- **Step-by-Step Worked Execution Trace on $letters = [\text{"c"}, \text{"f"}, \text{"j"}], target = \text{"c"}$:**
  - Array length: $n = 3$. Indices: $0, 1, 2$.
  - Search range: $low = 0, \; high = 3$.
  - Target character: $target = \text{"c"}$ (ASCII 99).
  - **Iteration 1 ($low = 0, high = 3$):**
    - Compute midpoint:
      $$
      mid = \lfloor (0 + 3) / 2 \rfloor = \mathbf{1}
      $$
    - Inspect $letters[1] = \text{"f"}$ (ASCII 102):
      $$
      \text{"f"} > \text{"c"} \iff 102 > 99 \quad \mathbf{(True)}
      $$
    - The character at $mid$ is strictly greater. The earliest such element could be at index 1 or earlier:
      $$
      high \leftarrow mid = \mathbf{1}
      $$
  - **Iteration 2 ($low = 0, high = 1$):**
    - Compute midpoint:
      $$
      mid = \lfloor (0 + 1) / 2 \rfloor = \mathbf{0}
      $$
    - Inspect $letters[0] = \text{"c"}$ (ASCII 99):
      $$
      \text{"c"} \le \text{"c"} \iff 99 \le 99 \quad \mathbf{(Not\ Strictly\ Greater)}
      $$
    - Index 0 cannot be the answer. Advance lower bound:
      $$
      low \leftarrow mid + 1 = \mathbf{1}
      $$
  - **Termination:**
    - $low = 1, high = 1 \implies$ Search space converged at index $i = 1$.
  - **Apply Modular Wraparound:**
    $$
    \text{final\_index} = 1 \pmod 3 = \mathbf{1}
    $$
    $$
    ans = letters[1] = \mathbf{\text{"f"}}
    $$
- **Circular Wraparound Trace ($letters = [\text{"x"}, \text{"x"}, \text{"y"}, \text{"y"}], target = \text{"z"}$):**
  - All characters are $\le \text{"z"}$.
  - Binary search converges to $i = 4 == n$.
  - Modular wraparound:
    $$
    4 \pmod 4 = \mathbf{0}
    $$
    $$
    ans = letters[0] = \mathbf{\text{"x"}}
    $$
- **Target Smaller Than All Elements ($letters = [\text{"c"}, \text{"f"}, \text{"j"}], target = \text{"a"}$):**
  - $letters[0] = \text{"c"} > \text{"a"}$.
  - Binary search converges to $i = 0$.
  - Returns $letters[0] = \mathbf{\text{"c"}}$.

This instance demonstrates logarithmic upper bound bisection over ordered alphabets and modular quotient projection, mathematically proves why strict inequality partition forces a unique insertion boundary, and derives $O(\log N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a sorted array of characters $letters$ and a $target$:
Find the **smallest character strictly greater than $target$**.
If no such character exists, **wrap around** to return the first character $letters[0]$.

```text
letters = [ "c", "f", "j" ], target = "c"

Compare:
  letters[0] = "c" <= "c" (not strictly greater)
  letters[1] = "f" >  "c" (strictly greater!)

Smallest strictly greater letter is "f".
Result: "f"
```

### The Invariant of the Upper Bound with Wraparound
- In a sorted array, finding the first element $> target$ is the upper bound binary search index $i$.
- If $i < n$, return $letters[i]$. If $i == n$, wrap around to $letters[0]$.
- Formula: $letters[i \pmod n]$.

---

## 2. Conceptual Foundation & Invariants

### 1. Upper Bound Binary Search:
$$
i = \text{bisect\_right}(letters, target)
$$

### 2. Circular Projection:
$$
ans = letters[i \bmod n]
$$

> **Circular Quotients Invariant.** The sequence of characters on the cyclic group $\mathbb{Z} / n\mathbb{Z}$ satisfies the circular successor condition $S(target) = A[\min \{j \in [0, n] \mid A[j] > target\} \bmod n]$, computable via binary search over the linear lift.

---

## 3. Step-by-Step Worked Execution

We trace $letters = [\text{"c"}, \text{"f"}, \text{"j"}], target = \text{"c"}$:

---

### Step 1: Search Range
- $low = 0, high = 3$.

---

### Step 2: Bisection
- $mid = 1 \implies letters[1] = \text{"f"} > \text{"c"} \implies high \leftarrow 1$.
- $mid = 0 \implies letters[0] = \text{"c"} \le \text{"c"} \implies low \leftarrow 1$.
- Converges at $i = 1$.

---

### Step 3: Wrap & Output
- $1 \pmod 3 = 1 \implies letters[1] = \mathbf{\text{"f"}}$.

---

## 4. Complete Execution Trace

| Step | Search Interval $[low, high)$ | Midpoint Index $mid$ | Character Tested | Condition $letters[mid] > target$? | Range Adjustment |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $[0, 3)$ | $1$ | `"f"` | Yes (`"f" > "c"`) | $high \leftarrow 1$ |
| $2$ | $[0, 1)$ | $0$ | `"c"` | No (`"c" <= "c"`) | $low \leftarrow 1$ |
| **Converged**| $[1, 1)$ | — | — | **Index $i = 1$** | **Result: `letters[1] = "f"`** |

---

## 5. Boundary Cases & Failure Modes

- **Target $\ge$ All Elements ($target = \text{"z"}$):** Converges to $i = n \implies n \pmod n = 0 \implies$ returns $letters[0]$.
- **Target $<$ All Elements ($target = \text{"a"}$):** Converges to $i = 0 \implies$ returns $letters[0]$.
- **Duplicate Characters ($[\text{"e"}, \text{"e"}, \text{"n"}, \text{"n"}], target = \text{"e"}$):** Upper bound skips all `"e"`s to land on `"n"`.
- **Target Equals Maximum Element ($target = \text{"j"}$):** Wraps around to $letters[0]$.

---

## 6. Traps & Common Anti-Patterns

- **Using Lower Bound (`bisect_left`):** Lower bound finds the first element $\ge target$. If $target$ is present in $letters$, lower bound returns $target$ itself instead of the strictly greater element! Must use upper bound (`bisect_right`).
- **Forgetting Wraparound:** If $i == n$, returning an out-of-bounds index throws an IndexError. Always use $i \pmod n$ or check `if i == n: return letters[0]`.
- **Linear Scan ($O(N)$):** While linear scan passes for small arrays, binary search runs in strictly logarithmic $\mathcal{O}(\log N)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Binary search divides the search space in half at each step: $\mathcal{O}(\log N)$.
  - Total Time: strictly logarithmic $\mathcal{O}(\log N)$. Completes in $< 0.05$ ms for $N = 10^4$.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (only scalar index pointers $low, high, mid$).