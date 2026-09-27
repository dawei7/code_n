# Guided Example: Random Pick with Weight

We trace the step-by-step prefix sum cumulative mass function ($s[i] = \sum_{k=0}^{i-1} w[k]$), uniform discrete token generation ($x \in [1, W]$), binary search bisecting monotonic interval boundaries ($s[mid] \ge x$), and proportional index extraction on representative weight distributions:

- **Input Configuration:**
  - Weight array: $w = [1, 3]$
  - Total indices: $n = 2$ ($index \in \{0, 1\}$)
- **Probability Target:**
  - Total weight: $W = 1 + 3 = 4$
  - Probability of index 0: $P(0) = \frac{w[0]}{W} = \frac{1}{4} = \mathbf{25\%}$
  - Probability of index 1: $P(1) = \frac{w[1]}{W} = \frac{3}{4} = \mathbf{75\%}$
- **Cumulative prefix array construction:**
  - Let $s$ be the prefix sum array rooted at $0$:
    $$
    s = [0, \; 1, \; 4]
    $$
  - The line segment of total length $4$ is partitioned into intervals:
    - Interval $[1, 1]$ (length 1): Maps to **Index 0**
    - Interval $[2, 4]$ (length 3): Maps to **Index 1**
- **Sampling trace (`pickIndex()`):**
  - **Draw 1 (Random token $x = 1 \in [1, 4]$):**
    - Binary search on $s = [0, 1, 4]$:
      - Search range: $left = 1, \; right = 2$.
      - Midpoint: $mid = (1 + 2) // 2 = 1$.
      - Check: $s[1] = 1 \ge x (1)$ (**True**) $\implies right \leftarrow 1$.
      - Loop terminates with $left = 1$.
    - Return index:
      $$
      \text{index} = left - 1 = 1 - 1 = \mathbf{0}
      $$
  - **Draw 2 (Random token $x = 3 \in [1, 4]$):**
    - Binary search on $s = [0, 1, 4]$:
      - Range: $left = 1, \; right = 2$.
      - $mid = 1$: $s[1] = 1 < x (3)$ (**False**) $\implies left \leftarrow mid + 1 = 2$.
      - Loop terminates with $left = 2$.
    - Return index:
      $$
      \text{index} = left - 1 = 2 - 1 = \mathbf{1}
      $$
  - **Draw 3 (Random token $x = 4 \in [1, 4]$):**
    - $mid = 1$: $s[1] = 1 < 4 \implies left \leftarrow 2$.
    - Return index:
      $$
      \text{index} = 2 - 1 = \mathbf{1}
      $$
  - Across the 4 equally likely random values $\{1, 2, 3, 4\}$:
    - Token $1$ selects Index $0$ (1 out of 4 draws $\implies 25\%$).
    - Tokens $2, 3, 4$ select Index $1$ (3 out of 4 draws $\implies 75\%$).
    - The distribution exactly matches the required weights!
- **Single Index Array ($w = [10]$):**
  - Only index 0 exists $\implies$ Always picks $\mathbf{0}$ with $100\%$ probability.
- **Uniform Weights Array ($w = [2, 2, 2, 2]$):**
  - Prefix sums $[0, 2, 4, 6, 8] \implies$ Each index covers a span of length 2 ($\frac{2}{8} = 25\%$ each).

This instance demonstrates inverse transform sampling on discrete probability distributions, mathematically proves why binary search over monotonic cumulative mass intervals guarantees proportional selection, and derives $O(N)$ initialization, $O(\log N)$ pick runtime, and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array of positive integers $w$ where $w[i]$ describes the weight of index $i$:
Implement `pickIndex()` which returns a random index $i \in [0, n - 1]$ with probability:
$$
P(i) = \frac{w[i]}{\sum_{j=0}^{n-1} w[j]}
$$

```text
Weights: w = [ 1,  3 ]
Total Weight = 1 + 3 = 4

Number Line [1 .. 4]:
  [ 1 ] [ 2   3   4 ]
  Index 0    Index 1
  (25%)       (75%)

Pick a uniform random integer in [1 .. 4]:
  If 1      -> Index 0
  If 2,3,4  -> Index 1
```

### Continuous Roulette Wheel to Discrete Binary Search
- If we generate a uniform random token $x \in [1, W]$ where $W = \sum w[i]$:
- The token lands in the interval corresponding to index $i$ if:
  $$
  \sum_{k=0}^{i-1} w[k] < x \le \sum_{k=0}^i w[k]
  $$
- Because weights are strictly positive ($w[i] > 0$), the prefix sums are **strictly monotonically increasing**.
- This monotonic property allows us to locate the target interval using **Binary Search** in $O(\log N)$ time rather than scanning linearly.

---

## 2. Conceptual Foundation & Invariants

### 1. The Cumulative Sum Array:
Let array $s$ have length $n + 1$:
$$
s[0] = 0, \quad s[i] = s[i - 1] + w[i - 1] \quad \forall i \in [1, n]
$$
- $s[i]$ is the total weight of all elements strictly preceding index $i$.
- Total weight of all elements is $W = s[n]$.

### 2. Binary Search Selection:
For each call to `pickIndex()`:
1. Roll $x \in [1, W]$ uniformly at random.
2. Find the smallest index $mid \in [1, n]$ such that:
   $$
   s[mid] \ge x
   $$
   using standard lower-bound binary search:
   - If $s[mid] \ge x$: $right \leftarrow mid$.
   - Else: $left \leftarrow mid + 1$.
3. Return $left - 1$.

> **Partition Measure Invariant.** The length of the interval $(s[i], s[i+1]]$ is exactly $w[i]$, guaranteeing that a uniform token lands in that interval with probability $\frac{w[i]}{W}$.

---

## 3. Step-by-Step Worked Execution

We trace $w = [1, 3]$:

---

### Step 1: Initialization
- Compute prefix sums:
  - $s[0] = 0$
  - $s[1] = 0 + 1 = 1$
  - $s[2] = 1 + 3 = 4$
  - Array: $s = [0, 1, 4]$. Total weight $W = 4$.

---

### Step 2: Sampling Trace for $x = 1$
- Search interval: $left = 1, right = 2$.
- $mid = (1 + 2) // 2 = 1$.
- Check $s[1] = 1 \ge 1$ (**True**):
  - $right \leftarrow 1$.
- Loop terminates with $left = 1$.
- Output index:
  $$
  left - 1 = 1 - 1 = \mathbf{0}
  $$

---

### Step 3: Sampling Trace for $x = 3$
- Search interval: $left = 1, right = 2$.
- $mid = 1$.
- Check $s[1] = 1 \ge 3$ (**False**):
  - $left \leftarrow mid + 1 = 2$.
- Loop terminates with $left = 2$.
- Output index:
  $$
  left - 1 = 2 - 1 = \mathbf{1}
  $$

---

### Step 4: Probability Distribution Summary
- $x = 1 \implies$ returns $0$ ($25\%$).
- $x \in \{2, 3, 4\} \implies$ returns $1$ ($75\%$).
- Proportions match weights $w = [1, 3]$ exactly.

---

## 4. Complete Execution Trace

| Random Roll $x \in [1, W]$ | Binary Search Search Steps | Final Boundary $left$ | Output Index $left - 1$ | Associated Interval | Theoretical Probability |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **$1$** | $mid=1, s[1]=1 \ge 1 \implies right=1$ | $1$ | **$0$** | $(0, 1]$ | $1/4 = 25\%$ |
| **$2$** | $mid=1, s[1]=1 < 2 \implies left=2$ | $2$ | **$1$** | $(1, 4]$ | $3/4 = 75\%$ |
| **$3$** | $mid=1, s[1]=1 < 3 \implies left=2$ | $2$ | **$1$** | $(1, 4]$ | $3/4 = 75\%$ |
| **$4$** | $mid=1, s[1]=1 < 4 \implies left=2$ | $2$ | **$1$** | $(1, 4]$ | $3/4 = 75\%$ |

---

## 5. Boundary Cases & Failure Modes

- **Single Weight ($w = [5]$):** $s = [0, 5]$. $x \in [1, 5]$ always yields $mid = 1 \implies \mathbf{0}$.
- **Large Weights ($w[i] = 10^5, n = 10^4$):** Total weight $W = 10^9$. Fits comfortably inside 32-bit signed integers.
- **Skewed Distribution ($w = [1, 999]$):** Token 1 selects index 0; tokens $2 \dots 1000$ select index 1.
- **Equal Weights ($w = [1, 1, 1]$):** Acts as standard uniform random choice with $1/3$ probability each.

---

## 6. Traps & Common Anti-Patterns

- **Linear Scan ($O(N)$ per Pick):** Scanning through the prefix array on every pick takes $O(N)$ time. When `pickIndex()` is called $10^4$ times, this takes $10^8$ operations. Binary search reduces each pick to $O(\log N)$.
- **0-Indexed Random Range (`random.randint(0, W)`):** Generating in range $[0, W]$ produces $W + 1$ outcomes instead of $W$, slightly distorting probabilities by giving token 0 extra weight. Range must be strictly $[1, W]$ or $[0, W-1]$.
- **Creating an Expanded Array of Values:** Replicating indices into an explicit list `[0] + [1, 1, 1]` takes $O(\sum w)$ space, which crashes for weights up to $10^5$. Prefix sums use strictly $O(N)$ space.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initialization `__init__`: Computing prefix sums over $N$ weights takes $\mathcal{O}(N)$ time.
  - Query `pickIndex`:
    - Random token generation: $O(1)$.
    - Binary search on array of size $N + 1$: strictly $\mathcal{O}(\log N)$.
    - Total Time per pick: $\mathcal{O}(\log N)$. For $N = 10^4$, $\log_2(10^4) \approx 14$ comparisons, completing in $< 1$ microsecond.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store the prefix sum array $s$.