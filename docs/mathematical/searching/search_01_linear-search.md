# Formal Mathematical Specification: Linear Search

## 1. Definitions and Notation

Let $A$ be an array (or sequence) of length $N \in \mathbb{N}_0$, where $N$ denotes the cardinality of the index set $I = \{0, 1, \dots, N-1\}$. The elements of the array are drawn from a set $\mathcal{D}$ (the domain of data), such that $A: I \to \mathcal{D}$. 

We define the following:
*   **Input:** A sequence $A = (a_0, a_1, \dots, a_{N-1})$ and a target value $\tau \in \mathcal{D}$.
*   **Output:** An index $k \in I \cup \{-1\}$, where $k$ is defined by the mapping:
    $$f(A, \tau) = \begin{cases} \min \{i \in I \mid a_i = \tau\} & \text{if } \exists i \in I : a_i = \tau \\ -1 & \text{otherwise} \end{cases}$$
*   **State Space:** The algorithm maintains a state variable $i \in \{0, 1, \dots, N\}$, representing the current index being inspected.

## 2. Algebraic Characterization

The correctness of the Linear Search algorithm is established via a loop invariant. Let $i$ be the loop counter.

**Loop Invariant:** At the start of each iteration $i$, for all $j$ such that $0 \le j < i$, $a_j \neq \tau$.

*   **Initialization:** Before the first iteration, $i = 0$. The set $\{j \in \mathbb{N} \mid 0 \le j < 0\}$ is empty; thus, the condition holds vacuously.
*   **Maintenance:** Suppose the invariant holds for $i$. In the current iteration, we inspect $a_i$. 
    *   If $a_i = \tau$, the algorithm terminates and returns $i$, which is the smallest index satisfying the condition.
    *   If $a_i \neq \tau$, the invariant holds for $i+1$, as the set of checked indices is now $\{0, \dots, i\}$, all of which are $\neq \tau$.
*   **Termination:** The loop terminates when $i = N$ (failure) or when $a_i = \tau$ (success). If $i = N$, the invariant implies $\forall j \in I, a_j \neq \tau$, justifying the return value of $-1$.

The algorithm can be expressed as the composition of a search function over the index set $I$:
$$\text{Search}(A, \tau) = \text{if } (\exists i \in I : a_i = \tau) \text{ then } \text{argmin}_{i \in I} \{i \mid a_i = \tau\} \text{ else } -1$$

## 3. Complexity Analysis

### Time Complexity
The time complexity $T(N)$ is determined by the number of comparisons performed. Let $c$ be the cost of a single comparison $a_i = \tau$.

*   **Worst-Case:** Occurs when $\tau \notin A$ or $\tau = a_{N-1}$. The algorithm performs $N$ comparisons.
    $$T_{worst}(N) = \sum_{i=0}^{N-1} c = c \cdot N \implies O(N)$$
*   **Best-Case:** Occurs when $\tau = a_0$. The algorithm performs exactly 1 comparison.
    $$T_{best}(N) = c \implies \Omega(1)$$
*   **Average-Case:** Assuming $\tau$ is present in $A$ at a uniformly random index $k \in \{0, \dots, N-1\}$, the expected number of comparisons $E[T]$ is:
    $$E[T] = \frac{1}{N} \sum_{i=1}^{N} i = \frac{1}{N} \frac{N(N+1)}{2} = \frac{N+1}{2} \implies \Theta(N)$$

### Space Complexity
The algorithm requires a constant amount of auxiliary space to store the loop index $i$ and the input references. 
*   Let $S_{aux}$ be the space required for variables. Since $i$ is a scalar integer, $S_{aux} = O(1)$.
*   The input array $A$ occupies $O(N)$ space in memory, but the algorithm operates in-place, requiring no additional data structures proportional to the input size.
*   Thus, the auxiliary space complexity is $O(1)$.