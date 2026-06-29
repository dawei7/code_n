# Color the Cube

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COLOR8TEST |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 1 |
| Official Link | [COLOR8TEST](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_01/problems/COLOR8TEST) |

---

## Problem Statement

Rubik’s cube has six sides in colors: white, blue, green, yellow, red, and orange. A liter of paint costs $X_1, X_2, X_3, X_4, X_5, X_6$ dollars for each color. Each side of the cube needs half a liter of paint to be painted. How much will you pay for coloring $N$ unpainted cubes?

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains 7 integers $N$ - number of unpainted cubes and $X_1, X_2, X_3, X_4, X_5, X_6$ - cost in dollars for each color.

---

## Output Format

For each test case, output a single line containing one integer - Total cost of coloring the cube

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq X_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
2 1 1 1 1 2 4
3 1 2 3 4 5 6
```

**Output**

```text
10
42
```

**Explanation**

Test Case 1 : We need to buy 1 liter of paint so total cost = 1 + 1 + 1 + 1 + 2 + 4 = 10
Test Case 2 : We need to buy 2 liter of paint so total cost = (1 + 2 + 3 + 4 + 5 + 6) * 2  = 42

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 1 1 1 1 2 4
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
3 1 2 3 4 5 6
```

**Output for this case**

```text
42
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we explore a problem where we need to compute the total cost of painting Rubik’s cubes. Each cube has six sides and every side requires ½ liter of paint. However, the paint is sold only by the liter. Since a cube uses ½ liter per color and each cube has one face of each color, if you paint one cube you need 0.5 liter for a particular color; if you paint two cubes, exactly 1 liter per color is used. When the number of cubes, $N$, is odd, the extra cube still requires 0.5 liter for each color. Because we cannot buy a fractional liter, we must round up the required quantity per color.

The key observation is: for each color, the liters required is the ceiling of $\frac{N}{2}$, i.e.,
$$
L = \left\lceil \frac{N}{2} \right\rceil.
$$
The overall cost then becomes:
$$
\text{Total Cost} = \left(\sum_{i=1}^{6} X_i \right) \times L,
$$
where $X_1, X_2, \dots, X_6$ are the costs per liter for the six colors.

Below are three approaches to solve the problem:

### **Approach 1: Direct Mathematical Calculation Using Integer Arithmetic**

For positive integers, a neat trick to compute the ceiling of $\frac{N}{2}$ is to use the expression $\frac{N+1}{2}$ (using integer division). This approach computes the total liters needed per color directly and then multiplies by the sum of the cost of the six colors.

**C++ Implementation:**

```cpp
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while(T--){
        long long N, sum = 0, cost;
        cin >> N;
        // Read the cost for each of the 6 colors.
        for (int i = 0; i < 6; i++){
            cin >> cost;
            sum += cost;
        }
        // Use integer arithmetic trick to compute ceiling of N/2.
        long long liters = (N + 1) / 2;
        cout << sum * liters << "\n";
    }
    return 0;
}
```

**Python Implementation:**

```python
import sys
input_data = sys.stdin.read().strip().split()
t = int(input_data[0])
index = 1
for _ in range(t):
    N = int(input_data[index])
    index += 1
    # Parse the costs for the 6 colors.
    costs = list(map(int, input_data[index:index+6]))
    index += 6
    liters = (N + 1) // 2  # Integer division for ceiling of N/2 for positive integers.
    print(sum(costs) * liters)
```

### **Approach 2: Using an Explicit Parity Check**

In this approach, we check whether $N$ is even or odd. If $N$ is even, then exactly $\frac{N}{2}$ liters per color are required, but if $N$ is odd, then we need $\frac{N}{2} + 1$ liters because that extra half liter will force us to buy an additional liter.

**C++ Implementation:**

```cpp
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while(T--){
        long long N;
        cin >> N;
        long long sum = 0, cost;
        for (int i = 0; i < 6; i++){
            cin >> cost;
            sum += cost;
        }
        long long liters;
        if (N % 2 == 0)
            liters = N / 2;
        else
            liters = N / 2 + 1;
        cout << sum * liters << "\n";
    }
    return 0;
}
```

**Python Implementation:**

```python
import sys
input_data = sys.stdin.read().split()
t = int(input_data[0])
index = 1
for _ in range(t):
    N = int(input_data[index])
    index += 1
    costs = list(map(int, input_data[index:index+6]))
    index += 6
    # Check parity of N and compute liters accordingly.
    if N % 2 == 0:
        liters = N // 2
    else:
        liters = N // 2 + 1
    print(sum(costs) * liters)
```

### **Approach 3: Using the Math Library to Compute the Ceiling**

Although the previous methods are efficient, another intuitive method is to explicitly compute the ceiling using built-in functions. In Python, you can use the `math.ceil` function, and in C++ the `` library provides `ceil()`. In C++, care must be taken since `ceil()` works on floating‑point numbers; hence, we convert the result back to an integer.

**C++ Implementation:**

```cpp
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while(T--){
        long long N;
        cin >> N;
        long long sum = 0, cost;
        for (int i = 0; i < 6; i++){
            cin >> cost;
            sum += cost;
        }
        // Using the ceil function from cmath. N/2.0 forces floating-point division.
        long long liters = (long long)ceil(N / 2.0);
        cout << sum * liters << "\n";
    }
    return 0;
}
```

**Python Implementation:**

```python
import sys
import math
input_data = sys.stdin.read().split()
t = int(input_data[0])
index = 1
for _ in range(t):
    N = int(input_data[index])
    index += 1
    costs = list(map(int, input_data[index:index+6]))
    index += 6
    # Use math.ceil to compute the ceiling of N/2.
    liters = math.ceil(N / 2)
    print(sum(costs) * liters)
```

---

**Explanation of Concepts:**

- **Ceiling Function:** The ceiling of a number $x$, denoted by $\lceil x \rceil$, is the smallest integer greater than or equal to $x$. Since each cube uses half a liter per side, for $N$ cubes we need $N \times \frac{1}{2}$ liters per color. Because we can't purchase half a liter, we use the ceiling function: $$L = \left\lceil \frac{N}{2} \right\rceil.$$

- **Integer Arithmetic Trick:** In many problems, instead of calling a function to compute the ceiling, you can use the trick $(N+1)//2$ (or $(N+1)/2$ in C++ with integer division) to avoid floating‑point operations when $N$ is positive.

- **Parity Check:** A straightforward method is to check if $N$ is even or odd. For even $N$, $\lceil \frac{N}{2} \rceil = \frac{N}{2}$; for odd $N$, it becomes $\frac{N}{2}+1$.

These approaches are efficient with a time complexity of $O(1)$ per test case, ensuring that they work well within the problem’s constraints.

Happy coding and best of luck with your DSA interview preparations!

</details>
