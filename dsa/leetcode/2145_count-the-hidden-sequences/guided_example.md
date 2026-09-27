# Guided Example: Count the Hidden Sequences

We analyze and execute the prefix-sum extremum bounding algorithm on a representative problem instance, demonstrating how tracking relative sequence displacement transforms an infinite search space into a closed-form algebraic interval intersection.

- **Input:** `differences = [1, -3, 4]`, `lower = 1`, `upper = 6`
- **Output:** `2`

This instance illustrates relative prefix integration, extremum envelope determination, and calculating the allowable translation slack within target bounds.

---

## 1. Problem Overview & Representative Instance

An unknown integer sequence $\text{hidden}$ of length $n + 1$ satisfies the transition rule:
$$\text{differences}[i] = \text{hidden}[i + 1] - \text{hidden}[i] \quad \text{for each } i \in [0, n - 1]$$

Every value in the sequence must lie within the inclusive interval $[\text{lower}, \text{upper}]$. The initial element $\text{hidden}[0]$ is unconstrained except by this global validity condition. Once $\text{hidden}[0]$ is fixed, the entire sequence is uniquely determined.

We must find the number of distinct valid initial choices for $\text{hidden}[0]$ such that every element of the resulting sequence remains strictly within $[\text{lower}, \text{upper}]$. If no valid initial value exists, we return $0$.

In our representative instance:
- `differences = [1, -3, 4]` ($n = 3$, sequence length $4$).
- Target interval: $[\text{lower}, \text{upper}] = [1, 6]$.
- Allowed target interval capacity: $\text{upper} - \text{lower} = 6 - 1 = 5$.

---

## 2. Mathematical & Algorithmic Principles

### Relative Displacement via Prefix Sums

Let the first element be an arbitrary parameter $x_0 = \text{hidden}[0]$. Express every subsequent element relative to $x_0$:
- $\text{hidden}[0] = x_0$
- $\text{hidden}[1] = x_0 + \text{differences}[0]$
- $\text{hidden}[2] = x_0 + \text{differences}[0] + \text{differences}[1]$
- In general:
$$\text{hidden}[k] = x_0 + P_k \quad \text{where } P_0 = 0 \text{ and } P_k = \sum_{j=0}^{k-1} \text{differences}[j]$$

Here, $P_k$ represents the exact relative displacement of the $k$-th element from the anchor $x_0$.

### The Displacement Envelope

The sequence of displacements $\{P_0, P_1, \dots, P_n\}$ defines a rigid geometric shape that can be translated along the integer line by varying $x_0$. 
Let:
$$P_{\min} = \min_{0 \le k \le n} P_k \quad \text{and} \quad P_{\max} = \max_{0 \le k \le n} P_k$$

Because $P_0 = 0$, we always have $P_{\min} \le 0 \le P_{\max}$.
The total vertical spread (or dynamic range) of the hidden sequence is:
$$\text{Spread} = P_{\max} - P_{\min}$$

### Interval Feasibility Bounds

For every element $\text{hidden}[k]$ to satisfy $\text{lower} \le \text{hidden}[k] \le \text{upper}$:
1. The global minimum element $x_0 + P_{\min}$ must be at least $\text{lower}$:
$$x_0 + P_{\min} \ge \text{lower} \iff x_0 \ge \text{lower} - P_{\min}$$
2. The global maximum element $x_0 + P_{\max}$ must be at most $\text{upper}$:
$$x_0 + P_{\max} \le \text{upper} \iff x_0 \le \text{upper} - P_{\max}$$

Combining these inequalities defines a single contiguous integer interval of valid starting values $x_0$:
$$x_0 \in \left[\text{lower} - P_{\min}, \, \text{upper} - P_{\max}\right]$$

The count of valid integers in an inclusive range $[A, B]$ is $\max(0, B - A + 1)$:
$$\text{Valid Count} = \max\left(0, (\text{upper} - P_{\max}) - (\text{lower} - P_{\min}) + 1\right) = \max\left(0, (\text{upper} - \text{lower}) - (P_{\max} - P_{\min}) + 1\right)$$

| Metric / Parameter | Formal Expression | Concrete Role in Instance |
|---|---|---|
| Prefix Displacement $P_k$ | $\sum_{j=0}^{k-1} \text{differences}[j]$ | Relative position of element $k$ relative to $x_0$ |
| Envelope Minimum $P_{\min}$ | $\min_{k} P_k$ | Deepest relative drop of the sequence below $x_0$ |
| Envelope Maximum $P_{\max}$ | $\max_{k} P_k$ | Highest relative peak of the sequence above $x_0$ |
| Sequence Spread | $P_{\max} - P_{\min}$ | Minimum span needed to contain all sequence values |
| Allowed Capacity | $\text{upper} - \text{lower}$ | Maximum span available between target bounds |
| Slack Count | $\text{Capacity} - \text{Spread} + 1$ | Number of integer shifts fitting the envelope in the target |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace `differences = [1, -3, 4]`, `lower = 1`, `upper = 6`.

```
Prefix integration starting at P[0] = 0:
P[0] = 0
P[1] = 0 + 1 = 1
P[2] = 1 + (-3) = -2
P[3] = -2 + 4 = 2

Envelopes: P_min = -2, P_max = 2
Spread = 2 - (-2) = 4
Allowed Capacity = 6 - 1 = 5
Slack = 5 - 4 = 1  =>  1 + 1 = 2 valid starting values
```

### Step 1: Initialize Prefix Anchor
- Anchor displacement: $P_0 = 0$.
- Running tracking minimum: $P_{\min} = 0$.
- Running tracking maximum: $P_{\max} = 0$.

### Step 2: Integrate Difference $0$ ($\text{differences}[0] = 1$)
- New prefix: $P_1 = P_0 + 1 = 0 + 1 = 1$.
- Update extremum:
  - $P_{\min} = \min(0, 1) = 0$.
  - $P_{\max} = \max(0, 1) = 1$.
- Sequence relative values so far: $\{0, 1\}$.

### Step 3: Integrate Difference $1$ ($\text{differences}[1] = -3$)
- New prefix: $P_2 = P_1 + (-3) = 1 - 3 = -2$.
- Update extremum:
  - $P_{\min} = \min(0, -2) = -2$.
  - $P_{\max} = \max(1, -2) = 1$.
- Sequence relative values so far: $\{0, 1, -2\}$.

### Step 4: Integrate Difference $2$ ($\text{differences}[2] = 4$)
- New prefix: $P_3 = P_2 + 4 = -2 + 4 = 2$.
- Update extremum:
  - $P_{\min} = \min(-2, 2) = -2$.
  - $P_{\max} = \max(1, 2) = 2$.
- Final envelope: $P_{\min} = -2$, $P_{\max} = 2$.

### Step 5: Compute Valid Start Bounds
- Minimum allowable start value:
  $$x_{0,\min} = \text{lower} - P_{\min} = 1 - (-2) = 3$$
- Maximum allowable start value:
  $$x_{0,\max} = \text{upper} - P_{\max} = 6 - 2 = 4$$
- Range of valid $x_0$: $[3, 4]$.
- Number of valid integers: $4 - 3 + 1 = 2$.

Both $x_0 = 3$ and $x_0 = 4$ produce fully valid sequences within $[1, 6]$.

---

## 4. Comprehensive State Trace

The table below catalogs prefix evolution, running envelope expansion, and boundary clamping:

| Step $k$ | Delta $\text{differences}[k-1]$ | Current Prefix $P_k$ | Running $P_{\min}$ | Running $P_{\max}$ | Envelope Spread | Slack vs Window $[1, 6]$ |
|---|---|---|---|---|---|---|
| $0$ (Base) | None | $0$ | $0$ | $0$ | $0$ | $5 - 0 = 5$ |
| $1$ | $+1$ | $+1$ | $0$ | $+1$ | $1$ | $5 - 1 = 4$ |
| $2$ | $-3$ | $-2$ | $-2$ | $+1$ | $3$ | $5 - 3 = 2$ |
| $3$ | $+4$ | $+2$ | $-2$ | $+2$ | $4$ | $5 - 4 = 1$ |

### Explicit Verification of Candidate Sequences

1. **Candidate $x_0 = 3$:**
   - $\text{hidden}[0] = 3$
   - $\text{hidden}[1] = 3 + 1 = 4$
   - $\text{hidden}[2] = 4 - 3 = 1$
   - $\text{hidden}[3] = 1 + 4 = 5$
   - Resulting sequence: $[3, 4, 1, 5]$.
   - Min element: $1 \ge 1$; Max element: $5 \le 6$. **Valid.**
2. **Candidate $x_0 = 4$:**
   - $\text{hidden}[0] = 4$
   - $\text{hidden}[1] = 4 + 1 = 5$
   - $\text{hidden}[2] = 5 - 3 = 2$
   - $\text{hidden}[3] = 2 + 4 = 6$
   - Resulting sequence: $[4, 5, 2, 6]$.
   - Min element: $2 \ge 1$; Max element: $6 \le 6$. **Valid.**
3. **Candidate $x_0 = 2$ (Out of bounds):**
   - $\text{hidden} = [2, 3, 0, 4]$. Element $0 < 1$. **Invalid.**
4. **Candidate $x_0 = 5$ (Out of bounds):**
   - $\text{hidden} = [5, 6, 3, 7]$. Element $7 > 6$. **Invalid.**

The count of valid sequences is strictly $2$.

---

## 5. Algorithmic Correctness & Soundness

### Necessary and Sufficient Interval Boundaries
- **Necessity:** If $x_0 < \text{lower} - P_{\min}$, then $\min_k \text{hidden}[k] = x_0 + P_{\min} < \text{lower}$, violating the lower bound constraint. Similarly, if $x_0 > \text{upper} - P_{\max}$, then $\max_k \text{hidden}[k] = x_0 + P_{\max} > \text{upper}$, violating the upper bound constraint.
- **Sufficiency:** If $\text{lower} - P_{\min} \le x_0 \le \text{upper} - P_{\max}$, then for all $k \in [0, n]$:
  $$\text{hidden}[k] = x_0 + P_k \ge (\text{lower} - P_{\min}) + P_k = \text{lower} + (P_k - P_{\min}) \ge \text{lower}$$
  $$\text{hidden}[k] = x_0 + P_k \le (\text{upper} - P_{\max}) + P_k = \text{upper} - (P_{\max} - P_k) \le \text{upper}$$
  Every element is strictly within bounds.

### Non-Negative Slack Invariant
If $P_{\max} - P_{\min} > \text{upper} - \text{lower}$, the intrinsic spread of the sequence exceeds the target interval width. The term $(\text{upper} - \text{lower}) - (P_{\max} - P_{\min}) + 1$ becomes $\le 0$, and taking $\max(0, \cdot)$ correctly yields $0$ valid sequences.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Spread Exceeds Allowed Capacity:** If `differences = [4, -7, 2]`, `lower = 3`, `upper = 6`:
   - $P = [0, 4, -3, -1] \implies P_{\min} = -3, P_{\max} = 4$.
   - Spread $= 4 - (-3) = 7$. Capacity $= 6 - 3 = 3$.
   - Slack $= 3 - 7 + 1 = -3 \implies \max(0, -3) = 0$.
2. **Single Difference ($n = 1$):** With two elements, $P = [0, \text{diff}[0]]$. Correctly calculates slack between the single step and interval.
3. **All Differences Zero:** Sequence is constant ($P_k = 0$ for all $k$). Spread is $0$. Number of valid choices is $\text{upper} - \text{lower} + 1$.
4. **64-bit Accumulation:** With $n \le 10^5$ and differences up to $\pm 10^5$, cumulative prefix sums can reach $\pm 10^{10}$, exceeding 32-bit signed integer capacity. Prefix variables must use 64-bit integers.

### Common Anti-Patterns
- **Iterating All Possible Starting Values $x_0$:** Testing every integer between $\text{lower}$ and $\text{upper}$ with full simulation takes $O(n \cdot (\text{upper} - \text{lower}))$ time, which times out for ranges of size $10^5 \times 10^5 = 10^{10}$.
- **Reconstructing Full Sequence Array:** Storing the sequence of length $n + 1$ costs $O(n)$ extra memory when only scalar $P_{\min}$ and $P_{\max}$ are needed.
- **Forgetting Anchor $P_0 = 0$:** Omitting $0$ from the extremum calculation ignores the position of the first element $\text{hidden}[0]$ relative to itself, corrupting the envelope.

---

## 7. Complexity Analysis

### Time Complexity
- A single linear scan iterates through the $n$ elements of `differences`.
- In each step:
  - Add $\text{differences}[i]$ to running prefix $P$: $O(1)$.
  - Update $P_{\min}$ and $P_{\max}$: $O(1)$.
- Final closed-form difference evaluation: $O(1)$.
- Total time complexity is strictly $O(n)$, executing in under $3$ milliseconds for $n = 10^5$.

### Auxiliary Space Complexity
- The algorithm tracks three scalar 64-bit numbers: running prefix $P$, minimum $P_{\min}$, and maximum $P_{\max}$.
- No arrays or heap buffers are allocated.
- Total auxiliary space complexity is $O(1)$.
