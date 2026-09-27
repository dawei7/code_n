# Guided Example: Minimum Operations to Make the Array Alternating

We analyze and execute the decoupled parity frequency-analysis algorithm on a representative array instance, demonstrating how extracting the top two most frequent elements per parity subsystem resolves value collisions in $O(n)$ time.

- **Input:** `nums = [3, 1, 3, 2, 4, 3]`
- **Output:** `3`

This instance captures even-odd index decoupling, separate frequency histogram compilation, majority candidate selection, and collision arbitration between conflicting parity targets.

---

## 1. Problem Overview & Representative Instance

An array `nums` of length $n$ is defined as **alternating** if:
1. `nums[i] == nums[i + 2]` for all valid $0 \le i \le n - 3$.
2. `nums[i] != nums[i + 1]` for all valid $0 \le i \le n - 2$.

In words, all even indices must share a single uniform value $e$, all odd indices must share a single uniform value $o$, and the two target values must be strictly distinct ($e \ne o$).

In one operation, we may change any element to any arbitrary positive integer. To minimize the total operations required to make `nums` alternating, we must maximize the number of existing elements that remain unchanged.

In our representative instance:
- `nums = [3, 1, 3, 2, 4, 3]` of length $n = 6$.
- Even indices $\{0, 2, 4\}$ contain elements $[3, 3, 4]$.
- Odd indices $\{1, 3, 5\}$ contain elements $[1, 2, 3]$.
- Preserving target $e = 3$ at evens retains $2$ elements ($nums[0]$ and $nums[2]$).
- Preserving target $o = 1$ at odds retains $1$ element ($nums[1]$).
- Because $3 \ne 1$, this choice is valid, preserving $2 + 1 = 3$ elements and changing the remaining $6 - 3 = 3$ elements.

---

## 2. Mathematical & Algorithmic Principles

### Decoupling and Frequency Maximization

Let $E$ denote the multiset of values at even indices, and $O$ denote the multiset of values at odd indices:
$$|E| = \lceil n / 2 \rceil, \quad |O| = \lfloor n / 2 \rfloor$$

If we choose target values $e \in E$ and $o \in O$ with $e \ne o$:
- The number of operations required at even positions is $|E| - \text{freq}_E(e)$.
- The number of operations required at odd positions is $|O| - \text{freq}_O(o)$.
- Total operations:
  $$\text{ops}(e, o) = (|E| - \text{freq}_E(e)) + (|O| - \text{freq}_O(o)) = n - (\text{freq}_E(e) + \text{freq}_O(o))$$

Minimizing total operations is mathematically equivalent to maximizing the sum of preserved frequencies:
$$\max_{\substack{e, o \\ e \ne o}} \left( \text{freq}_E(e) + \text{freq}_O(o) \right)$$

### The Sufficiency of Top-2 Candidates per Parity

Because the only constraint coupling $e$ and $o$ is $e \ne o$, we only need to inspect at most the two highest-frequency elements from each subsystem:
- Let $(e_1, c_{e1})$ and $(e_2, c_{e2})$ be the most frequent and second-most frequent values in $E$.
- Let $(o_1, c_{o1})$ and $(o_2, c_{o2})$ be the most frequent and second-most frequent values in $O$.

Two mutually exclusive cases arise:
1. **Disjoint Champions ($e_1 \ne o_1$):**
   The global optimum is immediately achieved by picking both primary champions:
   $$\text{Preserved}_{\max} = c_{e1} + c_{o1}$$
2. **Conflicting Champions ($e_1 = o_1$):**
   We cannot assign the same value to both even and odd indices. The optimal choice must compromise on either the even parity or the odd parity by falling back to its second runner-up:
   $$\text{Preserved}_{\max} = \max\left( c_{e1} + c_{o2}, \; c_{e2} + c_{o1} \right)$$

Any third-place candidate would have a frequency less than or equal to the second-place candidate, so evaluating beyond the top two candidates is provably unnecessary.

| Candidate Metric | Description | Role in Decision Boundary |
|---|---|---|
| Even Leader $(e_1, c_{e1})$ | Dominant element and count in even subsystem | First choice for even positions |
| Even Runner-Up $(e_2, c_{e2})$ | Second most frequent element in even subsystem | Fallback when $e_1 = o_1$ |
| Odd Leader $(o_1, c_{o1})$ | Dominant element and count in odd subsystem | First choice for odd positions |
| Odd Runner-Up $(o_2, c_{o2})$ | Second most frequent element in odd subsystem | Fallback when $o_1 = e_1$ |
| Conflict Flag | $e_1 == o_1$ | Determines if runner-up arbitration is triggered |

```mermaid
accTitle: Parity Decision Tree
accDescr: Decision diagram showing top-1 comparison and fallback to runner-ups when values collide.
flowchart TD
    Start["Extract Top-2 from Evens: (e1, c_e1), (e2, c_e2)<br/>Extract Top-2 from Odds: (o1, c_o1), (o2, c_o2)"] --> Check{"e1 == o1?"}
    Check -- "No (Disjoint)" --> Opt1["Preserve: c_e1 + c_o1<br/>Ops = n - (c_e1 + c_o1)"]
    Check -- "Yes (Collision)" --> Opt2["Evaluate Candidates:<br/>Option A: e1 + o2 => c_e1 + c_o2<br/>Option B: e2 + o1 => c_e2 + c_o1"]
    Opt2 --> Best["Preserve: max(c_e1 + c_o2, c_e2 + c_o1)<br/>Ops = n - max(...)"]
```

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace `nums = [3, 1, 3, 2, 4, 3]` ($n = 6$).

### Step 1: Separate Index Partitions
- **Even Subsystem ($i \in \{0, 2, 4\}$):**
  - Values: `nums[0] = 3`, `nums[2] = 3`, `nums[4] = 4`.
  - Total even positions $|E| = 3$.
- **Odd Subsystem ($i \in \{1, 3, 5\}$):**
  - Values: `nums[1] = 1`, `nums[3] = 2`, `nums[5] = 3`.
  - Total odd positions $|O| = 3$.

### Step 2: Build Frequency Tables and Extract Top-2
- **Even Frequencies:**
  - Count of `3`: $2$.
  - Count of `4`: $1$.
  - Sorting by count:
    - Primary candidate: $e_1 = 3$ with count $c_{e1} = 2$.
    - Secondary candidate: $e_2 = 4$ with count $c_{e2} = 1$.
- **Odd Frequencies:**
  - Count of `1`: $1$.
  - Count of `2`: $1$.
  - Count of `3`: $1$.
  - Top two candidates (order among equals is arbitrary):
    - Primary candidate: $o_1 = 1$ with count $c_{o1} = 1$.
    - Secondary candidate: $o_2 = 2$ with count $c_{o2} = 1$ (or $3$ with count $1$).

### Step 3: Test Collision Condition
- Compare primary leaders: $e_1 = 3$ and $o_1 = 1$.
- Check: $e_1 \ne o_1$ ($3 \ne 1$).
- Collision is absent! Both primary champions can be selected simultaneously without violating the alternating rule ($3 \ne 1$).

### Step 4: Compute Preserved Count & Operation Total
- Total preserved elements:
  $$\text{Preserved} = c_{e1} + c_{o1} = 2 + 1 = 3$$
- Required operations:
  $$\text{operations} = n - \text{Preserved} = 6 - 3 = 3$$
- Modified array structure:
  - Even positions become $3$: $[nums[0]=3, nums[2]=3, nums[4]=3]$ (1 change: $nums[4]$ from $4 \to 3$).
  - Odd positions become $1$: $[nums[1]=1, nums[3]=1, nums[5]=1]$ (2 changes: $nums[3]$ from $2 \to 1$, $nums[5]$ from $3 \to 1$).
  - Target alternating sequence: `[3, 1, 3, 1, 3, 1]`.
  - Total replacements: $1 + 2 = 3$.

---

## 4. Comprehensive State Trace

The full tabular trace across both parity groups and candidate selection is recorded below:

| Subsystem | Indexed Values | Frequency Histogram | Best Candidate $(k_1, v_1)$ | Runner-Up $(k_2, v_2)$ |
|---|---|---|---|---|
| Even ($i = 0, 2, 4$) | $[3, 3, 4]$ | $\{3: 2, 4: 1\}$ | $(3, 2)$ | $(4, 1)$ |
| Odd ($i = 1, 3, 5$) | $[1, 2, 3]$ | $\{1: 1, 2: 1, 3: 1\}$ | $(1, 1)$ | $(2, 1)$ |

### Collision & Pairing Evaluation Matrix

| Pair Configuration | Even Choice $e$ | Odd Choice $o$ | Validity ($e \ne o$) | Preserved Count | Total Operations ($6 - \text{Preserved}$) | Selection Status |
|---|---|---|---|---|---|---|
| $(e_1, o_1)$ | 3 | 1 | Valid ($3 \ne 1$) | $2 + 1 = 3$ | $6 - 3 = 3$ | **Optimal Chosen** |
| $(e_1, o_2)$ | 3 | 2 | Valid ($3 \ne 2$) | $2 + 1 = 3$ | $6 - 3 = 3$ | Tied Optimal |
| $(e_2, o_1)$ | 4 | 1 | Valid ($4 \ne 1$) | $1 + 1 = 2$ | $6 - 2 = 4$ | Suboptimal |
| $(e_2, o_2)$ | 4 | 2 | Valid ($4 \ne 2$) | $1 + 1 = 2$ | $6 - 2 = 4$ | Suboptimal |

---

## 5. Algorithmic Correctness & Soundness

### Proof of Sufficiency for Top-Two Candidates
Suppose the optimal solution chooses value $e^*$ for even positions and $o^*$ for odd positions.
- If $e_1 \ne o_1$, then $\text{freq}_E(e^*) \le c_{e1}$ and $\text{freq}_O(o^*) \le c_{o1}$ for all candidates, so $c_{e1} + c_{o1}$ is an upper bound on any pair. Because $e_1 \ne o_1$ is valid, $(e_1, o_1)$ achieves this bound and is globally optimal.
- If $e_1 = o_1 = v$, then any valid pair cannot pick both $e^* = v$ and $o^* = v$.
  - If $e^* = v$, then $o^* \ne v$, so $\text{freq}_O(o^*) \le c_{o2}$. The best achievable sum with $e^* = v$ is $c_{e1} + c_{o2}$.
  - If $o^* = v$, then $e^* \ne v$, so $\text{freq}_E(e^*) \le c_{e2}$. The best achievable sum with $o^* = v$ is $c_{e2} + c_{o1}$.
  - If neither equals $v$, then $\text{freq}_E(e^*) + \text{freq}_O(o^*) \le c_{e2} + c_{o2} \le \max(c_{e1} + c_{o2}, c_{e2} + c_{o1})$.
Thus, checking only $(e_1, o_2)$ and $(e_2, o_1)$ strictly covers the entire space of valid assignments.

---

## 6. Edge Cases & Anti-Patterns

### Boundary Scenarios

1. **Single Element Array ($n = 1$):**
   - E.g., `nums = [5]`.
   - Even parity has $[5]$ (count 1), odd parity is empty.
   - Operations: $1 - (1 + 0) = 0$. Already alternating.
2. **Two Identical Elements ($n = 2, nums = [2, 2]$):**
   - $e_1 = 2 (cnt 1)$, $o_1 = 2 (cnt 1)$. Collision occurs ($e_1 = o_1 = 2$).
   - Runner-ups have count $0$: $c_{e2} = 0, c_{o2} = 0$.
   - $\max(1 + 0, 0 + 1) = 1$. Total operations: $2 - 1 = 1$. Change one $2$ to any other integer (e.g. $[2, 1]$).
3. **Monolithic Uniform Array ($nums = [1, 1, 1, 1]$):**
   - All elements identical. Collision $e_1 = o_1 = 1$ with $c_{e1} = 2, c_{o1} = 2$.
   - Fallbacks have count $0$.
   - Preserved: $\max(2 + 0, 0 + 2) = 2$. Operations: $4 - 2 = 2$. Half of the array is changed.
4. **All Elements Distinct:**
   - Every element has count $1$. Any valid pairing with $e_1 \ne o_1$ preserves $1 + 1 = 2$ elements, requiring $n - 2$ operations.

### Common Pitfalls to Avoid

- **Global Mode Selection:** Finding the most frequent element across the entire array and assigning it to either parity is an anti-pattern. An element might be frequent in both parities, or only concentrated in one. Parities must be counted completely independently.
- **Ignoring the Collision Case ($e_1 == o_1$):** Assuming $e_1$ and $o_1$ can always be combined leads to invalid alternating arrays where $nums[i] == nums[i+1]$.
- **Over-inspecting Beyond Top-2:** Scanning all pairs of distinct values across parities takes $O(U^2)$ time where $U$ is distinct values. Keeping only top-2 per parity guarantees $O(1)$ arbitration.

---

## 7. Complexity Analysis

- **Time Complexity:** $O(n)$. Splitting `nums` into even and odd indices takes $O(n)$ time. Building the frequency maps takes $O(n)$ time. Finding the top-2 elements in each map takes $O(U)$ where $U \le n$ is the number of distinct elements. Arbitrating the final candidate pairs takes $O(1)$ arithmetic comparisons. The overall runtime is strictly linear $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Storing the frequency hash maps requires at most $O(n)$ auxiliary space to store counts of up to $n$ distinct integer keys. No recursive call stack or secondary arrays are required.
