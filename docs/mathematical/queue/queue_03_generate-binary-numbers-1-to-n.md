# Formal Mathematical Specification: Generate Binary Numbers 1 to N

## 1. Definitions and Notation

Let $\mathbb{N}^+ = \{1, 2, 3, \dots\}$ be the set of positive integers. We define the binary representation function $B: \mathbb{N}^+ \to \Sigma^*$, where $\Sigma = \{'0', '1'\}$, such that $B(n)$ is the unique string representation of $n$ in base 2 without leading zeros.

Let $\mathcal{Q}$ be a First-In-First-Out (FIFO) queue data structure, defined as an ordered sequence of strings $S = (s_1, s_2, \dots, s_k)$ where $s_i \in \Sigma^*$. 
- The operation $\text{enqueue}(s)$ appends $s$ to the rear of $\mathcal{Q}$.
- The operation $\text{dequeue}()$ removes and returns the element at the front of $\mathcal{Q}$.

The algorithm defines a state space $\mathcal{S} \subset \Sigma^*$ representing the set of all binary strings. We define a transition function $f: \Sigma^* \to \Sigma^* \times \Sigma^*$ such that $f(s) = (s \cdot '0', s \cdot '1')$, where $\cdot$ denotes string concatenation.

## 2. Algebraic Characterization

The algorithm constructs a sequence $L = (x_1, x_2, \dots, x_N)$ where $x_i = B(i)$. This is equivalent to a Breadth-First Search (BFS) traversal of an infinite binary tree $\mathcal{T}$ where the root is $r = '1'$ and each node $u$ has children $u \cdot '0'$ and $u \cdot '1'$.

**Loop Invariant:**
Let $q_i$ be the state of the queue at the start of iteration $i$ (for $1 \le i \le N$).
1. The set of elements in the queue $q_i$ corresponds to the nodes at the current and subsequent levels of $\mathcal{T}$ that have not yet been dequeued.
2. The sequence $L_{i-1} = (x_1, \dots, x_{i-1})$ contains the first $i-1$ binary numbers in lexicographical order, which is isomorphic to the numerical order of their integer values.

**Recurrence Relation:**
The queue evolution can be described by the state transition:
$$\mathcal{Q}_{i+1} = (\mathcal{Q}_i \setminus \{s_i\}) \cup \{s_i \cdot '0', s_i \cdot '1'\}$$
where $s_i = \text{dequeue}(\mathcal{Q}_i)$. Since the tree $\mathcal{T}$ is a complete binary tree, the level-order traversal guarantees that for any $n \in \mathbb{N}^+$, the sequence generated satisfies $val(x_i) < val(x_{i+1})$, where $val: \Sigma^* \to \mathbb{N}^+$ is the standard base-2 evaluation function.

## 3. Complexity Analysis

### Time Complexity
The algorithm executes a loop exactly $N$ times. In each iteration $i \in \{1, \dots, N\}$:
1. One `dequeue` operation: $O(1)$.
2. One `append` to result: $O(1)$.
3. Two `enqueue` operations: $O(1)$.
4. Two string concatenations: The length of the binary string $s$ is $\lfloor \log_2(i) \rfloor + 1$. Thus, concatenation takes $O(\log i)$.

The total time complexity $T(N)$ is given by the summation:
$$T(N) = \sum_{i=1}^{N} O(\log i) = O\left(\sum_{i=1}^{N} \log i\right) = O(\log(N!))$$
By Stirling's approximation, $\log(N!) \approx N \log N - N$. While the bit-wise complexity is $O(N \log N)$, in the context of standard word-RAM models where string operations are treated as amortized constant or where $N$ is bounded by machine word size, the complexity is effectively $O(N)$.

### Space Complexity
The space complexity $S(N)$ is determined by the maximum size of the queue $\mathcal{Q}$ and the result list.
1. The result list stores $N$ strings with an average length of $O(\log N)$, requiring $O(N \log N)$ bits.
2. The queue $\mathcal{Q}$ at iteration $i$ contains nodes from the current level and the next level of the tree. The number of nodes in the queue is bounded by $O(N)$. Specifically, at the end of the algorithm, the queue contains approximately $N$ elements.

Thus, the auxiliary space complexity is:
$$S(N) = O(N \cdot \text{avg\_length}) = O(N \log N)$$
In terms of the number of string objects stored, the space complexity is $O(N)$.