# Array - Wave Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP06 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [PREP06](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_03/problems/PREP06) |

---

## Problem Statement

You are given an array $A_1, A_2, \dots, A_N$ of length $N$. Rearrange the elements into a sequence such that $A_1 \geq A_2 \leq A_3 \geq A_4 \leq A_5 \dots$. If more than one arrangement is possible, then find the **lexicographically smallest** sequence.

Note: Sequence $A$ is lexicographically smaller than sequence $B$ if and only if there exists a position $i$ where $X_i \lt Y_i$ and $X_j = Y_j$ for all $j \lt i$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains an integer $N$ - the length of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$.

---

## Output Format

For each test case, output on a new line the $N$ space-separated integers of the sequence.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
4 5 15 12
5
5 6 7 8 9
1
5
```

**Output**

```text
5 4 15 12 
6 5 8 7 9 
5
```

**Explanation**

**Test case $1$**: Some possible arrangements can be $[5, 4, 15, 12]$, $[12, 4, 15, 5]$. $[5, 4, 15, 12]$ will be the **lexicographically smallest** sequence.

**Test case $2$**: The **lexicographically smallest** sequence will be $[6, 5, 8, 7, 9]$.

**Test case $3$**: Only arrangement will be $[5]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
4 5 15 12
```

**Output for this case**

```text
5 4 15 12
```



#### Test case 2

**Input for this case**

```text
5
5 6 7 8 9
```

**Output for this case**

```text
6 5 8 7 9
```



#### Test case 3

**Input for this case**

```text
1
5
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will discuss how to rearrange an array
$$\{A_1, A_2, \dots, A_N\}$$
into a “wave” or “zigzag” sequence that satisfies

$$
A_1 \geq A_2 \leq A_3 \geq A_4 \leq A_5 \dots
$$

and, among all possible valid sequences, returns the **lexicographically smallest** one.

The key observation is that if we start with the array sorted in non-decreasing order, then the sorted order is the lexicographically smallest ordering. However, the sorted order does not satisfy the wave conditions directly. To enforce the pattern while changing the sorted order minimally, we can rearrange the elements carefully. Below, we describe three approaches to achieve this.

---

### Approach 1: Sorting and Swapping Adjacent Pairs

**Idea:**
1. **Sort the array.**
   A sorted array is lexicographically smallest.
2. **Swap every adjacent pair.**
   For every pair of consecutive elements starting from index 0 (with 0-indexing), swap the two items.
   For example, if the sorted array is
   $$[S_0, S_1, S_2, S_3, \ldots],$$
   after swapping, we get
   $$[S_1, S_0, S_3, S_2, \dots].$$
   This arrangement ensures:
   - At index 0: $S_1 \geq S_0$ (thus $A_1 \geq A_2$ in 1-indexed notation).
   - At index 1 and 2: $S_0 \leq S_3$, so $A_2 \leq A_3$, and so on.

Because the only changes from the sorted order are these local swaps, the resulting sequence is indeed the lexicographically smallest valid wave.

**Complexity:**
The sorting step takes $O(N \log N)$ and the swapping takes $O(N)$.

Below is the code implementation in C++ and Python.

**C++ Code:**
```cpp
#include
#include
#include
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while(T--) {
        int N;
        cin >> N;
        vector arr(N);
        for (int i = 0; i < N; i++) {
            cin >> arr[i];
        }

        // Sort the array to start with lexicographically smallest order.
        sort(arr.begin(), arr.end());

        // Swap adjacent pairs: indices 0 and 1, 2 and 3, etc.
        for (int i = 0; i + 1 < N; i += 2) {
            swap(arr[i], arr[i + 1]);
        }

        // Output the rearranged array.
        for (int i = 0; i < N; i++) {
            cout << arr[i] << " ";
        }
        cout << "\n";
    }

    return 0;
}
```

**Python Code:**
```python
def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    pos = 1
    output = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        arr = list(map(int, data[pos:pos+n]))
        pos += n

        # Sort the array.
        arr.sort()

        # Swap adjacent pairs.
        for i in range(0, n - 1, 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]

        output.append(" ".join(map(str, arr)))
    print("\n".join(output))

if __name__ == "__main__":
    main()
```

---

### Approach 2: Constructing a New Result Array Using Pair Reordering

**Idea:**
Instead of doing in-place swaps, we can build a new result array by pairing the elements of the sorted array in the desired order:
1. **Sort the array.**
2. **Form pairs and append them into a new array.**
   Take two elements at a time from the sorted array. For each pair $(x, y)$ (with $x \le y$), place $y$ first and then $x$. This automatically forms the pattern:
   - For the first pair, placing the smaller element second ensures that $A_1 = y \geq x = A_2$.
   - For subsequent pairs, the same logic applies.
3. **Handle the odd case:**
   If $N$ is odd, append the last element as it is.

This results in the same wave pattern but constructs the answer explicitly rather than modifying the array in place.

**Complexity:**
Sorting takes $O(N \log N)$, and constructing the new result takes $O(N)$.

**C++ Code:**
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
        int N;
        cin >> N;
        vector arr(N);
        for (int i = 0; i < N; i++){
            cin >> arr[i];
        }

        sort(arr.begin(), arr.end());
        vector res;
        int i = 0;
        while (i + 1 < N) {
            res.push_back(arr[i+1]);
            res.push_back(arr[i]);
            i += 2;
        }
        // If N is odd, append the last element.
        if (N % 2 == 1) {
            res.push_back(arr[N-1]);
        }

        for (auto &x : res) {
            cout << x << " ";
        }
        cout << "\n";
    }

    return 0;
}
```

**Python Code:**
```python
def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    pos = 1
    results = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        arr = list(map(int, data[pos:pos+n]))
        pos += n

        s = sorted(arr)
        res = []
        i = 0
        while i + 1 < n:
            res.append(s[i+1])
            res.append(s[i])
            i += 2
        if n % 2 == 1:
            res.append(s[-1])

        results.append(" ".join(map(str, res)))
    print("\n".join(results))

if __name__ == '__main__':
    main()
```

---

### Approach 3: In-Place Greedy Correction Using Parity Checks

**Idea:**
Another way to achieve the required wave pattern is to make targeted swaps based on the index parity after sorting.
1. **Sort the array.**
2. **Iterate over the array and, for each index, check the necessary condition:**
   - **For even indices (0-indexed, representing odd positions in 1-indexed notation):**
     We require $$A[i] \geq A[i+1]$$ for indices where $i+1 < N$. If $$A[i] < A[i+1],$$ swap them.
   - **For odd indices:**
     We require $$A[i] \leq A[i+1]$$ if $i+1 < N$. If $$A[i] > A[i+1],$$ swap them.

   Since the array is initially sorted, many pairs are already in order, and only the even-indexed positions typically require a swap. This method is essentially similar to the adjacent-swap approach but checks conditions before swapping.

**Complexity:**
Again, sorting runs in $O(N \log N)$ and the one pass correction runs in $O(N)$.

**C++ Code:**
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
        int N;
        cin >> N;
        vector arr(N);
        for (int i = 0; i < N; i++){
            cin >> arr[i];
        }

        sort(arr.begin(), arr.end());

        // Check each adjacent pair with the parity based condition.
        for (int i = 0; i + 1 < N; i++){
            if (i % 2 == 0) {
                // Even index: ensure arr[i] >= arr[i+1]
                if(arr[i] < arr[i+1])
                    swap(arr[i], arr[i+1]);
            } else {
                // Odd index: ensure arr[i] <= arr[i+1]
                if(arr[i] > arr[i+1])
                    swap(arr[i], arr[i+1]);
            }
        }

        for(auto &x : arr)
            cout << x << " ";
        cout << "\n";
    }

    return 0;
}
```

**Python Code:**
```python
def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    pos = 1
    results = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        arr = list(map(int, data[pos:pos+n]))
        pos += n

        arr.sort()

        # Apply corrections based on index parity.
        for i in range(0, n - 1):
            if i % 2 == 0:
                if arr[i] < arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]

        results.append(" ".join(map(str, arr)))
    print("\n".join(results))

if __name__ == '__main__':
    main()
```

---

### Summary

All three approaches begin by sorting the array to guarantee the lexicographically smallest starting point. They then adjust the array to satisfy the wave condition:

- **Approach 1** swaps adjacent elements in fixed pairs.
- **Approach 2** builds a new array by reordering the sorted pairs.
- **Approach 3** makes conditional swaps based on parity during a single pass.

Each method has a similar time complexity of $O(N \log N)$ due to sorting and is easy to implement. These solutions illustrate fundamental techniques, including sorting and greedy reordering, which are very useful in data structures and algorithm problems.

</details>
