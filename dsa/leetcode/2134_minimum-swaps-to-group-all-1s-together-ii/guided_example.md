# Guided Example: Minimum Swaps to Group All 1's Together II

We trace the step-by-step execution of the fixed-size circular sliding window approach on a representative problem instance:

- **Input Array (`nums`):** `[0, 1, 0, 1, 1, 0, 0]`
- **Expected Output:** `1`

This instance illustrates how the total number of ones in a binary array rigidly defines the required target window length, proving why minimizing swap operations corresponds bijectively to maximizing the count of existing ones within a circular contiguous window.

---

## 1. Problem Overview & Representative Instance

A swap consists of choosing any two distinct positions in an array and interchanging their values. We are given a circular binary array `nums`. An array is circular if the end of the array wraps around to connect with the beginning. We wish to determine the minimum number of swaps required to group all `1`s together into a single contiguous block anywhere in the circular array.

Consider our representative instance `nums = [0, 1, 0, 1, 1, 0, 0]` with length $n = 7$:
- Count of ones: $k = 3$ (located at indices $1, 3, 4$).
- Any valid contiguous cluster of all ones must occupy a contiguous block of length exactly $k = 3$.
- Looking at window $[2, 4]$ (`[0, 1, 1]`), there are two $1$s and one $0$. Swapping the external $1$ at index $1$ into the gap at index $2$ groups all $1$s into $[2, 4]$ (`[1, 1, 1]`) in exactly $1$ swap.

---

## 2. Mathematical & Algorithmic Principles

### Conservation of Ones and Target Window Invariant
Let $k = \sum_{i=0}^{n-1} \text{nums}[i]$ be the total count of ones in the array.
If all $1$s are gathered into a contiguous block, that block must occupy an interval of length exactly $k$.
For any circular candidate window $W$ of length $k$:
- Let $c_1(W)$ be the number of $1$s currently inside $W$.
- The number of $0$s inside $W$ is $c_0(W) = k - c_1(W)$.
- Because the total number of $1$s in the entire array is $k$, there are exactly $k - c_1(W) = c_0(W)$ ones residing outside window $W$.
- Each external $1$ can be swapped with an internal $0$ in a single swap operation.
- Therefore, the number of swaps to make window $W$ completely filled with ones is:

$$\text{Swaps}(W) = k - c_1(W)$$

### Duality Between Minimum Swaps and Maximum Window Sum
To minimize swaps across all possible window positions, we must maximize the number of $1$s inside the window:

$$\min \text{Swaps} = k - \max_{W, |W| = k} c_1(W)$$

Because the array is circular, candidate windows can wrap around index $n - 1$ to index $0$. We slide a window of fixed length $k$ across all $n$ starting positions $i \in \{0, \dots, n-1\}$, accessing elements via modular indexing $(i + j) \bmod n$ in $\mathcal{O}(n)$ time and $\mathcal{O}(1)$ space.

| Metric | Role in Formulation | Definition / Formula |
|---|---|---|
| Total Ones ($k$) | Fixed length of every candidate target window | $k = \sum_{i=0}^{n-1} \text{nums}[i]$ |
| Window Ones ($c_1$) | Running count of $1$s in current window | $\sum_{j=0}^{k-1} \text{nums}[(i+j)\bmod n]$ |
| Maximum Density ($\mu$) | Maximum number of $1$s captured in any window | $\mu = \max c_1(W)$ |
| Minimum Swaps | Number of foreign $0$s that must be replaced | $k - \mu$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

Input: `nums = [0, 1, 0, 1, 1, 0, 0]`, $n = 7$.

### Phase 1: Total Ones Calculation
Summing all elements in `nums`:

$$k = 0 + 1 + 0 + 1 + 1 + 0 + 0 = 3$$

The target window size is fixed at $k = 3$.

### Phase 2: Initial Window Setup ($i = 0$)
Window covers indices $[0, 1, 2]$: elements $[0, 1, 0]$.
- Current window sum: $c_1 = 0 + 1 + 0 = 1$.
- Running maximum ones: $\mu = 1$.

### Phase 3: Sliding the Window
We advance the window by evicting the outgoing element and introducing the incoming element:

- **Window 1 (start index $1$, range $[1, 3]$):**
  - Outgoing: $\text{nums}[0] = 0$. Incoming: $\text{nums}[3] = 1$.
  - Delta: $c_1 \leftarrow 1 - 0 + 1 = 2$.
  - Update maximum: $\mu = \max(1, 2) = 2$.
- **Window 2 (start index $2$, range $[2, 4]$):**
  - Outgoing: $\text{nums}[1] = 1$. Incoming: $\text{nums}[4] = 1$.
  - Delta: $c_1 \leftarrow 2 - 1 + 1 = 2$.
  - Update maximum: $\mu = \max(2, 2) = 2$.
- **Window 3 (start index $3$, range $[3, 5]$):**
  - Outgoing: $\text{nums}[2] = 0$. Incoming: $\text{nums}[5] = 0$.
  - Delta: $c_1 \leftarrow 2 - 0 + 0 = 2$.
  - Update maximum: $\mu = 2$.
- **Window 4 (start index $4$, range $[4, 6]$):**
  - Outgoing: $\text{nums}[3] = 1$. Incoming: $\text{nums}[6] = 0$.
  - Delta: $c_1 \leftarrow 2 - 1 + 0 = 1$.
  - Update maximum: $\mu = 2$.
- **Window 5 (start index $5$, wrap-around range $[5, 0]$):**
  - Outgoing: $\text{nums}[4] = 1$. Incoming: $\text{nums}[0] = 0$.
  - Delta: $c_1 \leftarrow 1 - 1 + 0 = 0$.
  - Update maximum: $\mu = 2$.
- **Window 6 (start index $6$, wrap-around range $[6, 1]$):**
  - Outgoing: $\text{nums}[5] = 0$. Incoming: $\text{nums}[1] = 1$.
  - Delta: $c_1 \leftarrow 0 - 0 + 1 = 1$.
  - Update maximum: $\mu = 2$.

### Phase 4: Minimum Swaps Computation
Across all $7$ circular windows of length $3$, the maximum number of ones captured is $\mu = 2$.
The minimum swaps required is:

$$\text{Minimum Swaps} = k - \mu = 3 - 2 = 1$$

---

## 4. Comprehensive State Trace

The evaluation metrics across all circular windows of length $k = 3$ are tabulated below:

| Start Index | Window Elements | Outgoing Element | Incoming Element | Number of Ones ($c_1$) | Swaps Needed ($k - c_1$) | Running Min Swaps |
|---|---|---|---|---|---|---|
| $0$ | `[0, 1, 0]` | — | — | $1$ | $3 - 1 = 2$ | $2$ |
| $1$ | `[1, 0, 1]` | $0$ (Index 0) | $1$ (Index 3) | $2$ | $3 - 2 = 1$ | $1$ |
| $2$ | `[0, 1, 1]` | $1$ (Index 1) | $1$ (Index 4) | $2$ | $3 - 2 = 1$ | $1$ |
| $3$ | `[1, 1, 0]` | $0$ (Index 2) | $0$ (Index 5) | $2$ | $3 - 2 = 1$ | $1$ |
| $4$ | `[1, 0, 0]` | $1$ (Index 3) | $0$ (Index 6) | $1$ | $3 - 1 = 2$ | $1$ |
| $5$ | `[0, 0, 0]` | $1$ (Index 4) | $0$ (Index 0) | $0$ | $3 - 0 = 3$ | $1$ |
| $6$ | `[0, 0, 1]` | $0$ (Index 5) | $1$ (Index 1) | $1$ | $3 - 1 = 2$ | $1$ |

The minimum swaps across all circular configurations is verified as $1$.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** Any valid final state contains all $k$ ones in some contiguous circular block $W^*$. If that block originally contained $c_1(W^*)$ ones, then exactly $k - c_1(W^*)$ zeros were present inside it. Because each swap can exchange one external $1$ with one internal $0$, at least $k - c_1(W^*)$ swaps are necessary, and exactly $k - c_1(W^*)$ swaps are sufficient.

**Completeness.** There are exactly $n$ distinct circular windows of length $k$. The sliding window examines all $n$ starting positions $i \in \{0, \dots, n-1\}$. By evaluating the exact number of ones inside every candidate window and selecting the maximum, the algorithm finds the global infimum of required swaps without omitting any configuration.

---

## 6. Edge Cases & Anti-Patterns

- **All Zeros ($k = 0$):** If there are no ones in the array, $k = 0$. Zero swaps are needed, correctly returning $0$.
- **All Ones ($k = n$):** If all elements are ones, $k = n$. The window covers the entire array, so $c_1 = n$ and swaps needed is $n - n = 0$.
- **Wrap-Around Windows:** A target block spanning the boundary (e.g. indices $n-1$ and $0$) is evaluated seamlessly via modular indexing.
- **Anti-Pattern — Quadratic Re-summation:** Recalculating the sum of each length-$k$ window from scratch costs $\mathcal{O}(n \cdot k)$ time. Maintaining a sliding window with $\mathcal{O}(1)$ updates per step yields optimal $\mathcal{O}(n)$ runtime.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of `nums`. Computing total ones $k$ takes $\mathcal{O}(n)$ time. Initializing the first window of size $k$ takes $\mathcal{O}(k)$ time. Sliding the window $n - 1$ times takes $\mathcal{O}(1)$ per step. Total time is $\mathcal{O}(n)$.
- **Auxiliary Space Complexity:** $\mathcal{O}(1)$. The algorithm requires only a few scalar variables for the total ones count, current window count, and maximum count, without duplicating the array.