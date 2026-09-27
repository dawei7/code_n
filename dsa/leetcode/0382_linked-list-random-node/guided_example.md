# Guided Example: Linked List Random Node

We trace the step-by-step Reservoir Sampling protocol on an unknown-length streaming linked list, dynamic sampling replacement probability ($\frac{1}{n}$ at step $n$), telescoping probability cancellation proof, and memory-less $O(1)$ space guarantees on representative linked list sequences:

- **Input:** Linked list $\text{head} = 1 \to 2 \to 3$ ($N = 3$)
- **Required output:** Random node value from $\{1, 2, 3\}$ with each having probability exactly $\frac{1}{3}$
  - Reservoir step-by-step trace:
    - Step 1 (Node 1): $n = 1 \implies \text{randint}(1, 1) = 1 \implies ans = 1$ (Selected with prob $1$)
    - Step 2 (Node 2): $n = 2 \implies \text{randint}(1, 2) \implies$ replace with prob $\frac{1}{2}$
      - Prob($ans = 2$) $= \frac{1}{2}$
      - Prob($ans = 1$) $= 1 \times (1 - \frac{1}{2}) = \frac{1}{2}$
    - Step 3 (Node 3): $n = 3 \implies \text{randint}(1, 3) \implies$ replace with prob $\frac{1}{3}$
      - Prob($ans = 3$) $= \frac{1}{3}$
      - Prob($ans = 2$) $= \frac{1}{2} \times (1 - \frac{1}{3}) = \frac{1}{2} \times \frac{2}{3} = \mathbf{\frac{1}{3}}$
      - Prob($ans = 1$) $= \frac{1}{2} \times (1 - \frac{1}{3}) = \frac{1}{2} \times \frac{2}{3} = \mathbf{\frac{1}{3}}$
  - All 3 nodes achieve exact uniform probability $\frac{1}{3}$!
- **Single Node List:** $\text{head} = [10] \implies$ returns $10$ with probability $1$
- **Streaming Context:** Works on infinite streams where total length $N$ is never known in advance

This instance demonstrates streaming randomized algorithms (Alan G. Waterman's Algorithm R), mathematically proves uniform selection via telescoping product series, avoids precomputing list length or storing nodes, and operates in $O(N)$ time and $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a singly linked list $\text{head} = 1 \to 2 \to 3$:
Return a random node's value such that each node in the list has **equal probability ($\frac{1}{N}$)** of being chosen:
Solve the problem **without pre-calculating the list length** and using **$O(1)$ auxiliary memory** (Reservoir Sampling):

```text
Stream of Unknown Length:  1 -> 2 -> 3 -> None

Node 1 (n=1): pick with prob 1/1 -> ans = 1
Node 2 (n=2): pick with prob 1/2 -> ans = 2 (prob 1/2), ans = 1 (prob 1/2)
Node 3 (n=3): pick with prob 1/3 -> ans = 3 (prob 1/3)
                                    ans = 2 (prob 1/2 * 2/3 = 1/3)
                                    ans = 1 (prob 1/2 * 2/3 = 1/3)

All nodes have identical final probability = 1/3!
```

---

## 2. Conceptual Foundation & Invariants

### 1. The Reservoir Sampling Principle (Algorithm R)
When sampling $k = 1$ item from a stream of unknown length:
1. Maintain current candidate `ans` and count $n = 0$.
2. Traverse each node in the stream:
   - Increment count: $n \leftarrow n + 1$.
   - Generate random integer:
     $$
     x = \text{random.randint}(1, \; n)
     $$
   - **Replacement Condition:** If $x == n$ (which occurs with probability $\frac{1}{n}$):
     $$
     ans \leftarrow \text{head.val}
     $$
3. After traversing all $N$ nodes, return `ans`.

### 2. The Telescoping Proof of Uniformity
For any specific node $k \in [1, N]$:
1. Node $k$ is selected as the candidate at step $k$ with probability:
   $$
   P(\text{chosen at step } k) = \frac{1}{k}
   $$
2. For each subsequent step $j \in [k + 1, N]$, node $k$ survives if it is **not replaced**:
   $$
   P(\text{not replaced at step } j) = 1 - \frac{1}{j} = \frac{j - 1}{j}
   $$
3. By independence, the probability that node $k$ remains the final answer at step $N$ is the telescoping product:
   $$
   P(\text{node } k \text{ survives to end}) = \frac{1}{k} \times \frac{k}{k + 1} \times \frac{k + 1}{k + 2} \times \dots \times \frac{N - 1}{N}
   $$
   Every numerator from $k$ to $N - 1$ cancels with the denominator of the preceding fraction:
   $$
   P = \frac{1}{N}
   $$

> **Invariant.** After processing the first $n$ elements, every element seen so far has survived with probability exactly $\frac{1}{n}$.

---

## 3. Step-by-Step Worked Execution

We trace `head = 1 -> 2 -> 3`:
Initialized: $n = 0, ans = 0$.

---

### Step 1: Visit Node 1 ($val = 1$)
- Stream count: $n = 1$.
- Sample: $x = \text{randint}(1, 1) = 1$.
- Condition $x == n \iff 1 == 1$ is **True** (Probability $= 1/1 = 1$).
- Update candidate:
  $$
  ans \leftarrow 1
  $$
- Distribution so far:
  $$
  P(1) = 1
  $$

---

### Step 2: Visit Node 2 ($val = 2$)
- Stream count: $n = 2$.
- Sample: $x = \text{randint}(1, 2) \in \{1, 2\}$.
- Condition $x == 2$ occurs with probability $\frac{1}{2}$:
  - If $x == 2$: $ans \leftarrow 2$.
  - If $x == 1$: $ans$ remains $1$.
- Distribution after 2 nodes:
  $$
  P(2) = \frac{1}{2}
  $$
  $$
  P(1) = 1 \times \left(1 - \frac{1}{2}\right) = \mathbf{\frac{1}{2}}
  $$

---

### Step 3: Visit Node 3 ($val = 3$)
- Stream count: $n = 3$.
- Sample: $x = \text{randint}(1, 3) \in \{1, 2, 3\}$.
- Condition $x == 3$ occurs with probability $\frac{1}{3}$:
  - If $x == 3$: $ans \leftarrow 3$.
  - If $x \in \{1, 2\}$ (probability $\frac{2}{3}$): retain current `ans`.
- Distribution after 3 nodes:
  $$
  P(3) = \mathbf{\frac{1}{3}}
  $$
  $$
  P(2) = \frac{1}{2} \times \frac{2}{3} = \mathbf{\frac{1}{3}}
  $$
  $$
  P(1) = \frac{1}{2} \times \frac{2}{3} = \mathbf{\frac{1}{3}}
  $$

---

### Step 4: Stream End
List ends (`head is None`). Return final reservoir candidate:
$$
ans \in \{1, 2, 3\} \quad \text{with equal probability } \frac{1}{3}
$$

---

## 4. Complete Execution Trace

```text
Linked List: 1 -> 2 -> 3 -> None

Step 1: Node 1, n=1
  randint(1, 1) = 1 == 1 -> ans = 1
  Probabilities: {1: 1.0}

Step 2: Node 2, n=2
  randint(1, 2) == 2 (prob 1/2) -> ans = 2
  Probabilities: {1: 1/2, 2: 1/2}

Step 3: Node 3, n=3
  randint(1, 3) == 3 (prob 1/3) -> ans = 3
  Probabilities: {1: 1/3, 2: 1/3, 3: 1/3}

Return ans
```

| Step $n$ | Node Value | Random Range Sampled | Replacement Condition | Replacement Probability | Survival Probability of Previous Candidates | Candidate Distribution |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 1 | $[1, 1] \implies x = 1$ | $x == 1$ | $1$ ($100\%$) | - | $\{1: 1.0\}$ |
| 2 | 2 | $[1, 2] \implies x \in \{1, 2\}$ | $x == 2$ | $\frac{1}{2}$ ($50\%$) | $1 - \frac{1}{2} = \frac{1}{2}$ | $\{1: 0.5, \; 2: 0.5\}$ |
| **3** | **3** | **$[1, 3] \implies x \in \{1, 2, 3\}$** | **$x == 3$** | **$\frac{1}{3}$ ($33.3\%$)** | **$1 - \frac{1}{3} = \frac{2}{3}$** | **$\{1: \frac{1}{3}, \; 2: \frac{1}{3}, \; 3: \frac{1}{3}\}$** |

---

## 5. Algorithmic Correctness

**Soundness.** At any step $n$, replacing the reservoir with probability $1/n$ ensures by induction that all $n$ processed elements have probability $1/n$ of being held. If true for $n - 1$, each of the first $n - 1$ elements had probability $1/(n - 1)$ of being in the reservoir; each survives step $n$ with probability $(n - 1)/n$, yielding $(1/(n - 1)) \times ((n - 1)/n) = 1/n$. The new element is chosen with probability $1/n$. By mathematical induction, exact uniformity holds for all $N \ge 1$.

**Completeness.** Every node in the singly linked list is visited exactly once until `head is None`. Because each node gets an opportunity to replace the reservoir with non-zero probability, no node is excluded from selection.

---

## 6. Traps This Instance Exposes

- **Storing All Nodes in an Array:** Converting the list to an array takes $O(N)$ extra memory. For huge lists with millions of nodes or streaming pipelines, this violates the $O(1)$ memory constraint.
- **Two-Pass Count-Then-Sample:** Counting length $N$ in pass 1 and picking a random index $k \in [0, N-1]$ in pass 2 requires 2 full traversals of the list. Reservoir sampling achieves the same distribution in a single pass.
- **Zero-Indexed vs One-Indexed Replacement:** `random.randint(1, n)` includes both $1$ and $n$. Testing `n == x` happens with probability $1/n$. If using `random.randint(0, n)`, the range has $n + 1$ outcomes, causing an off-by-one distortion.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `__init__(head)`: $O(1)$ time to store the head pointer.
  - `getRandom()`: $O(N)$ time, where $N$ is the number of nodes in the linked list, making a single forward pass.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space, storing only scalar counters $n$, $x$, and candidate value $ans$.