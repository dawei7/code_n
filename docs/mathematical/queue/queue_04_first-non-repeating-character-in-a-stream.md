# Formal Mathematical Specification: First Non-repeating Character in a Stream

## 1. Definitions and Notation

Let $\Sigma$ be a finite alphabet (e.g., $\Sigma = \{a, b, \dots, z\}$). A stream is represented as a sequence $S = (s_1, s_2, \dots, s_n)$, where $s_i \in \Sigma$. 

We define the following structures to maintain the state of the stream at index $k$:
*   **Frequency Map:** A function $f_k: \Sigma \to \mathbb{N}_0$, where $f_k(c) = |\{i \in \{1, \dots, k\} : s_i = c\}|$.
*   **Chronological Queue:** An ordered sequence $Q_k = (q_1, q_2, \dots, q_m)$ containing elements $c \in \Sigma$ such that $f_k(c) = 1$. The elements in $Q_k$ are ordered by their first appearance in the stream $S$.
*   **Output Function:** A mapping $O: \{1, \dots, n\} \to \Sigma \cup \{\#\}$, defined as:
    $$O(k) = \begin{cases} q_1 & \text{if } Q_k \neq \emptyset \\ \# & \text{if } Q_k = \emptyset \end{cases}$$

## 2. Algebraic Characterization

The state transition from $k-1$ to $k$ involves the arrival of character $s_k$. The update rules are defined as follows:

1.  **Frequency Update:**
    $$f_k(c) = f_{k-1}(c) + \delta_{c, s_k}$$
    where $\delta_{i,j}$ is the Kronecker delta.

2.  **Queue Evolution:**
    Let $Q'_k$ be the intermediate queue after appending $s_k$ if $f_k(s_k) = 1$:
    $$Q'_k = \begin{cases} Q_{k-1} \cdot (s_k) & \text{if } f_k(s_k) = 1 \\ Q_{k-1} & \text{if } f_k(s_k) > 1 \end{cases}$$
    
    The final queue $Q_k$ is obtained by removing all elements from the front of $Q'_k$ that have become non-unique:
    $$Q_k = \text{dropwhile}(c \in Q'_k \mid f_k(c) > 1)$$
    Formally, $Q_k = (q_j, q_{j+1}, \dots, q_m)$ where $j$ is the smallest index such that $f_k(q_j) = 1$. If no such $j$ exists, $Q_k = \emptyset$.

**Loop Invariant:** At any step $k$, the queue $Q_k$ contains exactly the set of characters $\{c \in \Sigma : f_k(c) = 1\}$, ordered by their first occurrence index $i = \min \{t : s_t = c\}$.

## 3. Complexity Analysis

### Time Complexity
Let $T(n)$ be the total time complexity for a stream of length $n$. The algorithm performs $n$ iterations. In each iteration $k$:
1.  Updating $f_k$ takes $O(1)$ time.
2.  Appending to $Q$ takes $O(1)$ time.
3.  The `while` loop removes elements from the front of the queue. 

To derive the amortized cost, we use the aggregate method. Each character $s_i$ is added to the queue at most once (when $f_i(s_i)=1$) and removed from the queue at most once (when $f_k(s_i) > 1$). Let $N_{push}$ be the total number of push operations and $N_{pop}$ be the total number of pop operations.
$$\sum_{k=1}^n (\text{cost of iteration } k) = \sum_{k=1}^n (O(1) + \text{cost of pops}_k)$$
Since $N_{push} = n$ and $N_{pop} \leq n$, the total time is $O(n)$. Thus, the amortized time complexity per character is:
$$\frac{O(n)}{n} = O(1)$$

### Space Complexity
The space complexity is determined by the storage of the frequency map and the queue.
*   **Frequency Map:** Stores at most $|\Sigma|$ entries.
*   **Queue:** Stores at most $|\Sigma|$ entries, as it only contains unique characters.

Given $|\Sigma|$ is a constant (e.g., 256 for extended ASCII), the auxiliary space complexity is:
$$S(n) = O(|\Sigma|) = O(1)$$
The total space complexity, including the input and output storage, is $O(n)$. However, the auxiliary space required for the algorithm's state is strictly bounded by the size of the alphabet, independent of the stream length $n$.