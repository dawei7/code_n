# Formal Mathematical Specification: Jump Game (I and II)

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be an array of non-negative integers where $n \in \mathbb{Z}^+$. Each index $i \in \{0, 1, \dots, n-1\}$ represents a position in a discrete state space $\mathcal{S} = \{0, 1, \dots, n-1\}$. 

For any position $i$, the set of reachable positions in a single jump is defined by the set:
$$\mathcal{R}(i) = \{j \in \mathcal{S} \mid i < j \le i + a_i\}$$

**Jump Game I (Decision):** Define a reachability predicate $P(k)$ which is true if there exists a sequence of indices $(i_0, i_1, \dots, i_m)$ such that $i_0 = 0$, $i_m = k$, and $i_{t+1} \in \mathcal{R}(i_t)$ for all $0 \le t < m$. The problem asks to determine the truth value of $P(n-1)$.

**Jump Game II (Optimization):** Let $\mathcal{P}$ be the set of all valid sequences $(i_0, i_1, \dots, i_m)$ such that $i_0 = 0$ and $i_m = n-1$. We seek the value:
$$\min \{m \mid (i_0, \dots, i_m) \in \mathcal{P}\}$$

## 2. Algebraic Characterization

### Jump Game I: Reachability Invariant
Define $M_k$ as the maximum reachable index after considering elements up to index $k$:
$$M_k = \max_{0 \le i \le k} (i + a_i)$$
The algorithm maintains the invariant that at any step $k$, if $k > M_{k-1}$, then $P(n-1)$ is false, as the set of reachable indices is bounded by $M_{k-1} < k$. The condition for reachability is:
$$\forall k \in \{0, \dots, n-1\}, k \le M_k \implies P(n-1) \text{ is true if } M_{n-1} \ge n-1$$

### Jump Game II: Greedy Recurrence
Let $J_k$ be the minimum number of jumps to reach index $k$. Let $E_m$ be the maximum index reachable with exactly $m$ jumps. We define the state transition as:
$$E_m = \max_{0 \le i \le E_{m-1}} (i + a_i)$$
where $E_0 = 0$. The minimum number of jumps $m^*$ is the smallest $m$ such that $E_m \ge n-1$. 

The algorithm computes this by maintaining a "window" $[L_m, E_m]$, where $L_m$ is the start of the range reachable in $m$ jumps. The greedy choice property holds because for any $i \in [L_m, E_m]$, the choice of $i$ that maximizes $i + a_i$ strictly dominates all other choices in the current window for the purpose of extending the reach to $E_{m+1}$.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a single linear scan over the array $A$. At each index $i \in \{0, \dots, n-2\}$, the algorithm performs a constant number of operations: one addition, one comparison for the `max` function, and one conditional check.

The total work $W(n)$ is given by the summation:
$$W(n) = \sum_{i=0}^{n-2} c = c(n-1)$$
where $c$ is the constant time required for the operations within the loop. Since $W(n) = c(n-1)$, we conclude:
$$W(n) \in \Theta(n)$$
Thus, the time complexity is $O(n)$.

### Space Complexity
The algorithm utilizes a fixed set of auxiliary variables: `jumps`, `current_end`, `farthest`, and the loop iterator `i`. 
Let $S_{aux}$ be the space required for these variables. Since each variable is a primitive integer (typically 32-bit or 64-bit), the space required is independent of the input size $n$:
$$S_{aux} = \text{sizeof}(\text{int}) \times 4 \in O(1)$$
The input array $A$ occupies $O(n)$ space, but the auxiliary space complexity is strictly:
$$S(n) \in O(1)$$