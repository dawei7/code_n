# Formal Mathematical Specification: Anagram Equivalence

## 1. Definitions and Notation
Let $\Sigma$ be a finite alphabet. Let $S, T \in \Sigma^*$ be two strings of lengths $n = |S|$ and $m = |T|$.
A string $S$ is defined as an ordered sequence of characters $S = (s_1, s_2, \dots, s_n)$ where $s_i \in \Sigma$.

Let $\Pi_n$ be the symmetric group of all permutations on $n$ elements.
Two strings $S$ and $T$ are defined to be **anagrams** (denoted $S \sim T$) if and only if:
1. $n = m$
2. $\exists \pi \in \Pi_n$ such that $\forall i \in \{1, \dots, n\}, s_i = t_{\pi(i)}$

## 2. Algebraic Characterization via Frequency Vectors
For any string $S$, define its **frequency vector** $\mathbf{v}_S \in \mathbb{N}^{|\Sigma|}$ such that the component corresponding to character $c \in \Sigma$ is:
$$ \mathbf{v}_S(c) = \sum_{i=1}^n \mathbb{I}(s_i = c) $$
where $\mathbb{I}$ is the indicator function.

**Theorem 1:** $S \sim T \iff \mathbf{v}_S = \mathbf{v}_T$

**Proof:**
($\implies$) Assume $S \sim T$. Then $|S| = |T| = n$ and there exists a bijection $\pi : \{1..n\} \to \{1..n\}$ such that $s_i = t_{\pi(i)}$. For any $c \in \Sigma$, the number of occurrences in $S$ is exactly the number of indices $i$ where $s_i = c$. Since $\pi$ is bijective, mapping $i \mapsto \pi(i)$ preserves the cardinality of the set of indices. Thus $\mathbf{v}_S(c) = \mathbf{v}_T(c)$.
($\impliedby$) Assume $\mathbf{v}_S = \mathbf{v}_T$. Let $n = \sum_{c \in \Sigma} \mathbf{v}_S(c)$. Since the total length is the same, $|S| = |T| = n$. Because every character $c$ appears the exact same number of times in $S$ and $T$, we can construct a bijection $\pi$ by mapping the $k$-th occurrence of $c$ in $S$ to the $k$-th occurrence of $c$ in $T$. Thus $S \sim T$. $\blacksquare$

## 3. Algorithm Formalization
The optimal algorithm computes the difference vector $\mathbf{\Delta} = \mathbf{v}_S - \mathbf{v}_T$.
By Theorem 1, $S \sim T \iff \mathbf{\Delta} = \mathbf{0}$.

We define the state at step $k$ (for $1 \leq k \leq n$) as $\mathbf{\Delta}^{(k)} \in \mathbb{Z}^{|\Sigma|}$, with the recurrence:
$$ \mathbf{\Delta}^{(0)} = \mathbf{0} $$
$$ \mathbf{\Delta}^{(k)}(c) = \mathbf{\Delta}^{(k-1)}(c) + \mathbb{I}(s_k = c) - \mathbb{I}(t_k = c) $$

The algorithm asserts that $\mathbf{\Delta}^{(n)} = \mathbf{0}$.

## 4. Complexity Analysis
- **Time Complexity:** The recurrence relation is evaluated $n$ times. Each evaluation involves two $O(1)$ operations (vector element access and arithmetic). Verifying $\mathbf{\Delta}^{(n)} = \mathbf{0}$ requires iterating over $|\Sigma|$ elements. Thus, the time complexity is strictly bounded by $O(n + |\Sigma|)$.
- **Space Complexity:** The algorithm maintains exactly one state vector $\mathbf{\Delta}$ in $\mathbb{Z}^{|\Sigma|}$. The space complexity is exactly $O(|\Sigma|)$, which is $O(1)$ with respect to $n$.
