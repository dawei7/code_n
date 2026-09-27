# Guided Example: Friends Of Appropriate Ages

We trace the step-by-step age distribution histogram construction ($cnt[age]$), request eligibility criteria ($0.5 \cdot ax + 7 < ay \le ax$), minimum sender threshold ($ax > 14$), self-request exclusion ($ax == ay \implies cnt[ax] - 1$), Cartesian age pair cross-multiplication, and total friend request tally accumulation on representative age demographics:

- **Input:**
  $$
  ages = [16, 17, 18]
  $$
- **Required output:** `2`
  - Friend request criteria:
    - A person $x$ of age $ax$ sends a friend request to person $y$ of age $ay$ if and only if **NONE** of the following reject conditions hold:
      1. $ay \le 0.5 \cdot ax + 7$ (Too young relative to $x$)
      2. $ay > ax$ (Strictly older than $x$)
      3. $ay > 100 \land ax < 100$ (Redundant; subsumed by condition 2)
    - Reversing these negative conditions, a request is sent if and only if $ay$ falls in the half-open interval:
      $$
      0.5 \cdot ax + 7 < ay \le ax
      $$
    - People cannot send friend requests to themselves ($x \ne y$).
    - Requests are directed (asymmetric).
    - For $ages = [16, 17, 18]$:
      - For Person with age 17:
        - Eligible age range: $0.5(17) + 7 = 15.5 < ay \le 17 \implies ay \in \{16, 17\}$.
        - Person 16 qualifies ($16 > 15.5$ and $16 \le 17$) $\implies \mathbf{1\ request}$ ($17 \to 16$).
      - For Person with age 18:
        - Eligible age range: $0.5(18) + 7 = 16.0 < ay \le 18 \implies ay \in \{17, 18\}$.
        - Notice Person 16 does **not** qualify because $16 \le 16.0$!
        - Person 17 qualifies ($17 > 16$ and $17 \le 18$) $\implies \mathbf{1\ request}$ ($18 \to 17$).
      - For Person with age 16:
        - Eligible age range: $0.5(16) + 7 = 15.0 < ay \le 16 \implies ay \in \{16\}$.
        - There are no other people of age 16 $\implies \mathbf{0\ requests}$.
      - Total friend requests: $1 + 1 = \mathbf{2}$.
- **Age Interval & Bucket Multiplicity Invariant:**
  - **The Feasibility Threshold ($ax > 14$):**
    - For the interval $(0.5 \cdot ax + 7, \; ax]$ to contain any integers, the upper bound must strictly exceed the lower bound:
      $$
      ax > 0.5 \cdot ax + 7 \iff 0.5 \cdot ax > 7 \iff ax > 14
      $$
    - Anyone aged $14$ or younger can **never send any friend requests**!
  - **Bucket Aggregation ($1 \le age \le 120$):**
    - The array $ages$ can contain up to $20,000$ entries, but ages are bounded by $120$.
    - Instead of checking all $N^2 = 4 \times 10^8$ person pairs, count frequencies into an array $cnt$ of size 121:
      $$
      cnt[a] = \text{number of people with age } a
      $$
  - **Pairwise Multiplication:**
    - For each pair of ages $(ax, ay) \in [1, 120]^2$:
      - If $0.5 \cdot ax + 7 < ay \le ax$:
        - If $ax == ay$: each of the $cnt[ax]$ people sends requests to all other $cnt[ax] - 1$ people of the same age:
          $$
          \text{requests} = cnt[ax] \times (cnt[ax] - 1)
          $$
        - If $ax \ne ay$: each of the $cnt[ax]$ people sends requests to all $cnt[ay]$ people of age $ay$:
          $$
          \text{requests} = cnt[ax] \times cnt[ay]
          $$
- **Step-by-Step Worked Execution Trace on $ages = [16, 17, 18]$:**
  - Construct frequency histogram:
    - $cnt[16] = 1$
    - $cnt[17] = 1$
    - $cnt[18] = 1$
    - All other $cnt[a] = 0$.
  - Initialize total requests: $ans = 0$.
  - **Evaluating Sender Age $ax = 16$ ($cnt[16] = 1$):**
    - Minimum recipient age: $\lfloor 0.5(16) + 7 \rfloor + 1 = 15 + 1 = \mathbf{16}$.
    - Allowed interval: $16 \le ay \le 16 \implies ay = 16$.
    - Self-exclusion check ($ax == ay$):
      $$
      cnt[16] \times (cnt[16] - 1) = 1 \times (1 - 1) = \mathbf{0}
      $$
  - **Evaluating Sender Age $ax = 17$ ($cnt[17] = 1$):**
    - Lower threshold: $0.5(17) + 7 = 15.5 \implies ay \ge 16$.
    - Allowed interval: $16 \le ay \le 17$.
    - **Target $ay = 16$ ($ax \ne ay$):**
      $$
      cnt[17] \times cnt[16] = 1 \times 1 = \mathbf{1}
      $$
      *(Request: $17 \to 16$)*.
    - **Target $ay = 17$ ($ax == ay$):**
      $$
      cnt[17] \times (cnt[17] - 1) = 1 \times 0 = \mathbf{0}
      $$
    - Subtotal from age 17: $\mathbf{1}$.
  - **Evaluating Sender Age $ax = 18$ ($cnt[18] = 1$):**
    - Lower threshold: $0.5(18) + 7 = 16.0 \implies ay > 16 \implies ay \ge 17$.
    - Allowed interval: $17 \le ay \le 18$.
    - **Target $ay = 16$:**
      - $16 \le 16.0 \implies \mathbf{Disqualified.}$
    - **Target $ay = 17$ ($ax \ne ay$):**
      $$
      cnt[18] \times cnt[17] = 1 \times 1 = \mathbf{1}
      $$
      *(Request: $18 \to 17$)*.
    - **Target $ay = 18$ ($ax == ay$):**
      $$
      cnt[18] \times (cnt[18] - 1) = 1 \times 0 = \mathbf{0}
      $$
    - Subtotal from age 18: $\mathbf{1}$.
  - **Total Aggregation:**
    $$
    ans = 0 + 1 + 1 = \mathbf{2}
    $$
- **Equal Age Pair Trace ($ages = [16, 16]$):**
  - $cnt[16] = 2$.
  - Interval for $ax = 16$: $15.5 < ay \le 16 \implies ay = 16$.
  - Formula: $2 \times (2 - 1) = 2 \times 1 = \mathbf{2}$ (each 16-year-old requests the other).
- **Sub-15 Demographic Trace ($ages = [10, 12, 14]$):**
  - All $ax \le 14$.
  - For $ax = 14$: lower bound is $0.5(14) + 7 = 14$, interval $14 < ay \le 14$ is empty!
  - Requests generated: $\mathbf{0}$.

This instance demonstrates Cartesian reduction over finite quotient groups and 1D interval counting on bounded integer alphabets, mathematically proves why pre-aggregating identical elements into frequency measures reduces $O(N^2)$ relation matching to $O(A^2)$ arithmetic, and derives $O(N + A^2)$ runtime and $O(A)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given ages of people:
Person of age $ax$ requests person of age $ay$ if and only if:
$$
0.5 \cdot ax + 7 < ay \le ax
$$
Count the total number of friend requests.

```text
ages = [ 16, 17, 18 ]

Person 17:
  Valid range: 0.5 * 17 + 7 = 15.5 < ay <= 17 -> { 16, 17 }
  Sends request to 16 (+1)

Person 18:
  Valid range: 0.5 * 18 + 7 = 16.0 < ay <= 18 -> { 17, 18 }
  Notice 16 is NOT > 16.0!
  Sends request to 17 (+1)

Person 16:
  Valid range: 0.5 * 16 + 7 = 15.0 < ay <= 16 -> { 16 }
  No other person of age 16 (+0)

Total requests = 1 + 1 = 2
Result: 2
```

### The Invariant of Age Bucket Counting
- $N$ can be $20,000$, but ages are only $1 \dots 120$.
- Count frequencies in an array of size 121.
- People aged $\le 14$ never send requests ($0.5 \cdot ax + 7 \ge ax$).
- Self-requests are excluded ($cnt[ax] \times (cnt[ax] - 1)$ when $ax == ay$).

---

## 2. Conceptual Foundation & Invariants

### 1. Request Eligibility Predicate:
$$
\text{Valid}(ax, ay) \iff (0.5 \cdot ax + 7 < ay) \;\land\; (ay \le ax)
$$

### 2. Multiplicity Formula:
$$
\text{Requests}(ax, ay) = cnt[ax] \times \Big( cnt[ay] - [ax == ay] \Big)
$$
$$
ans = \sum_{ax = 15}^{120} \sum_{ay = \lfloor 0.5 ax + 7 \rfloor + 1}^{ax} \text{Requests}(ax, ay)
$$

> **Quotient Graph Invariant.** The friend relation $R$ on individuals factors through the age projection $\pi: People \to \{1, \dots, 120\}$. The cardinality $|R|$ is the pushforward measure under $\pi \times \pi$ minus the diagonal self-loops.

---

## 3. Step-by-Step Worked Execution

We trace $ages = [16, 17, 18]$:

---

### Step 1: Histogram
- $cnt[16] = 1, cnt[17] = 1, cnt[18] = 1$.

---

### Step 2: Senders of Age 16
- Allowed $ay$: $16$. Self only $\implies 0$.

---

### Step 3: Senders of Age 17
- Allowed $ay$: $16, 17$.
- $17 \to 16$: $1 \times 1 = \mathbf{1}$.

---

### Step 4: Senders of Age 18
- Allowed $ay$: $17, 18$ ($16$ is rejected by $16 \le 16.0$).
- $18 \to 17$: $1 \times 1 = \mathbf{1}$.

---

### Step 5: Output
- $1 + 1 = \mathbf{2}$.

---

## 4. Complete Execution Trace

| Sender Age $ax$ | Sender Count | Valid Recipient Interval | Recipient Age $ay$ | Multiplier Term | Requests Generated |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $16$ | $1$ | $(15.0, 16]$ | $16$ | $1 \times (1 - 1)$ | $0$ |
| $17$ | $1$ | $(15.5, 17]$ | $16$ | $1 \times 1$ | $1$ |
| $17$ | $1$ | $(15.5, 17]$ | $17$ | $1 \times (1 - 1)$ | $0$ |
| **$18$** | **$1$** | **$(16.0, 18]$** | **$16$** | **Disqualified ($16 \le 16.0$)** | **$0$** |
| **$18$** | **$1$** | **$(16.0, 18]$** | **$17$** | **$1 \times 1$** | **`1`** |
| **Total** | — | — | — | — | **`2`** |

---

## 5. Boundary Cases & Failure Modes

- **Strict Inequality on Lower Bound:** $ay \le 0.5 \cdot ax + 7$ is rejected, meaning $ay$ must be **strictly greater** than $0.5 \cdot ax + 7$. For $ax = 18$, $0.5(18) + 7 = 16.0$, so $ay = 16$ is strictly rejected.
- **Ages $\le 14$:** Interval is empty $\implies 0$ requests.
- **Large Populations ($N = 20,000$):** Frequency histogram handles arbitrary $N$ without quadratic slowdown.
- **Identical Ages ($[16, 16]$):** Both send to each other $\implies 2$.

---

## 6. Traps & Common Anti-Patterns

- **Comparing All Pairs ($O(N^2)$):** For $N = 20,000$, an $N^2$ loop executes $4 \times 10^8$ operations (TLE). Bucket counting over max age 120 executes only $120^2 = 14,400$ iterations.
- **Permitting Self-Requests:** A person cannot send a friend request to themselves; when $ax == ay$, subtract 1 from recipient count ($y - 1$).
- **Allowing $ay > ax$:** A person never sends a request to someone older than themselves ($ay \le ax$).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Building histogram: $\mathcal{O}(N)$ where $N \le 20,000$.
  - Nested loops over age range: $\mathcal{O}(A^2)$ where $A = 120 \implies 14,400$ iterations.
  - Total Time: strictly $\mathcal{O}(N + A^2)$. Completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(A)$ memory for the frequency array ($A = 121$).
