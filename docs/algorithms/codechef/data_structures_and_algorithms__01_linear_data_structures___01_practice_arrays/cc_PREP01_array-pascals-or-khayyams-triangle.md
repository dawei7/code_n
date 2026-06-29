# Array - Pascals or Khayyams triangle

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP01 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [PREP01](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/PREP01) |

---

## Problem Statement

Given an integer $N$, you need to generate and output the $N^{th}$ row of [Pascal's triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle) - also known as Khayyam triangle.

**Note**: It might be possible that the elements of a row do **not** fit into a $32$-bit signed integer data type.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of one lines of input - the integer $N$.

---

## Output Format

For each test case, output on a new line the $N^{th}$ row of Pascal's triangle with a single space between all elements of the row.

**Note**: It might be possible that the elements of a row do **not** fit into a $32$-bit signed integer data type.

---

## Constraints

- $1 \leq T \leq 3\cdot 10^4$
- $1 \leq N \leq 50$

---

## Examples

**Example 1**

**Input**

```text
4
1
2
3
4
```

**Output**

```text
1
1 1
1 2 1
1 3 3 1
```

**Explanation**

The first couple of rows of pascal triangle look like:

![](https://s3.amazonaws.com/codechef_shared/download/Images/INTPREP/PREP01.jpeg)

**Test case $1$:** The first row contains only the element $1$.

**Test case $2$:** The second row contains the elements $1$ and $1$.

**Test case $3$:** The third row contains the elements $1, 2,$ and $1$.

**Test case $4$:** The fourth row contains the elements $1,3, 3,$ and $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
1 1
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
1 2 1
```



#### Test case 4

**Input for this case**

```text
4
```

**Output for this case**

```text
1 3 3 1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Generating the Nᵗʰ Row of Pascal's Triangle

In this lesson, we explore two different methods to generate the Nᵗʰ row of Pascal's Triangle (also known as Khayyam’s Triangle). The problem asks you to print the row corresponding to a given integer $N$ where the first row is defined as $[1]$, the second as $[1, 1]$, and so on. Note that the values in the row may be very large, so even 32-bit integers might not suffice.

Below, we describe **two different approaches** and provide sample implementations in both **C++** and **Python**.

---

## Approach 1: Direct Computation Using the Combination Formula

### Concept
Recall that the $N^\text{th}$ row (with $N$ starting at $1$) can be described using binomial coefficients. The $k^\text{th}$ element in the $N^\text{th}$ row is given by:
$$
\binom{N-1}{k} \quad \text{for} \quad k = 0, 1, 2, \ldots, N-1.
$$
Instead of computing factorials, we use the following recurrence relation to compute the $k^\text{th}$ coefficient from the previous one:
$$
C(n, k) = C(n, k-1) \times \frac{n-k+1}{k}, \quad \text{where} \quad n = N-1.
$$
This method is efficient and avoids overflow problems by computing each coefficient iteratively.

### Code Implementation

#### C++ Code
```cpp
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--){
        int N;
        cin >> N;
        // Using combination formula to compute each element
        unsigned long long element = 1;
        for (int k = 0; k < N; k++){
            cout << element;
            if (k != N - 1)
                cout << " ";
            element = element * (N - 1 - k) / (k + 1);
        }
        cout << "\n";
    }
    return 0;
}
```

#### Python Code
```python
T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    element = 1
    row = []
    for k in range(N):
        row.append(str(element))
        element = element * (N - 1 - k) // (k + 1)
    print(" ".join(row))
```

---

## Approach 2: Precomputation of All Rows

### Concept
Given that $N \leq 50$, we can precompute all rows of Pascal's Triangle up to the 50ᵗʰ row once at the beginning. For each test case, we simply retrieve and print the precomputed row. This method is particularly useful when the number of test cases ($T$) is large (up to $3 \cdot 10^4$), as it eliminates redundant computation.

### Code Implementation

#### C++ Code
```cpp
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    const int maxRow = 50;
    // Precompute Pascal's Triangle rows up to 50
    vector> triangle(maxRow);
    triangle[0] = {1};
    for (int i = 1; i < maxRow; i++){
        triangle[i].resize(i + 1);
        triangle[i][0] = triangle[i][i] = 1;
        for (int j = 1; j < i; j++){
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
        }
    }

    int T;
    cin >> T;
    while (T--){
        int N;
        cin >> N;
        // Adjust for 0-based indexing
        for (int i = 0; i < triangle[N - 1].size(); i++){
            cout << triangle[N - 1][i] << (i + 1 == triangle[N - 1].size() ? "\n" : " ");
        }
    }
    return 0;
}
```

#### Python Code
```python
# Precompute Pascal's Triangle up to 50 rows
maxRow = 50
triangle = [[1]]
for i in range(1, maxRow):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(row)

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(" ".join(map(str, triangle[N - 1])))
```

---

## Final Thoughts

Both of these approaches have their own merits:

1. **Direct Computation Using the Combination Formula:**
   - **Pros:** Efficient, providing constant time per element, and avoids redundant calculations.
   - **Cons:** Requires careful handling of arithmetic to avoid overflow (using unsigned long long in C++ helps mitigate this).

2. **Precomputation of All Rows:**
   - **Pros:** Highly optimized for multiple test cases since the computation is performed only once.
   - **Cons:** Uses additional space to store the precomputed rows.

For performance-critical applications or scenarios with a large number of test cases, both methods offer significant advantages. Beginners might find the Direct Computation approach more straightforward due to its direct application of the binomial coefficient properties.

Happy Coding!

</details>
