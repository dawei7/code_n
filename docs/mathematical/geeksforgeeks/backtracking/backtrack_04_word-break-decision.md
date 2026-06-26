# Formal Mathematical Specification: Word Break II (Backtracking)

This document provides a rigorous mathematical specification of the **Word Break II** algorithm using backtracking. While the basic feasibility problem (Word Break I) determines if a valid segmentation exists, Word Break II requires generating the complete set of all valid segmentations.

---

## 1. Definitions and Notation

### 1.1 Alphabets and Strings
Let $\Sigma$ be a finite, non-empty set of characters called the *alphabet*. 
* A *string* $s$ of length $N \in \mathbb{N}_0$ is a sequence of characters $(s_0, s_1, \dots, s_{N-1}) \in \Sigma^N$. We write $s \in \Sigma^*$ to denote that $s$ belongs to the Kleene closure of $\Sigma$.
* The length of $s$ is denoted by $|s| = N$.
* The empty string is denoted by $\epsilon$, where $|\epsilon| = 0$.
* For $0 \le i \le j \le N$, the *substring* $s[i:j]$ is defined as:
  $$s[i:j] = \begin{cases} 
  s_i s_{i+1} \dots s_{j-1} & \text{if } i < j \\
  \epsilon & \text{if } i = j 
  \end{cases}$$

### 1.2 The Dictionary
Let $D \subset \Sigma^+$ be a finite set of non-empty strings representing the *dictionary*, where $\Sigma^+ = \Sigma^* \setminus \{\epsilon\}$.

### 1.3 Concatenation and Joining
* Let $\cdot : \Sigma^* \times \Sigma^* \to \Sigma^*$ denote the string concatenation operator, where $u \cdot v$ (or simply $uv$) represents the concatenation of strings $u$ and $v$.
* For a sequence of strings $\alpha = (w_1, w_2, \dots, w_k) \in (\Sigma^*)^k$, we define the concatenation product:
  $$\prod_{m=1}^k w_m = w_1 \cdot w_2 \cdots w_k$$
* We define the space-joining operator $\text{join} : (\Sigma^*)^k \to \Sigma^*$ as:
  $$\text{join}(w_1, w_2, \dots, w_k) = \begin{cases}
  w_1 & \text{if } k = 1 \\
  w_1 \cdot \text{" "} \cdot \text{join}(w_2, \dots, w_k) & \text{if } k > 1
  \end{cases}$$

### 1.4 The Solution Space
Given an input string $s \in \Sigma^*$ of length $N$ and a dictionary $D$, the set of all valid segmentations $\mathcal{P}(s, D)$ is defined as:
$$\mathcal{P}(s, D) = \left\{ (w_1, w_2, \dots, w_k) \in D^k \;\middle|\; k \ge 1, \;\; \prod_{m=1}^k w_m = s \right\}$$

The target output of the Word Break II algorithm is the set of space-separated sentences $\mathcal{O}(s, D)$, defined as:
$$\mathcal{O}(s, D) = \left\{ \text{join}(\mathbf{w}) \;\middle|\; \mathbf{w} \in \mathcal{P}(s, D) \right\}$$

---

## 2. Algebraic Characterization

The backtracking algorithm systematically explores the search space of prefixes to construct $\mathcal{O}(s, D)$. This can be modeled recursively using set-valued functions and state-space transitions.

### 2.1 Recursive Formulation
Let $S(i)$ denote the set of all valid segmentations of the suffix $s[i:N]$ for $0 \le i \le N$. We define $S(i)$ recursively as:

$$S(i) = \begin{cases} 
\{ () \} & \text{if } i = N \\
\bigcup_{j=i+1}^{N} \left\{ (s[i:j]) \cdot \sigma \;\middle|\; s[i:j] \in D \land \sigma \in S(j) \right\} & \text{if } i < N 
\end{cases}$$

where $()$ is the empty sequence, and for a word $w \in D$ and a sequence of words $\sigma = (u_1, \dots, u_p)$, the operation $w \cdot \sigma$ denotes the prepending of $w$ to the sequence, yielding $(w, u_1, \dots, u_p)$.

The complete set of valid segmentations for the entire string is given by $S(0) = \mathcal{P}(s, D)$.

### 2.2 State-Space Representation
The backtracking execution can be formalized as a Depth-First Search (DFS) over a state-transition Directed Acyclic Graph (DAG) $\mathcal{G} = (\mathcal{V}, \mathcal{E})$.

* **State Space ($\mathcal{V}$):** A state is a tuple $(i, \alpha) \in \mathcal{V}$, where:
  * $i \in \{0, 1, \dots, N\}$ represents the current boundary index in $s$.
  * $\alpha = (w_1, \dots, w_m) \in D^m$ is the sequence of words successfully parsed from the prefix $s[0:i]$, such that $\prod_{r=1}^m w_r = s[0:i]$.
* **Initial State:** $s_{\text{start}} = (0, ())$.
* **Terminal States:** $\mathcal{T} = \{ (N, \alpha) \in \mathcal{V} \}$. For any terminal state $(N, \alpha)$, the sequence $\alpha$ is a valid segmentation of $s$, and $\text{join}(\alpha) \in \mathcal{O}(s, D)$.
* **Transition Relation ($\mathcal{E}$):** A directed edge exists from state $(i, \alpha)$ to $(j, \beta)$ if and only if:
  $$i < j \le N \quad \land \quad s[i:j] \in D \quad \land \quad \beta = \alpha \cdot (s[i:j])$$

Because $j > i$ for every transition, the graph $\mathcal{G}$ contains no cycles, ensuring that the backtracking search terminates.

### 2.3 Memoized Algebraic Formulation (DP-Hybrid)
To prevent redundant exploration of identical suffixes, we define a memoized function $f: \{0, \dots, N\} \to \mathcal{P}(\Sigma^*)$ that maps each suffix index $i$ to its set of valid space-separated suffix segmentations:

$$f(i) = \begin{cases}
\{ \epsilon \} & \text{if } i = N \\
\bigcup_{\substack{j=i+1 \\ s[i:j] \in D}}^{N} \left\{ s[i:j] \cdot \Phi(\sigma) \;\middle|\; \sigma \in f(j) \right\} & \text{if } i < N
\end{cases}$$

where the formatting operator $\Phi: \Sigma^* \to \Sigma^*$ is defined as:
$$\Phi(\sigma) = \begin{cases} 
\epsilon & \text{if } \sigma = \epsilon \\
\text{" "} \cdot \sigma & \text{otherwise}
\end{cases}$$

---

## 3. Complexity Analysis

Let $N = |s|$ be the length of the input string, and let $M = |D|$ be the number of words in the dictionary. Let $L$ be the maximum length of any word in $D$.

### 3.1 Time Complexity

#### Worst-Case Analysis (Without Memoization)
Consider the worst-case input where $s = a^N$ (a string of $N$ identical characters) and the dictionary contains all possible prefixes:
$$D = \{a, a^2, a^3, \dots, a^N\}$$

Under these conditions, every substring $s[i:j]$ is a valid dictionary word. 
1. **Number of Valid Segmentations:**
   The number of ways to partition a string of length $N$ is equivalent to placing a binary choice (cut or no cut) at each of the $N-1$ internal character boundaries. Thus, the total number of valid segmentations is:
   $$|\mathcal{P}(s, D)| = 2^{N-1}$$

2. **Work Done by Backtracking:**
   The recursion tree has $2^{N-1}$ leaf nodes. At each leaf node, the algorithm constructs a space-separated string of length $O(N)$ by joining the chosen words. This string construction takes $\Theta(N)$ time.
   The total time complexity to generate and output all solutions is:
   $$T(N) = \sum_{k=1}^{N} \binom{N-1}{k-1} \cdot O(N) = O(N \cdot 2^N)$$

#### Worst-Case Analysis (With Memoization / DP-Hybrid)
If the string cannot be segmented (e.g., $s = a^N$ and $D = \{b\}$), pure backtracking without memoization can still take exponential time if there are overlapping partial matches. 

With memoization:
1. There are $N+1$ unique states (indices $0$ to $N$).
2. For each state $i$, we iterate through $j \in \{i+1, \dots, \min(i+L, N)\}$, performing a substring slice of length at most $L$ and a dictionary lookup. Using a Hash Set or Trie, the lookup takes $O(L)$ time.
3. If no valid segmentation exists, the state space is pruned, and the algorithm terminates in:
   $$T_{\text{fail}}(N) = O(N \cdot L^2) \subseteq O(N^2) \text{ time}$$
4. If valid segmentations exist, we must still construct the output. The time complexity is dominated by the size of the output set, which remains $O(N \cdot 2^N)$ in the worst case.

Thus, the overall worst-case time complexity is:
$$\Theta(N^2 + N \cdot 2^N)$$

### 3.2 Space Complexity

#### Auxiliary Space (Recursion Stack)
The maximum depth of the recursion tree occurs when the string is segmented into $N$ individual characters of length $1$. The maximum call stack depth is:
$$S_{\text{stack}}(N) = O(N)$$

#### Auxiliary Space (Memoization Table)
The memoization table stores the set of valid suffix segmentations $f(i)$ for each index $i \in \{0, \dots, N\}$.
In the worst-case scenario ($s = a^N$, $D = \{a, \dots, a^N\}$), the size of the set $f(i)$ is $2^{N-1-i}$, and each string in $f(i)$ has an average length of $O(N-i)$.
The total memory required to store the memoization table is:
$$S_{\text{memo}}(N) = \sum_{i=0}^{N} |f(i)| \cdot O(N-i) = \sum_{i=0}^{N} 2^{N-1-i} \cdot O(N-i) = O(2^N)$$

#### Total Space Complexity
Including the memory required to store the final output list $\mathcal{O}(s, D)$, which contains $2^{N-1}$ sentences of average length $O(N)$, the total space complexity is:
$$S_{\text{total}}(N) = O(N + 2^N) \text{ Auxiliary Space (excluding output)}$$
$$S_{\text{total}}(N) = O(N \cdot 2^N) \text{ Total Space (including output)}$$