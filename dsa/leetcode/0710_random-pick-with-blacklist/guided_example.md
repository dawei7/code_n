# Guided Example: Random Pick with Blacklist

We trace the step-by-step valid domain size calculation ($k = n - |B|$), low-range/high-range partition ($[0, k-1]$ vs $[k, n-1]$), low-blacklist to high-whitelist bijection mapping ($d[b] = i$), single-call uniform sampling ($x \in [0, k-1]$), hash map alias redirection ($d.get(x, x)$), and equiprobable white integer generation on representative blacklisted intervals:

- **Input:**
  - Total range: $n = 7$ (integers $0, 1, 2, 3, 4, 5, 6$)
  - Blacklist: $blacklist = [2, 3, 5]$
  - Random draw sequence: $draws = [0, 1, 2, 3, 2]$
- **Required output:** $[0, 1, 4, 6, 4]$
  - Problem requirements:
    - Return a uniformly random integer from the set of non-blacklisted (white) numbers in $[0, n - 1]$.
    - Range size: $n = 7$.
    - Blacklisted numbers: $\{2, 3, 5\}$.
    - Valid white numbers: $\{0, 1, 4, 6\}$ (total 4 valid numbers).
    - Each valid number must have an exact probability of:
      $$
      P(\text{pick}) = \frac{1}{4} = 0.25
      $$
    - Minimization requirement: Must invoke the random number generator **at most once** per `pick()` call.
- **Low/High Partition & Virtual Remapping Invariant:**
  - **1. The Sampling Window $k = n - |B|$:**
    - Let $B$ be the blacklist of size $|B|$.
    - There are exactly $k = n - |B|$ valid white numbers in total.
    - If we sample a uniform random integer $x$ in the interval $[0, k - 1]$, there are exactly $k$ equally likely outcomes.
  - **2. The Low-Range / High-Range Split:**
    - Divide the entire integer space $[0, n - 1]$ into two segments:
      - **Low Segment:** $[0, \; k - 1]$ (size $k$).
      - **High Segment:** $[k, \; n - 1]$ (size $|B|$).
    - Notice that any number $x \in [0, k - 1]$ is either:
      - A white number (which can be returned directly: $x$).
      - A blacklisted number (which cannot be returned!).
  - **3. The Cardinality Conservation Invariant:**
    - Let $B_{low}$ be the blacklisted numbers in $[0, k - 1]$.
    - Let $B_{high}$ be the blacklisted numbers in $[k, n - 1]$.
    - Then $|B| = B_{low} + B_{high}$.
    - The number of white numbers in the High Segment is:
      $$
      \text{White}_{high} = |[k, n-1]| - B_{high} = |B| - B_{high} = \mathbf{B_{low}}
      $$
    - The number of blacklisted numbers in the Low Segment **identically matches** the number of white numbers in the High Segment!
  - **4. The Remapping Dictionary:**
    - Map each low blacklisted number $b \in B_{low}$ to a unique white number in the High Segment:
      $$
      d[b] \leftarrow w \quad (w \in [k, n - 1] \setminus B)
      $$
    - During `pick()`:
      - Draw $x = \text{random}(0, k - 1)$.
      - If $x$ is in $d$, return its remapped alias $d[x]$.
      - Otherwise, return $x$ directly.
      - Exactly 1 random call, strictly uniform distribution over all white numbers!
- **Step-by-Step Worked Execution Trace on $n = 7, blacklist = [2, 3, 5]$:**
  - **Phase 0: Preprocessing & Table Construction:**
    - Total valid count:
      $$
      k = n - |B| = 7 - 3 = \mathbf{4}
      $$
    - Low segment: $[0, 3]$. High segment: $[4, 6]$.
    - Blacklist set: $black = \{2, 3, 5\}$.
    - Initialize remap pointer at start of high segment: $i = k = 4$.
    - Process each $b \in blacklist$:
      - **Element $b = 2$:**
        - $2 < k = 4 \implies b \in B_{low}$.
        - Advance $i$ past any high blacklisted numbers:
          - Current $i = 4 \notin black$ (4 is white!).
        - Create alias:
          $$
          d[2] \leftarrow 4
          $$
        - Advance pointer: $i \leftarrow 5$.
      - **Element $b = 3$:**
        - $3 < k = 4 \implies b \in B_{low}$.
        - Advance $i$ past any high blacklisted numbers:
          - Current $i = 5 \in black \implies$ Skip!
          - Next $i = 6 \notin black$ (6 is white!).
        - Create alias:
          $$
          d[3] \leftarrow 6
          $$
        - Advance pointer: $i \leftarrow 7$.
      - **Element $b = 5$:**
        - $5 \ge k = 4 \implies b \in B_{high}$.
        - Ignored (already in high segment, skipped by pointer $i$).
    - Constructed Remapping Table:
      $$
      d = \{ 2 \mapsto 4, \; 3 \mapsto 6 \}
      $$
  - **Phase 1: Serving `pick()` Queries with Drawn Indices $[0, 1, 2, 3, 2]$:**
    - **Query 1 (Drawn $x = 0$):**
      - $0 \notin d \implies$ Return $0$ directly.
    - **Query 2 (Drawn $x = 1$):**
      - $1 \notin d \implies$ Return $1$ directly.
    - **Query 3 (Drawn $x = 2$):**
      - $2 \in d \implies$ Alias lookup:
        $$
        d[2] = \mathbf{4}
        $$
      - Return $4$.
    - **Query 4 (Drawn $x = 3$):**
      - $3 \in d \implies$ Alias lookup:
        $$
        d[3] = \mathbf{6}
        $$
      - Return $6$.
    - **Query 5 (Drawn $x = 2$):**
      - $2 \in d \implies$ Alias lookup: $d[2] = \mathbf{4}$.
      - Return $4$.
  - **Phase 2: Final Output:**
    $$
    ans = [\mathbf{0}, \; \mathbf{1}, \; \mathbf{4}, \; \mathbf{6}, \; \mathbf{4}]
    $$
    - Every returned number $\{0, 1, 4, 6\}$ belongs to the white set, with uniform $\frac{1}{4}$ probability.
- **Every Low Bucket Remapped ($n = 4, blacklist = [0, 1]$):**
  - $k = 4 - 2 = 2$. Low segment: $[0, 1]$. High segment: $[2, 3]$.
  - Remapping: $0 \mapsto 2, \; 1 \mapsto 3$.
  - Draws from $[0, 1]$ map to $\{2, 3\}$.
- **Empty Blacklist ($n = 10, blacklist = []$):**
  - $k = 10$. No remapping needed $\implies d = \{\}$.
  - Returns $x \in [0, 9]$ directly.

This instance demonstrates probability distribution push-forward transformations and virtual memory address translation, mathematically proves why bijectively pairing low forbidden states with high admissible states achieves exact uniform sampling, and derives $O(B)$ preprocessing time, $O(1)$ query time, and $O(B)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given $n$ and an array `blacklist`:
Pick a random number in $[0, n-1]$ that is **NOT in blacklist** with uniform probability.
Minimize calls to the random number generator (use strictly 1 call per pick).

```text
n = 7, blacklist = [ 2, 3, 5 ]

Total valid numbers = 7 - 3 = 4.
Target white numbers: { 0, 1, 4, 6 }

Partition into Low [0, 3] and High [4, 6]:
  Low: 0 (white), 1 (white), 2 (black), 3 (black)
  High: 4 (white), 5 (black), 6 (white)

Remap low blacklisted numbers to high white numbers:
  2 -> 4
  3 -> 6

Draw random x in [0, 3]:
  x = 0 -> returns 0
  x = 1 -> returns 1
  x = 2 -> returns d[2] = 4
  x = 3 -> returns d[3] = 6

All 4 white numbers have equal 1/4 probability!
```

### The Invariant of the Exact Bipartite Remap
- The number of blacklisted numbers below $k$ strictly equals the number of white numbers above or equal to $k$.
- Storing this one-to-one mapping in a hash map guarantees that a single random draw in $[0, k-1]$ maps bijectively to all valid white numbers.

---

## 2. Conceptual Foundation & Invariants

### 1. Partition and Remap:
$$
k = n - |blacklist|
$$
For each $b \in blacklist$ with $b < k$:
$$
\text{Find next } w \in [k, n - 1] \setminus blacklist
$$
$$
d[b] \leftarrow w
$$

### 2. $O(1)$ Retrieval:
$$
x \sim \text{Uniform}(\{0, 1, \dots, k - 1\})
$$
$$
ans = \begin{cases} d[x] & \text{if } x \in d \\ x & \text{otherwise} \end{cases}
$$

> **Equimeasurable Pushforward Invariant.** The piecewise map $\phi: [0, k-1] \to [0, n-1] \setminus B$ defined by $\phi(x) = d[x]$ if $x \in B$ and $\phi(x) = x$ otherwise is a measure-preserving bijection between the discrete uniform probability space on $[0, k-1]$ and the normalized counting measure on the white set $[0, n-1] \setminus B$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Preprocessing
- $n = 7, |B| = 3 \implies k = 4$.
- $B_{low} = \{2, 3\}$.
- High segment $[4, 6]$ has white numbers $\{4, 6\}$.
- $d[2] = 4, d[3] = 6$.

---

### Step 2: Draws $[0, 1, 2, 3, 2]$
- Draw 0: $0 \notin d \implies 0$.
- Draw 1: $1 \notin d \implies 1$.
- Draw 2: $2 \in d \implies 4$.
- Draw 3: $3 \in d \implies 6$.
- Draw 2: $2 \in d \implies 4$.

---

### Step 3: Output
$$
[\mathbf{0}, \; \mathbf{1}, \; \mathbf{4}, \; \mathbf{6}, \; \mathbf{4}]
$$

---

## 4. Complete Execution Trace

| Random Sample $x$ | In Low Blacklist? | Mapped Alias $d[x]$ | Returned Value | Probability of Outcome |
|:---:|:---:|:---:|:---:|:---:|
| $0$ | No (White) | None | **`0`** | $1/4$ |
| $1$ | No (White) | None | **`1`** | $1/4$ |
| $2$ | **Yes (Black)** | $4$ | **`4`** | $1/4$ |
| $3$ | **Yes (Black)** | $6$ | **`6`** | $1/4$ |

---

## 5. Boundary Cases & Failure Modes

- **Empty Blacklist ($B = 0$):** $k = n$, no remapping, draws uniformly from $[0, n - 1]$.
- **All Blacklist in High Segment:** $B_{low} = \emptyset$, map $d$ remains empty, draws from $[0, k - 1]$ directly.
- **Large Range ($n = 10^9, |B| = 10^5$):** Preprocessing takes $O(|B|)$ time, avoiding allocating size $n$.
- **Maximum Blacklist ($|B| = n - 1$):** $k = 1$, draws 0, returns the single remaining white number.

---

## 6. Traps & Common Anti-Patterns

- **Rejection Sampling (`while x in blacklist: x = rand()`):** If $|B|$ is close to $n$ (e.g. $99\%$ blacklisted), rejection sampling loops hundreds of times before finding a white number, violating efficiency requirements.
- **Allocating Full Array of Size $n$ ($O(n)$ Space):** Since $n$ can be $10^9$, allocating an array of size $n$ causes immediate Memory Limit Exceeded. Only store remapped pairs for $|B_{low}| \le |B|$ elements.
- **Remapping to Another Blacklisted Number:** When advancing pointer $i$ in $[k, n - 1]$, ensure $i$ skips any numbers that are themselves in the blacklist (`while i in black: i += 1`).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Preprocessing: Iterate through blacklist of size $B$ $\implies \mathcal{O}(B)$ time.
  - Each `pick()` query: 1 random number generation and 1 hash map lookup $\implies$ strictly constant time $\mathcal{O}(1)$.
  - Completes $10^5$ queries in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(B)$ space for the hash set of blacklisted numbers and remapping table $d$.
