# Pixel Damage

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PIXDAM |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 1 |
| Official Link | [PIXDAM](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_01/problems/PIXDAM) |

---

## Problem Statement

You are given a rectangle with dimensions $H \times W$, where $H$ and $W$ are positive integers representing the vertical and horizontal dimensions of the rectangle respectively. You are also given a point $P$ which is at distance $X$ from the rectangle's left edge and at distance $Y$ from the rectangle's top edge.

Find whether the distance from the point $P$ to the bottom right corner of the rectangle is strictly less than $K$.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains five space-separated integers $H$, $W$, $X$, $Y$ and $K$.

---

## Output Format

- For each test case, print a single line containing one integer. That integer should be $1$ if the distance from the point $P$ to the bottom right corner of the rectangle is less than $K$ and $0$ otherwise.

---

## Constraints

- $1 \le T \le 10^4$
- $1 \le H,W \le 10^9$
- $0 \le X \le W$
- $0 \le Y \le H$
- $0 \le K \le 10^9$

---

## Examples

**Example 1**

**Input**

```text
5
2 3 3 2 1
2 3 1 1 2
2 3 1 1 3
2 3 0 2 3
2 3 3 1 2
```

**Output**

```text
1
0
1
0
1
```

**Explanation**

The rectangle has height $H=2$ and width $W=3$ in all test cases. Therefore, the distance from the bottom right corner to the left edge and the distance from the bottom right corner to the top edge are $3$ and $2$ respectively.

**Example case 1:** The given point $P$ is at distance $X=3$ from the left edge and at distance $Y=2$ from the top edge. Therefore, its distance from the bottom right corner is $\sqrt{(3-3)^2+(2-2)^2}=0$ which is less than $K=1$, so the answer is $1$.

**Example case 2:** The given point $P$ is at distance $X=1$ from the left edge and at distance $Y=1$ from the top edge. Therefore, its distance from the bottom right corner is $\sqrt{(3-1)^2+(2-1)^2}=\sqrt{5}$ which is greater than $K=2$, so the answer is $0$.

**Example case 3:** The given point $P$ is at distance $X=1$ from the left edge and at distance $Y=1$ from the top edge. Therefore, its distance from the bottom right corner is $\sqrt{(3-1)^2+(2-1)^2}=\sqrt{5}$ which is less than $K=3$, so the answer is $1$.

**Example case 4:** The given point $P$ is at distance $X=0$ from the left edge and at distance $Y=2$ from the top edge. Therefore, its distance from the bottom right corner is $\sqrt{(3-0)^2+(2-2)^2}=3$ which is equal to $K=3$, so the answer is $0$.

**Example case 5:** The given point $P$ is at distance $X=3$ from the left edge and at distance $Y=1$ from the top edge. Therefore, its distance from the bottom right corner is $\sqrt{(3-3)^2+(2-1)^2}=1$ which is less than $K=2$, so the answer is $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 3 3 2 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2 3 1 1 2
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
2 3 1 1 3
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
2 3 0 2 3
```

**Output for this case**

```text
0
```



#### Test case 5

**Input for this case**

```text
2 3 3 1 2
```

**Output for this case**

```text
1
```



**Example 2**

**Input**

```text
3
8 8 6 4 5
8 8 6 4 4
8 8 8 8 0
```

**Output**

```text
1
0
0
```

**Explanation**

The rectangle has height $H=8$ and width $W=8$ in all test cases. Therefore, the distance from the bottom right corner to the left edge and the distance from the bottom right corner to the top edge are $8$ and $8$ respectively.

**Example case 1:** The given point $P$ is at distance $X=6$ from the left edge and at distance $Y=4$ from the top edge. Therefore, its distance from the bottom right corner is $\sqrt{(8-6)^2+(8-4)^2}=\sqrt{20}$ which is less than $K=5$, so the answer is $1$.

**Example case 2:** The given point $P$ is at distance $X=6$ from the left edge and at distance $Y=4$ from the top edge. Therefore, its distance from the bottom right corner is $\sqrt{(8-6)^2+(8-4)^2}=0$ which is greater than $K=4$, so the answer is $0$.

**Example case 3:** The given point $P$ is at distance $X=8$ from the left edge and at distance $Y=8$ from the top edge. Therefore, its distance from the bottom right corner is $\sqrt{(8-8)^2+(8-8)^2}=0$ which is equal to $K=0$, so the answer is $0$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
8 8 6 4 5
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
8 8 6 4 4
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
8 8 8 8 0
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this problem, we are given a rectangle with height $H$ and width $W$. A point $P$ is specified by its distance $X$ from the left edge and $Y$ from the top edge. The goal is to determine whether the Euclidean distance from $P$ to the bottom right corner of the rectangle is strictly less than a value $K$. The bottom right corner of the rectangle is at the coordinate $(W, H)$, so the distance is computed as

$$
\text{distance} = \sqrt{(W - X)^2 + (H - Y)^2}.
$$

We then need to check if

$$
\sqrt{(W - X)^2 + (H - Y)^2} < K.
$$

There are several approaches to solve this problem. Below, we discuss two key approaches that beginners should know.

---

### **Approach 1: Direct Calculation Using the Square Root**

#### **Methodology**
In this approach, we directly calculate the Euclidean distance using the square root function:
1. Compute the differences: $dx = W - X$ and $dy = H - Y$.
2. Calculate the distance using:
   $$
   \text{distance} = \sqrt{dx^2 + dy^2}.
   $$
3. Compare the computed distance with $K$. If $\text{distance} < K$, we output `1`; otherwise, we output `0`.

#### **Relevance**
- This approach is straightforward and directly mirrors the problem statement.
- It is simple to implement and understand for beginners.

#### **Code Implementations**

**C++ Code:**
```cpp
#include
#include
using namespace std;
typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        ll H, W, X, Y, K;
        cin >> H >> W >> X >> Y >> K;

        double dx = W - X;
        double dy = H - Y;
        double distance = sqrt(dx * dx + dy * dy);

        cout << (distance < K ? 1 : 0) << "\n";
    }
    return 0;
}
```

**Python Code:**
```python
import math

T = int(input())
for _ in range(T):
    H, W, X, Y, K = map(int, input().split())
    dx = W - X
    dy = H - Y
    distance = math.sqrt(dx * dx + dy * dy)
    print(1 if distance < K else 0)
```

---

### **Approach 2: Comparison by Squaring (Avoiding Floating-Point Computation)**

#### **Methodology**
In this approach, instead of computing the square root (which might incur minor performance overhead or floating-point precision issues), we compare the square of the distance with $K^2$. The mathematical equivalence is:
$$
\sqrt{(W - X)^2 + (H - Y)^2} < K \iff (W - X)^2 + (H - Y)^2 < K^2.
$$
The steps are:
1. Compute $dx = W - X$ and $dy = H - Y$.
2. Calculate the squared distance:
   $$
   \text{distSq} = dx^2 + dy^2.
   $$
3. Compute $K^2$ and compare:
   - If $\text{distSq} < K^2$, output `1`.
   - Otherwise, output `0`.

#### **Relevance**
- This approach uses integer arithmetic (if inputs are integers) and avoids potential floating-point issues.
- It is efficient and particularly recommended when dealing with very large numbers.

#### **Code Implementations**

**C++ Code:**
```cpp
#include
using namespace std;
typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        ll H, W, X, Y, K;
        cin >> H >> W >> X >> Y >> K;

        ll dx = W - X;
        ll dy = H - Y;
        if (dx * dx + dy * dy < K * K)
            cout << 1 << "\n";
        else
            cout << 0 << "\n";
    }
    return 0;
}
```

**Python Code:**
```python
T = int(input())
for _ in range(T):
    H, W, X, Y, K = map(int, input().split())
    dx = W - X
    dy = H - Y
    if dx * dx + dy * dy < K * K:
        print(1)
    else:
        print(0)
```

---

### **Summary of Key Points**

- **Approach 1 (Direct Calculation):**
  - Directly computes the Euclidean distance using the square root function.
  - Easier to understand and implement, but involves floating-point computation.

- **Approach 2 (Squared Comparison):**
  - Avoids the square root by comparing squared distances, which is both efficient and precise.
  - Preferred when working with large numbers or when precision is critical.

Both approaches work in $O(1)$ time per test case, ensuring that the solution is efficient even for the maximum input sizes.

With these explanations and code samples in both C++ and Python, you now have a thorough understanding of solving the problem using multiple approaches. Happy coding and best of luck with your DSA interviews!

</details>
