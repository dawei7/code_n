# Guided Example: Sort Transformed Array

We trace the step-by-step quadratic parabola convexity analysis ($a > 0$ vs $a \le 0$), two-pointer endpoint comparison ($f(\text{nums}[i])$ vs $f(\text{nums}[j])$), bidirectional array placement (back-filling from $n - 1$ vs front-filling from $0$), and $O(N)$ linear time sorted array construction on representative quadratic instances:

- **Input:** $\text{nums} = [-4, -2, 2, 4], \quad a = 1, \; b = 3, \; c = 5$
- **Required output:** $[3, 9, 15, 33]$
  - Quadratic equation: $f(x) = 1 \cdot x^2 + 3x + 5$
  - Since $a = 1 > 0$, the parabola opens upward (convex):
    - Maximum values reside at the outer extremities
    - We compare outer endpoints and fill `ans` backwards from index $n - 1$ down to $0$
  - Evaluation steps:
    - Compare $f(-4) = 9$ and $f(4) = 33 \implies$ place $33$ at index 3, retreat right pointer
    - Compare $f(-4) = 9$ and $f(2) = 15 \implies$ place $15$ at index 2, retreat right pointer
    - Compare $f(-4) = 9$ and $f(-2) = 3 \implies$ place $9$ at index 1, advance left pointer
    - Place remaining $f(-2) = 3$ at index 0
  - Final sorted array: $[3, 9, 15, 33]$
- **Concave Parabola ($a < 0$):** $f(x) = -x^2$. Parabola opens downward $\implies$ minimum values reside at endpoints $\implies$ fill `ans` forwards from index $0$ up to $n - 1$
- **Linear Function ($a = 0$):** $f(x) = bx + c$. Monotonic line $\implies$ grouped under $a \le 0$ front-fill logic

This instance demonstrates exploiting mathematical curvature in sorted arrays, proves why two-pointer endpoint convergence guarantees non-decreasing order in strictly $O(N)$ linear time without general sorting algorithms, and analyzes memory bounds.

---

## 1. Instance & Teaching Goal

Given a sorted integer array $\text{nums} = [-4, -2, 2, 4]$ and quadratic coefficients $a = 1, b = 3, c = 5$:
Transform each element via $f(x) = ax^2 + bx + c$ and return the transformed values in sorted order in **$O(N)$ time**:

```text
Transformation: f(x) = x^2 + 3x + 5
Input: [-4, -2, 2, 4]

Transformed Values:
f(-4) = 16 - 12 + 5 = 9
f(-2) =  4 -  6 + 5 = 3
f(2)  =  4 +  6 + 5 = 15
f(4)  = 16 + 12 + 5 = 33

Raw output: [9, 3, 15, 33] (Unsorted!)
Sorted target: [3, 9, 15, 33]
```

### The Curvature Principle of Parabolas
For any parabola $f(x) = ax^2 + bx + c$ on a closed interval $[x_L, x_R]$:
1. **Case $a > 0$ (Convex / Opens Upward):**
   The vertex is a minimum. The **maximum** of $f(x)$ over $[x_L, x_R]$ must occur at one of the two boundaries: $x_L$ or $x_R$.
   We can repeatedly extract the global maximum from the endpoints and place it at the **back** of the output array (`ans[n - k - 1]`).
2. **Case $a \le 0$ (Concave / Opens Downward or Line):**
   The vertex is a maximum (or monotone if $a = 0$). The **minimum** of $f(x)$ over $[x_L, x_R]$ must occur at $x_L$ or $x_R$.
   We can repeatedly extract the global minimum from the endpoints and place it at the **front** of the output array (`ans[k]`).

---

## 2. Conceptual Foundation & Invariants

### 1. Pointer Setup:
Initialize:
$$
i = 0, \quad j = n - 1, \quad ans = [0] \times n
$$

### 2. Decision Logic per Iteration $k \in [0 \dots n - 1]$:
Evaluate endpoint values:
$$
y_1 = f(\text{nums}[i]), \quad y_2 = f(\text{nums}[j])
$$
- **If $a > 0$ (Fill from Back at Index $n - k - 1$):**
  - If $y_1 > y_2$: $ans[n - k - 1] \leftarrow y_1, \; i \leftarrow i + 1$
  - Else: $ans[n - k - 1] \leftarrow y_2, \; j \leftarrow j - 1$
- **If $a \le 0$ (Fill from Front at Index $k$):**
  - If $y_1 > y_2$: $ans[k] \leftarrow y_2, \; j \leftarrow j - 1$
  - Else: $ans[k] \leftarrow y_1, \; i \leftarrow i + 1$

> **Invariant.** At iteration $k$, the unprocessed elements $\text{nums}[i \dots j]$ contain all remaining values, and their extreme value (max if $a > 0$, min if $a \le 0$) is always $\max(y_1, y_2)$ or $\min(y_1, y_2)$.

---

## 3. Step-by-Step Worked Execution

We trace $\text{nums} = [-4, -2, 2, 4]$ with $a = 1, b = 3, c = 5$:
Parabola opens upward ($a = 1 > 0$); target slots fill from index $3$ down to $0$.

---

### Step 1: Iteration $k = 0$ (Target Slot: $n - 1 - 0 = 3$)
- Pointers: $i = 0, j = 3$.
- Evaluate endpoints:
  $$
  y_1 = f(\text{nums}[0]) = f(-4) = (-4)^2 + 3(-4) + 5 = 16 - 12 + 5 = \mathbf{9}
  $$
  $$
  y_2 = f(\text{nums}[3]) = f(4) = 4^2 + 3(4) + 5 = 16 + 12 + 5 = \mathbf{33}
  $$
- Compare: $y_1 > y_2 \iff 9 > 33$ (**False**).
- Selection: $y_2 = 33$ is larger!
  - Write to back: $ans[3] \leftarrow 33$.
  - Retreat right pointer: $j \leftarrow 3 - 1 = 2$.
- Array state: $[0, 0, 0, \mathbf{33}]$.

---

### Step 2: Iteration $k = 1$ (Target Slot: $n - 1 - 1 = 2$)
- Pointers: $i = 0, j = 2$.
- Evaluate endpoints:
  $$
  y_1 = f(\text{nums}[0]) = f(-4) = \mathbf{9}
  $$
  $$
  y_2 = f(\text{nums}[2]) = f(2) = 2^2 + 3(2) + 5 = 4 + 6 + 5 = \mathbf{15}
  $$
- Compare: $9 > 15$ (**False**).
- Selection: $y_2 = 15$ is larger!
  - Write: $ans[2] \leftarrow 15$.
  - Retreat right pointer: $j \leftarrow 2 - 1 = 1$.
- Array state: $[0, 0, \mathbf{15}, 33]$.

---

### Step 3: Iteration $k = 2$ (Target Slot: $n - 1 - 2 = 1$)
- Pointers: $i = 0, j = 1$.
- Evaluate endpoints:
  $$
  y_1 = f(\text{nums}[0]) = f(-4) = \mathbf{9}
  $$
  $$
  y_2 = f(\text{nums}[1]) = f(-2) = (-2)^2 + 3(-2) + 5 = 4 - 6 + 5 = \mathbf{3}
  $$
- Compare: $9 > 3$ (**True**).
- Selection: $y_1 = 9$ is larger!
  - Write: $ans[1] \leftarrow 9$.
  - Advance left pointer: $i \leftarrow 0 + 1 = 1$.
- Array state: $[0, \mathbf{9}, 15, 33]$.

---

### Step 4: Iteration $k = 3$ (Target Slot: $n - 1 - 3 = 0$)
- Pointers: $i = 1, j = 1$.
- Only one element remains: $\text{nums}[1] = -2$.
  $$
  y_1 = y_2 = f(-2) = \mathbf{3}
  $$
- Write to remaining slot: $ans[0] \leftarrow 3$.
- Array state: $[\mathbf{3}, 9, 15, 33]$.

---

### Step 5: Termination
All $n = 4$ positions filled. Return:
$$
\mathbf{[3, 9, 15, 33]}
$$

---

## 4. Complete Execution Trace

```text
nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5 (a > 0: fill from back)
f(x) = x^2 + 3x + 5

k = 0 (slot 3): i=0 (x=-4, y1=9),  j=3 (x=4,  y2=33) -> y2>y1 -> ans[3]=33, j=2
k = 1 (slot 2): i=0 (x=-4, y1=9),  j=2 (x=2,  y2=15) -> y2>y1 -> ans[2]=15, j=1
k = 2 (slot 1): i=0 (x=-4, y1=9),  j=1 (x=-2, y2=3)  -> y1>y2 -> ans[1]=9,  i=1
k = 3 (slot 0): i=1 (x=-2, y1=3),  j=1 (x=-2, y2=3)  -> y2>=y1-> ans[0]=3,  j=0

Final Sorted Array: [3, 9, 15, 33]
```

| Iteration $k$ | Left Index $i$ | Right Index $j$ | $y_1 = f(\text{nums}[i])$ | $y_2 = f(\text{nums}[j])$ | Dominant Value | Target Slot | Updated `ans` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0 | 3 | 9 | 33 | $y_2 = 33$ | 3 | `[0, 0, 0, 33]` |
| 1 | 0 | 2 | 9 | 15 | $y_2 = 15$ | 2 | `[0, 0, 15, 33]` |
| 2 | 0 | 1 | 9 | 3 | $y_1 = 9$ | 1 | `[0, 9, 15, 33]` |
| **3** | **1** | **1** | **3** | **3** | **$y_2 = 3$** | **0** | **`[3, 9, 15, 33]`** |

---

## 5. Algorithmic Correctness

**Soundness.** For $a > 0$, the second derivative $f''(x) = 2a > 0$ is strictly positive, making $f(x)$ strictly convex. By the maximum principle for convex functions on compact intervals, the supremum of $f$ on $[\text{nums}[i], \text{nums}[j]]$ is achieved at either $\text{nums}[i]$ or $\text{nums}[j]$. Selecting $\max(y_1, y_2)$ guarantees that the placed value is greater than or equal to all remaining unprocessed values, producing a strictly non-decreasing array when filled from right to left. By symmetry, for $a \le 0$, concave minimization guarantees non-decreasing order when filled from left to right.

**Completeness.** Each iteration places exactly one element into `ans` and reduces the window size $j - i + 1$ by 1. Exactly $n$ iterations run, placing every transformed value into `ans` without omitting any elements.

---

## 6. Traps This Instance Exposes

- **Filling Direction Inversion:** Placing the maximum at the front when $a > 0$ yields a reverse-sorted (descending) array. Convex parabolas must fill backwards ($n - 1 \to 0$); concave parabolas must fill forwards ($0 \to n - 1$).
- **Quadratic Sorting Overhead:** Transforming the array and calling `.sort()` takes $O(N \log N)$ time, failing the problem's explicit $O(N)$ linear time follow-up.
- **Handling $a = 0$:** When $a = 0$, $f(x) = bx + c$ is linear. Grouping $a = 0$ with $a \le 0$ works cleanly regardless of whether $b$ is positive, negative, or zero.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = \text{len}(nums)$. Exactly $N$ loop iterations are performed. Each iteration computes two quadratic evaluations and updates one array slot in $O(1)$ constant time.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store the returned array `ans`.
