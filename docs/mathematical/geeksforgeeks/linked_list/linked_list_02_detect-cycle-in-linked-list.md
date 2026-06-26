# Formal Mathematical Specification: Detect Cycle in Linked List

## 1. Definitions and Notation

Let the linked list be represented as a directed graph $G = (V, E)$, where $V = \{v_0, v_1, \dots, v_{n-1}\}$ is the set of nodes and $E \subseteq V \times V$ is the set of edges. Since the structure is a singly linked list, each node $v_i$ has an out-degree of at most 1. Specifically, there exists a successor function $f: V \to V \cup \{\text{null}\}$ such that $(v_i, v_j) \in E \iff f(v_i) = v_j$.

- **Path:** A sequence of nodes $(p_0, p_1, \dots, p_k)$ such that $p_{i+1} = f(p_i)$ for all $0 \le i < k$.
- **Cycle:** A path $(p_0, p_1, \dots, p_k)$ is a cycle if $p_k = p_0$ and $k > 0$.
- **State Space:** Let $\mathcal{S} = V \times V$ be the state space of the two pointers, where a state $s_t = (\sigma_t, \phi_t)$ represents the positions of the slow pointer $\sigma$ and fast pointer $\phi$ at time step $t$.
- **Transition Function:** The evolution of the pointers is defined by the mapping $\delta: \mathcal{S} \to \mathcal{S}$:
  $$\delta(\sigma, \phi) = (f(\sigma), f(f(\phi)))$$
  where $f(\text{null}) = \text{null}$.

## 2. Algebraic Characterization

### The Cycle Condition
A cycle exists if and only if there exists a $t > 0$ such that $\sigma_t = \phi_t$. 

Let $L$ be the distance from the head $v_0$ to the first node of the cycle $v_c$, and let $C$ be the length of the cycle. At time $t$, the positions are:
- $\sigma_t = f^t(v_0)$
- $\phi_t = f^{2t}(v_0)$

If a cycle exists, for sufficiently large $t$, the pointers enter the cycle. Let $t = L + k$. The pointers meet when:
$$L + k \equiv 2(L + k) \pmod C$$
$$L + k \equiv 2L + 2k \pmod C$$
$$k \equiv -(L) \pmod C$$
This implies $k = mC - L$ for some integer $m$. Thus, the meeting occurs at $t = L + (mC - L) = mC$. The distance from the head to the meeting point is $mC$, which is a multiple of the cycle length.

### The Start of the Cycle
To find the start of the cycle, we reset a pointer to $v_0$ and move both at unit speed. Let the meeting point be $v_m$. The distance from $v_0$ to $v_c$ is $L$. The distance from $v_m$ to $v_c$ is $C - (L \pmod C)$. By moving both pointers at speed 1, they will coincide at $v_c$ after exactly $L$ steps, as:
$$v_0 \xrightarrow{L} v_c \quad \text{and} \quad v_m \xrightarrow{L} v_c$$

## 3. Complexity Analysis

### Time Complexity
The time complexity is $O(N)$, where $N = |V|$.
- **Phase 1 (Detection):** The fast pointer $\phi$ enters the cycle in at most $L$ steps. Once inside, the relative distance between $\phi$ and $\sigma$ increases by 1 each step. Since the cycle length is $C \le N$, the fast pointer will "lap" the slow pointer in at most $C$ steps. Total steps $T_1 \le L + C \le N$.
- **Phase 2 (Finding Start):** The pointers traverse the distance $L$ from the head to the cycle start. Since $L < N$, $T_2 = L < N$.
- **Total Time:** $T(N) = T_1 + T_2 = O(N)$.

### Space Complexity
The algorithm maintains exactly two pointers, $\sigma$ and $\phi$, regardless of the input size $N$. 
- The auxiliary space required is $S(N) = \Theta(1)$.
- Since the input is provided as a reference to the head of the list, the total space complexity is $O(1)$ beyond the storage of the input graph itself.