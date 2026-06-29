# Recover The Permutation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECPERM |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 2 |
| Official Link | [RECPERM](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_02/problems/RECPERM) |

---

## Problem Statement

You are given a sequence $A_1, A_2, \ldots, A_N$ whose elements are zeros and ones.

A sequence that consists of $L$ integers is called a permutation if and only if each integer from $1$ to $L$ appears exactly once in it.

You need to find any permutation $P$ of integers from $1$ to $N$ for which it holds that for every valid index $i$, $A_i=1$ if the prefix of $P$ of length $i$ is a permutation of numbers from $1$ to $i$ and $A_i=0$ otherwise, or determine that such a permutation does not exist.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains a single integer $N$.

- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

---

## Output Format

- For each test case, print a single line.

- In case a suitable permutation $P$ does not exist, print a single integer $-1$.

- Otherwise, print $N$ space-separated integers $P_1, P_2, \ldots, P_N$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 2 \cdot 10^5$
- $A_i=0$ or $A_i=1$ for each valid $i$
- $A_N=1$
- the sum of $N$ over all test cases does not exceed $4 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
4
4
1 0 1 1
4
1 1 1 1
8
0 0 1 0 0 0 1 1
3
0 0 1
```

**Output**

```text
1 3 2 4
1 2 3 4
3 1 2 7 4 5 6 8
3 1 2
```

**Explanation**

**Example case 1:** The prefixes of lengths $1$, $3$ and $4$ are valid permutations and the prefix of length $2$ is not a valid permutation.

**Example case 2:** This is the only valid permutation such that all its prefixes are valid permutations.

**Example case 3:** The prefixes of lengths $3$, $7$ and $8$ are valid permutations and the rest of the prefixes are not valid permutations.

**Example case 4:** Only the prefix of length $3$ is a valid permutation.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 0 1 1
```

**Output for this case**

```text
1 3 2 4
```



#### Test case 2

**Input for this case**

```text
4
1 1 1 1
```

**Output for this case**

```text
1 2 3 4
```



#### Test case 3

**Input for this case**

```text
8
0 0 1 0 0 0 1 1
```

**Output for this case**

```text
3 1 2 7 4 5 6 8
```



#### Test case 4

**Input for this case**

```text
3
0 0 1
```

**Output for this case**

```text
3 1 2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this problem, we are given a binary sequence $A_1,A_2,\ldots,A_N$ that indicates, for each prefix of a permutation $P$ of $\{1, 2, \ldots, N\}$, whether that prefix is “complete” – that is, whether it forms a permutation of $\{1,2,\ldots,i\}$ for the prefix ending at index $i$. Our task is to construct any permutation $P$ that satisfies the condition:
$$
A_i =
\begin{cases}
1 & \text{if } \{P_1, P_2, \ldots, P_i\} = \{1,2,\ldots,i\},\\[1mm]
0 & \text{otherwise.}
\end{cases}
$$
One key observation is that $A_N=1$ always holds because $P$ itself must be a permutation of $\{1,2,\dots,N\}$. In the following, we describe two important approaches to solve the problem, detail their reasoning, and then provide implementations in both C++ and Python.

### Approach 1: Segment Partitioning with Reverse Ordering

**Idea:**
We first identify the indices where $A_i=1$. Let these indices be stored in an array called `validIndices`. These indices indicate that the prefix ending there must be exactly a permutation of $\{1,2,\ldots,i\}$. Consider partitioning the permutation into segments by letting each segment run from the last valid index plus one (or start of the array) up to the current valid index. In each segment, the numbers appearing are exactly from $\{prev+1, \ldots, m\}$ (where `prev` is the previous valid index and $m$ is the current valid index). If we output the numbers of each segment in descending order, we guarantee two things:

1. **Correct Completion:** The entire segment yields exactly the numbers required by the permutation condition when the segment is finished.
2. **Avoiding Intermediate Validity:** For any prefix that does not end exactly at a valid index, the set of elements is “incomplete” (elements are not in natural ascending order), so it does not accidentally form a permutation of $\{1,2,\ldots,i\}$.

**Example:**
Let $N=4$ and $A=[1, 0, 1, 1]$. Then:
- The valid indices are $1$, $3$, and $4$.
- For the segment from $0+1$ to $1$, we output $\{1\}$.
- For the segment from $1+1$ to $3$, we output in descending order: $3$, then $2$.
- For the segment from $3+1$ to $4$, we output $\{4\}$.

Thus, the output permutation is $\{1, 3, 2, 4\}$ which meets the conditions.

**Code Implementation:**

Below, you find the implementations for this approach:

- **C++ Code:**

```cpp
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        // Using 1-indexing for A
        vector A(n+1);
        for (int i = 1; i <= n; i++){
            cin >> A[i];
        }

        // Collect indices where prefix must be a permutation (A[i] == 1)
        vector validIndices;
        for (int i = 1; i <= n; i++){
            if(A[i] == 1)
                validIndices.push_back(i);
        }

        // Build the permutation by partitioning into segments:
        // For each valid index m, the segment from (prev+1) to m consists of the integers {prev+1, ..., m}
        // We output them in descending order to avoid forming a permutation before m.
        vector perm;
        int prev = 0;
        for (int m : validIndices){
            for (int num = m; num >= prev + 1; num--){
                perm.push_back(num);
            }
            prev = m;
        }

        // Check and output the obtained permutation
        if((int)perm.size() != n){
            cout << -1 << "\n";
        } else {
            for (int i = 0; i < n; i++){
                cout << perm[i] << (i == n - 1 ? "\n" : " ");
            }
        }
    }
    return 0;
}
```

- **Python Code:**

```python
def solve():
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    index = 1
    output_lines = []

    for _ in range(t):
        n = int(input_data[index])
        index += 1
        # Using 1-indexing: store a dummy at index 0
        A = [0] + [int(input_data[index+i]) for i in range(n)]
        index += n

        validIndices = []
        for i in range(1, n+1):
            if A[i] == 1:
                validIndices.append(i)

        perm = []
        prev = 0
        for m in validIndices:
            # Append numbers from m down to prev+1 (inclusive)
            for num in range(m, prev, -1):
                perm.append(num)
            prev = m

        if len(perm) != n:
            output_lines.append("-1")
        else:
            output_lines.append(" ".join(map(str, perm)))

    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    solve()
```

---

### Approach 2: Stack-Based Simulation

**Idea:**
An alternative yet equivalent approach utilizes a stack to process the permutation. We iterate through indices $i=1$ to $N$, and at each step we push $i$ onto a stack. When we encounter an index where $A_i=1$, it indicates that the prefix must form a complete permutation of $\{1,2,\ldots,i\}$. At that moment, we pop all elements from the stack (thus reversing the order for the current segment) and append them to our result. This method accomplishes the same goal as the segment partitioning approach but does so in a more “online” fashion.

**Steps:**
1. Initialize an empty stack and an empty result list.
2. For every $i$ from $1$ to $N$, push $i$ onto the stack.
3. If $A_i=1$, pop all elements from the stack (thereby reversing the order) and immediately add them to the result.
4. At the end, if the result has exactly $N$ elements, output it; otherwise, output $-1$.

**Example:**
For $N = 4$ and $A = [1, 0, 1, 1]$:
- At $i=1$: push $1$. Since $A_1=1$, pop and output $1$.
- At $i=2$: push $2$, no pop since $A_2=0$.
- At $i=3$: push $3$. Now $A_3=1$, so pop $3$ then $2$ to output them.
- At $i=4$: push $4$. Since $A_4=1$, pop $4$.

The resulting permutation is $[1,3,2,4]$, which satisfies the conditions.

**Code Implementation:**

- **C++ Code:**

```cpp
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        // Using 1-indexing for A
        vector A(n+1, 0);
        for (int i = 1; i <= n; i++){
            cin >> A[i];
        }

        vector res;
        vector st; // stack for holding current segment
        for (int i = 1; i <= n; i++){
            st.push_back(i);
            if(A[i] == 1){
                while(!st.empty()){
                    res.push_back(st.back());
                    st.pop_back();
                }
            }
        }

        if((int)res.size() != n){
            cout << -1 << "\n";
        } else {
            for (int i = 0; i < n; i++){
                cout << res[i] << (i == n - 1 ? "\n" : " ");
            }
        }
    }
    return 0;
}
```

- **Python Code:**

```python
def solve():
    import sys
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    index = 1
    results = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        A = [0] * (n + 1)
        for i in range(1, n+1):
            A[i] = int(data[index])
            index += 1

        res = []
        stack = []
        for i in range(1, n+1):
            stack.append(i)
            if A[i] == 1:
                while stack:
                    res.append(stack.pop())

        if len(res) != n:
            results.append("-1")
        else:
            results.append(" ".join(map(str, res)))

    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()
```

---

### Summary

Both approaches rely on the idea of preventing any prefix (except when allowed by $A_i = 1$) from forming a complete permutation of $\{1,2,\ldots,i\}$. By reversing segments either explicitly (Approach 1) or through a stack (Approach 2), we ensure that any intermediate prefix does not inadvertently become complete. These methods run in $\mathcal{O}(N)$ per test case, which is efficient given the problem constraints.

We encourage you to try both approaches to build your understanding of how different algorithmic techniques can solve the same problem.

</details>
