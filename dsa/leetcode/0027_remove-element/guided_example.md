# Guided Example: Remove Element

We trace the step-by-step two-pointer in-place compaction on a representative array instance:

- **Input:** $\text{nums} = [0, 1, 2, 2, 3, 0, 4, 2]$, $\text{val} = 2$
- **Required output:** $k = 5$ with prefix $[0, 1, 3, 0, 4]$

This instance demonstrates in-place filtering, slow-writer pointer tracking, preserving non-target elements, skipping target elements without shifting remaining values, and array safety invariants.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums}$ of length $N = 8$ and a target value $\text{val} = 2$:
$$
[0, 1, 2, 2, 3, 0, 4, 2]
$$

We must remove all occurrences of $\text{val} = 2$ in place, returning the count $k$ of elements not equal to $\text{val}$. The first $k$ elements of $\text{nums}$ must contain the preserved elements.

A naive approach calls `nums.remove(val)`, which searches for each target value and shifts all subsequent elements left, leading to $O(N^2)$ quadratic overhead. The optimal algorithm scans the array in a single forward pass with a reader pointer and writes valid elements to a compacting writer pointer $k$, achieving $O(N)$ time and $O(1)$ auxiliary space.

---

## 2. Conceptual Foundation & Invariants

### Two-Pointer Roles
- **Fast Reader $i$:** Scans every element $\text{nums}[i]$ from index $0$ to $N - 1$.
- **Slow Writer $k$:** Points to the next index in the prefix that should receive a retained value.

### Compaction Rule
Initialize $k = 0$. For each index $i \in [0, N-1]$:
1. If $\text{nums}[i] \ne \text{val}$:
   - Assign $\text{nums}[k] \leftarrow \text{nums}[i]$.
   - Increment $k \leftarrow k + 1$.
2. If $\text{nums}[i] == \text{val}$:
   - Skip the element. $k$ does not advance.

### In-Place Safety Invariant
At all times, $k \le i$ because $k$ advances at most once per element read. Therefore:
- Writing to $\text{nums}[k]$ can never overwrite an unread element at index $> i$.
- The reader $i$ always operates on intact original array data.

> **Invariant.** After processing index $i$, $\text{nums}[0 \dots k-1]$ contains exactly the elements from $\text{nums}[0 \dots i]$ that are not equal to $\text{val}$, in their original relative order.

---

## 3. Step-by-Step Worked Execution

We process $\text{nums} = [0, 1, 2, 2, 3, 0, 4, 2]$ with $\text{val} = 2$:

### Step 0: Initialization
- Writer pointer: $k = 0$.

---

### Reader Iterations ($i = 0$ to $7$)

- **Index 0 ($i = 0, \text{nums}[0] = 0$):**
  - Compare: $0 \ne 2$ (retained).
  - Write: $\text{nums}[0] \leftarrow 0$.
  - Advance: $k \leftarrow 1$.

- **Index 1 ($i = 1, \text{nums}[1] = 1$):**
  - Compare: $1 \ne 2$ (retained).
  - Write: $\text{nums}[1] \leftarrow 1$.
  - Advance: $k \leftarrow 2$.

- **Index 2 ($i = 2, \text{nums}[2] = 2$):**
  - Compare: $2 == 2$ (target match).
  - Action: Discard/skip element. $k$ remains $2$.

- **Index 3 ($i = 3, \text{nums}[3] = 2$):**
  - Compare: $2 == 2$ (target match).
  - Action: Discard/skip element. $k$ remains $2$.

- **Index 4 ($i = 4, \text{nums}[4] = 3$):**
  - Compare: $3 \ne 2$ (retained).
  - Write: $\text{nums}[2] \leftarrow 3$.
  - Advance: $k \leftarrow 3$.
  - Compacted prefix so far: $[0, 1, 3]$.

- **Index 5 ($i = 5, \text{nums}[5] = 0$):**
  - Compare: $0 \ne 2$ (retained).
  - Write: $\text{nums}[3] \leftarrow 0$.
  - Advance: $k \leftarrow 4$.
  - Compacted prefix so far: $[0, 1, 3, 0]$.

- **Index 6 ($i = 6, \text{nums}[6] = 4$):**
  - Compare: $4 \ne 2$ (retained).
  - Write: $\text{nums}[4] \leftarrow 4$.
  - Advance: $k \leftarrow 5$.
  - Compacted prefix so far: $[0, 1, 3, 0, 4]$.

- **Index 7 ($i = 7, \text{nums}[7] = 2$):**
  - Compare: $2 == 2$ (target match).
  - Action: Discard/skip element. $k$ remains $5$.

### Termination
Array scan complete. Final count of non-target elements is $k = 5$.
The prefix $\text{nums}[0 \dots 4]$ is $[0, 1, 3, 0, 4]$.

---

## 4. Complete Execution Trace

| Fast Reader $i$ | Current Value $\text{nums}[i]$ | Match Condition ($\text{val} = 2$) | Action Performed | Write Pointer $k$ | Modified Prefix $\text{nums}[0 \dots k-1]$ |
|:---:|:---:|:---:|:---|:---:|:---|
| 0 | 0 | $0 \ne 2$ | Write $\text{nums}[0] \leftarrow 0$ | 1 | $[0]$ |
| 1 | 1 | $1 \ne 2$ | Write $\text{nums}[1] \leftarrow 1$ | 2 | $[0, 1]$ |
| 2 | 2 | $2 == 2$ | Target found; skip | 2 | $[0, 1]$ |
| 3 | 2 | $2 == 2$ | Target found; skip | 2 | $[0, 1]$ |
| 4 | 3 | $3 \ne 2$ | Write $\text{nums}[2] \leftarrow 3$ | 3 | $[0, 1, 3]$ |
| 5 | 0 | $0 \ne 2$ | Write $\text{nums}[3] \leftarrow 0$ | 4 | $[0, 1, 3, 0]$ |
| 6 | 4 | $4 \ne 2$ | Write $\text{nums}[4] \leftarrow 4$ | 5 | $[0, 1, 3, 0, 4]$ |
| 7 | 2 | $2 == 2$ | Target found; skip | **5** | $[0, 1, 3, 0, 4]$ |

---

## 5. Algorithmic Correctness

**Soundness.** A value is copied to $\text{nums}[k]$ if and only if $\text{nums}[i] \ne \text{val}$. Therefore, no element equal to $\text{val}$ can ever be written into the prefix $\text{nums}[0 \dots k-1]$. The prefix contains only legitimate, non-target values.

**Completeness.** Reader $i$ systematically inspects every index from $0$ to $N - 1$. Every non-target element is assigned to the next available position $k$. Thus, all valid elements from the input are retained.

---

## 6. Traps This Instance Exposes

- **Overwriting Future Unread Values:** Writing ahead of the read pointer would destroy values before they can be evaluated. Because $k \le i$ is strictly invariant, writes always occur at or behind the reader, preserving data integrity.
- **Values Past $k$:** The problem statement explicitly allows elements past index $k$ to contain arbitrary remaining values. There is no need to clear or zero out indices $\ge k$.
- **Array Containing Only Target Value:** If $\text{nums} = [2, 2, 2]$, the condition $\text{nums}[i] \ne 2$ is never met. The writer pointer never increments, correctly returning $k = 0$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = |\text{nums}|$. The reader pointer visits each of the $N$ elements exactly once, performing constant-time comparisons and assignments.
- **Auxiliary Space Complexity:** $O(1)$. In-place updates require only two scalar index variables ($i$ and $k$).
