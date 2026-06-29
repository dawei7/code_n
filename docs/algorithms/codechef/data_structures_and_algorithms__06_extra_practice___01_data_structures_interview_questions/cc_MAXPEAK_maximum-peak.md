# Maximum Peak

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXPEAK |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 2 |
| Official Link | [MAXPEAK](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_02/problems/MAXPEAK) |

---

## Problem Statement

You are given a sequence $A_1, A_2, \ldots, A_N$.

A **peak** is a subarray (a contiguous subsequence) of $A$ whose elements first strictly increase and then strictly decrease in value.

More formally, a subarray from $L$ to $R$ is a **peak** if and only if there exists an integer $X$ such that $L \le X \le R$ for which the subarray from $L$ to $X$ is strictly increasing and the subarray from $X$ to $R$ is strictly decreasing. Note that subarrays that are only strictly increasing and subarrays that are only strictly decreasing are considered **peaks** as well.

Find the maximum length of a **peak** in the sequence $A$.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains an integer $N$.

- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

---

## Output Format

- For each test case, print a single line containing one integer ― the maximum length of a **peak** in the sequence $A$.

---

## Constraints

- $1 \leq T \leq 200$
- $1 \leq N \leq 2 \cdot 10^{5}$
- the sum of $N$ over all test cases does not exceed $4 \cdot 10^{5}$
- $1 \leq A_i \leq 10^9$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
4
6
1 3 5 3 1 9
7
3 5 4 7 5 6 3
4
1 5 7 8
3
9 5 1
```

**Output**

```text
5
3
4
3
```

**Explanation**

**Example case 1:** The longest peak is of length $5$. One such subarray is from position $1$ to position $5$ in the sequence.

**Example case 2:** The longest peak is of length $3$. One such subarray is from position $1$ to position $3$ in the sequence.

**Example case 3:** The longest peak is of length $4$. One such subarray is from position $1$ to position $4$ in the sequence. Although it is strictly increasing, it is still considered a peak.

**Example case 4:** The longest peak is of length $3$. One such subarray is from position $1$ to position $3$ in the sequence. Although it is strictly decreasing, it is still considered a peak.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
1 3 5 3 1 9
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
7
3 5 4 7 5 6 3
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
4
1 5 7 8
```

**Output for this case**

```text
4
```



#### Test case 4

**Input for this case**

```text
3
9 5 1
```

**Output for this case**

```text
3
```



**Example 2**

**Input**

```text
3
6
2 30 30 30 30 2
10
5 9 13 9 7 10 14 18 13 6
5
9 9 9 9 9
1
1000000000
```

**Output**

```text
2
6
1
1
```

**Explanation**

**Example case 1:** The longest peak is of length $2$. One such subarray is from position $1$ to position $2$ in the sequence. Although it is strictly increasing, it is still considered a peak. Note that the subarray from position $1$ to position $6$ in the sequence is not a peak because it has equal consecutive values.

**Example case 2:** The longest peak is of length $6$. One such subarray is from position $5$ to position $10$ in the sequence.

**Example case 3:** The longest peak is of length $1$. One such subarray is from position $1$ to position $5$.

**Example case 4:** The longest peak is of length $1$. That subarray is from position $1$ to position $1$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we explore the “Longest Peak” problem. You are given a sequence of numbers and need to find the length of the longest subarray (or “peak”) that is first strictly increasing and then strictly decreasing. Note that subarrays that are only strictly increasing or strictly decreasing are also valid peaks.

In the following sections, we discuss two approaches that can help you solve this problem efficiently.

---

### Approach 1: Precomputed Left and Right Arrays

**Idea:**
For each index in the array, we can determine:
- How many consecutive numbers (including the current one) in the **left** part form a strictly increasing sequence.
- How many consecutive numbers in the **right** part form a strictly decreasing sequence.

By calculating these two values:
- Let **left[i]** be the length of the strictly increasing subarray ending at index *i*.
- Let **right[i]** be the length of the strictly decreasing subarray starting at index *i*.

The peak (which may include only one of these monotonic sequences) that uses index *i* as the turning point has a length of:
$$
\text{length} = \text{left}[i] + \text{right}[i] - 1
$$
We subtract 1 because index *i* is counted twice. Iterating through all indices and taking the maximum value gives the answer.

**Methodology:**
1. **Compute Increasing Run (Left Array):**
   Start from the beginning of the array. For each element, if it is greater than the previous one, increase the count from the previous index; otherwise, reset the count to 1.

2. **Compute Decreasing Run (Right Array):**
   Start from the end of the array. For each element, if it is greater than the next element, increase the count from the next index; otherwise, reset the count to 1.

3. **Compute Peak Length:**
   For each index *i*, calculate
   $$\text{peak\_length} = \text{left}[i] + \text{right}[i] - 1$$
   and determine the maximum peak length.

**Complexity:**
This approach operates in \( O(n) \) time per test case, which satisfies the problem constraints.

Below are the code implementations in both C++ and Python:

#### C++ Code for Approach 1:
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
    while(T--){
        int n;
        cin >> n;
        vector A(n);
        for (int i = 0; i < n; i++) {
            cin >> A[i];
        }
        vector left(n, 1), right(n, 1);

        // Compute length of increasing subarray ending at each index.
        for (int i = 1; i < n; i++){
            if (A[i] > A[i - 1])
                left[i] = left[i - 1] + 1;
        }

        // Compute length of decreasing subarray starting at each index.
        for (int i = n - 2; i >= 0; i--){
            if (A[i] > A[i + 1])
                right[i] = right[i + 1] + 1;
        }

        int ans = 0;
        for (int i = 0; i < n; i++){
            ans = max(ans, left[i] + right[i] - 1);
        }

        cout << ans << "\n";
    }

    return 0;
}
```

#### Python Code for Approach 1:
```python
import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index+n]))
        index += n

        left = [1] * n
        right = [1] * n

        # Compute increasing sequence lengths
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                left[i] = left[i-1] + 1

        # Compute decreasing sequence lengths
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]:
                right[i] = right[i+1] + 1

        ans = 0
        for i in range(n):
            ans = max(ans, left[i] + right[i] - 1)

        results.append(str(ans))

    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    main()
```

---

### Approach 2: Two-Pointer Scanning Technique

**Idea:**
This approach iterates through the array with two pointers to directly identify contiguous segments (peaks). The idea is to advance a pointer while the sequence is strictly increasing and then further advance while it is strictly decreasing. This way, you capture the entire peak in one go.

**Methodology:**
1. **Initialize a Pointer:**
   Start with index `i = 0`.

2. **Scan for Increasing Sequence:**
   Advance a temporary pointer `j` as long as the next element is greater than the current element.

3. **Scan for Decreasing Sequence:**
   After finishing the increasing part, continue to advance `j` while the next element is less than the current element.

4. **Peak Length Calculation:**
   The length of the current peak is given by `j - i + 1`. Update the maximum found peak length accordingly.

5. **Handle Plateaus:**
   If no increasing or decreasing condition is met (i.e., the element is equal to the next), just move the pointer forward.

**Complexity:**
This scanning approach also runs in \( O(n) \) time per test case. It is typically less memory intensive since we do not require auxiliary arrays.

Below are the code implementations in both C++ and Python:

#### C++ Code for Approach 2:
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
        int n;
        cin >> n;
        vector A(n);
        for (int i = 0; i < n; i++){
            cin >> A[i];
        }
        int ans = 0;
        int i = 0;

        while(i < n){
            int j = i;
            // Extend through the strictly increasing sequence.
            while(j + 1 < n && A[j + 1] > A[j])
                j++;
            // Extend through the strictly decreasing sequence.
            while(j + 1 < n && A[j + 1] < A[j])
                j++;
            ans = max(ans, j - i + 1);
            // If no advance was made, move to the next element.
            if(j == i)
                i++;
            else
                i = j;
        }
        cout << ans << "\n";
    }

    return 0;
}
```

#### Python Code for Approach 2:
```python
import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index+n]))
        index += n

        ans = 0
        i = 0
        while i < n:
            j = i
            # Extend through the strictly increasing segment.
            while j + 1 < n and arr[j+1] > arr[j]:
                j += 1
            # Extend through the strictly decreasing segment.
            while j + 1 < n and arr[j+1] < arr[j]:
                j += 1
            ans = max(ans, j - i + 1)
            # If no valid peak is formed (plateau case), move i by one.
            if j == i:
                i += 1
            else:
                i = j
        results.append(str(ans))

    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    main()
```

---

### Summary

Both approaches have their merits:
- **Approach 1** is intuitive because it uses precomputation of increasing and decreasing sequences and is less error prone.
- **Approach 2** uses a two-pointer scanning technique that is memory efficient and performs well.

Understanding both methods will strengthen your problem-solving skills and equip you with strategies that can be adapted to similar DSA challenges.

Happy coding and best of luck with your interviews!

</details>
