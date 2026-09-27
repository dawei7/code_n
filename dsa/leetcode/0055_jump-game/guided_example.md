# Guided Example: Jump Game

We trace the step-by-step greedy reachability horizon evaluation on representative reachable and trapped array instances:

- **Reachable Instance:** $\text{nums} = [2, 3, 1, 1, 4] \implies \text{True}$
- **Trapped Instance (Zero Barrier):** $\text{nums} = [3, 2, 1, 0, 4] \implies \text{False}$

This instance demonstrates tracking the maximum reachable index horizon ($\text{max\_reach} = \max(\text{max\_reach}, i + \text{nums}[i])$), early-exit optimization upon reaching destination, and detecting impassable zero-trap barriers in $O(N)$ time and $O(1)$ space.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums}$ where each element $\text{nums}[i]$ represents the maximum jump length from position $i$, determine if you can reach the last index ($N - 1$) starting from index $0$.

Consider two contrasting cases:
1. $[2, 3, 1, 1, 4]$: From index 0 we reach index 1, and from index 1 we jump 3 units directly to index 4 ($\text{True}$).
2. $[3, 2, 1, 0, 4]$: Any jump from indices 0, 1, or 2 lands at index 3 at most. But index 3 has value $0$, trapping the path before index 4 can be reached ($\text{False}$).

A naive recursive search explores exponential $O(2^N)$ jump paths. The optimal greedy approach tracks a single scalar variable, $\text{max\_reach}$, representing the furthest index reachable so far. If the current index $i$ ever exceeds $\text{max\_reach}$, a disconnected barrier has been reached.

---

## 2. Conceptual Foundation & Invariants

### The Greedy Horizon Invariant
Let $\text{max\_reach}$ be the maximum index reachable from any previously visited index $0 \dots i$:
$$
\text{max\_reach}_{\text{new}} = \max(\text{max\_reach}, \, i + \text{nums}[i])
$$

### Algorithm Execution Rules
For each index $i \in [0, N - 1]$:
1. **Connectivity Check:** If $i > \text{max\_reach}$, then index $i$ is unreachable from the start. Return $\text{False}$ immediately.
2. **Horizon Update:** $\text{max\_reach} \leftarrow \max(\text{max\_reach}, i + \text{nums}[i])$.
3. **Early Exit:** If $\text{max\_reach} \ge N - 1$, the final index is reachable. Return $\text{True}$ immediately.

> **Invariant.** All indices $k \in [0, \text{max\_reach}]$ are reachable from index $0$. If $i > \text{max\_reach}$, index $i$ and all subsequent indices are disconnected from index $0$.

---

## 3. Step-by-Step Worked Execution

### Case 1: Reachable Instance ($[2, 3, 1, 1, 4]$, $N = 5$)
Initialize $\text{max\_reach} = 0$. Target is $N - 1 = 4$.

- **Step 0 ($i = 0, \text{nums}[0] = 2$):**
  - Check: $0 \le \text{max\_reach} = 0$ (Reachable).
  - Update: $\text{max\_reach} = \max(0, 0 + 2) = 2$.
  - State: Can reach any cell up to index 2.
- **Step 1 ($i = 1, \text{nums}[1] = 3$):**
  - Check: $1 \le \text{max\_reach} = 2$ (Reachable).
  - Update: $\text{max\_reach} = \max(2, 1 + 3) = 4$.
  - Target check: $\text{max\_reach} = 4 \ge 4$.
  - **Early Exit:** Destination reached! Return $\text{True}$.

---

### Case 2: Trapped Zero-Barrier Instance ($[3, 2, 1, 0, 4]$, $N = 5$)
Initialize $\text{max\_reach} = 0$. Target is $N - 1 = 4$.

- **Step 0 ($i = 0, \text{nums}[0] = 3$):**
  - $0 \le 0 \implies \text{max\_reach} = \max(0, 0 + 3) = 3$.
- **Step 1 ($i = 1, \text{nums}[1] = 2$):**
  - $1 \le 3 \implies \text{max\_reach} = \max(3, 1 + 2) = 3$.
- **Step 2 ($i = 2, \text{nums}[2] = 1$):**
  - $2 \le 3 \implies \text{max\_reach} = \max(3, 2 + 1) = 3$.
- **Step 3 ($i = 3, \text{nums}[3] = 0$):**
  - $3 \le 3 \implies \text{max\_reach} = \max(3, 3 + 0) = 3$.
- **Step 4 ($i = 4, \text{nums}[4] = 4$):**
  - Check: $i = 4 > \text{max\_reach} = 3$!
  - **Barrier Encountered:** Cannot reach index 4 from prior positions!
  - Return $\text{False}$.

---

## 4. Complete Execution Trace

### Reachable Instance Trace ($[2, 3, 1, 1, 4]$)

| Step $i$ | Value $\text{nums}[i]$ | $i \le \text{max\_reach}$? | Potential Reach ($i + \text{nums}[i]$) | Updated $\text{max\_reach}$ | Target Reached ($\ge 4$)? | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 2 | Yes ($0 \le 0$) | $0 + 2 = 2$ | 2 | No ($2 < 4$) | Advance to $i=1$ |
| 1 | 3 | Yes ($1 \le 2$) | $1 + 3 = 4$ | **4** | **Yes ($4 \ge 4$)** | **Early return True** |

### Trapped Instance Trace ($[3, 2, 1, 0, 4]$)

| Step $i$ | Value $\text{nums}[i]$ | $i \le \text{max\_reach}$? | Potential Reach ($i + \text{nums}[i]$) | Updated $\text{max\_reach}$ | Status |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 3 | Yes ($0 \le 0$) | $0 + 3 = 3$ | 3 | Active |
| 1 | 2 | Yes ($1 \le 3$) | $1 + 2 = 3$ | 3 | Active |
| 2 | 1 | Yes ($2 \le 3$) | $2 + 1 = 3$ | 3 | Active |
| 3 | 0 | Yes ($3 \le 3$) | $3 + 0 = 3$ | 3 | Trapped at zero barrier |
| 4 | 4 | **No ($4 > 3$)** | - | 3 | **Return False** |

---

## 5. Algorithmic Correctness

**Soundness.** If $i \le \text{max\_reach}$, there exists some valid path from index 0 to index $i$. Because any jump from $i$ can reach any index in $[i, i + \text{nums}[i]]$, updating $\text{max\_reach} = \max(\text{max\_reach}, i + \text{nums}[i])$ maintains the exact continuous interval of reachable indices $[0, \text{max\_reach}]$.

**Completeness.** The greedy algorithm halts with $\text{False}$ only when the current index $i$ exceeds $\text{max\_reach}$. Because all previous positions could reach at most $\text{max\_reach} < i$, no possible sequence of jumps could ever cross this gap. The negative verdict is mathematically certain.

---

## 6. Traps This Instance Exposes

- **Zero-Barrier Stagnation:** Having a value of `0` is only problematic if $\text{max\_reach}$ cannot surpass that index. For example, in $[2, 0, 0]$, index 0 can jump over index 1 straight to index 2, so the zero does not trap the runner.
- **Single Element Array:** If $\text{nums} = [0]$ ($N = 1$), you are already at the destination before taking any jumps. The algorithm initializes $\text{max\_reach} = 0 \ge N - 1 = 0$, correctly returning $\text{True}$.
- **Backward Simulation:** Alternatively, one can iterate backwards from $N - 2$ down to $0$, tracking the leftmost index that can reach the current goal. If the final goal index reaches $0$, return $\text{True}$. The forward reachability approach is mathematically equivalent.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = |\text{nums}|$. The loop executes at most $N$ iterations, doing $O(1)$ operations per index.
- **Auxiliary Space Complexity:** $O(1)$ using a single scalar variable $\text{max\_reach}$.