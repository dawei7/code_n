# Guided Example: Count the Repetitions

We trace the step-by-step state machine transition mapping ($d[j] = (cnt, next\_j)$), Pigeonhole periodic cycle detection, fast-forward modular cycle leaping, and integer quotient block reduction ($m = \lfloor K / n_2 \rfloor$) on representative repeated string patterns:

- **Input:**
  - $s_1 = \text{"acb"}, \quad n_1 = 4$ (Source string: $str_1 = [\text{"acb"}, 4]$)
  - $s_2 = \text{"ab"}, \quad n_2 = 2$ (Target block: $str_2 = [\text{"ab"}, 2]$)
- **Required output:** `2`
  - We seek the maximum $m$ such that $[str_2, m] = [s_2, m \times n_2]$ is a subsequence of $[s_1, n_1]$.
  - Step 1: Precompute deterministic state transitions for each index in $s_2$:
    - Length of $s_2$: $|s_2| = 2$ (indices $0$ and $1$)
    - **From start index $j = 0$ in $s_2$:**
      - Scan one full copy of $s_1 = \text{"acb"}$:
        - Read `'a'`: matches $s_2[0] = \text{'a'} \implies j \leftarrow 1$
        - Read `'c'`: does not match $s_2[1] = \text{'b'} \implies$ skip
        - Read `'b'`: matches $s_2[1] = \text{'b'} \implies j \leftarrow 2 == |s_2|$
        - Full copy of $s_2$ completed! $cnt \leftarrow 1, \; j \leftarrow 0$
      - Transition from $0$: emits $cnt = 1$, next index $j = 0$.
      - Mapping: $d[0] = (1, 0)$
    - **From start index $j = 1$ in $s_2$:**
      - Scan $s_1 = \text{"acb"}$:
        - Read `'a'`: does not match $s_2[1]$
        - Read `'c'`: does not match $s_2[1]$
        - Read `'b'`: matches $s_2[1] \implies cnt \leftarrow 1, \; j \leftarrow 0$
      - Mapping: $d[1] = (1, 0)$
  - Step 2: Simulate $n_1 = 4$ blocks of $s_1$:
    - Start at $j = 0, \; ans = 0$
    - Block 1: $d[0] \implies ans \leftarrow 0 + 1 = 1, \; j \leftarrow 0$
    - Block 2: $d[0] \implies ans \leftarrow 1 + 1 = 2, \; j \leftarrow 0$
    - Block 3: $d[0] \implies ans \leftarrow 2 + 1 = 3, \; j \leftarrow 0$
    - Block 4: $d[0] \implies ans \leftarrow 3 + 1 = 4, \; j \leftarrow 0$
    - Total completed copies of $s_2$: $K = 4$.
  - Step 3: Compute maximum repetitions $m$:
    $$
    m = \lfloor K / n_2 \rfloor = \lfloor 4 / 2 \rfloor = \mathbf{2}
    $$
- **Identical Strings Instance:** $s_1 = \text{"acb"}, n_1 = 1, s_2 = \text{"acb"}, n_2 = 1 \implies K = 1 \implies \lfloor 1 / 1 \rfloor = \mathbf{1}$
- **Missing Character Instance:** $s_1 = \text{"ab"}, s_2 = \text{"d"} \implies$ Character `'d'` never appears $\implies K = 0 \implies \mathbf{0}$

This instance demonstrates deterministic finite automaton (DFA) state compression on periodic strings, mathematically proves how the Pigeonhole Principle guarantees cycle detection in at most $|s_2|$ steps, and derives $O(|s_1| \times |s_2| + |s_2|)$ runtime and $O(|s_2|)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two strings $s_1 = \text{"acb"}$ and $s_2 = \text{"ab"}$ with repetition counts $n_1 = 4$ and $n_2 = 2$:
Let $str_1 = [s_1, n_1]$ and $str_2 = [s_2, n_2]$.
Find the maximum integer $m$ such that $[str_2, m]$ can be formed as a subsequence of $str_1$.

```text
Source String: str1 = "acb acb acb acb" (s1 repeated 4 times)
Target Unit:   s2   = "ab"
Target Block:  str2 = "abab" (s2 repeated n2 = 2 times)

Subsequence Matching:
  "acb acb acb acb"
   a b a b a b a b  -> Exactly 4 copies of s2 ("ab") matched!

How many copies of str2 ("abab" = 2 copies of s2) fit in 4 copies?
  m = 4 // 2 = 2
```

### The Subsequence Counting Reduction
Notice that:
$$
[str_2, m] = [[s_2, n_2], m] = [s_2, m \times n_2]
$$
This means that $[str_2, m]$ is simply $s_2$ repeated $m \times n_2$ times.
Therefore, the problem reduces to:
1. Find the total number of times $K$ that $s_2$ can be matched as a subsequence inside $[s_1, n_1]$.
2. The maximum $m$ is then simply the integer division:
   $$
   m = \lfloor K / n_2 \rfloor
   $$

---

## 2. Conceptual Foundation & Invariants

### 1. The DFA State Transition Operator:
Because $s_1$ repeats identically $n_1$ times, its effect on matching $s_2$ is completely determined by the **current index $j \in [0, |s_2| - 1]$** at the beginning of the $s_1$ block.
We define a transition map $d$:
$$
d[j] = (cnt, \; next\_j)
$$
Where:
- $cnt$ is the number of times $s_2$ is completed during one pass through $s_1$.
- $next\_j$ is the index in $s_2$ waiting to be matched at the end of the pass.
Computing $d[j]$ for all $j \in [0, |s_2| - 1]$ takes $O(|s_1| \times |s_2|)$ time.

### 2. Periodicity & The Pigeonhole Principle:
Since there are only $|s_2|$ distinct states ($j \in [0, |s_2| - 1]$):
- As we iterate through copies of $s_1$, the state $j$ must repeat within at most $|s_2| + 1$ iterations.
- A repeated state $j_{t_1} == j_{t_2}$ marks the detection of a **cycle**:
  - The cycle length in $s_1$ blocks is $\Delta t = t_2 - t_1$.
  - The number of $s_2$ copies produced per cycle is $\Delta cnt = cnt_{t_2} - cnt_{t_1}$.
- For massive $n_1$ (e.g. $10^6$), we can fast-forward by calculating how many full cycles fit into the remaining iterations using division and modulo.

> **State Invariant.** For any index $j \in [0, |s_2|-1]$, scanning $s_1$ deterministically advances the matching cursor by a fixed number of completed $s_2$ words and terminates at a uniquely determined residual index $next\_j$.

---

## 3. Step-by-Step Worked Execution

We trace $s_1 = \text{"acb"}, n_1 = 4$ and $s_2 = \text{"ab"}, n_2 = 2$:

---

### Step 1: Compute Transitions $d[j]$ for $s_2 = \text{"ab"}$ ($|s_2| = 2$)

- **For $j = 0$ (Expecting `'a'`):**
  - Read $s_1[0] = \text{'a'}$: matches $s_2[0] \implies j \leftarrow 1$.
  - Read $s_1[1] = \text{'c'}$: no match.
  - Read $s_1[2] = \text{'b'}$: matches $s_2[1] \implies j \leftarrow 2 == |s_2|$.
    - Completed 1 copy of $s_2$! $cnt = 1, \; j \leftarrow 0$.
  - Result: $d[0] = (1, 0)$.

- **For $j = 1$ (Expecting `'b'`):**
  - Read $s_1[0] = \text{'a'}$: no match.
  - Read $s_1[1] = \text{'c'}$: no match.
  - Read $s_1[2] = \text{'b'}$: matches $s_2[1] \implies j \leftarrow 2 == |s_2|$.
    - Completed 1 copy of $s_2$! $cnt = 1, \; j \leftarrow 0$.
  - Result: $d[1] = (1, 0)$.

---

### Step 2: Iterate Across $n_1 = 4$ Blocks
Initialize $j = 0, \; ans = 0$:
- **Block 1:** Lookup $d[0] \implies cnt = 1, \; j = 0$.
  - $ans \leftarrow 0 + 1 = \mathbf{1}$.
- **Block 2:** Lookup $d[0] \implies cnt = 1, \; j = 0$.
  - $ans \leftarrow 1 + 1 = \mathbf{2}$.
- **Block 3:** Lookup $d[0] \implies cnt = 1, \; j = 0$.
  - $ans \leftarrow 2 + 1 = \mathbf{3}$.
- **Block 4:** Lookup $d[0] \implies cnt = 1, \; j = 0$.
  - $ans \leftarrow 3 + 1 = \mathbf{4}$.

Total completed $s_2$ units: $K = 4$.

---

### Step 3: Compute Final $m$
Divide by $n_2 = 2$:
$$
m = \lfloor K / n_2 \rfloor = \lfloor 4 / 2 \rfloor = \mathbf{2}
$$

---

## 4. Complete Execution Trace

| Block # | Start State $j$ | Block Scanned | Characters Matched | $s_2$ Copies Added | New Total $s_2$ | Next State $j$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | $0$ | `"acb"` | `'a'`, `'b'` | $+1$ | $1$ | $0$ |
| **2** | $0$ | `"acb"` | `'a'`, `'b'` | $+1$ | $2$ | $0$ |
| **3** | $0$ | `"acb"` | `'a'`, `'b'` | $+1$ | $3$ | $0$ |
| **4** | $0$ | `"acb"` | `'a'`, `'b'` | $+1$ | **$4$** | $0$ |
| **Final** | — | — | — | — | **$m = 4 // 2$** | **Result: $2$** |

---

## 5. Boundary Cases & Failure Modes

- **Impossible Matching ($s_2$ has character absent from $s_1$):** Transitions always yield $cnt = 0$, progress stalls $\implies K = 0 \implies m = \mathbf{0}$.
- **Large Repetition ($n_1 = 10^7$):** The loop detects a cycle within at most $|s_2| \le 100$ iterations. Cycle fast-forwarding divides remaining iterations by period length, completing in $O(|s_2|)$ steps.
- **Single Character Match ($s_1 = \text{"a"}, n_1 = 5, s_2 = \text{"a"}, n_2 = 1$):** Each $s_1$ block matches 1 character $\implies K = 5 \implies m = \mathbf{5}$.
- **Target Long Relative to Source:** If $s_2$ requires 10 blocks of $s_1$ to complete once, $cnt$ remains 0 for 9 blocks, then emits 1 on block 10.

---

## 6. Traps & Common Anti-Patterns

- **Materializing Full Strings ($O(N_1 \cdot |s_1|)$):** Constructing $s_1 \times n_1$ into a single string consumes gigabytes of memory and causes Out-Of-Memory crashes for $n_1 = 10^6$. The state machine approach only allocates $|s_2|$ integers.
- **Incorrect Cycle Remainder Accounting:** When skipping cycles, forgetting to simulate the remaining $n_1 \pmod{\text{period}}$ iterations loses tail matches.
- **Modulo Handling on Partial Matches:** Transition state must record the exact matching index in $s_2$, not just completed count, to preserve continuity across block boundaries.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Computing the transition table $d$ takes $|s_2|$ iterations of scanning $s_1$: $O(|s_1| \times |s_2|)$.
  - Simulating $n_1$ blocks with cycle detection takes at most $O(|s_2|)$ steps.
  - Total Time: $\mathcal{O}(|s_1| \times |s_2| + |s_2|)$. For $|s_1|, |s_2| \le 100$, takes $< 10^4$ operations, completing in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(|s_2|)$ space to store the transition map of size $|s_2| \le 100$.
