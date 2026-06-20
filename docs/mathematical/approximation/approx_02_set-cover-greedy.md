# Formal Mathematical Specification: Set Cover (Greedy Approximation)

## 1. Definitions and Notation

Let the problem instance be defined by a tuple $(U, \mathcal{S})$, where:
*   $U = \{u_1, u_2, \dots, u_n\}$ is a finite set of elements called the **universe**, with cardinality $|U| = n \in \mathbb{N}^+$.
*   $\mathcal{S} = \{S_1, S_2, \dots, S_m\}$ is a family of non-empty subsets of $U$, where $m = |\mathcal{S}| \in \mathbb{N}^+$, such that $\bigcup_{i=1}^m S_i = U$.
*   $I = \{1, 2, \dots, m\}$ is the index set of the family $\mathcal{S}$.

### Definition 1.1: Set Cover
A subset of indices $J \subseteq I$ is a **set cover** of $U$ if and only if:
$$\bigcup_{j \in J} S_j = U$$

### Definition 1.2: Optimal Set Cover
The optimization objective is to find a set cover $J^*$ of minimum cardinality. We define the optimal index set $J^*$ as:
$$J^* \in \arg\min_{J \subseteq I} \left\{ |J| \;\middle|\; \bigcup_{j \in J} S_j = U \right\}$$
We denote the size of the optimal cover as $OPT = |J^*|$.

### Definition 1.3: State Space
The state of the greedy algorithm at any step $t \in \mathbb{N}$ is represented by the tuple $(U_t, J_t) \in \mathcal{P}(U) \times \mathcal{P}(I)$, where:
*   $U_t \subseteq U$ is the set of elements remaining **uncovered** at step $t$.
*   $J_t \subseteq I$ is the set of indices of the subsets **selected** up to step $t$.

The initial state is defined as:
$$(U_0, J_0) = (U, \emptyset)$$

The algorithm terminates at step $T$ when the terminal state $(U_T, J_T)$ satisfies $U_T = \emptyset$.

---

## 2. Algebraic Characterization

### 2.1 The Greedy Choice Function
At each step $t \ge 0$, the algorithm selects an index $j_{t+1} \in I \setminus J_t$ that maximizes the number of newly covered elements. Let $f: I \times \mathcal{P}(U) \to \mathbb{N}$ be the coverage function defined by:
$$f(j, U_t) = |S_j \cap U_t|$$

The greedy choice at step $t+1$ is given by:
$$j_{t+1} = \arg\max_{j \in I \setminus J_t} f(j, U_t)$$

To ensure determinism, we assume a total ordering on $I$ such that ties are broken by selecting the lexicographically smallest index:
$$j_{t+1} = \min \left( \arg\max_{j \in I \setminus J_t} f(j, U_t) \right)$$

### 2.2 State Transition Relations
The state transitions from step $t$ to $t+1$ are governed by the following recurrence relations:
$$J_{t+1} = J_t \cup \{j_{t+1}\}$$
$$U_{t+1} = U_t \setminus S_{j_{t+1}}$$

### 2.3 Loop Invariants
For any step $t \in \{0, 1, \dots, T\}$, the following invariants hold:
1.  **Set Cover Progress:** $U_t = U \setminus \left( \bigcup_{j \in J_t} S_j \right)$.
2.  **Cardinality Monotonicity:** $|J_t| = t$.
3.  **Termination Guarantee:** $U_t = \emptyset \iff t = T$. Since $U$ is finite and $\bigcup_{i=1}^m S_i = U$, the sequence of uncovered sets is strictly nested: $U_0 \supset U_1 \supset \dots \supset U_T = \emptyset$, ensuring $T \le n$.

### 2.4 Mathematical Proof of the Approximation Ratio
Let $H_d = \sum_{i=1}^d \frac{1}{i}$ denote the $d$-th harmonic number. We prove that the greedy algorithm achieves an approximation ratio of $H_g$, where $g = \max_{j \in I} |S_j|$.

**Theorem:** Let $J_T$ be the cover returned by the greedy algorithm, and let $J^*$ be an optimal cover. Then:
$$|J_T| \le H_g \cdot |J^*| \le H_n \cdot |J^*|$$

*Proof:*
We use the price-method (dual fitting) formulation. Let a total cost of $1$ be charged to the algorithm for each set selected. When set $S_{j_{t+1}}$ is selected at step $t+1$, we distribute its unit cost equally among the newly covered elements. For each element $x \in U$, let $c_x$ denote the cost allocated to $x$. If $x \in S_{j_{t+1}} \cap U_t$, then:
$$c_x = \frac{1}{|S_{j_{t+1}} \cap U_t|}$$

Because the elements partition the cost of each selected set, the total cost of the greedy cover is:
$$\sum_{x \in U} c_x = \sum_{t=0}^{T-1} \sum_{x \in S_{j_{t+1}} \cap U_t} c_x = \sum_{t=0}^{T-1} 1 = T = |J_T|$$

Now, consider any set $S \in \mathcal{S}$ (including those in the optimal cover $J^*$). Let the elements of $S$ be ordered in the sequence they are covered by the greedy algorithm: $x_1, x_2, \dots, x_k$, where $k = |S| \le g$. 

When element $x_i$ is covered (say, at step $t+1$), the elements $\{x_i, x_{i+1}, \dots, x_k\}$ must still be uncovered. Thus, $|S \cap U_t| \ge k - i + 1$. By the definition of the greedy choice, the selected set $S_{j_{t+1}}$ must satisfy:
$$|S_{j_{t+1}} \cap U_t| \ge |S \cap U_t| \ge k - i + 1$$

Consequently, the cost allocated to $x_i$ is bounded by:
$$c_{x_i} = \frac{1}{|S_{j_{t+1}} \cap U_t|} \le \frac{1}{k - i + 1}$$

Summing the costs over all elements in $S$:
$$\sum_{x \in S} c_x = \sum_{i=1}^k c_{x_i} \le \sum_{i=1}^k \frac{1}{k - i + 1} = \sum_{p=1}^k \frac{1}{p} = H_k \le H_g$$

Since $J^*$ is a valid cover of $U$, we can write:
$$|J_T| = \sum_{x \in U} c_x \le \sum_{S \in \mathcal{S}_{J^*}} \sum_{x \in S} c_x \le \sum_{S \in \mathcal{S}_{J^*}} H_{|S|} \le |J^*| \cdot H_g$$
where $\mathcal{S}_{J^*} = \{S_j \mid j \in J^*\}$. This completes the proof. $\blacksquare$

---

## 3. Complexity Analysis

Let $N = |U|$ be the size of the universe, and $S = |\mathcal{S}|$ be the number of subsets. Let $L = \sum_{i=1}^S |S_i|$ represent the total size of the input representation.

### 3.1 Time Complexity

#### Naive Implementation (as provided in the Python code)
In the provided implementation, the algorithm performs the following operations:
1.  **Initialization:** Creating the `uncovered` set takes $\Theta(N)$ time.
2.  **Outer Loop:** Runs at most $T \le N$ times.
3.  **Inner Loop:** In each iteration of the outer loop, the algorithm iterates over all $S$ subsets. For each subset $S_i$, it computes the intersection size with the `uncovered` set:
    $$\text{Work per subset } S_i = \sum_{x \in S_i} O(1) = O(|S_i|)$$
    Summing over all subsets, the work done in one iteration of the outer loop is:
    $$\sum_{i=1}^S O(|S_i|) = O(L)$$
4.  **State Update:** Discarding elements of the chosen set $S_{j^*}$ from `uncovered` takes $O(|S_{j^*}|) = O(N)$ time.

Thus, the total worst-case time complexity of the naive implementation is:
$$\mathcal{T}_{\text{naive}}(N, S) = O(N) + \sum_{t=1}^T \left( O(L) + O(|S_{j_t}|) \right) = O(T \cdot L) = O(N \cdot L)$$

Since $L \le S \cdot N$, the worst-case time complexity is:
$$\mathcal{T}_{\text{naive}}(N, S) = O(S \cdot N^2)$$

#### Optimal $O(S \cdot N)$ Implementation
The time complexity can be optimized to $O(L)$ (which is $O(S \cdot N)$ in the worst case) by avoiding redundant intersection computations:
1.  **Inverted Index Construction:** Construct a mapping from each element $x \in U$ to the list of subset indices containing $x$. This takes $O(L)$ time.
2.  **Active Tracking:** Maintain an array `count` of size $S$, where `count[i]` stores $|S_i \cap U_t|$.
3.  **Bucket Queue:** Store the subsets in an array of buckets indexed by their current coverage count (since counts are integers in $[0, N]$). This allows $O(1)$ retrieval of the subset with the maximum count.
4.  **Updates:** When a subset $S_{j^*}$ is selected, for each element $x \in S_{j^*} \cap U_t$, we find all subsets $S_i$ containing $x$ using the inverted index, decrement their counts, and update their positions in the bucket queue. Each element is processed this way at most once when it transitions from uncovered to covered.

The total work for updates across the entire execution is bounded by:
$$\sum_{x \in U} \sum_{i : x \in S_i} O(1) = O(L)$$

Thus, the optimized time complexity is:
$$\mathcal{T}_{\text{optimal}}(N, S) = \Theta(S + N + L) = O(S \cdot N)$$

### 3.2 Space Complexity

#### Auxiliary Space
The auxiliary space is the memory allocated for state tracking, excluding the input representation:
*   `uncovered` set: Stores at most $N$ elements, requiring $O(N)$ space.
*   `chosen` list: Stores at most $S$ indices, requiring $O(S)$ space.
*   Temporary variables for loop execution: $O(1)$ space.

Thus, the auxiliary space complexity is:
$$\mathcal{S}_{\text{aux}}(N, S) = O(N + S)$$

#### Total Space
The total space complexity includes the input representation $\mathcal{S}$ and the universe $U$:
$$\mathcal{S}_{\text{total}}(N, S) = O\left( N + \sum_{i=1}^S |S_i| \right) = O(N + L)$$

In the worst-case scenario where each subset contains a constant fraction of the universe, $L = \Theta(S \cdot N)$, yielding:
$$\mathcal{S}_{\text{total}}(N, S) = O(S \cdot N)$$