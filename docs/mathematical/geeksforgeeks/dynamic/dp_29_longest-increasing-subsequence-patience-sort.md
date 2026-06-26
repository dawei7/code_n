# Formal Mathematical Specification: Longest Increasing Subsequence ($O(n \log n)$ Patience Sort)

## 1. Definitions and Notation

Let $A = \langle a_1, a_2, \dots, a_n \rangle$ be a sequence of $n$ elements drawn from a totally ordered set $(\mathcal{X}, \le)$. 

A subsequence of $A$ is a sequence $\langle a_{i_1}, a_{i_2}, \dots, a_{i_k} \rangle$ such that $1 \le i_1 < i_2 < \dots < i_k \le n$. The subsequence is strictly increasing if $a_{i_1} < a_{i_2} < \dots < a_{i_k}$. We denote the set of all strictly increasing subsequences of $A$ as $\mathcal{S}$. The objective is to find the length of the longest such subsequence:
$$L = \max \{ k \mid \exists \langle a_{i_1}, \dots, a_{i_k} \rangle \in \mathcal{S} \}$$

We define the state space $\mathcal{T}$ as a sequence of "tails" $T = \langle t_1, t_2, \dots, t_m \rangle$, where $t_j$ represents the smallest terminal element of all strictly increasing subsequences of length $j$ found in the prefix $A[1 \dots i]$.

## 2. Algebraic Characterization

The algorithm maintains the invariant that at any step $i \in \{1, \dots, n\}$, the sequence $T$ is strictly increasing: $t_1 < t_2 < \dots < t_m$.

### The State Transition
Let $T^{(i)}$ be the state of the tails array after processing $a_i$. Given $T^{(i-1)} = \langle t_1, \dots, t_m \rangle$:
1. If $a_i > t_m$, then $T^{(i)} = \langle t_1, \dots, t_m, a_i \rangle$.
2. If $a_i \le t_m$, let $j$ be the unique index such that $t_{j-1} < a_i \le t_j$ (with $t_0 = -\infty$). Then $T^{(i)} = \langle t_1, \dots, t_{j-1}, a_i, t_{j+1}, \dots, t_m \rangle$.

### Correctness Invariant
The length of the longest increasing subsequence ending at or before index $i$ is exactly the length of the sequence $T^{(i)}$. 
**Proof Sketch:**
- **Monotonicity:** By induction, if $T^{(i-1)}$ is sorted, the binary search operation preserves the sorted property. If $a_i$ is appended, the property holds by the condition $a_i > t_m$. If $a_i$ replaces $t_j$, the property $t_{j-1} < a_i < t_{j+1}$ holds because $t_{j-1} < a_i \le t_j < t_{j+1}$.
- **Optimality:** For any length $j$, $t_j$ is the minimum possible value for the end of an increasing subsequence of length $j$. By replacing $t_j$ with a smaller value $a_i$, we increase the potential to extend the subsequence in future steps without decreasing the current maximum length $m$.

## 3. Complexity Analysis

### Time Complexity
The algorithm processes each element $a_i \in A$ exactly once. For each $a_i$, we perform a binary search on the sequence $T$.
- Let $m_i$ be the length of $T$ at step $i$. The binary search operation takes $O(\log m_i)$ time.
- Since $m_i \le n$ for all $i$, the cost per iteration is bounded by $O(\log n)$.
- The total time complexity $T(n)$ is given by the summation:
$$T(n) = \sum_{i=1}^{n} O(\log i) = O\left(\sum_{i=1}^{n} \log i\right) = O(\log(n!))$$
Applying Stirling's approximation, $\log(n!) \approx n \log n - n$, thus:
$$T(n) = O(n \log n)$$

### Space Complexity
The algorithm maintains the sequence $T$. In the worst case (where the input array $A$ is already strictly increasing), the length of $T$ grows to $n$.
- The auxiliary space required is the storage for $T$, which is $O(n)$.
- No additional data structures are required that scale with $n$, thus the total space complexity is:
$$S(n) = O(n)$$