# Guided Example: Shortest Subarray with Sum at Least K

We trace the step-by-step prefix sum construction, failure of naive sliding windows on non-monotonic sequences, double-ended queue monotonicity maintenance, front-end optimality popping, and back-end dominance elimination on representative integer arrays:

- **Input:**
  $$
  nums = [2, -1, 2], \quad k = 3
  $$
- **Required output:** `3`
  - Subarray sum definition:
    - A contiguous subarray $nums[j \dots i - 1]$ has sum $\sum_{m=j}^{i-1} nums[m]$.
    - We require $\sum_{m=j}^{i-1} nums[m] \ge k = 3$.
    - We seek the **minimum length** $i - j$ among all qualifying subarrays.
    - If no such subarray exists, return $-1$.
    - For $nums = [2, -1, 2]$:
      - Subarray $[2]$ (len 1): sum $2 < 3$.
      - Subarray $[2, -1]$ (len 2): sum $1 < 3$.
      - Subarray $[-1, 2]$ (len 2): sum $1 < 3$.
      - Subarray $[2, -1, 2]$ (len 3): sum $2 - 1 + 2 = 3 \ge 3$. Length is $3$.
      - Minimum length: **`3`**.
- **Prefix Sum & Monotonic Deque Invariants:**
  - **Prefix Sum Formulation:**
    - Let $s[0] = 0$, and $s[i] = \sum_{m=0}^{i-1} nums[m]$ for $i \in [1, N]$.
    - Any subarray sum is represented as a difference of two prefix sums:
      $$
      \sum_{m=j}^{i-1} nums[m] = s[i] - s[j] \ge k \iff s[j] \le s[i] - k
      $$
    - Our objective is to minimize $i - j$ subject to $s[i] - s[j] \ge k$ with $j < i$.
  - **Why Standard Two Pointers Fails:**
    - Because elements of $nums$ can be **negative**, prefix sums $s$ are **not non-decreasing**!
    - A negative element causes $s$ to dip, violating the monotonicity required by standard sliding windows.
  - **Front Pop Rule (Optimality Exhaustion):**
    - Suppose at index $i$, we find that $s[i] - s[q[0]] \ge k$.
    - The subarray starting at $q[0]$ and ending at $i$ has length $i - q[0]$.
    - Could index $q[0]$ ever yield a shorter subarray for any future index $i' > i$?
    - No! Any future index $i' > i$ would have length $i' - q[0] > i - q[0]$, which is strictly worse (longer).
    - Therefore, **$q[0]$ can be permanently evicted from the front**!
  - **Back Pop Rule (Strict Dominance Elimination):**
    - Before inserting index $i$ with prefix sum $s[i]$, look at the tail of the deque $q[-1]$.
    - If $s[q[-1]] \ge s[i]$:
      - Index $i$ has a smaller (or equal) prefix sum than $q[-1]$ ($s[i] \le s[q[-1]]$).
      - Index $i$ comes after $q[-1]$ ($i > q[-1]$).
      - For any future index $i'$, subtracting $s[i]$ yields a larger sum ($s[i'] - s[i] \ge s[i'] - s[q[-1]]$) AND a shorter length ($i' - i < i' - q[-1]$).
      - Thus, index $q[-1]$ is **strictly dominated by $i$ in every possible future scenario**.
      - Therefore, **$q[-1]$ can be permanently discarded from the back**!
    - This maintains the deque with strictly increasing prefix sums: $s[q_0] < s[q_1] < \dots < s[q_m]$.

---

## 1. Instance & Teaching Goal

Given $nums = [2, -1, 2]$ and $k = 3$, demonstrate how the monotonic deque processes negative dips and captures the global minimum subarray length.

```text
Array:        [ 2,  -1,   2 ]
Indices:        0    1    2
Prefix Sums: [0, 2,  1,   3]
Prefix Idx:   0  1   2    3

Trace:
i = 0 (s = 0): Deque: [0]
i = 1 (s = 2): 2 - 0 = 2 < 3. s[1] > s[0]. Deque: [0, 1]
i = 2 (s = 1): 1 - 0 = 1 < 3.
               s[1]=2 >= s[2]=1 -> Pop 1 from back! Deque: [0, 2]
i = 3 (s = 3): 3 - s[0] = 3 >= 3 -> Found length 3 - 0 = 3! Pop 0 from front.
               3 - s[2] = 3 - 1 = 2 < 3. Deque: [2, 3]

Minimum length = 3
```

The teaching goal is to justify both the front pop (no future index can do better with that start) and the back pop (the newer, smaller prefix sum strictly dominates the older, larger one).

---

## 2. Conceptual Foundation & Invariants

### 1. Dual Monotonicity Conditions:
For indices stored in deque $Q = [q_0, q_1, \dots, q_{m-1}]$:
$$
q_0 < q_1 < \dots < q_{m-1} \quad \text{and} \quad s[q_0] < s[q_1] < \dots < s[q_{m-1}]
$$

### 2. The Two Deque Invariant Operations:
- **Condition A (Solution Detection & Front Eviction):**
  $$
  \text{While } Q \ne \emptyset \land s[i] - s[Q.\text{front}()] \ge k:
  $$
  $$
  ans \leftarrow \min(ans, i - Q.\text{pop\_front}())
  $$
- **Condition B (Dominance Pruning & Back Eviction):**
  $$
  \text{While } Q \ne \emptyset \land s[Q.\text{back}()] \ge s[i]:
  $$
  $$
  Q.\text{pop\_back}()
  $$
  $$
  Q.\text{push\_back}(i)
  $$

---

## 3. Step-by-Step Worked Execution

Prefix sums array:
$$
s = [0, 2, 1, 3]
$$
Initialize $ans = \infty$, Deque $Q = [\,]$.

---

### Step 1: Process Prefix Index $i = 0$ ($s[0] = 0$)
- Deque is empty.
- Push index $0$: $Q = [0]$.
- $ans = \infty$.

---

### Step 2: Process Prefix Index $i = 1$ ($s[1] = 2$, Element $nums[0] = 2$)
- **Check Front:**
  - $s[1] - s[Q[0]] = 2 - s[0] = 2 - 0 = 2 < k = 3$. Condition not met.
- **Check Back:**
  - $s[Q[-1]] = s[0] = 0 < s[1] = 2$. No dominance.
- Push index $1$: $Q = [0, 1]$.
- Deque values: $s = [0, 2]$.

---

### Step 3: Process Prefix Index $i = 2$ ($s[2] = 1$, Element $nums[1] = -1$)
- **Check Front:**
  - $s[2] - s[Q[0]] = 1 - 0 = 1 < 3$.
- **Check Back:**
  - $s[Q[-1]] = s[1] = 2$.
  - Compare with current: $s[1] = 2 \ge s[2] = 1 \implies$ **Back Dominance!**
  - Index $1$ has a higher prefix sum ($2$) and an earlier position than index $2$ ($1$). It can never form a shorter or easier-to-satisfy subarray than index $2$.
  - Pop index $1$ from back!
  - Now $Q[-1] = 0$, with $s[0] = 0 < s[2] = 1$.
- Push index $2$: $Q = [0, 2]$.
- Deque values: $s = [0, 1]$.

---

### Step 4: Process Prefix Index $i = 3$ ($s[3] = 3$, Element $nums[2] = 2$)
- **Check Front:**
  - $s[3] - s[Q[0]] = 3 - s[0] = 3 - 0 = 3 \ge k = 3 \implies$ **Valid Subarray!**
  - Candidate length: $i - Q[0] = 3 - 0 = 3$.
  - Update: $ans = \min(\infty, 3) = \mathbf{3}$.
  - Pop index $0$ from front (it can never produce a shorter length with $i' > 3$).
  - Now front is index $2$: $s[3] - s[2] = 3 - 1 = 2 < 3$. Stop front pops.
- **Check Back:**
  - $s[Q[-1]] = s[2] = 1 < s[3] = 3$. No dominance.
- Push index $3$: $Q = [2, 3]$.
- Deque values: $s = [1, 3]$.

---

### Final Evaluation:
All prefix sums processed.
$$
ans = \mathbf{3}
$$

---

## 4. Complete Execution Trace

| Current $i$ | Current $s[i]$ | Front Condition ($s[i] - s[Q[0]] \ge 3$) | Front Pops (Length Recorded) | Back Condition ($s[Q[-1]] \ge s[i]$) | Back Pops | Resulting Deque $Q$ | Best Length $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $0$ | Deque empty | None | Deque empty | None | $[0]$ | $\infty$ |
| $1$ | $2$ | $2 - 0 = 2 < 3$ | None | $0 < 2$ | None | $[0, 1]$ | $\infty$ |
| $2$ | $1$ | $1 - 0 = 1 < 3$ | None | $s[1] = 2 \ge 1$ | Pop index $1$ | $[0, 2]$ | $\infty$ |
| **$3$** | **$3$** | **$3 - 0 = 3 \ge 3$** | **Pop $0$ (Len: $3 - 0 = 3$)** | $s[2] = 1 < 3$ | None | $[2, 3]$ | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Element Meets $k$ (e.g. $nums = [3], k = 3$):** $s = [0, 3]$. At $i = 1$, $3 - 0 = 3 \ge 3 \implies$ returns $1$.
- **No Subarray Sums to $k$ (e.g. $nums = [1, 2], k = 4$):** Max prefix difference is $3 - 0 = 3 < 4$. $ans$ remains $\infty \implies$ returns $-1$.
- **All Negative Array (e.g. $nums = [-1, -2], k = 1$):** Prefix sums strictly decrease: $0, -1, -3$. No difference can be $\ge 1 \implies$ returns $-1$.
- **Large Positive Spikes:** When $nums[i] \ge k$, $s[i] - s[i-1] \ge k$ immediately triggers a length-1 check.

---

## 6. Traps & Common Anti-Patterns

- **Attempting Sliding Window Without Deque:** Standard two pointers fails because moving the left pointer when a sum is negative can discard valid windows, while keeping it can miss optimal windows.
- **Retaining $q[0]$ After Finding a Valid Subarray:** If $q[0]$ is not popped after yielding length $i - q[0]$, subsequent indices $i' > i$ would re-evaluate $q[0]$ yielding strictly longer lengths $i' - q[0] > i - q[0]$, wasting time and creating incorrect bounds.
- **Retaining Dominated Back Elements:** If $s[q[-1]] \ge s[i]$ is not pruned, the deque loses monotonicity, requiring a linear scan of the entire deque on every step, degrading time to $\mathcal{O}(N^2)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Prefix sums computation: $\mathcal{O}(N)$.
  - Each index $i \in [0, N]$ is pushed into the deque exactly once.
  - Each index is popped from the front at most once.
  - Each index is popped from the back at most once.
  - Total deque amortized operations: $\mathcal{O}(N)$.
  - Total Time: strictly $\mathcal{O}(N)$, handling $N = 10^5$ in $< 25$ ms.
- **Auxiliary Space Complexity:**
  - Prefix sum array and double-ended queue store at most $N + 1$ integers: $\mathcal{O}(N)$ space.
