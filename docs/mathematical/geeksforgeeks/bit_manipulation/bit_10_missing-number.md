# Formal Mathematical Specification: Missing Number

## 1. Definitions and Notation

Let $A$ be the input array, denoted as a sequence of integers $A = (a_0, a_1, \ldots, a_{n-1})$.
The length of the array is $n \in \mathbb{N}$, where $n \ge 0$.

The problem specifies the following properties for the input:
*   The elements $a_i$ are distinct integers.
*   The range of these integers is $[0, n]$, meaning $a_i \in \{0, 1, \ldots, n\}$ for all $i \in \{0, 1, \ldots, n-1\}$.
*   There are $n$ distinct numbers in the array $A$, chosen from the set of $n+1$ integers $\{0, 1, \ldots, n\}$. Consequently, exactly one number from this set is missing from $A$.

Let $S_{expected}$ be the complete set of integers in the specified range:
$S_{expected} = \{k \in \mathbb{Z} \mid 0 \le k \le n\} = \{0, 1, \ldots, n\}$.

Let $S_{actual}$ be the set of integers present in the input array $A$:
$S_{actual} = \{a_i \mid i \in \{0, 1, \ldots, n-1\}\}$.

The output of the algorithm is the unique integer $m$ that is missing from the array $A$. Formally, $m$ is defined as:
$m = S_{expected} \setminus S_{actual}$.
By the problem statement, $m$ is guaranteed to be a single element.

We use the following notation for the bitwise XOR operation: $\oplus$.
The algorithm employs an accumulator variable, denoted $R$, initialized to $n$.
The loop index is $i \in \{0, 1, \ldots, n-1\}$.
The element at index $i$ in the array is $a_i$.

## 2. Algebraic Characterization

The correctness of the algorithm relies on the fundamental properties of the bitwise XOR operation:
1.  **Commutativity:** For any integers $x, y$, $x \oplus y = y \oplus x$.
2.  **Associativity:** For any integers $x, y, z$, $(x \oplus y) \oplus z = x \oplus (y \oplus z)$.
3.  **Identity Element:** For any integer $x$, $x \oplus 0 = x$.
4.  **Self-Inverse Property:** For any integer $x$, $x \oplus x = 0$.

The algorithm initializes an accumulator $R$ with the value $n$.
$R_0 = n$.

It then iterates through the array $A$ from $i=0$ to $n-1$, updating $R$ in each step:
$R_{i+1} = R_i \oplus i \oplus a_i$.

The final value of the accumulator, $R_f$, after $n$ iterations, can be expressed as the XOR sum of all terms:
$R_f = n \oplus \left( \bigoplus_{i=0}^{n-1} i \right) \oplus \left( \bigoplus_{i=0}^{n-1} a_i \right)$.

Let's analyze each component of this XOR sum:
*   The term $n$ is the initial value.
*   The term $\bigoplus_{i=0}^{n-1} i$ represents the XOR sum of all indices from $0$ to $n-1$.
*   The term $\bigoplus_{i=0}^{n-1} a_i$ represents the XOR sum of all elements present in the input array $A$.

Combining the initial value $n$ with the XOR sum of indices, we get the XOR sum of all numbers in the expected range $S_{expected}$:
$\bigoplus_{k=0}^{n} k = n \oplus \left( \bigoplus_{i=0}^{n-1} i \right)$.

Therefore, the final accumulator value $R_f$ can be rewritten as:
$R_f = \left( \bigoplus_{k=0}^{n} k \right) \oplus \left( \bigoplus_{i=0}^{n-1} a_i \right)$.

Let $X_{expected} = \bigoplus_{k \in S_{expected}} k = \bigoplus_{k=0}^{n} k$.
Let $X_{actual} = \bigoplus_{k \in S_{actual}} k = \bigoplus_{i=0}^{n-1} a_i$.

So, $R_f = X_{expected} \oplus X_{actual}$.

By definition, $S_{expected} = S_{actual} \cup \{m\}$, where $m$ is the unique missing number.
Due to the properties of XOR (commutativity and associativity), the XOR sum over a set can be decomposed:
$X_{expected} = \left( \bigoplus_{k \in S_{actual}} k \right) \oplus m = X_{actual} \oplus m$.

Substituting this into the expression for $R_f$:
$R_f = (X_{actual} \oplus m) \oplus X_{actual}$.

Using the commutativity and associativity of XOR:
$R_f = (X_{actual} \oplus X_{actual}) \oplus m$.

Applying the self-inverse property ($x \oplus x = 0$):
$R_f = 0 \oplus m$.

Finally, applying the identity property ($x \oplus 0 = x$):
$R_f = m$.

Thus, the algorithm correctly computes the missing number $m$.

## 3. Complexity Analysis

### Time Complexity

Let $T(n)$ denote the time complexity of the algorithm for an input array of length $n$.

1.  **Initialization:** The assignment `result = n` involves a single constant-time operation. This contributes $O(1)$ to the total time.
2.  **Loop Execution:** The `for` loop iterates $n$ times, for $i$ from $0$ to $n-1$.
    *   In each iteration, `enumerate(arr)` provides the index $i$ and the value $v = a_i$. This is a constant-time operation for each element.
    *   The core operation `result ^= i ^ v` involves two bitwise XOR operations. Assuming that integers fit within a machine word, each XOR operation takes constant time, $O(1)$.
    *   Therefore, each iteration of the loop takes $O(1)$ time.
3.  **Return Statement:** The `return result` statement is a constant-time operation, $O(1)$.

Summing these contributions, the total time complexity is:
$T(n) = O(1) \text{ (initialization)} + n \times O(1) \text{ (loop iterations)} + O(1) \text{ (return)}$.
$T(n) = O(1) + O(n) + O(1) = O(n)$.

More formally, there exist constants $c_1, c_2, c_3 > 0$ such that:
$T(n) = c_1 + n \cdot c_2 + c_3$.
As $n \to \infty$, $T(n)$ is asymptotically proportional to $n$.
Thus, the time complexity is $\Theta(n)$, which implies $O(n)$.

### Space Complexity

Let $S(n)$ denote the auxiliary space complexity of the algorithm for an input array of length $n$. Auxiliary space refers to the extra space used by the algorithm, not including the input itself.

1.  **Variables:** The algorithm uses a single integer variable `result` to store the accumulated XOR sum. This variable occupies a constant amount of memory, typically one machine word, regardless of the input size $n$.
2.  **Loop Variables:** The loop index `i` and the current array element `v` (from `enumerate`) also occupy constant space.
3.  **No Auxiliary Data Structures:** The algorithm does not allocate any additional data structures (like lists, dictionaries, etc.) whose size depends on $n$.

Therefore, the total auxiliary space used by the algorithm is constant:
$S(n) = O(1)$.