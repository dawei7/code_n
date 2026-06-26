# Formal Mathematical Specification: Job Sequencing Problem

## 1. Definitions and Notation

Let $\mathcal{J} = \{J_1, J_2, \dots, J_N\}$ be a set of $N$ jobs. Each job $J_i$ is defined as a triple $(id_i, d_i, p_i)$, where:
*   $id_i \in \mathbb{Z}^+$ is the unique identifier.
*   $d_i \in \{1, 2, \dots, D_{max}\}$ is the deadline, representing the latest time slot by which the job must be completed.
*   $p_i \in \mathbb{R}^+$ is the profit associated with the completion of job $J_i$.

Let $\mathcal{T} = \{1, 2, \dots, D_{max}\}$ be the set of discrete time slots, where each slot $t \in \mathcal{T}$ has a capacity of one job. A schedule is a partial injective mapping $\sigma: \mathcal{J}' \to \mathcal{T}$, where $\mathcal{J}' \subseteq \mathcal{J}$ is the subset of scheduled jobs, such that for every $J_i \in \mathcal{J}'$, the condition $\sigma(J_i) \leq d_i$ is satisfied.

The objective is to find a subset $\mathcal{J}^* \subseteq \mathcal{J}$ and a valid mapping $\sigma^*$ that maximizes the total profit:
$$\text{Maximize } \sum_{J_i \in \mathcal{J}^*} p_i$$

## 2. Algebraic Characterization

The algorithm relies on the **Matroid Greedy Property**. Specifically, the set of all schedulable subsets of jobs forms a *forest matroid* (or more generally, a transversal matroid), which guarantees that a greedy strategy yields an optimal solution.

### The Greedy Choice Property
Let the jobs be sorted such that $p_{(1)} \geq p_{(2)} \geq \dots \geq p_{(N)}$. The algorithm constructs the optimal set $\mathcal{J}^*$ iteratively. Let $\mathcal{S}_k$ be the set of occupied time slots after considering the first $k$ jobs. For a job $J_{(k)}$ with deadline $d_{(k)}$, the job is added to $\mathcal{J}^*$ if and only if there exists a slot $t \in \mathcal{T}$ such that $t \leq d_{(k)}$ and $t \notin \mathcal{S}_{k-1}$.

To maximize the availability of slots for future jobs with potentially tighter deadlines, the algorithm selects the latest possible slot:
$$\sigma(J_{(k)}) = \max \{t \in \mathcal{T} \mid t \leq d_{(k)} \land t \notin \mathcal{S}_{k-1}\}$$
If the set $\{t \in \mathcal{T} \mid t \leq d_{(k)} \land t \notin \mathcal{S}_{k-1}\}$ is empty, the job $J_{(k)}$ is discarded.

### Loop Invariant
At the start of each iteration $k$ (where $k$ is the index of the sorted jobs), the set of occupied slots $\mathcal{S}_{k-1}$ represents the optimal packing of the highest-profit jobs considered thus far. The greedy choice ensures that for any subset of jobs $\mathcal{J}' \subseteq \{J_{(1)}, \dots, J_{(k)}\}$, the profit $\sum_{J \in \mathcal{J}'} p_J$ is maximized subject to the deadline constraints.

## 3. Complexity Analysis

### Time Complexity
The total time complexity $T(N)$ is the sum of the sorting phase and the scheduling phase.

1.  **Sorting:** Sorting $N$ jobs by profit takes $O(N \log N)$ comparisons.
2.  **Scheduling:** We iterate through $N$ jobs. For each job, we perform a linear scan of the `slots` array. In the worst case, for each job $J_i$, we may scan $O(D_{max})$ slots.
    $$T(N) = O(N \log N) + \sum_{i=1}^{N} O(\min(d_i, N)) = O(N \log N + N \cdot \min(N, D_{max}))$$
    Given that $D_{max}$ is often bounded by $N$ in practical instances, the worst-case complexity is $O(N^2)$. However, using a Disjoint Set Union (DSU) data structure to find the nearest available slot, the scheduling phase reduces to $O(N \alpha(N))$, where $\alpha$ is the inverse Ackermann function. Thus, the optimized complexity is $O(N \log N)$.

### Space Complexity
The algorithm requires:
1.  **Storage for Jobs:** $O(N)$ to store the job objects.
2.  **Slots Array:** $O(D_{max})$ to maintain the boolean status of time slots.

Total auxiliary space complexity is $O(N + D_{max})$. In scenarios where $D_{max} \gg N$, the effective space is limited to $O(N)$ by considering only the distinct deadlines present in the input.