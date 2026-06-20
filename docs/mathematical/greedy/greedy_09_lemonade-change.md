# Formal Mathematical Specification: Lemonade Change

## 1. Definitions and Notation

Let $B = (b_1, b_2, \dots, b_n)$ be a sequence of bills representing the queue of customers, where each $b_i \in \{5, 10, 20\}$. 
Let $c_5^{(i)}$ and $c_{10}^{(i)}$ denote the number of 5-unit and 10-unit bills held in the register after processing the $i$-th customer, with initial state $c_5^{(0)} = 0$ and $c_{10}^{(0)} = 0$.

The state of the register at step $i$ is defined by the tuple $\mathcal{S}_i = (c_5^{(i)}, c_{10}^{(i)}) \in \mathbb{N}_0^2$.
The objective is to determine if there exists a sequence of transitions such that for all $i \in \{1, \dots, n\}$, the change required $r_i = b_i - 5$ can be satisfied by the current register state $\mathcal{S}_{i-1}$.

## 2. Algebraic Characterization

The algorithm processes each bill $b_i$ and updates the state $\mathcal{S}_i$ based on the following transition function $f: (\mathcal{S}_{i-1}, b_i) \to \mathcal{S}_i \cup \{\perp\}$, where $\perp$ denotes an invalid state (failure):

1. **Case $b_i = 5$:**
   $c_5^{(i)} = c_5^{(i-1)} + 1, \quad c_{10}^{(i)} = c_{10}^{(i-1)}$

2. **Case $b_i = 10$:**
   If $c_5^{(i-1)} \geq 1$:
   $c_5^{(i)} = c_5^{(i-1)} - 1, \quad c_{10}^{(i)} = c_{10}^{(i-1)} + 1$
   Else: $\perp$

3. **Case $b_i = 20$:**
   We require change $r_i = 15$. The greedy choice is defined by the priority of using a 10-unit bill:
   - If $c_{10}^{(i-1)} \geq 1$ and $c_5^{(i-1)} \geq 1$:
     $c_5^{(i)} = c_5^{(i-1)} - 1, \quad c_{10}^{(i)} = c_{10}^{(i-1)} - 1$
   - Else if $c_5^{(i-1)} \geq 3$:
     $c_5^{(i)} = c_5^{(i-1)} - 3, \quad c_{10}^{(i)} = c_{10}^{(i-1)}$
   - Else: $\perp$

**Loop Invariant:**
At any step $k$, the register state $\mathcal{S}_k$ is the unique state that maximizes the potential to satisfy future requests $b_j$ ($j > k$). Specifically, since $c_5$ is required for both 10-unit and 20-unit change, and $c_{10}$ is only required for 20-unit change, the greedy strategy of consuming $c_{10}$ before $c_5$ when $b_i=20$ preserves the maximum possible value of $c_5$, which is the most "liquid" asset in the system.

## 3. Complexity Analysis

### Time Complexity
The algorithm iterates through the input sequence $B$ exactly once. For each element $b_i$, the transition function $f$ performs a constant number of arithmetic operations and comparisons, denoted as $T_{step} = O(1)$.
The total time complexity $T(n)$ is given by the summation:
$$T(n) = \sum_{i=1}^{n} T_{step} = \sum_{i=1}^{n} O(1) = O(n)$$
Thus, the algorithm is linear with respect to the number of customers $n$.

### Space Complexity
The algorithm maintains only two scalar variables, $c_5$ and $c_{10}$, to represent the state $\mathcal{S}_i$. The memory required is independent of the input size $n$.
$$S(n) = O(1)$$
The auxiliary space is constant, as no additional data structures (such as arrays or hash maps) are required to store the history of transactions or the register state.