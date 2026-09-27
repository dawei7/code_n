# Guided Example: Minimum Moves to Equal Array Elements

We trace the step-by-step mathematical relative-difference inversion (incrementing $n-1$ elements $\equiv$ decrementing $1$ element), baseline offset summation ($\sum (nums[i] - \min)$), forward operation simulation, and closed-form algebra on representative numeric arrays:

- **Input:** $nums = [1, 2, 3]$
- **Required output:** `3`
  - Array length: $n = 3$
  - Minimum element: $\min(nums) = 1$
  - Inversion reduction:
    - Incrementing $n - 1 = 2$ elements by $1$ changes relative differences identically to **decrementing the remaining 1 element by 1**.
    - To equalize all numbers by decrementing, each element must be reduced to the global minimum $1$:
      $$
      \text{Moves} = (1 - 1) + (2 - 1) + (3 - 1) = 0 + 1 + 2 = \mathbf{3}
    $$
  - Forward simulation of the 3 increments:
    - Start: $[1, 2, 3]$
    - **Move 1 (Increment indices 0 and 1):** $[1+1, 2+1, 3] \implies [2, 3, 3]$
    - **Move 2 (Increment indices 0 and 1):** $[2+1, 3+1, 3] \implies [3, 4, 3]$
    - **Move 3 (Increment indices 0 and 2):** $[3+1, 4, 3+1] \implies [\mathbf{4}, \mathbf{4}, \mathbf{4}]$
    - All elements equal $4$ in exactly $3$ moves.
- **Algebraic Formula:**
  $$
  \text{Moves} = \sum_{i=0}^{n-1} nums[i] - n \times \min(nums) = 6 - 3(1) = \mathbf{3}
  $$
- **Already Equal Elements:** $nums = [1, 1, 1] \implies \sum nums - 3(1) = 3 - 3 = \mathbf{0}$
- **Two Elements:** $nums = [1, 100] \implies 100 - 1 = \mathbf{99}$ moves

This instance demonstrates mathematical symmetry inversion, proves why reducing relative differences to the minimum element is optimal, and derives $O(N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [1, 2, 3]$ of size $n = 3$:
In one move, you can **increment $n - 1$ elements of the array by 1**.
Return the **minimum number of moves** required to make all array elements equal.

```text
Original Array: [ 1,  2,  3 ]

Relative Shift Inversion:
  Incrementing 2 elements is equivalent to Decrementing 1 element!
  Targeting the minimum (1):
    Distance for 1: 1 - 1 = 0 moves
    Distance for 2: 2 - 1 = 1 move
    Distance for 3: 3 - 1 = 2 moves

Total Moves: 0 + 1 + 2 = 3
```

### The Inversion Insight
Simulating increments of $n - 1$ elements directly is complicated because the target equalized value grows dynamically with every operation.
However, consider the **relative differences** between elements:
- Adding $+1$ to all elements except $x$ increases every element relative to $x$ by $+1$.
- Equivalently, subtracting $-1$ from element $x$ while holding all other elements fixed produces the **exact same relative difference**:
  $$
  (a + 1) - (b + 1) = a - b, \quad \text{while } a - (x - 1) = (a - x) + 1
  $$
Since we want to make all elements equal, and we can only reduce elements in the inverted perspective:
The target equal value must be the **minimum element in the original array**, because no element can be decreased below the minimum without extra unnecessary operations.

---

## 2. Conceptual Foundation & Invariants

### 1. Algebraic Derivation of Target Value:
Let $m$ be the total number of moves performed.
In each move, the sum of the array increases by $n - 1$.
After $m$ moves, the final sum of the array is:
$$
\text{Final Sum} = \sum nums + m(n - 1)
$$
At the end, all $n$ elements are equal to some final value $x$:
$$
\text{Final Sum} = n \cdot x
$$
Equating the two expressions:
$$
\sum nums + m(n - 1) = n \cdot x
$$
Notice that the minimum element $\min(nums)$ was incremented in every single move (if it were left out, another element would increase, widening the gap). Thus:
$$
x = \min(nums) + m
$$
Substitute $x$ into the equation:
$$
\sum nums + m(n - 1) = n \cdot (\min(nums) + m)
$$
$$
\sum nums + m \cdot n - m = n \cdot \min(nums) + m \cdot n
$$
Subtract $m \cdot n$ from both sides:
$$
\sum nums - m = n \cdot \min(nums)
$$
Solving for $m$:
$$
m = \sum nums - n \cdot \min(nums)
$$

### 2. Difference Sum Form:
$$
m = \sum_{i=0}^{n-1} (nums[i] - \min(nums))
$$

> **Invariance Principle.** The minimum number of moves is strictly invariant under coordinate shifts and equals the Manhattan distance of all elements to the minimum element.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 2, 3]$ ($n = 3$):

---

### Step 1: Identify Extrema & Array Sum
Scan array once:
- Minimum element: $\min(nums) = \mathbf{1}$.
- Total sum: $\sum nums = 1 + 2 + 3 = \mathbf{6}$.
- Length: $n = \mathbf{3}$.

---

### Step 2: Evaluate Formula
Substitute values into the closed form:
$$
m = \sum nums - n \cdot \min(nums) = 6 - (3 \times 1) = 6 - 3 = \mathbf{3}
$$

---

### Step 3: Forward Verification (Move-by-Move)
Let us verify by explicitly incrementing $n-1 = 2$ elements in each move:
- **Move 0 (Start):**
  $$
  [1, 2, 3] \quad (\min = 1, \max = 3, \text{ spread } = 2)
  $$
- **Move 1 (Increment smallest two: indices 0 and 1):**
  $$
  [1 + 1, 2 + 1, 3] = [2, 3, 3] \quad (\text{spread } = 1)
  $$
- **Move 2 (Increment indices 0 and 1):**
  $$
  [2 + 1, 3 + 1, 3] = [3, 4, 3] \quad (\text{spread } = 1)
  $$
- **Move 3 (Increment indices 0 and 2):**
  $$
  [3 + 1, 4, 3 + 1] = [4, 4, 4] \quad (\text{spread } = 0)
  $$
All 3 elements equal 4.
Moves required: **`3`**.

---

## 4. Complete Execution Trace

| Element $nums[i]$ | Minimum Element $\min$ | Distance to Minimum $nums[i] - \min$ | Cumulative Required Moves |
|:---:|:---:|:---:|:---:|
| $nums[0] = 1$ | $1$ | $1 - 1 = 0$ | $0$ |
| $nums[1] = 2$ | $1$ | $2 - 1 = 1$ | $1$ |
| $nums[2] = 3$ | $1$ | $3 - 1 = 2$ | **$3$** |
| **Formula Result** | — | $\sum nums - n \cdot \min = 6 - 3$ | **$3$** |

---

## 5. Boundary Cases & Failure Modes

- **All Elements Equal ($[5, 5, 5]$):** $\min = 5$, sum $= 15 \implies 15 - 3(5) = \mathbf{0}$.
- **Two Elements ($[1, 10^9]$):** $\min = 1 \implies 10^9 - 1$ moves.
- **Negative Elements ($[-5, -2, 0]$):**
  - $\min = -5$.
  - Distances: $(-5 - (-5)) + (-2 - (-5)) + (0 - (-5)) = 0 + 3 + 5 = \mathbf{8}$.
  - Formula: $\sum nums - n \cdot \min = -7 - 3(-5) = -7 + 15 = \mathbf{8}$.
  - Handles negative numbers without sign distortion.

---

## 6. Traps & Common Anti-Patterns

- **Direct Step Simulation:** Simulating each move by sorting and incrementing $n-1$ elements takes $O(N \cdot m)$ time. Since $m$ can be up to $2 \times 10^9$, this causes catastrophic Time Limit Exceeded. The mathematical formula solves it in a single pass.
- **Integer Overflow in Summation:** The sum $\sum nums$ can exceed 32-bit signed integers ($N \times 10^9 = 10^{14}$). Sums must be accumulated using 64-bit integers (`long long`).
- **Targeting the Maximum or Median:** Increments cannot decrease elements, only raise them; attempting to target the median or maximum requires non-standard operations. Inverting to decrements uniquely identifies the minimum as the sole target.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Finding the minimum element takes $O(N)$ time.
  - Computing the sum of the array takes $O(N)$ time.
  - Total Time: $\mathcal{O}(N)$ in a single pass.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ space using scalar accumulator variables.
