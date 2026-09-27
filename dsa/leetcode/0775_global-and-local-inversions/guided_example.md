# Guided Example: Global and Local Inversions

We trace the step-by-step inversion classification (local vs global), strict subset relation ($\text{Local} \subseteq \text{Global}$), non-local inversion equivalence theorem ($j \ge i + 2 \implies nums[i] \le nums[j]$), running prefix maximum tracking with distance gap 2 ($mx = \max(mx, nums[i-2])$), early violation detection ($mx > nums[i]$), and permutation displacement characterization ($|nums[i] - i| \le 1$) on representative permutations:

- **Input:** $nums = [1, 0, 2]$
- **Required output:** `true`
  - Inversion definitions:
    - **Global Inversion:** Any pair of indices $(i, j)$ such that $0 \le i < j < n$ and $nums[i] > nums[j]$.
    - **Local Inversion:** Any index $i$ such that $0 \le i < n - 1$ and $nums[i] > nums[i + 1]$.
    - Objective: Return `true` if and only if:
      $$
      \text{count(Global Inversions)} == \text{count(Local Inversions)}
      $$
    - For $nums = [1, 0, 2]$:
      - Local inversions:
        - Index 0: $nums[0] = 1 > nums[1] = 0 \implies$ Pair $(0, 1)$ is local. (Total: 1).
      - Global inversions:
        - Pair $(0, 1)$: $1 > 0 \implies$ Inversion.
        - Pair $(0, 2)$: $1 < 2 \implies$ Not an inversion.
        - Pair $(1, 2)$: $0 < 2 \implies$ Not an inversion.
        - Total global inversions: 1.
      - Global count ($1$) equals Local count ($1$) $\implies$ return **`true`**.
- **Non-Local Inversion Absence Invariant:**
  - **The Subset Theorem:**
    - Notice that every local inversion $(i, i + 1)$ is by definition a global inversion where $j = i + 1$.
    - Therefore, the set of local inversions is a **strict subset** of global inversions:
      $$
      \text{Local} \subseteq \text{Global}
      $$
    - The two counts are equal if and only if **no other global inversions exist**!
  - **The Distance $\ge 2$ Condition:**
    - Any global inversion $(i, j)$ that is NOT a local inversion must satisfy:
      $$
      j \ge i + 2 \quad \text{and} \quad nums[i] > nums[j]
      $$
    - Consequently, the problem is completely equivalent to testing:
      $$
      \text{Does there exist any pair } (i, j) \text{ with } j - i \ge 2 \text{ such that } nums[i] > nums[j]?
      $$
    - If such a pair exists, global inversions strictly outnumber local inversions $\implies$ return `false`.
    - If no such pair exists, the counts are guaranteed equal $\implies$ return `true`.
  - **Prefix Maximum Verification:**
    - For each position $i \in [2, n - 1]$:
      - Maintain $mx$, the maximum element seen so far at distance $\ge 2$:
        $$
        mx \leftarrow \max(mx, \; nums[i - 2])
        $$
      - If $mx > nums[i]$, a non-local inversion is proven! Return `false` immediately.
- **Step-by-Step Worked Execution Trace on $nums = [1, 0, 2]$:**
  - Length $n = 3$. Scan begins at index $i = 2$.
  - Initialize prefix maximum: $mx = 0$.
  - **Index $i = 2$ ($nums[2] = 2$):**
    - Eligible previous element at distance $\ge 2$:
      $$
      nums[i - 2] = nums[2 - 2] = nums[0] = \mathbf{1}
      $$
    - Update running prefix maximum:
      $$
      mx \leftarrow \max(0, 1) = \mathbf{1}
      $$
    - Compare with current element:
      $$
      mx > nums[2] \iff 1 > 2 \quad \mathbf{(False)}
      $$
      No inversion with index 2.
  - **Loop Terminates:**
    - No non-local inversions detected throughout the entire array.
    - Result:
      $$
      ans = \mathbf{true}
      $$
- **Non-Local Inversion Violation Trace ($nums = [1, 2, 0]$):**
  - Length $n = 3$. Scan at index $i = 2$ ($nums[2] = 0$).
  - Eligible distance $\ge 2$ element: $nums[0] = 1$.
  - Update prefix maximum: $mx \leftarrow \max(0, 1) = 1$.
  - Compare:
    $$
    mx > nums[2] \iff 1 > 0 \quad \mathbf{(Violation\ Found!)}
    $$
  - Pair $(0, 2)$ has $nums[0] = 1 > nums[2] = 0$ with distance $2 - 0 = 2 \ge 2$.
  - This is a non-local global inversion!
  - Global inversions (2: pairs $(0, 2)$ and $(1, 2)$) strictly exceed local inversions (1: pair $(1, 2)$).
  - Returns **`false`**.
- **The Absolute Displacement Alternative ($|nums[i] - i| \le 1$):**
  - In any valid permutation where every inversion is local (adjacent swaps only), each number can move at most 1 position away from its original index:
    $$
    \forall i: \quad |nums[i] - i| \le 1
    $$
  - In $nums = [1, 2, 0]$: value $0$ is at index 2 $\implies |0 - 2| = 2 > 1 \implies$ immediate failure!

This instance demonstrates inversion poset reduction and separation gap testing on finite permutations, mathematically proves why identity between Coxeter length and adjacent transposition count forces maximal displacement $\le 1$, and derives $O(N)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a permutation $nums$ of $[0, n - 1]$:
Determine if the number of **global inversions** equals the number of **local inversions**.

```text
nums = [ 1, 0, 2 ]

Local inversions: (nums[i] > nums[i+1])
  nums[0] > nums[1] (1 > 0) -> 1 local inversion

Global inversions: (i < j and nums[i] > nums[j])
  nums[0] > nums[1] (1 > 0) -> 1 global inversion

Both counts equal 1!
Result: true
```

### The Invariant of the Non-Local Inversion
- Every local inversion is already a global inversion.
- The counts are equal if and only if **there are NO non-local inversions** ($nums[i] > nums[j]$ with $j \ge i + 2$).
- Maintaining the maximum of elements at distance $\ge 2$ checks for violations in a single $O(N)$ pass.

---

## 2. Conceptual Foundation & Invariants

### 1. Inversion Inclusion:
$$
\text{Local} = \{(i, i + 1) \mid nums[i] > nums[i + 1]\} \subseteq \text{Global}
$$
$$
|\text{Global}| = |\text{Local}| \iff \forall j \ge i + 2: \; nums[i] \le nums[j]
$$

### 2. Prefix Maximum at Distance 2:
$$
mx \leftarrow \max(mx, \; nums[i - 2])
$$
$$
\text{if } mx > nums[i] \implies \text{return false}
$$

> **Coxeter Group Length Invariant.** On the symmetric group $S_n$, the total inversion count equals the Coxeter length $\ell(w)$, which equals the descent count $\text{Des}(w)$ if and only if $w$ is a product of disjoint adjacent transpositions $s_i = (i, i+1)$, equivalent to $|w(i) - i| \le 1$ for all $i$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 0, 2]$:

---

### Step 1: Scan $i = 2$
- $nums[i - 2] = nums[0] = 1$.
- $mx \leftarrow \max(0, 1) = 1$.
- Compare: $mx \le nums[2] \iff 1 \le 2$ (Valid).

---

### Step 2: Output
$$
\mathbf{true}
$$

---

## 4. Complete Execution Trace

| Index $i$ | Current Element $nums[i]$ | Distant Element $nums[i-2]$ | Running Maximum $mx$ | Violation $mx > nums[i]$? | Result |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $2$ | $2$ | $nums[0] = 1$ | $1$ | No ($1 \le 2$) | Proceed |
| **Final** | — | — | — | — | **`true`** |

---

## 5. Boundary Cases & Failure Modes

- **Non-Local Inversion ($[1, 2, 0]$):** At $i = 2$, $mx = 1 > nums[2] = 0 \implies$ returns `false`.
- **Already Sorted ($[0, 1, 2, 3]$):** $0$ global and $0$ local $\implies$ returns `true`.
- **Length 1 or 2 ($[1, 0]$):** Loop for $i \ge 2$ does not run $\implies$ trivially `true`.
- **Reverse Sorted ($[2, 1, 0]$):** At $i = 2$, $nums[0] = 2 > nums[2] = 0 \implies$ returns `false`.

---

## 6. Traps & Common Anti-Patterns

- **Counting All Global Inversions ($O(N \log N)$ or $O(N^2)$):** Using Merge Sort or a Fenwick Tree to count all global inversions is unnecessary and wastes time. You only need to check if any non-local inversion exists.
- **Checking Only Adjacent Elements:** Local inversions only check adjacent elements. The check must compare $nums[i]$ against elements at distance $\ge 2$ ($nums[i-2], nums[i-3], \dots$).
- **Scanning Backwards from Every Index ($O(N^2)$):** Comparing each element to all earlier elements takes $O(N^2)$. Storing a single cumulative variable $mx = \max(mx, nums[i-2])$ makes the check $O(1)$ per index.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Single pass from index 2 to $N - 1$: $\mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 10^5$. Completes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (single scalar variable $mx$).
