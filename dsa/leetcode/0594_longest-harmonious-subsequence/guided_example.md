# Guided Example: Longest Harmonious Subsequence

We trace the step-by-step element frequency histogram construction ($cnt = \text{Counter}(nums)$), adjacent predecessor-successor pairing ($(x, x + 1)$), non-zero difference enforcement ($\max - \min == 1$), joint frequency sum maximization ($cnt[x] + cnt[x + 1]$), and global longest harmonious length extraction on representative integer arrays:

- **Input:** $nums = [1, 3, 2, 2, 5, 2, 3, 7]$
- **Required output:** `5`
  - Harmonious array definition: An array where the difference between its maximum value and its minimum value is **strictly equal to 1**:
    $$
    \max(A) - \min(A) = 1
    $$
  - Subsequence property: Elements can be chosen in any arbitrary subset from $nums$ without altering their relative order.
  - Objective: Find the length of the longest such subsequence.
- **Adjacent Value Frequency Pair Principle:**
  - If a subsequence has $\max - \min = 1$, all its elements must belong to a set of the form:
    $$
    \{x, \; x + 1\}
    $$
  - Furthermore:
    1. The value $x$ must appear at least once ($cnt[x] \ge 1$).
    2. The value $x + 1$ must appear at least once ($cnt[x + 1] \ge 1$).
    3. No other values can be included.
  - Since order within a subsequence is unconstrained by value choice, the maximum possible length of a harmonious subsequence using values $\{x, x + 1\}$ is simply:
    $$
    \text{Length}(x) = cnt[x] + cnt[x + 1]
    $$
  - The problem therefore reduces to finding the pair $(x, x + 1)$ in the frequency map that maximizes $cnt[x] + cnt[x + 1]$!
- **Step-by-Step Worked Trace on $[1, 3, 2, 2, 5, 2, 3, 7]$:**
  - **Step 1: Construct Frequency Map:**
    - Scan $nums$ and count occurrences:
      - Value $1$: $1$ occurrence $\implies cnt[1] = 1$
      - Value $2$: $3$ occurrences (indices $2, 3, 5$) $\implies cnt[2] = 3$
      - Value $3$: $2$ occurrences (indices $1, 6$) $\implies cnt[3] = 2$
      - Value $5$: $1$ occurrence $\implies cnt[5] = 1$
      - Value $7$: $1$ occurrence $\implies cnt[7] = 1$
    - Histogram:
      $$
      cnt = \{1: 1, \; 2: 3, \; 3: 2, \; 5: 1, \; 7: 1\}
      $$
  - **Step 2: Evaluate All Consecutive Pairs $(x, x + 1)$:**
    - **Pair $x = 1$:**
      - Does successor $x + 1 = 2$ exist in $cnt$?
      - Yes! $cnt[2] = 3$.
      - Combined length:
        $$
        cnt[1] + cnt[2] = 1 + 3 = \mathbf{4}
        $$
    - **Pair $x = 2$:**
      - Does successor $x + 1 = 3$ exist in $cnt$?
      - Yes! $cnt[3] = 2$.
      - Combined length:
        $$
        cnt[2] + cnt[3] = 3 + 2 = \mathbf{5}
        $$
    - **Pair $x = 3$:**
      - Does successor $x + 1 = 4$ exist in $cnt$?
      - No! $cnt[4] = 0$.
      - Cannot form a harmonious subsequence with $3$ as the minimum.
    - **Pair $x = 5$:**
      - Does successor $x + 1 = 6$ exist in $cnt$?
      - No! $cnt[6] = 0$.
    - **Pair $x = 7$:**
      - Does successor $x + 1 = 8$ exist in $cnt$?
      - No! $cnt[8] = 0$.
  - **Step 3: Extract Maximum Length:**
    $$
    ans = \max(4, 5) = \mathbf{5}
    $$
    - The optimal subsequence is formed by taking all three $2$s and both $3$s:
      $$
      [3, 2, 2, 2, 3] \quad (\text{Length } 5, \; \min = 2, \; \max = 3, \; 3 - 2 = 1)
      $$
- **All Identical Elements Instance ($nums = [1, 1, 1, 1]$):**
  - Frequency map: $\{1: 4\}$.
  - $x + 1 = 2$ does not exist $\implies$ No valid pair $\implies \max - \min = 0 \ne 1$.
  - Return default: **`0`**.
- **Dense Consecutive Run ($nums = [1, 2, 3, 4]$):**
  - Pairs evaluated:
    - $(1, 2) \implies 1 + 1 = 2$
    - $(2, 3) \implies 1 + 1 = 2$
    - $(3, 4) \implies 1 + 1 = 2$
  - Maximum length: **`2`**.

This instance demonstrates multiset frequency projection for difference-constrained subgraphs, mathematically proves why contiguous range constraints reduce subsequence search to hash map neighbor probing, and derives $O(N)$ runtime and $O(U)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums$:
A **harmonious array** has $\max - \min == 1$ exactly.
Find the **maximum length** of a harmonious subsequence.
If no harmonious subsequence exists, return `0`.

```text
nums: [ 1,  3,  2,  2,  5,  2,  3,  7 ]

Frequencies:
  1: 1
  2: 3   <-- Pair (2, 3) has count 3 + 2 = 5!
  3: 2
  5: 1
  7: 1

Subsequence: [3, 2, 2, 2, 3]
Min = 2, Max = 3 (Difference = 1)
Length = 5
```

### Why Sorting is Unnecessary
- Subsequences can be formed from any subset of elements.
- Because a harmonious subsequence contains only elements with values $x$ and $x + 1$, the length depends strictly on **how many times $x$ and $x + 1$ appear in the entire array**.
- Counting frequencies with a hash map allows looking up $cnt[x + 1]$ in $O(1)$ time for each distinct $x$.

---

## 2. Conceptual Foundation & Invariants

### 1. Invariant of Support:
For any chosen minimum value $x$, a harmonious subsequence exists if and only if:
$$
cnt[x] > 0 \quad \text{and} \quad cnt[x + 1] > 0
$$

### 2. Objective Function:
$$
\text{Ans} = \max_{x \in cnt: cnt[x+1] > 0} (cnt[x] + cnt[x+1])
$$
Defaulting to $0$ if no such $x$ exists.

> **Exact Range Invariant.** Requiring $cnt[x+1] > 0$ strictly enforces $\max - \min = 1$, preventing mono-valued arrays with $\max - \min = 0$ from falsely qualifying.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Count Frequencies
- $cnt[1] = 1$
- $cnt[2] = 3$
- $cnt[3] = 2$
- $cnt[5] = 1$
- $cnt[7] = 1$

---

### Step 2: Probe $x + 1$ for Each Unique Key
- $x = 1$: $cnt[2] = 3 > 0 \implies 1 + 3 = \mathbf{4}$.
- $x = 2$: $cnt[3] = 2 > 0 \implies 3 + 2 = \mathbf{5}$.
- $x = 3$: $cnt[4] = 0 \implies$ skip.
- $x = 5$: $cnt[6] = 0 \implies$ skip.
- $x = 7$: $cnt[8] = 0 \implies$ skip.

---

### Step 3: Maximum Value
$$
\max(4, 5) = \mathbf{5}
$$

---

## 4. Complete Execution Trace

| Key $x$ | Frequency $cnt[x]$ | Key $x+1$ Present? | Frequency $cnt[x+1]$ | Sum $cnt[x] + cnt[x+1]$ | Global Max $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $1$ | Yes ($2$) | $3$ | $1 + 3 = 4$ | $4$ |
| **$2$** | **$3$** | **Yes ($3$)** | **$2$** | **$3 + 2 = 5$** | **`5`** |
| $3$ | $2$ | No ($4$) | $0$ | — | $5$ |
| $5$ | $1$ | No ($6$) | $0$ | — | $5$ |
| $7$ | $1$ | No ($8$) | $0$ | — | $5$ |
| **Final** | — | — | — | — | **`5`** |

---

## 5. Boundary Cases & Failure Modes

- **All Elements Equal ($[2, 2, 2]$):** Difference is 0, not 1 $\implies$ returns $0$.
- **No Adjacent Pairs ($[1, 3, 5, 7]$):** All differences $\ge 2 \implies$ returns $0$.
- **Two Adjacent Numbers Repeated ($[1, 2, 1, 2]$):** $cnt[1] + cnt[2] = 2 + 2 = 4$.
- **Negative Numbers ($[-3, -2, -2, 0]$):** Handled identically: $-3$ and $-2$ yield $1 + 2 = 3$.

---

## 6. Traps & Common Anti-Patterns

- **Checking Contiguous Subarrays Instead of Subsequences:** This problem asks for *subsequences*, meaning elements do not need to be contiguous in the input array.
- **Allowing $\max - \min == 0$:** If all numbers are identical (e.g. $[1, 1, 1]$), the difference is 0, which violates the strict harmonious condition ($\max - \min = 1$). Checking that $cnt[x+1] > 0$ prevents this.
- **Sorting with Two Pointers ($O(N \log N)$):** While sorting works, counting with a hash map runs in strictly linear $O(N)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Counting occurrences of $N$ elements takes $\mathcal{O}(N)$ average operations.
  - Iterating over $U$ distinct keys and probing $x + 1$ takes $\mathcal{O}(U)$ where $U \le N$.
  - Total Time: strictly linear $\mathcal{O}(N)$. For $N = 2 \times 10^4$, completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(U)$ space to store the frequency map.