# Backtracking - Subsets

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP42 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Backtracking |
| Official Link | [PREP42](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_16/problems/PREP42) |

---

## Problem Statement

Given an integer array $A$, print all possible **non-empty** subsets of $A$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two integers $N$ - size of array $A$.
    - The second line contains $N$ space-separated integers - the array $A$.

---

## Output Format

For each test case, output $M+1$ lines, where $M$ is the number of subsets:
- The first line contains a single integer $M$.
- The next $M$ lines contains a subset of $A$.

Note:
- Elements in the subset must be in non-decreasing order.
- Subsets must not be duplicated.
- The subsets must be sorted lexicographically. Subset $X$ is said to be lexicographically smaller than subset $Y$ if either $X$ is a prefix of $Y$ or there exists an index $i$ such that for all $j \lt i$, $X_j = Y_j$ and $X_i \lt Y_i$.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 20$
- $1 \leq A_i \leq 100$
- The sum of $N$ over all test cases won't exceed $30$.

---

## Examples

**Example 1**

**Input**

```text
3
1
1
3
1 2 2
3
1 2 3
```

**Output**

```text
1
1 
5
1 
1 2 
1 2 2 
2 
2 2 
7
1 
1 2 
1 2 3 
1 3 
2 
2 3 
3
```

**Explanation**

**Test case $1$:** Given $A$ as $[1]$.

There is only $1$ non-empty subset of $A$ which is$\{[1]\}$.

**Test case $2$:** Given $A$ as $[1, 2, 2]$.

There are $5$ different non-empty subsets which are $\{[1], [1, 2], [1, 2, 2], [2], [2, 2]\}$.

**Test case $3$:** Given $A$ as $[1, 2, 3]$.

There are $7$ different non-empty subsets which are $\{[1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]\}$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial on Generating All Non-Empty Subsets

In this lesson, we tackle the problem of generating all the non-empty subsets of an integer array while ensuring the following:
- Each subset's elements are in non-decreasing order.
- We do not include duplicate subsets.
- The subsets are printed in lexicographical order.

We will explore a **backtracking (DFS) approach**, which offers clarity in recursively exploring the solution space.

---

## Approach 1: Backtracking (DFS) – Recursive Exploration

### **Idea**
This approach leverages recursion (depth-first search, DFS) to build subsets by exploring each element. We first sort the input array so that:
- The subsets are automatically built in non-decreasing order.
- We can easily skip over duplicate elements to avoid generating duplicate subsets.

During the recursion:
- We start with an empty subset.
- At every recursive call, we add the current subset configuration to our list of results (excluding the empty subset when printing).
- We iterate from the current index to the end, and if we see duplicate elements (i.e. if $A[i] = A[i-1]$ and $i$ is greater than the starting index), we skip processing that element further.

### **Complexity**
Since the maximum array size is $20$, this method is efficient. The lexicographic order is achieved naturally by our recursive exploration.

### **C++ Implementation**
```cpp
#include
#include
#include
using namespace std;

void generateSubsets(const vector& A, vector& current, int index, vector>& result) {
    result.push_back(current);
    for (int i = index; i < A.size(); i++) {
        if (i > index && A[i] == A[i - 1]) continue; // Skip duplicates
        current.push_back(A[i]);
        generateSubsets(A, current, i + 1, result);
        current.pop_back();
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--){
        int N;
        cin >> N;
        vector A(N);
        for (int i = 0; i < N; i++){
            cin >> A[i];
        }
        sort(A.begin(), A.end());
        vector> result;
        vector current;
        generateSubsets(A, current, 0, result);

        // Remove the empty subset (first element)
        cout << result.size() - 1 << "\n";
        for (int i = 1; i < result.size(); i++){
            for (int num : result[i]){
                cout << num << " ";
            }
            cout << "\n";
        }
    }
    return 0;
}
```

### **Python Implementation**
```python
def generateSubsets(A, index, current, result):
    result.append(list(current))
    for i in range(index, len(A)):
        if i > index and A[i] == A[i-1]:
            continue  # Skip duplicates
        current.append(A[i])
        generateSubsets(A, i+1, current, result)
        current.pop()

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    result = []
    generateSubsets(A, 0, [], result)
    # Exclude the empty subset (first element)
    print(len(result) - 1)
    for subset in result[1:]:
        print(" ".join(map(str, subset)))
```

---

## Final Thoughts

The backtracking (DFS) approach provides a clear and robust method for generating all non-empty subsets with elements in non-decreasing order. It naturally manages ordering and duplicate elimination, making it an effective solution given the problem constraints.

Understanding this method strengthens your grasp of recursion and efficient subset generation. This editorial focuses solely on this correct and reliable approach.

</details>
