# Guided Example: Maximum Swap

We trace the step-by-step decimal digit array representation ($s = \text{list}(\text{str}(num))$), suffix maximum index precomputation ($d[i] = \arg\max_{j \ge i} s[j]$), rightmost tie-breaking preservation ($s[i] \le s[d[i+1]] \implies d[i] = d[i+1]$), leftmost strictly improvable position scan ($s[i] < s[d[i]]$), single greedy transposition execution, and maximized numerical value synthesis on representative integer inputs:

- **Input:** $num = 2736$
- **Required output:** `7236`
  - Problem objective:
    - You are permitted to swap any two digits of $num$ **at most once**.
    - Maximize the resulting integer value.
- **Positional Place-Value & Rightmost Suffix Maximum Invariant:**
  - **The Greedy Place-Value Principle:**
    - A number's magnitude is overwhelmingly dominated by its highest place values (the leftmost digits).
    - To maximize the number with a single swap:
      - We want to increase the digit at the **earliest possible index** $i$ (furthest left).
      - We want to replace it with the **largest possible digit** appearing anywhere to its right.
  - **The Rightmost Tie-Breaker Rule:**
    - If the largest digit in the suffix appears multiple times (e.g. in $98368$, digit `'8'` appears at index 1 and index 4):
      - We must swap with the **rightmost** occurrence (index 4)!
      - Swapping with the rightmost occurrence leaves the earlier duplicate in its higher place value, maximizing the final value (e.g. $98863 > 98368$).
  - **Suffix Array Precomputation ($d[i]$):**
    - Let $d[i]$ record the index of the maximum digit in suffix $s[i \dots n - 1]$.
    - Iterate backwards from $n - 2$ down to $0$:
      $$
      d[i] = \begin{cases} d[i + 1] & \text{if } s[i] \le s[d[i + 1]] \\ i & \text{otherwise} \end{cases}
      $$
    - The non-strict inequality ($\le$) naturally pulls the rightmost index forward in case of duplicate maximum values.
  - **Single Swap Execution:**
    - Scan $i = 0 \dots n - 1$:
      - If $s[i] < s[d[i]]$:
        - Swap $s[i]$ with $s[d[i]]$.
        - Halt immediately (only one swap allowed).
- **Step-by-Step Worked Execution Trace on $num = 2736$:**
  - Digit array: $s = [\text{'2'}, \; \text{'7'}, \; \text{'3'}, \; \text{'6'}]$, length $n = 4$.
  - Initialize suffix index array:
    $$
    d = [0, \; 1, \; 2, \; 3]
    $$
  - **Step 1: Compute Suffix Maximum Indices Backwards:**
    - Base at $i = 3$:
      $$
      d[3] = 3 \quad (s[3] = \text{'6'})
      $$
    - At $i = 2$ ($s[2] = \text{'3'}$):
      - Compare $s[2] = \text{'3'}$ with $s[d[3]] = \text{'6'}$:
        $$
        \text{'3'} \le \text{'6'} \implies d[2] = d[3] = \mathbf{3}
        $$
      - (In suffix $s[2 \dots 3] = \text{"36"}$, the largest digit is at index 3).
    - At $i = 1$ ($s[1] = \text{'7'}$):
      - Compare $s[1] = \text{'7'}$ with $s[d[2]] = \text{'6'}$:
        $$
        \text{'7'} > \text{'6'} \implies d[1] = \mathbf{1}
        $$
      - (In suffix $s[1 \dots 3] = \text{"736"}$, the largest digit is at index 1).
    - At $i = 0$ ($s[0] = \text{'2'}$):
      - Compare $s[0] = \text{'2'}$ with $s[d[1]] = \text{'7'}$:
        $$
        \text{'2'} \le \text{'7'} \implies d[0] = d[1] = \mathbf{1}
        $$
      - (In full number, the largest digit is at index 1).
    - Suffix pointer array:
      $$
      d = [1, \; 1, \; 3, \; 3]
      $$
  - **Step 2: Forward Scan for First Opportunity to Increase Value:**
    - **Test Index $i = 0$ ($s[0] = \text{'2'}$):**
      - Target maximum index: $j = d[0] = 1$.
      - Compare digits:
        $$
        s[0] = \text{'2'}, \quad s[1] = \text{'7'} \implies \mathbf{\text{'2'} < \text{'7'}}
        $$
      - An improvement is possible at the most significant digit!
      - Execute transposition between index $0$ and index $1$:
        $$
        \text{swap}(s[0], \; s[1])
        $$
      - Digit array transforms:
        $$
        s = [\mathbf{'7'}, \; \mathbf{'2'}, \; \text{'3'}, \; \text{'6'}]
        $$
      - Halt search immediately.
  - **Step 3: Reconstitute Integer:**
    $$
    ans = \text{int}(\text{"7236"}) = \mathbf{7236}
    $$
- **Rightmost Tie-Breaking Trace ($num = 98368$):**
  - Digits: `['9', '8', '3', '6', '8']`.
  - Suffix max indices:
    - At index 4: $d[4] = 4$ (`'8'`).
    - At index 3: $'6' \le '8' \implies d[3] = 4$.
    - At index 2: $'3' \le '8' \implies d[2] = 4$.
    - At index 1: $'8' \le '8' \implies d[1] = 4$ (Picks rightmost `'8'` at index 4!).
    - At index 0: $'9' > '8' \implies d[0] = 0$.
  - Scan:
    - $i = 0$: $s[0] == s[d[0]]$ (`'9' == '9'`) $\to$ skip.
    - $i = 1$: $s[1] == s[d[1]]$ (`'8' == '8'`) $\to$ skip.
    - $i = 2$: $s[2] = \text{'3'} < s[d[2]] = \text{'8'}$ $\to$ **SWAP!**
    - Swap index 2 and index 4:
      $$
      98\mathbf{3}6\mathbf{8} \to 98\mathbf{8}6\mathbf{3}
      $$
    - Result: `98863`.
- **Already Maximal Input ($num = 9973$):**
  - Digits are already in non-increasing order.
  - For all $i$: $s[i] == s[d[i]]$.
  - 0 swaps performed $\implies$ returns `9973` unchanged.

This instance demonstrates lexicographical greedy maximization and suffix argmax tracking, mathematically proves why rightmost extremum selection preserves higher-order positional digits, and derives $O(L)$ runtime and $O(L)$ auxiliary space bounds where $L \le 9$ is the digit length.

---

## 1. Instance & Teaching Goal

Given an integer $num$:
You can swap two digits **at most once**.
Find the **maximum number** achievable.

```text
num = 2736

Digits: [ 2, 7, 3, 6 ]

Precompute largest digit to the right:
  At index 0 (2): best digit to the right is 7 (index 1)
  At index 1 (7): best digit to the right is 6 (index 3)
  At index 2 (3): best digit to the right is 6 (index 3)
  At index 3 (6): 6

First index i where s[i] < best_right:
  i = 0: 2 < 7 -> SWAP index 0 and index 1!

Result: 7236
```

### The Invariant of the Rightmost Maximum Suffix
- To maximize the number, the first digit from the left that is smaller than some digit to its right must be swapped.
- To maximize the result, it must be swapped with the **largest** digit to its right.
- In case of ties for the largest digit, always choose the **rightmost** occurrence.

---

## 2. Conceptual Foundation & Invariants

### 1. Suffix Argmax Recurrence:
For $i = n - 2 \dots 0$:
$$
d[i] = \begin{cases} d[i + 1] & \text{if } s[i] \le s[d[i + 1]] \\ i & \text{otherwise} \end{cases}
$$

### 2. The First Improvable Position:
Find the smallest index $i$ such that:
$$
s[i] < s[d[i]]
$$
Swap $s[i]$ and $s[d[i]]$, then terminate.

> **Positional Valuation Dominance Invariant.** A single transposition $(i, j)$ with $i < j$ produces value change $\Delta = (s_j - s_i)(10^{n-1-i} - 10^{n-1-j})$, which is strictly maximized by minimizing index $i$, and secondarily maximizing digit value $s_j$ and index $j$.

---

## 3. Step-by-Step Worked Execution

We trace $num = 2736$:

---

### Step 1: Precompute Suffix Max Indices
- $d = [1, 1, 3, 3]$.

---

### Step 2: Check Index 0
- $s[0] = \text{'2'}$.
- $j = d[0] = 1$, $s[1] = \text{'7'}$.
- $s[0] < s[1]$ ('2' < '7') $\implies$ Swap!

---

### Step 3: Swap and Finish
- $s[0] \leftrightarrow s[1] \implies \text{"7236"}$.
- Return **`7236`**.

---

## 4. Complete Execution Trace

| Digit Position $i$ | Digit $s[i]$ | Suffix Max Index $d[i]$ | Suffix Max Digit $s[d[i]]$ | Condition $s[i] < s[d[i]]$? | Transposition Executed | Result String |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$0$** | **`'2'`** | **$1$** | **`'7'`** | **Yes (`'2' < '7'`)** | **`swap(0, 1)`** | **`"7236"`** |
| $1$ | `'7'` | $1$ | `'7'` | Skipped (Halted) | — | — |
| $2$ | `'3'` | $3$ | `'6'` | Skipped | — | — |
| $3$ | `'6'` | $3$ | `'6'` | Skipped | — | — |

---

## 5. Boundary Cases & Failure Modes

- **Already Sorted Descending ($num = 9876$):** 0 swaps performed $\implies$ returns $9876$.
- **Duplicate Leading Digits ($num = 9973$):** Leaves 9s intact, returns $9973$.
- **Single Digit ($num = 5$):** Returns $5$.
- **Trailing Maximum ($num = 199$):** Swaps 1 with the *second* 9 $\implies 991$.

---

## 6. Traps & Common Anti-Patterns

- **Picking the Leftmost Maximum on Ties:** If $num = 199$, swapping 1 with the first 9 gives $919$; swapping 1 with the *second* 9 gives $991$. The rightmost occurrence must always be chosen!
- **Swapping Equal Digits:** Swapping two identical digits wastes the single permitted swap without increasing value. Only swap when $s[i] < s[d[i]]$.
- **Brute Force All Pairs ($O(L^2)$):** While $O(L^2)$ works because $L \le 9$, the linear $O(L)$ suffix tracking algorithm is strictly optimal and teaches general positional monotonicity.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Converting integer to string of length $L$: $\mathcal{O}(L)$.
  - Backward pass to compute $d$: $\mathcal{O}(L)$.
  - Forward pass to find first swap: $\mathcal{O}(L)$.
  - Since $num \le 10^8$, $L \le 8$.
  - Total Time: $\mathcal{O}(L)$ operations, executing in $< 0.01$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(L)$ auxiliary space for the character array and suffix index array.
