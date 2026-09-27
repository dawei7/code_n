# Guided Example: Teemo Attacking

We trace the step-by-step poison interval overlap resolution, timer reset dynamics ($[t, t + duration - 1]$), pairwise gap evaluation ($\min(duration, b - a)$), terminal attack duration preservation, and total poisoned second summation on representative attack timelines:

- **Input:** $timeSeries = [1, 2], \quad duration = 2$
- **Required output:** `3`
  - Attack sequence: Teemo attacks at seconds $t = 1$ and $t = 2$.
  - Poison duration per attack: $2$ seconds.
  - **Timeline Analysis:**
    - Attack 1 at $t = 1$:
      - Poisons Ashe during seconds $[1, 2]$ (interval length 2).
    - Attack 2 at $t = 2$:
      - Occurs while Ashe is still poisoned at second $2$.
      - Timer resets! Poison extends from second $2$ through second $2 + 2 - 1 = 3$.
      - Poisons Ashe during seconds $[2, 3]$.
    - Union of poisoned intervals:
      $$
      [1, 2] \cup [2, 3] = [1, 3] \implies \{1, 2, 3\}
      $$
    - Total poisoned seconds: $\mathbf{3}$.
- **Pairwise Delta Trace:**
  - Base allocation: Final attack at $t = 2$ runs uninterrupted $\implies ans = duration = 2$
  - Inspect pair $(a = 1, b = 2)$:
    - Time elapsed between attacks: $\Delta t = b - a = 2 - 1 = 1$
    - Since $\Delta t = 1 < duration = 2$, the first attack's effect is cut short after $1$ second.
    - Effective contribution:
      $$
      \min(duration, \; b - a) = \min(2, 1) = \mathbf{1}
      $$
    - Add to total: $ans \leftarrow 2 + 1 = \mathbf{3}$
  - Final result: **`3`**.
- **Separated Attacks Instance ($timeSeries = [1, 4], duration = 2$):**
  - $\Delta t = 4 - 1 = 3 \ge 2 \implies \min(2, 3) = 2$
  - Total duration: $2 + 2 = \mathbf{4}$ (intervals $[1, 2]$ and $[4, 5]$ are completely disjoint)
- **Single Attack Instance ($timeSeries = [5], duration = 10$):**
  - Only one attack $\implies ans = duration = \mathbf{10}$
- **Multiple Overlapping Cascades ($timeSeries = [1, 2, 3, 4, 5], duration = 5$):**
  - Each attack resets the timer after $1$ second until the final attack runs for $5$ seconds $\implies 1 + 1 + 1 + 1 + 5 = \mathbf{9}$ seconds

This instance demonstrates interval union measurement on sorted 1D timelines, mathematically proves why pairwise $\min(duration, b - a)$ accumulation computes exact set unions in a single pass, and derives $O(N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a non-decreasing integer array $timeSeries$ and an integer $duration$:
Teemo attacks at each second $t \in timeSeries$, poisoning the target for the interval $[t, t + duration - 1]$ inclusive.
If a new attack lands while the poison is active, the poison timer resets.
Return the **total number of seconds** the target is poisoned.

```text
Overlapping Attack Timeline (timeSeries = [1, 2], duration = 2):

Second:       1     2     3     4
Attack 1:    [=====]
Attack 2:          [=====]
----------------------------------
Combined:    [===========]
Active at:    t=1,  t=2,  t=3   -> Total 3 seconds
```

### The Continuous Interval Union Principle
Rather than maintaining a set of covered seconds or performing expensive interval merges:
- Every attack $timeSeries[i]$ would normally poison the enemy for $duration$ seconds.
- However, if the next attack arrives at $timeSeries[i+1]$ before $duration$ seconds elapse:
  The first attack is interrupted and only contributes $timeSeries[i+1] - timeSeries[i]$ seconds!
- The final attack has no subsequent attack to interrupt it, so it **always contributes its full $duration$ seconds**.

---

## 2. Conceptual Foundation & Invariants

### 1. The Pairwise Minimum Contribution Formula:
For any two adjacent attack timestamps $a = timeSeries[i]$ and $b = timeSeries[i+1]$:
$$
\text{Contribution of attack } a = \min(duration, \; b - a)
$$
- Case 1 ($b - a \ge duration$): The intervals $[a, a + duration - 1]$ and $[b, b + duration - 1]$ are completely disjoint. Attack $a$ contributes its full $duration$ seconds.
- Case 2 ($b - a < duration$): The intervals overlap. Attack $a$ contributes $b - a$ seconds until attack $b$ resets the clock.

### 2. The Complete Summation Formula:
Let $N = |timeSeries|$:
$$
\text{Total Poisoned Duration} = duration + \sum_{i=0}^{N-2} \min(duration, \; timeSeries[i+1] - timeSeries[i])
$$

> **Overlap Invariant.** Bounding each inter-attack gap by $\min(duration, \Delta t)$ guarantees that every unit of time in $\bigcup [t_i, t_i + duration - 1]$ is counted exactly once without double-counting overlapping seconds.

---

## 3. Step-by-Step Worked Execution

We trace $timeSeries = [1, 2]$ with $duration = 2$:

---

### Step 1: Initialize Accumulator
The final attack at index $N-1$ is never interrupted:
$$
ans = duration = \mathbf{2}
$$

---

### Step 2: Iterate Over Adjacent Pairs
Examine pair $(a, b) = (1, 2)$:
- Compute time delta:
  $$
  \Delta t = b - a = 2 - 1 = \mathbf{1}
  $$
- Compare with $duration = 2$:
  $$
  \text{contribution} = \min(2, 1) = \mathbf{1}
  $$
- Add to accumulator:
  $$
  ans \leftarrow 2 + 1 = \mathbf{3}
  $$

---

### Step 3: Termination
No more pairs remain.
Output: **`3`**.

---

## 4. Complete Execution Trace

| Consecutive Pair $(a, b)$ | Timestamp Gap $\Delta t = b - a$ | Duration Limit | Contribution $\min(duration, \Delta t)$ | Running Poisoned Seconds $ans$ |
|:---:|:---:|:---:|:---:|:---:|
| **Initial (Final Attack)** | — | $2$ | Full duration | $2$ |
| **$(1, 2)$** | $2 - 1 = 1$ | $2$ | $\min(2, 1) = \mathbf{1}$ | $2 + 1 = \mathbf{3}$ |
| **Final Result** | — | — | — | **`3`** |

### Comparison with Disjoint Input $timeSeries = [1, 4], duration = 2$:
| Consecutive Pair $(a, b)$ | Timestamp Gap $\Delta t = b - a$ | Duration Limit | Contribution $\min(duration, \Delta t)$ | Running Poisoned Seconds $ans$ |
|:---:|:---:|:---:|:---:|:---:|
| **Initial (Final Attack)** | — | $2$ | Full duration | $2$ |
| **$(1, 4)$** | $4 - 1 = 3$ | $2$ | $\min(2, 3) = \mathbf{2}$ | $2 + 2 = \mathbf{4}$ |
| **Final Result** | — | — | — | **`4`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Attack ($N = 1$):** Loop over pairs does not execute $\implies$ returns $duration$.
- **Zero Duration ($duration = 0$):** Target is never poisoned $\implies \mathbf{0}$.
- **Simultaneous / Repeated Attacks ($timeSeries = [1, 1, 1]$):** $\Delta t = 0 \implies \min(duration, 0) = 0$, correctly contributing 0 extra seconds for redundant identical timestamps.
- **Large Spacing ($timeSeries = [1, 10^7], duration = 5$):** $10^7 - 1 > 5 \implies 5 + 5 = \mathbf{10}$.

---

## 6. Traps & Common Anti-Patterns

- **Creating an Explicit Set of Covered Seconds:** Adding every integer from $t$ to $t + duration - 1$ into a hash set causes Memory Limit Exceeded for $duration = 10^7$ or $N = 10^4$. The mathematical delta formula computes the answer in $O(1)$ space.
- **Off-by-One in Interval Sizing:** An attack at second 1 with duration 2 covers seconds 1 and 2 (length 2). Treating it as $[1, 1+2] = [1, 3]$ covers 3 seconds, corrupting the calculation.
- **Forgetting the Last Attack:** Forgetting to add $duration$ for the final attack causes the last segment to be completely omitted.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The loop performs a single linear pass over the $N - 1$ adjacent pairs.
  - Each pair evaluates one subtraction and one $\min()$ comparison.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^4$, finishes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ space using a scalar accumulator.
