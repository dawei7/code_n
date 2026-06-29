# Lists in ranges

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KLISTS |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [KLISTS](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_04/problems/KLISTS) |

---

## Problem Statement

Chef gave you $K$ lists and an integer $X$. He further defined different ranges in the following manner:
- The extremum of ranges are $[X*i,(i+1)*X-1]$  for every $i$ in range $[0,10^5]$

He further defined that a list, say $S$ lies in a range $[L,R]$ if and only if $L \leq min(S) , max(S) \leq R$

Let $f(i)$ denote the number of lists which lies in range  $[X*i,X*(i+1)-1]$. Find $\sum f(i)$ for $i$ in range $[0,10^5]$.

---

## Input Format

- First-line will contain $T$, the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $K,X$, then $K$ lists follow
- The Next line of each list contains a single integer $N_i$ - the length of the $i$-th length
- Next Line contains $N_i$ integers - the elements of $i$-th list

---

## Output Format

For each test case, output in a single line - the $i$-th integer denotes the answer for the $i$-th test case.

---

## Constraints

- $1 \leq T \leq 1500$
- $1 \leq K \leq 5 \cdot 10^4$
- $1 \leq X \leq 10^9 $
- $1 \leq N_i \leq 10^5$
- $ \sum N_i \leq 5 \cdot 10^5$ over all test cases
- Each value $A_i$ in the list is in range $[1,10^9]$

---

## Examples

**Example 1**

**Input**

```text
2
2 18
4
13 18 13 1
5
14 2 7 9 1
2 15
1
1
1
9
```

**Output**

```text
1
2
```

**Explanation**

**Test case 1:** Only the $2$-nd list satisfies the condition.

**Test Case 2:** All the lists satisfies the conditions.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 18
4
13 18 13 1
5
14 2 7 9 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2 15
1
1
1
9
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Counting Valid Lists in Ranges

In this lesson, we address the problem of counting how many of the given lists satisfy a condition based on specific ranges. Each range is of the form
$$
[X \cdot i,\, X \cdot (i+1) - 1],
$$
for every integer $i$ in the interval $[0, 10^5]$. A list $S$ is said to lie in a range if and only if
$$
L \leq \min(S) \quad \text{and} \quad \max(S) \leq R,
$$
where $L$ and $R$ are the lower and upper bounds of that range, respectively.

We need to count the number of lists that lie entirely within one of these ranges. A crucial observation is that a list will lie in a single range if both its minimum and maximum elements fall into the same “bucket.” To determine the bucket index for any number, we use the formula:
$$
\text{bucket} = \left\lfloor\frac{\text{value}}{X}\right\rfloor.
$$

Thus, for a list $S$, the condition becomes:
$$
\left\lfloor\frac{\min(S)}{X}\right\rfloor = \left\lfloor\frac{\max(S)}{X}\right\rfloor.
$$

Below, we discuss two approaches to solve this problem.

## Approach 1: Direct Calculation

### Explanation
For each list:
- **Step 1:** Determine the minimum element, $\min(S)$.
- **Step 2:** Determine the maximum element, $\max(S)$.
- **Step 3:** Compute the bucket indices for both $\min(S)$ and $\max(S)$ using
  $$
  \text{bucket} = \left\lfloor\frac{\text{value}}{X}\right\rfloor.
  $$
- **Step 4:** If the two bucket indices are equal, then the list lies entirely within one range, and we increment our count.

This approach directly computes the necessary values in a single pass through each list, resulting in an overall time complexity of
$$
O\left(\sum N_i\right),
$$
where $N_i$ is the length of the $i$-th list.

### Code Implementation

#### C++ Code for Approach 1
```cpp
#include
#include
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while (T--) {
        int K, X;
        cin >> K >> X;
        long long countValid = 0;  // Count of valid lists
        for (int i = 0; i < K; i++) {
            int n;
            cin >> n;
            int mn = 1000000001, mx = 0;  // Initialize minimum and maximum
            for (int j = 0; j < n; j++) {
                int val;
                cin >> val;
                if (val < mn)
                    mn = val;
                if (val > mx)
                    mx = val;
            }
            // Check if both minimum and maximum lie in the same bucket
            if ((mn / X) == (mx / X))
                countValid++;
        }
        cout << countValid << "\n";
    }
    return 0;
}
```

#### Python Code for Approach 1
```python
import sys
input_data = sys.stdin.read().strip().split()
it = iter(input_data)
T = int(next(it))
results = []

for _ in range(T):
    K = int(next(it))
    X = int(next(it))
    countValid = 0
    for _ in range(K):
        n = int(next(it))
        values = [int(next(it)) for _ in range(n)]
        mn = min(values)
        mx = max(values)
        # If minimum and maximum are in the same bucket, the list is valid
        if mn // X == mx // X:
            countValid += 1
    results.append(countValid)

print("\n".join(map(str, results)))
```

## Approach 2: Sorting-Based Approach

### Explanation
An alternative method is to sort each list and then inspect the first (smallest) and last (largest) elements. While sorting each list will correctly produce the minimum and maximum, it introduces an extra computational overhead of
$$
O(n \log n)
$$
for each list, making it less efficient compared to the direct approach. This method is primarily useful for conceptual understanding.

The condition remains the same:
$$
\left\lfloor\frac{\text{first element}}{X}\right\rfloor = \left\lfloor\frac{\text{last element}}{X}\right\rfloor.
$$

### Code Implementation

#### C++ Code for Approach 2
```cpp
#include
#include
#include
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while (T--) {
        int K, X;
        cin >> K >> X;
        long long countValid = 0;
        for (int i = 0; i < K; i++) {
            int n;
            cin >> n;
            vector nums(n);
            for (int j = 0; j < n; j++) {
                cin >> nums[j];
            }
            // Sorting the list to get the minimum and maximum easily
            sort(nums.begin(), nums.end());
            int mn = nums.front();
            int mx = nums.back();
            if ((mn / X) == (mx / X))
                countValid++;
        }
        cout << countValid << "\n";
    }
    return 0;
}
```

#### Python Code for Approach 2
```python
import sys
input_data = sys.stdin.read().strip().split()
it = iter(input_data)
T = int(next(it))
results = []

for _ in range(T):
    K = int(next(it))
    X = int(next(it))
    countValid = 0
    for _ in range(K):
        n = int(next(it))
        values = [int(next(it)) for _ in range(n)]
        values.sort()  # Sorting to identify the minimum and maximum
        if values[0] // X == values[-1] // X:
            countValid += 1
    results.append(countValid)

print("\n".join(map(str, results)))
```

## Conclusion

Both approaches revolve around the key idea of checking whether
$$
\left\lfloor\frac{\min(S)}{X}\right\rfloor = \left\lfloor\frac{\max(S)}{X}\right\rfloor.
$$
In the **Direct Calculation** approach, we extract the minimum and maximum values by traversing the list once, which is optimal given the problem constraints. The **Sorting-Based Approach** simplifies the logic by sorting the list, but it comes at the cost of higher computational complexity.

For large inputs, the direct method is recommended due to its efficiency. Understanding both methods enriches your problem-solving toolkit and deepens your grasp of how different algorithmic strategies can be applied to the same problem.

</details>
