# Guided Example: Repeated String Match

We trace the step-by-step length ceiling lower bound computation ($k_{min} = \lceil |b| / |a| \rceil$), prefix-boundary and suffix-boundary spillover analysis ($k \le k_{min} + 2$), repeated string concatenation testing ($b \in a \times k$), early match identification, and periodicity failure detection ($-1$) on representative string instances:

- **Input:** $a = \text{"abcd"}, \quad b = \text{"cdabcdab"}$
- **Required output:** `3`
  - Problem objective:
    - Determine the **minimum number of repetitions** of string $a$ needed such that string $b$ appears as a contiguous substring within $a \times k$.
    - If no finite repetition of $a$ can ever contain $b$, return $-1$.
    - For $a = \text{"abcd"}$ and $b = \text{"cdabcdab"}$:
      - Repetition $k = 1$: `"abcd"` (length 4, too short).
      - Repetition $k = 2$: `"abcdabcd"` (length 8, does not contain $b$).
      - Repetition $k = 3$: `"abcdabcdabcd"`:
        - Contains `"cdabcdab"` starting at index 2 (`ab [cd abcd ab] cd`).
      - Minimum repetitions required is **3**.
- **Length Lower Bound & Boundary Spillover Invariant:**
  - **The Length Lower Bound ($k_{min}$):**
    - For $b$ to fit inside a repeated string of $a$, the total character length of the repeated string must be at least the length of $b$:
      $$
      k \cdot |a| \ge |b| \implies k \ge \left\lceil \frac{|b|}{|a|} \right\rceil
      $$
    - Let $k_{min} = \lceil |b| / |a| \rceil$. No repetition count strictly less than $k_{min}$ can ever contain $b$.
  - **The At-Most-Two Spillover Invariant:**
    - A match for $b$ does not necessarily align with the start of a copy of $a$.
    - In the worst case:
      - The match begins on the **very last character** of the first copy of $a$ (offset $|a| - 1$).
      - The body of $b$ spans across intermediate complete copies of $a$.
      - The tail of $b$ finishes inside a final trailing copy of $a$.
    - This offset can shift the required string across at most **2 extra boundary transitions**:
      $$
      k \in \left\{ k_{min}, \; k_{min} + 1, \; k_{min} + 2 \right\}
      $$
    - If $b$ is not a substring of $a \times (k_{min} + 2)$, it is mathematically impossible for $b$ to be a substring of $a \times k$ for any $k > k_{min} + 2$.
    - Thus, checking at most 3 integer values of $k$ exhaustively resolves the problem.
- **Step-by-Step Worked Execution Trace on $a = \text{"abcd"}, b = \text{"cdabcdab"}$:**
  - String lengths:
    $$
    m = |a| = 4, \quad n = |b| = 8
    $$
  - **Step 1: Compute Initial Repetition Count:**
    $$
    k = \left\lceil \frac{n}{m} \right\rceil = \left\lceil \frac{8}{4} \right\rceil = \mathbf{2}
    $$
  - **Step 2: Test $k = 2$:**
    - Form repeated string:
      $$
      t_2 = a \times 2 = \text{"abcdabcd"} \quad (\text{length } 8)
      $$
    - Search for $b = \text{"cdabcdab"}$ in $t_2$:
      - $t_2$ starts with `"ab"`, whereas $b$ starts with `"cd"`.
      - Does $b$ appear in $t_2$? No ($\text{"cdabcdab"} \notin \text{"abcdabcd"}$).
    - Advance repetition count:
      $$
      k \leftarrow 2 + 1 = \mathbf{3}
      $$
  - **Step 3: Test $k = 3$:**
    - Form repeated string:
      $$
      t_3 = a \times 3 = \text{"abcdabcdabcd"} \quad (\text{length } 12)
      $$
    - Search for $b = \text{"cdabcdab"}$ in $t_3$:
      - Index 0: `"abcdabcd"` $\ne b$
      - Index 1: `"bcdabcda"` $\ne b$
      - Index 2: `"cdabcdab"` $\mathbf{== b!}$
    - Contiguous match found at slice $t_3[2 \dots 9]$:
      ```text
      t_3:    a  b [ c  d  a  b  c  d  a  b ] c  d
      b:           c  d  a  b  c  d  a  b
      ```
    - Substring match confirmed!
    - Return current repetition count:
      $$
      ans = \mathbf{3}
      $$
- **Absent Character Immediate Rejection ($a = \text{"a"}, b = \text{"b"}$):**
  - Character `'b'` does not even exist in $a$.
  - $k_{min} = 1$. Tests $k = 1, 2, 3$, none contain `'b'`.
  - Loop terminates and returns **`-1`**.
- **Internal Match Without Spillover ($a = \text{"abcd"}, b = \text{"bc"}$):**
  - $m = 4, n = 2 \implies k_{min} = \lceil 2 / 4 \rceil = 1$.
  - Test $k = 1$: `"bc"` is in `"abcd"`!
  - Returns **`1`** immediately on the first check.

This instance demonstrates periodic string pattern matching and boundary offset dilation analysis, mathematically proves why fractional quotient bounds plus two boundary segments exhaust all alignment offsets, and derives $O(M + N)$ KMP / Robin-Karp runtime and $O(M + N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two strings $a$ and $b$:
Find the **minimum repetitions of $a$** such that $b$ is a substring of the repeated string.
If impossible, return $-1$.

```text
a = "abcd", b = "cdabcdab"

Length of a = 4, Length of b = 8
Minimum copies needed for length: ceil(8 / 4) = 2

Test copies:
  k = 2: "abcdabcd"         -> "cdabcdab" NOT found
  k = 3: "abcdabcdabcd"     -> "cdabcdab" FOUND at index 2!
          ..[cdabcdab]..

Result: 3
```

### The Invariant of the 3-Step Search Window
- The minimum copies for length is $k_{min} = \lceil |b| / |a| \rceil$.
- Because $b$ can start anywhere inside the first copy of $a$ and end anywhere inside the last copy of $a$, it can span at most:
  $$
  k \in \{ k_{min}, \; k_{min} + 1, \; k_{min} + 2 \}
  $$
- If $b$ is not found in $k_{min} + 2$ copies, it will NEVER appear in any number of copies.

---

## 2. Conceptual Foundation & Invariants

### 1. The Search Range Ceiling:
$$
k_{min} = \left\lceil \frac{|b|}{|a|} \right\rceil
$$
$$
k \in [k_{min}, \; k_{min} + 2]
$$

### 2. Decision Rule:
For $k = k_{min}, k_{min} + 1, k_{min} + 2$:
$$
\text{If } b \subseteq a^k \implies \text{return } k
$$
If loop completes without finding $b$:
$$
\text{return } -1
$$

> **Periodic Factor Covering Invariant.** Any contiguous factor $w$ of an infinite periodic word $u^\infty$ has length $|w|$, begins at phase offset $\phi \in [0, |u|-1]$, and is entirely contained within the prefix of length $(\lceil |w|/|u| \rceil + 1)|u|$.

---

## 3. Step-by-Step Worked Execution

We trace $a = \text{"abcd"}, b = \text{"cdabcdab"}$:

---

### Step 1: Compute $k_{min}$
- $m = 4, n = 8$.
- $k_{min} = \lceil 8 / 4 \rceil = 2$.

---

### Step 2: Test $k = 2$
- $t = \text{"abcdabcd"}$.
- $b \notin t$.

---

### Step 3: Test $k = 3$
- $t = \text{"abcdabcdabcd"}$.
- $b \in t$ at index 2.
- Match! Return **`3`**.

---

## 4. Complete Execution Trace

| Repetition $k$ | Repeated String $t = a^k$ | Length of $t$ | Target $b$ Present? | Offset in $t$ | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $2$ ($k_{min}$) | `"abcdabcd"` | $8$ | No | — | Increment to $k = 3$ |
| **$3$ ($k_{min} + 1$)** | **`"abcdabcdabcd"`** | **$12$** | **Yes** | **Index 2** | **Return `3`** |
| $4$ ($k_{min} + 2$) | Unreached | — | — | — | — |

---

## 5. Boundary Cases & Failure Modes

- **$b$ Shorter than $a$ ($a = \text{"abc"}, b = \text{"b"}$):** $k_{min} = 1$, found immediately in 1 copy.
- **$a == b$:** $k_{min} = 1$, found in 1 copy.
- **Impossible Match ($a = \text{"abc"}, b = \text{"d"}$):** Checks $k \in \{1, 2, 3\}$, none contain `'d'` $\implies -1$.
- **Spillover Requiring $+2$ Copies ($a = \text{"abcd"}, b = \text{"dabcdab"}$):** Starts at end of $a$ and ends at start of $a$, requiring $k_{min} + 1$ or $+2$.

---

## 6. Traps & Common Anti-Patterns

- **Unbounded While Loop:** Using `while b not in t: t += a` without a strict upper bound results in an infinite loop (Time Limit Exceeded) whenever $b$ is impossible.
- **Checking Only $k_{min}$:** Forgetting that alignment offsets can require an extra copy leads to false negatives on inputs like `"abcd"` and `"cdabcdab"`.
- **String Multiplications in Loop:** Pre-allocating list tokens `t = [a] * k` and appending incrementally avoids quadratic string allocation overhead.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - String search on text of length at most $(k_{min} + 2) \cdot M \le 2M + N$.
  - Using KMP or Python's Boyer-Moore-Horspool search (`in`), each check takes $\mathcal{O}(M + N)$.
  - At most 3 checks are performed.
  - Total Time: $\mathcal{O}(M + N)$. Completes in $< 1$ ms for $M, N = 10^4$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M + N)$ space to hold the repeated string of length $\le 2M + N$.
