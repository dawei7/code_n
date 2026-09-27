# Guided Example: Container With Most Water

We trace the step-by-step execution of the optimal two-pointer shrinkage method on a representative instance:

- **Input:** $\text{height} = [1, 8, 6, 2, 5, 4, 8, 3, 7]$
- **Required output:** $49$

This instance demonstrates how starting from the maximum possible width and systematically shrinking inward using height dominance eliminates suboptimal configurations without evaluating all $O(N^2)$ candidate pairs.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{height}$ of length $N = 9$, each index represents a vertical line of height $\text{height}[i]$ at coordinate $(i, 0)$.

A container formed by two lines at indices $l$ and $r$ with $l < r$ has:
- **Width:** $r - l$
- **Effective Height:** $\min(\text{height}[l], \text{height}[r])$
- **Water Capacity (Area):**
  $$
  A(l, r) = (r - l) \cdot \min(\text{height}[l], \text{height}[r])
  $$

The objective is to find the pair $(l, r)$ that maximizes $A(l, r)$.

For $\text{height} = [1, 8, 6, 2, 5, 4, 8, 3, 7]$, the optimal container is bounded by index $l = 1$ ($\text{height}[1] = 8$) and index $r = 8$ ($\text{height}[8] = 7$):
$$
\text{Area} = (8 - 1) \cdot \min(8, 7) = 7 \cdot 7 = 49
$$

---

## 2. Conceptual Foundation & Invariants

### The Monotone Elimination Argument

Evaluating all $\frac{N(N-1)}{2}$ pairs takes $O(N^2)$ time. To achieve $O(N)$, we exploit a key geometric property:

Suppose we currently consider the interval $[l, r]$ with $\text{height}[l] < \text{height}[r]$.
The area is $(r - l) \cdot \text{height}[l]$.

Now consider pairing index $l$ with any other inner index $k$ such that $l < k < r$:
1. The width is strictly smaller: $k - l < r - l$.
2. The height is at most $\text{height}[l]$:
   $$
   \min(\text{height}[l], \text{height}[k]) \le \text{height}[l]
   $$
3. Therefore, the area for any pair $(l, k)$ is strictly bounded:
   $$
   A(l, k) = (k - l) \cdot \min(\text{height}[l], \text{height}[k]) < (r - l) \cdot \text{height}[l] = A(l, r)
   $$

**Crucial Deduction:** Index $l$ can *never* form a larger container with any remaining candidate inside $(l, r)$ than it already does with $r$. Thus, index $l$ can be permanently discarded!

Symmetrically, if $\text{height}[r] < \text{height}[l]$, all pairs $(k, r)$ with $l < k < r$ are strictly inferior to $(l, r)$, so index $r$ can be permanently discarded.

> **Invariant.** At every step, the optimal container either has been evaluated or lies entirely within the active subarray $[l, r]$. Discarding the pointer pointing to the shorter vertical line never eliminates the global optimum.

---

## 3. Step-by-Step Worked Execution

We initialize pointers at the extreme ends: $l = 0$ and $r = 8$, maintaining $\text{max\_area} = 0$.

### Step 1: Evaluate $l=0, r=8$
- Left height: $\text{height}[0] = 1$.
- Right height: $\text{height}[8] = 7$.
- Width: $8 - 0 = 8$.
- Area: $8 \cdot \min(1, 7) = 8 \cdot 1 = 8$.
- Update $\text{max\_area} = \max(0, 8) = 8$.
- **Decision:** Since $\text{height}[0] = 1 < \text{height}[8] = 7$, discard index $0$. Advance left pointer: $l \leftarrow 1$.

### Step 2: Evaluate $l=1, r=8$
- Left height: $\text{height}[1] = 8$.
- Right height: $\text{height}[8] = 7$.
- Width: $8 - 1 = 7$.
- Area: $7 \cdot \min(8, 7) = 7 \cdot 7 = 49$.
- Update $\text{max\_area} = \max(8, 49) = 49$.
- **Decision:** Since $\text{height}[8] = 7 < \text{height}[1] = 8$, discard index $8$. Decrement right pointer: $r \leftarrow 7$.

### Step 3: Evaluate $l=1, r=7$
- Left height: $\text{height}[1] = 8$.
- Right height: $\text{height}[7] = 3$.
- Width: $7 - 1 = 6$.
- Area: $6 \cdot \min(8, 3) = 6 \cdot 3 = 18$.
- Max area remains $49$.
- **Decision:** Since $\text{height}[7] = 3 < \text{height}[1] = 8$, discard index $7$. Decrement right pointer: $r \leftarrow 6$.

### Step 4: Evaluate $l=1, r=6$
- Left height: $\text{height}[1] = 8$.
- Right height: $\text{height}[6] = 8$.
- Width: $6 - 1 = 5$.
- Area: $5 \cdot \min(8, 8) = 5 \cdot 8 = 40$.
- Max area remains $49$.
- **Decision:** $\text{height}[1] = \text{height}[6] = 8$. Either pointer may be moved without losing optimality; decrement right pointer: $r \leftarrow 5$.

### Step 5: Evaluate $l=1, r=5$
- Left height: $\text{height}[1] = 8$.
- Right height: $\text{height}[5] = 4$.
- Width: $5 - 1 = 4$.
- Area: $4 \cdot \min(8, 4) = 4 \cdot 4 = 16$.
- **Decision:** Discard index $5$. Decrement: $r \leftarrow 4$.

### Step 6: Evaluate $l=1, r=4$
- Left height: $\text{height}[1] = 8$.
- Right height: $\text{height}[4] = 5$.
- Width: $4 - 1 = 3$.
- Area: $3 \cdot \min(8, 5) = 3 \cdot 5 = 15$.
- **Decision:** Discard index $4$. Decrement: $r \leftarrow 3$.

### Step 7: Evaluate $l=1, r=3$
- Left height: $\text{height}[1] = 8$.
- Right height: $\text{height}[3] = 2$.
- Width: $3 - 1 = 2$.
- Area: $2 \cdot \min(8, 2) = 2 \cdot 2 = 4$.
- **Decision:** Discard index $3$. Decrement: $r \leftarrow 2$.

### Step 8: Evaluate $l=1, r=2$
- Left height: $\text{height}[1] = 8$.
- Right height: $\text{height}[2] = 6$.
- Width: $2 - 1 = 1$.
- Area: $1 \cdot \min(8, 6) = 1 \cdot 6 = 6$.
- **Decision:** Discard index $2$. Decrement: $r \leftarrow 1$.

### Termination
Pointers meet at $l = r = 1$. The search terminates with $\text{max\_area} = 49$.

---

## 4. Complete Execution Trace

| Step | Left $l$ | Right $r$ | $\text{height}[l]$ | $\text{height}[r]$ | Width $(r-l)$ | Effective Height | Area Computed | Max Area So Far | Pointer Shift | Mathematical Justification |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 0 | 8 | 1 | 7 | 8 | 1 | $8 \cdot 1 = 8$ | 8 | $l \leftarrow 1$ | $\text{height}[0] < \text{height}[8]$; any pair $(0, k)$ has area $< 8$ |
| 2 | 1 | 8 | 8 | 7 | 7 | 7 | $7 \cdot 7 = 49$ | **49** | $r \leftarrow 7$ | $\text{height}[8] < \text{height}[1]$; any pair $(k, 8)$ has area $< 49$ |
| 3 | 1 | 7 | 8 | 3 | 6 | 3 | $6 \cdot 3 = 18$ | 49 | $r \leftarrow 6$ | $\text{height}[7] < \text{height}[1]$; any pair $(k, 7)$ has area $< 18$ |
| 4 | 1 | 6 | 8 | 8 | 5 | 8 | $5 \cdot 8 = 40$ | 49 | $r \leftarrow 5$ | Equal heights; neither side can pair with a wider inner line |
| 5 | 1 | 5 | 8 | 4 | 4 | 4 | $4 \cdot 4 = 16$ | 49 | $r \leftarrow 4$ | $\text{height}[5] < \text{height}[1]$; any pair $(k, 5)$ has area $< 16$ |
| 6 | 1 | 4 | 8 | 5 | 3 | 5 | $3 \cdot 5 = 15$ | 49 | $r \leftarrow 3$ | $\text{height}[4] < \text{height}[1]$; any pair $(k, 4)$ has area $< 15$ |
| 7 | 1 | 3 | 8 | 2 | 2 | 2 | $2 \cdot 2 = 4$ | 49 | $r \leftarrow 2$ | $\text{height}[3] < \text{height}[1]$; any pair $(k, 3)$ has area $< 4$ |
| 8 | 1 | 2 | 8 | 6 | 1 | 6 | $1 \cdot 6 = 6$ | 49 | $r \leftarrow 1$ | $\text{height}[2] < \text{height}[1]$; any pair $(k, 2)$ has area $< 6$ |

---

## 5. Algorithmic Correctness

**Soundness.** Every computed area corresponds to a valid pair of indices $(l, r)$ evaluating the exact physical capacity formula $(r-l) \cdot \min(\text{height}[l], \text{height}[r])$. Thus, the returned maximum is achievable by a real pair of lines.

**Completeness.** At each iteration where $\text{height}[l] < \text{height}[r]$, we prove that all uninspected pairs $(l, k)$ for $l < k < r$ have capacity strictly smaller than $(l, r)$. Symmetrically, when $\text{height}[r] < \text{height}[l]$, all pairs $(k, r)$ have capacity strictly smaller than $(l, r)$. Because the discarded lines cannot participate in any pair strictly better than the current maximum, the global maximum is never discarded.

---

## 6. Traps This Instance Exposes

- **Moving the Taller Line:** A common pitfall is greedily moving the taller line in hopes of finding an even taller line inward. Because width decreases monotonically with every step, moving the taller line can only reduce or preserve the limiting height, guaranteeing a smaller area. Only moving the shorter line offers any chance of an increased minimum height that compensates for the lost width.
- **Equal Heights Case:** When $\text{height}[l] = \text{height}[r]$, moving either pointer (or both) is sound, because any inner container formed with one of these lines would have strictly smaller width and a height bounded by that line's height.
- **Premature Termination:** One cannot stop when the area decreases; area fluctuations are non-monotonic because tall lines may exist deeper inside the array.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in $\text{height}$. Initially $r - l = N - 1$. Each iteration advances $l$ or decrements $r$ by exactly $1$, terminating in exactly $N - 1$ steps.
- **Auxiliary Space Complexity:** $O(1)$. Pointers $l$, $r$, and scalar accumulator $\text{max\_area}$ require constant memory without dynamic allocations.
