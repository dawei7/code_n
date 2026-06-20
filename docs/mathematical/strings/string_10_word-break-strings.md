# Formal Mathematical Specification: Word Break

## 1. Definitions and Notation
Let $S \in \Sigma^*$ be a string of length $n$ and $\mathcal{D} \subset \Sigma^*$ be a dictionary.
We define a predicate $W(i)$ representing whether the prefix $S[1 \dots i]$ can be segmented into a space-separated sequence of one or more dictionary words.

## 2. Algebraic Characterization
Base case: $W(0) = \text{True}$ (the empty string is trivially valid).
For $1 \leq i \leq n$, the recurrence is:
$$ W(i) = \bigvee_{j=0}^{i-1} \Big( W(j) \land (S[j+1 \dots i] \in \mathcal{D}) \Big) $$

## 3. Complexity Analysis
- **Time Complexity:** Evaluating $W(i)$ for all $i$ requires iterating over $j < i$. There are $n(n-1)/2$ state evaluations. Checking $S[j+1 \dots i] \in \mathcal{D}$ via a hash set takes time proportional to the substring length $O(i-j)$. The mathematically strict upper bound is $O(n^3)$. (If substring hashing or a Trie is used, it can be reduced to $O(n^2)$).
- **Space Complexity:** The boolean array $W$ requires $O(n)$ space. The dictionary $\mathcal{D}$ is stored externally, requiring $O(\sum_{w \in \mathcal{D}} |w|)$ space.
