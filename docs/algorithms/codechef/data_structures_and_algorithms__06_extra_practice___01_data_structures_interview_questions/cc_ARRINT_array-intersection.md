# Array Intersection

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ARRINT |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Binary Search |
| Official Link | [ARRINT](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_06/problems/ARRINT) |

---

## Problem Statement

You are given three sequences $A_1, A_2, \ldots, A_N$, $B_1, B_2, \ldots, B_M$ and $C_1, C_2, \ldots, C_K$. Each sequence consists of pairwise distinct integers. You need to find how many integers there are that appear in all three of the given sequences.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains three space-separated integers $N$, $M$ and $K$.

- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

- The third line contains $M$ space-separated integers $B_1, B_2, \ldots, B_M$.

- The fourth line contains $K$ space-separated integers $C_1, C_2, \ldots, C_K$.

---

## Output Format

- For each test case, print a single line containing one integer ― the number of integers that appear in all three sequences.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N,M,K \leq 10^{5}$
- the sum of $N$ over all test cases does not exceed $10^{5}$
- the sum of $M$ over all test cases does not exceed $10^{5}$
- the sum of $K$ over all test cases does not exceed $10^{5}$
- in each sequence, the numbers are pairwise distinct
- $1 \leq A_i,B_i,C_i \leq 10^9$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
3
3 4 5
5 2 6
2 8 3 5
9 1 2 5 7
4 4 4
1 2 3 4
4 5 1 7
3 8 9 2
4 4 4
1 2 3 4
3 4 1 6
7 1 3 4
```

**Output**

```text
2
0
3
```

**Explanation**

**Example case 1:** Numbers $2$ and $5$ appear in all three sequences.

**Example case 2:** No numbers appear in all three sequences.

**Example case 3:** Numbers $1$, $3$ and $4$ appear in all three sequences.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 4 5
5 2 6
2 8 3 5
9 1 2 5 7
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
4 4 4
1 2 3 4
4 5 1 7
3 8 9 2
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
4 4 4
1 2 3 4
3 4 1 6
7 1 3 4
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this editorial, we will explore two primary approaches to solve the problem of finding how many integers appear in all three sequences. Given three sequences with pairwise distinct integers, our goal is to count the common elements across the three sequences. We assume the sequences are denoted as:
$$ A = \{ A_1, A_2, \ldots, A_N \}, \quad B = \{ B_1, B_2, \ldots, B_M \}, \quad C = \{ C_1, C_2, \ldots, C_K \}. $$

Below, we discuss two approaches to solve this task:

---

### Approach 1: Using Hash Sets (Set Intersection)

**Idea:**

We leverage hash sets to utilize fast membership tests. Since the sequences contain distinct integers, we can insert elements from the first two sequences into separate hash sets. Then, for each element in the third sequence, we check if it exists in both hash sets. This approach benefits from an average time complexity of
$$ O(N + M + K), $$
as set operations generally have constant time complexity on average.

**C++ Implementation:**

```cpp
#include
#include
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int N, M, K;
        cin >> N >> M >> K;
        unordered_set setA, setB;
        int num;

        for (int i = 0; i < N; i++) {
            cin >> num;
            setA.insert(num);
        }
        for (int i = 0; i < M; i++) {
            cin >> num;
            setB.insert(num);
        }

        int commonCount = 0;
        for (int i = 0; i < K; i++) {
            cin >> num;
            // Check if the current number is in both setA and setB.
            if (setA.count(num) && setB.count(num)) {
                commonCount++;
            }
        }
        cout << commonCount << "\n";
    }
    return 0;
}
```

**Python Implementation:**

```python
def solve():
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    idx = 1
    results = []

    for _ in range(t):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        k = int(input_data[idx + 2])
        idx += 3

        # Build sets for the first two sequences.
        set_a = set(map(int, input_data[idx: idx + n]))
        idx += n
        set_b = set(map(int, input_data[idx: idx + m]))
        idx += m

        common_count = 0
        # Check each element of the third sequence.
        for x in map(int, input_data[idx: idx + k]):
            if x in set_a and x in set_b:
                common_count += 1
        idx += k
        results.append(common_count)

    sys.stdout.write("\n".join(map(str, results)))

if __name__ == "__main__":
    solve()
```

---

### Approach 2: Sorting and Three-Pointer Merge

**Idea:**

Another efficient method is to sort all three sequences and then use three pointers (or indices) to traverse them simultaneously. The procedure is as follows:

1. **Sort** all sequences.
2. Initialize three pointers $i$, $j$, and $k$ for sequences $A$, $B$, and $C$, respectively.
3. Compare $A[i]$, $B[j]$, and $C[k]$:
   - If they are equal, increment the common count and all three pointers.
   - Otherwise, increase the pointer corresponding to the smallest element among $A[i]$, $B[j]$, and $C[k]$ to try and catch up with the larger numbers.

This method takes $$ O(N\log N + M\log M + K\log K) $$ for sorting plus $$ O(N + M + K) $$ for merging, which is efficient given the input constraints.

**C++ Implementation:**

```cpp
#include
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        int N, M, K;
        cin >> N >> M >> K;
        vector A(N), B(M), C(K);
        for(int i = 0; i < N; i++)
            cin >> A[i];
        for(int i = 0; i < M; i++)
            cin >> B[i];
        for(int i = 0; i < K; i++)
            cin >> C[i];

        sort(A.begin(), A.end());
        sort(B.begin(), B.end());
        sort(C.begin(), C.end());

        int i = 0, j = 0, l = 0, count = 0;

        while(i < N && j < M && l < K) {
            if (A[i] == B[j] && B[j] == C[l]) {
                count++;
                i++; j++; l++;
            } else {
                int minimum = min(A[i], min(B[j], C[l]));
                if (A[i] == minimum)
                    i++;
                else if (B[j] == minimum)
                    j++;
                else
                    l++;
            }
        }

        cout << count << "\n";
    }
    return 0;
}
```

**Python Implementation:**

```python
def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    results = []

    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        k = int(data[idx + 2])
        idx += 3

        A = list(map(int, data[idx: idx + n]))
        idx += n
        B = list(map(int, data[idx: idx + m]))
        idx += m
        C = list(map(int, data[idx: idx + k]))
        idx += k

        A.sort()
        B.sort()
        C.sort()

        i = j = l = 0
        count = 0

        while i < n and j < m and l < k:
            if A[i] == B[j] and B[j] == C[l]:
                count += 1
                i += 1
                j += 1
                l += 1
            else:
                min_val = min(A[i], B[j], C[l])
                if A[i] == min_val:
                    i += 1
                elif B[j] == min_val:
                    j += 1
                else:
                    l += 1
        results.append(count)

    sys.stdout.write("\n".join(map(str, results)))

if __name__ == "__main__":
    solve()
```

---

### Summary

- **Approach 1 (Hash Sets):**
  - **Time Complexity:** $O(N + M + K)$
  - **Methodology:** Use hash sets to check membership, iterating through the third sequence and counting common elements.

- **Approach 2 (Sorting and Three Pointers):**
  - **Time Complexity:** $$O(N\log N + M\log M + K\log K + N + M + K)$$
  - **Methodology:** Sort each sequence and use three pointers to simultaneously traverse and find intersections.

Both approaches are efficient under the given problem constraints and provide valuable insights into solving intersection problems in sequences. For beginners, the hash set method is more straightforward, while the sorting and merge technique helps reinforce the concept of multi-array traversal and pointer manipulation.

Happy Coding!

</details>
