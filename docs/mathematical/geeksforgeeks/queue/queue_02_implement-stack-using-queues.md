# Formal Mathematical Specification: Implement Stack using Queues

## 1. Definitions and Notation

Let $\mathcal{Q}$ be a FIFO (First-In, First-Out) queue, defined as an ordered sequence of elements $q = (e_1, e_2, \dots, e_n)$ where $e_1$ is the front and $e_n$ is the back. We define the following primitive operations on $\mathcal{Q}$:
*   $\text{enqueue}(x)$: Maps $\mathcal{Q} \to \mathcal{Q}'$ such that $\mathcal{Q}' = (e_1, \dots, e_n, x)$.
*   $\text{dequeue}()$: Maps $\mathcal{Q} \to \mathcal{Q}'$ such that $\mathcal{Q}' = (e_2, \dots, e_n)$, returning $e_1$.
*   $\text{size}(\mathcal{Q}) = n$.
*   $\text{peek}(\mathcal{Q}) = e_1$.

Let $\mathcal{S}$ be a LIFO (Last-In, First-Out) stack, defined as an ordered sequence $s = (a_1, a_2, \dots, a_n)$ where $a_n$ is the top (the most recently added element). We define the stack operations:
*   $\text{push}(x)$: Maps $\mathcal{S} \to \mathcal{S}'$ such that $\mathcal{S}' = (a_1, \dots, a_n, x)$.
*   $\text{pop}()$: Maps $\mathcal{S} \to \mathcal{S}'$ such that $\mathcal{S}' = (a_1, \dots, a_{n-1})$, returning $a_n$.
*   $\text{top}()$: Returns $a_n$.

The objective is to define a mapping $f: \mathcal{S} \to \mathcal{Q}$ such that the LIFO property of $\mathcal{S}$ is preserved by the FIFO operations of $\mathcal{Q}$.

## 2. Algebraic Characterization

To maintain the stack invariant where the most recently pushed element $x$ occupies the front position of the queue, we define the state transition for $\text{push}(x)$ as follows:

Given a queue $\mathcal{Q}$ of size $n$, let $\mathcal{Q}_0 = (e_1, e_2, \dots, e_n)$.
1.  Perform $\text{enqueue}(x)$, resulting in $\mathcal{Q}_1 = (e_1, e_2, \dots, e_n, x)$.
2.  For $i = 1$ to $n$:
    *   Let $y = \text{dequeue}(\mathcal{Q}_i)$.
    *   Perform $\text{enqueue}(y)$.
    *   $\mathcal{Q}_{i+1} = (e_2, \dots, e_n, x, e_1, \dots, e_i)$.

After $n$ rotations, the state becomes $\mathcal{Q}_{n+1} = (x, e_1, e_2, \dots, e_n)$. 

**Invariant:** At the completion of any $\text{push}(x)$ operation, the queue $\mathcal{Q}$ is a permutation of the stack $\mathcal{S}$ such that $\text{peek}(\mathcal{Q}) = \text{top}(\mathcal{S})$. Specifically, if $\mathcal{S} = (a_1, a_2, \dots, a_n)$, then $\mathcal{Q} = (a_n, a_{n-1}, \dots, a_1)$.

The correctness of the stack operations is then trivial:
*   $\text{top}(\mathcal{S}) \equiv \text{peek}(\mathcal{Q})$
*   $\text{pop}(\mathcal{S}) \equiv \text{dequeue}(\mathcal{Q})$

## 3. Complexity Analysis

### Time Complexity
Let $N$ be the number of elements currently in the stack.

*   **Push Operation:** The algorithm performs one $\text{enqueue}$ operation followed by $N$ $\text{dequeue}$ and $\text{enqueue}$ operations. The total number of primitive queue operations is $1 + 2N$. Since each primitive operation is $O(1)$, the time complexity is:
    $$T_{\text{push}}(N) = \sum_{i=1}^{N} O(1) = O(N)$$
*   **Pop/Top Operations:** These operations consist of a single $\text{dequeue}$ or $\text{peek}$ operation respectively.
    $$T_{\text{pop}}(N) = O(1), \quad T_{\text{top}}(N) = O(1)$$

The worst-case time complexity for a sequence of $M$ operations, where $K$ are pushes, is $O(M \cdot K)$, which simplifies to $O(N^2)$ for $N$ total operations.

### Space Complexity
The algorithm utilizes a single queue to store $N$ elements. No additional data structures are required beyond the storage for the elements themselves.
*   **Auxiliary Space:** $O(1)$ (excluding the space required to store the $N$ elements).
*   **Total Space:** $O(N)$, where $N$ is the maximum number of elements in the stack at any given time.