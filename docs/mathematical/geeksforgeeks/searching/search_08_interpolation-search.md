# Formal Mathematical Specification: Interpolation Search

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be a sequence of elements drawn from a totally ordered set $(\mathcal{X}, \leq)$, such that $a_i \leq a_{i+1}$ for all $0 \leq i < n-1$. We define the search space as the index set $\mathcal{I} = \{0, 1, \dots, n-1\}$.

Given a target value $t \in \mathcal{X}$, the objective is to determine an index $k \in \mathcal{I}$ such that $a_k = t$, or to return a sentinel value $\bot \notin \mathcal{I}$ if no such $k$ exists.

The algorithm maintains a dynamic sub-interval $[L, R] \subseteq \mathcal{I}$, initialized as $[0, n-1]$. At each iteration, we define the state space $\mathcal{S} = \{(L, R) \in \mathcal{I}^2 \mid L \leq R\}$.

## 2. Algebraic Characterization

The algorithm relies on the assumption that the values $a_i$ are distributed linearly with respect to their indices $i$. We define the probe position $P$ as a linear interpolation between the values at the boundaries of the current interval $[L, R]$:

$$P = L + \left\lfloor \frac{(t - a_L)(R - L)}{a_R - a_L} \right\rfloor$$

### Loop Invariant
For the algorithm to be correct, the following invariant must hold at the start of each iteration:
If $t \in \{a_i \mid L \leq i \leq R\}$, then there exists some $k \in [L, R]$ such that $a_k = t$. 

### Transition Logic
The state $(L, R)$ is updated based on the comparison between $a_P$ and $t$:
1. If $a_P = t$, the algorithm terminates and returns $P$.
2. If $a_P < t$, the new state is $(P + 1, R)$.
3. If $a_P > t$, the new state is $(L, P - 1)$.

The algorithm terminates when $L > R$ or $t < a_L$ or $t > a_R$, at which point it returns $\bot$.

## 3. Complexity Analysis

### Time Complexity
The time complexity is contingent upon the distribution of the elements in $A$.

**Average Case:**
For a set of $n$ elements drawn from a uniform distribution, the expected number of probes required to locate the target is $O(\log(\log n))$. This is derived from the recurrence relation for the expected number of elements remaining after one probe:
$$E[n_{k+1}] \approx \sqrt{E[n_k]}$$
Solving this recurrence, we find that the number of iterations $k$ satisfies $n^{(1/2)^k} \approx 2$, which yields $k \approx \log_2(\log_2 n)$. Thus, the average time complexity is $\Theta(\log(\log n))$.

**Worst Case:**
In the case of highly non-uniform distributions (e.g., exponential growth where $a_i = 2^i$), the interpolation formula may consistently yield $P = L$ or $P = R$. In such instances, the search space reduces by only one element per iteration:
$$T(n) = T(n-1) + O(1)$$
This results in a worst-case time complexity of $O(n)$, effectively reducing the algorithm to a linear search.

### Space Complexity
The algorithm operates in-place, requiring only a constant number of auxiliary variables ($L, R, P, \text{value}$) to store the current bounds and the probe index. 

Let $S(n)$ be the auxiliary space complexity:
$$S(n) = \text{space}(\text{pointers}) + \text{space}(\text{scalars}) = O(1) + O(1) = O(1)$$
Thus, the space complexity is $O(1)$.