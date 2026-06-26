# Formal Mathematical Specification: Trapping Rain Water

## 1. Definitions and Notation

Let $H = [h_0, h_1, \dots, h_{n-1}]$ be a sequence of non-negative integers representing the elevation map, where $h_i \in \mathbb{N}_0$ for all $i \in \{0, 1, \dots, n-1\}$. The width of each bar is defined as a unit interval.

We define the following sets and variables:
*   **Index Set:** $I = \{0, 1, \dots, n-1\}$.
*   **Stack:** A sequence $S = (s_1, s_2, \dots, s_k)$ where $s_j \in I$ represents the indices of bars in the stack. The stack maintains the monotonic property $h_{s_1} \geq h_{s_2} \geq \dots \geq h_{s_k}$.
*   **Water Volume:** The total trapped water $W$ is a scalar value defined by the sum of water trapped in each horizontal layer or "valley" formed by the elevation map.
*   **State Space:** The state at iteration $i$ is defined by the tuple $(S_i, W_i)$, where $S_i$ is the stack configuration and $W_i$ is the cumulative volume of water trapped after processing index $i$.

## 2. Algebraic Characterization

The algorithm computes the total trapped water by decomposing the area into horizontal rectangles. For any index $i$, if $h_i > h_{s_k}$ (where $s_k$ is the top of the stack), a valley is identified.

Let $t$ be the index popped from the stack ($t = s_k$), representing the bottom of the valley. Let $l$ be the new top of the stack ($l = s_{k-1}$), representing the left boundary. The right boundary is the current index $i$.

The volume of water $\Delta W$ trapped by the current bar $i$ relative to the popped bottom $t$ is given by:
$$\Delta W = (\min(h_i, h_l) - h_t) \times (i - l - 1)$$

The total volume $W$ is the summation over all such events:
$$W = \sum_{i=0}^{n-1} \sum_{t \in \text{Popped}_i} (\min(h_i, h_{l_i}) - h_t) \cdot (i - l_i - 1)$$
where $\text{Popped}_i$ is the set of indices popped from the stack at step $i$, and $l_i$ is the index remaining at the top of the stack after the pop.

**Loop Invariant:**
At the start of each iteration $i$, the stack $S$ contains indices $s_1, s_2, \dots, s_k$ such that $h_{s_1} \geq h_{s_2} \geq \dots \geq h_{s_k}$. The variable $W$ correctly stores the total volume of water trapped by all bars $h_0, \dots, h_{i-1}$ that are bounded by at least one bar to their left and one to their right.

## 3. Complexity Analysis

### Time Complexity
The time complexity is $O(n)$. 
**Proof:** 
Consider the operations performed on the stack. Each index $j \in I$ is pushed onto the stack exactly once. An index $j$ is popped from the stack at most once. 
Let $T(n)$ be the total number of operations. The loop runs $n$ times. Inside the loop, the `while` condition checks the stack, and the `pop` operation occurs. Since each element is pushed once and popped at most once, the total number of `pop` operations across the entire execution is bounded by $n$. Thus, the total work is:
$$T(n) = \sum_{i=0}^{n-1} (1 + \text{pops}_i) = n + \sum_{i=0}^{n-1} \text{pops}_i = n + n = 2n$$
As $2n \in O(n)$, the algorithm is linear in time.

### Space Complexity
The space complexity is $O(n)$.
**Proof:**
The auxiliary space is dominated by the stack $S$. In the worst-case scenario, the input array $H$ is strictly decreasing (e.g., $h_i > h_{i+1}$ for all $i$). In this case, the `while` condition $h_i > h_{s_k}$ is never satisfied, and every index $i \in I$ is pushed onto the stack without any being popped. The stack size $|S|$ reaches $n$. Therefore, the space complexity is $O(n)$.