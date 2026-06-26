# Formal Mathematical Specification: Majority Element (Divide and Conquer)

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be an array of $n$ elements where each $a_i \in \mathcal{X}$, and $\mathcal{X}$ is a totally ordered set. 

Define the frequency function $f: \mathcal{X} \times \mathcal{P}(A) \to \mathbb{N}_0$ such that for any value $x \in \mathcal{X}$ and any subarray $S \subseteq A$, $f(x, S) = \sum_{a \in S} \mathbb{I}(a = x)$, where $\mathbb{I}(\cdot)$ is the indicator function.

The **Majority Element** $m \in \mathcal{X}$ is defined as the unique element satisfying the condition:
$$f(m, A) > \left\lfloor \frac{|A|}{2} \right\rfloor$$

We define the recursive function $\mathcal{M}(S)$ which returns the majority candidate for a subarray $S$ of length $k = |S|$. The domain of the algorithm is the set of all finite sequences over $\mathcal{X}$ that contain a majority element.

## 2. Algebraic Characterization

The correctness of the Divide and Conquer approach relies on the **Majority Lemma**: If $m$ is the majority element of $A$, and $A$ is partitioned into two disjoint subarrays $A_L$ and $A_R$ such that $A = A_L \cup A_R$, then $m$ must be the majority element of at least one of the subarrays $A_L$ or $A_R$.

### Recurrence Relation
Let $T(n)$ denote the time complexity for an input of size $n$. The algorithm is defined by the following recurrence:
$$T(n) = 2T\left(\frac{n}{2}\right) + g(n)$$
where $g(n)$ represents the cost of the merge step. The merge step involves two linear scans of the current subarray to count the occurrences of the candidates returned by the recursive calls:
$$g(n) = \Theta(n)$$

### Correctness Invariant
For a subarray $S$, let $c_L = \mathcal{M}(S_L)$ and $c_R = \mathcal{M}(S_R)$. The merge step defines the output $\mathcal{M}(S)$ as:
$$\mathcal{M}(S) = \begin{cases} c_L & \text{if } f(c_L, S) > \frac{|S|}{2} \\ c_R & \text{if } f(c_R, S) > \frac{|S|}{2} \\ \text{undefined} & \text{otherwise} \end{cases}$$
Given the problem constraint that a majority element is guaranteed to exist, the merge step is guaranteed to return a valid $m$.

## 3. Complexity Analysis

### Time Complexity
The time complexity is governed by the Master Theorem for divide-and-conquer recurrences of the form $T(n) = aT(n/b) + f(n)$.
Here, $a=2$, $b=2$, and $f(n) = O(n)$. 
Comparing $f(n) = n^1$ with $n^{\log_b a} = n^{\log_2 2} = n^1$, we fall into Case 2 of the Master Theorem.
Thus:
$$T(n) = \Theta(n^{\log_b a} \log n) = \Theta(n \log n)$$
The total work at each depth $d$ of the recursion tree is $\sum_{i=1}^{2^d} O(n/2^d) = O(n)$. Since the tree depth is $\log_2 n$, the total time complexity is $O(n \log n)$.

### Space Complexity
The space complexity $S(n)$ is determined by the maximum depth of the recursion stack. Each recursive call adds a frame to the call stack.
$$S(n) = S\left(\frac{n}{2}\right) + O(1)$$
Solving this recurrence:
$$S(n) = O(\log n)$$
The auxiliary space is dominated by the recursion stack, as the counting process in the merge step can be performed in-place using $O(1)$ additional variables. Therefore, the total space complexity is $O(\log n)$.