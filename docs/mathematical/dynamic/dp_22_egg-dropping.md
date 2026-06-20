# Formal Mathematical Specification: Egg Dropping (Mathematical $O(K \log N)$)

## 1. Definitions and Notation

Let $k \in \mathbb{Z}^+$ denote the number of available eggs and $n \in \mathbb{Z}^+$ denote the number of floors in the building. We define the objective as finding the minimum number of trials $m$ required to determine the critical floor $f_c \in \{0, 1, \dots, n\}$, where $f_c$ is the highest floor from which an egg can be dropped without breaking.

We define the state space $\mathcal{S}$ via the function $f(m, k)$, representing the maximum number of floors that can be uniquely tested given $m$ moves and $k$ eggs. 
- The domain of $m$ is $\mathbb{Z}_{\ge 0}$.
- The domain of $k$ is $\mathbb{Z}_{\ge 0}$.
- The codomain is $\mathbb{Z}_{\ge 0}$, representing the capacity of the testing strategy.

The problem is equivalent to finding the smallest $m$ such that:
$$f(m, k) \ge n$$

## 2. Algebraic Characterization

To derive the recurrence relation, consider the state $(m, k)$. Upon dropping an egg from an arbitrary floor, two mutually exclusive outcomes occur:
1. **The egg breaks:** We have consumed 1 move and 1 egg. To guarantee the result, we must be able to test the remaining floors below the current one. The maximum number of such floors is $f(m-1, k-1)$.
2. **The egg survives:** We have consumed 1 move and 0 eggs. We must be able to test the remaining floors above the current one. The maximum number of such floors is $f(m-1, k)$.

Including the floor from which the drop was initiated, the recurrence relation is defined as:
$$f(m, k) = f(m-1, k-1) + f(m-1, k) + 1$$

**Boundary Conditions:**
- $f(m, 0) = 0$ (Zero eggs cannot test any floors).
- $f(0, k) = 0$ (Zero moves cannot test any floors).
- $f(m, 1) = m$ (With one egg, we must test floors sequentially).

**Closed-Form Representation:**
By induction, the recurrence relation $f(m, k) = \sum_{i=1}^{k} \binom{m}{i}$ can be established. This identity demonstrates that the maximum number of floors testable is the sum of the first $k$ binomial coefficients of $m$.

## 3. Complexity Analysis

### Time Complexity
The algorithm seeks the smallest $m$ such that $\sum_{i=1}^{k} \binom{m}{i} \ge n$. 
1. **Search Space:** Since $f(m, k)$ is strictly increasing with respect to $m$, and $f(m, k) \approx \frac{m^k}{k!}$ for $m \gg k$, the value of $m$ is bounded by $O(n)$ in the worst case ($k=1$) and $O(\log n)$ for $k \ge \log_2 n$.
2. **Computation:** For a fixed $m$, calculating the sum $\sum_{i=1}^{k} \binom{m}{i}$ can be performed in $O(k)$ time using the identity $\binom{m}{i} = \binom{m}{i-1} \times \frac{m-i+1}{i}$.
3. **Binary Search:** By performing a binary search over the range $[1, n]$ for the optimal $m$, we evaluate the sum $O(\log n)$ times.

Thus, the total time complexity is:
$$T(n, k) = O(k \log n)$$

### Space Complexity
The algorithm utilizes a 1D array of size $k+1$ to store the values of $f(m, \cdot)$ for the current move iteration. 
- The state transition $f(m, k) = f(m-1, k-1) + f(m-1, k) + 1$ allows for in-place updates if the array is traversed in descending order of $k$ (similar to the 0/1 Knapsack optimization).
- The auxiliary space required is $O(k)$ to maintain the state vector.

Thus, the total space complexity is:
$$S(n, k) = O(k)$$