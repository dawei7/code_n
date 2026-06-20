# Formal Mathematical Specification: Activity Selection Problem

## 1. Definitions and Notation

Let $A = \{a_1, a_2, \dots, a_n\}$ be a set of $n$ activities. Each activity $a_i$ is defined as an ordered pair of real numbers $(s_i, f_i)$, where $s_i \in \mathbb{R}_{\ge 0}$ denotes the start time and $f_i \in \mathbb{R}_{> s_i}$ denotes the finish time.

We define a binary relation $\mathcal{C}$ on the set $A$, representing the "non-conflicting" condition. Two activities $a_i, a_j$ are compatible if and only if:
$$a_i \mathcal{C} a_j \iff f_i \le s_j \lor f_j \le s_i$$

A subset $S \subseteq A$ is defined as a **mutually compatible set** if for every pair $a_i, a_j \in S$ where $i \neq j$, the condition $a_i \mathcal{C} a_j$ holds. The objective is to find a subset $S^* \subseteq A$ such that $|S^*|$ is maximized, subject to the constraint that $S^*$ is mutually compatible.

## 2. Algebraic Characterization

Let the activities be indexed such that they are sorted by their finish times: $f_1 \le f_2 \le \dots \le f_n$. 

### The Greedy Choice Property
The optimality of the greedy strategy relies on the existence of an optimal solution that includes the activity with the earliest finish time. Let $S_{opt}$ be an optimal solution. Let $a_k$ be the activity in $A$ with the minimum finish time. If $a_k \in S_{opt}$, the greedy choice is consistent with an optimal solution. If $a_k \notin S_{opt}$, let $a_j$ be the activity in $S_{opt}$ with the minimum finish time. Since $f_k \le f_j$, replacing $a_j$ with $a_k$ in $S_{opt}$ results in a set $S' = (S_{opt} \setminus \{a_j\}) \cup \{a_k\}$. Because $f_k \le f_j$, $S'$ remains mutually compatible and $|S'| = |S_{opt}|$. Thus, $S'$ is also an optimal solution.

### Recurrence Relation
Let $OPT(i)$ be the maximum number of compatible activities that can be selected from the subset of activities $\{a_i, a_{i+1}, \dots, a_n\}$ given that the last selected activity finished at time $t_{last}$. The state transition is defined as:

$$OPT(i, t_{last}) = 
\begin{cases} 
0 & \text{if } i > n \\
1 + OPT(i+1, f_i) & \text{if } s_i \ge t_{last} \\
OPT(i+1, t_{last}) & \text{if } s_i < t_{last}
\end{cases}$$

The algorithm effectively computes this recurrence greedily by always choosing the branch that increments the count when $s_i \ge t_{last}$.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of two primary phases:
1. **Sorting:** The set $A$ is sorted based on the finish times $f_i$. Using a comparison-based sort (e.g., Timsort or Heapsort), the time complexity is $T_{sort}(n) = \Theta(n \log n)$.
2. **Selection:** The algorithm performs a single linear scan over the sorted set $A$. For each element, it performs a constant-time comparison $s_i \ge t_{last}$. This phase is $T_{scan}(n) = \Theta(n)$.

The total time complexity is:
$$T(n) = T_{sort}(n) + T_{scan}(n) = \Theta(n \log n) + \Theta(n) = O(n \log n)$$

### Space Complexity
The space complexity is determined by the storage of the activity tuples.
1. **Auxiliary Space:** The algorithm requires $O(1)$ auxiliary space for the variables `count` and `last_finish`.
2. **Total Space:** If the input arrays are provided as separate structures, creating the list of tuples requires $O(n)$ space. If the input is provided as a pre-allocated array of objects, the sorting can be performed in-place (e.g., using Heapsort), resulting in $O(1)$ auxiliary space. In the standard implementation provided, the space complexity is $O(n)$ due to the creation of the `pairs` list.