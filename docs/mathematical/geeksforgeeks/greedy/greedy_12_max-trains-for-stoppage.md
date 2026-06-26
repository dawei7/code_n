# Formal Mathematical Specification: Maximum Trains for Stoppage

## 1. Definitions and Notation

Let $\mathcal{T} = \{t_1, t_2, \dots, t_N\}$ be the set of $N$ trains. Each train $t_i$ is defined as a triplet $t_i = (a_i, d_i, p_i)$, where:
*   $a_i \in \mathbb{R}_{\ge 0}$ is the arrival time.
*   $d_i \in \mathbb{R}_{\ge 0}$ is the departure time, with the constraint $a_i < d_i$.
*   $p_i \in \{1, 2, \dots, P\}$ is the platform index.

Let $\mathcal{P}_j = \{t_i \in \mathcal{T} \mid p_i = j\}$ denote the subset of trains assigned to platform $j$, for $j \in \{1, \dots, P\}$. Note that the collection $\{\mathcal{P}_1, \mathcal{P}_2, \dots, \mathcal{P}_P\}$ forms a partition of $\mathcal{T}$ such that $\bigcup_{j=1}^P \mathcal{P}_j = \mathcal{T}$ and $\mathcal{P}_j \cap \mathcal{P}_k = \emptyset$ for $j \neq k$.

A subset of trains $\mathcal{S}_j \subseteq \mathcal{P}_j$ is considered *feasible* if for any two distinct trains $t_u, t_v \in \mathcal{S}_j$, the intervals $[a_u, d_u]$ and $[a_v, d_v]$ are non-overlapping, specifically:
$$\forall t_u, t_v \in \mathcal{S}_j, u \neq v \implies d_u \le a_v \lor d_v \le a_u$$

The objective is to find the cardinality of the maximum feasible subset $\mathcal{S} = \bigcup_{j=1}^P \mathcal{S}_j^*$, where $\mathcal{S}_j^*$ is the maximum feasible subset of $\mathcal{P}_j$. The total number of trains is given by:
$$\text{MaxTrains} = \sum_{j=1}^P |\mathcal{S}_j^*|$$

## 2. Algebraic Characterization

The problem decomposes into $P$ independent instances of the **Activity Selection Problem**. For a fixed platform $j$, let the elements of $\mathcal{P}_j$ be indexed such that their departure times are non-decreasing: $d_{(1)} \le d_{(2)} \le \dots \le d_{(|\mathcal{P}_j|)}$.

The greedy choice property for activity selection states that selecting the activity with the earliest finish time leaves the maximum possible time for subsequent activities. Let $f(j, \tau)$ be the maximum number of trains that can be scheduled on platform $j$ given that the platform is available at time $\tau$. The recurrence relation is:

$$f(j, \tau) = \max \begin{cases} f(j, \tau) & \text{if } a_i < \tau \\ 1 + f(j, d_i) & \text{if } a_i \ge \tau \end{cases}$$

For each platform $j$, we define the greedy selection sequence $S_j = \{s_1, s_2, \dots, s_k\}$ where:
1. $s_1 = \text{argmin}_{t \in \mathcal{P}_j} \{d_t\}$
2. $s_{m+1} = \text{argmin}_{t \in \mathcal{P}_j, a_t \ge d_{s_m}} \{d_t\}$

The optimality of this greedy strategy is guaranteed by the exchange argument: if an optimal solution $\mathcal{O}_j$ does not contain the train with the earliest finish time, one can replace the first train in $\mathcal{O}_j$ with the earliest finishing train without violating the feasibility constraint, thereby maintaining optimality.

## 3. Complexity Analysis

### Time Complexity
The algorithm proceeds in three phases:
1. **Bucketing:** Distributing $N$ trains into $P$ lists takes $O(N)$ time.
2. **Sorting:** For each platform $j$, we sort the trains by departure time. Let $n_j = |\mathcal{P}_j|$. The total time for sorting is $\sum_{j=1}^P O(n_j \log n_j)$. Since $\sum n_j = N$, and $n_j \log n_j \le n_j \log N$, the total time is bounded by:
   $$\sum_{j=1}^P O(n_j \log N) = O(N \log N)$$
3. **Selection:** Iterating through the sorted lists takes $O(n_j)$ per platform, totaling $O(\sum n_j) = O(N)$.

Thus, the total time complexity is $O(N) + O(N \log N) + O(N) = O(N \log N)$.

### Space Complexity
1. **Auxiliary Space:** We store the trains in a 2D structure (an array of lists). The total number of elements stored is $N$, and the structure itself requires $O(P)$ pointers/references.
2. **Total Space:** The space complexity is $O(N + P)$. In the context of $N \ge P$, this is effectively $O(N)$.