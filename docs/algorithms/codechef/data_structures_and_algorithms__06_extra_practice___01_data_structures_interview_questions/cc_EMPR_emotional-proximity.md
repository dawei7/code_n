# Emotional Proximity

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EMPR |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 1 |
| Official Link | [EMPR](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_01/problems/EMPR) |

---

## Problem Statement

You are given $T$ testcases , each testcase consists of 4 numbers , $P$,$X$,$Y$,$Z$.

You have a best friend named Rahul. $Z$ is $1$ if you will meet Rahul and $0$ otherwise. You initially has an Emotional Proximity of $P$, which increases by $Y\%$ if you meet Rahul and decreases by $X\%$ otherwise. You have to print the final Emotional Proximity.

---

## Input Format

- First line contains $T$ , Number of Testcases

- Now each test case contains
4 integers $P$,$X$,$Y$,$Z$

---

## Output Format

- For each testcase print one line containing a single real number - the final emotional proximity.

- Your answer is considered correct if its absolute or relative error doesn't exceed 1e-6.

---

## Constraints

- $1 \leq T \leq 30000$
- $1 \leq P \leq 10^6$
- $0 \leq X,Y \leq 100$
- $0 \leq Z \leq 1$

---

## Examples

**Example 1**

**Input**

```text
2
1 1 1 1 
1 1 1 0
```

**Output**

```text
1.0100000000
0.9900000000
```

**Explanation**

In first test case since $Z$ is 1 , so you meet Rahul and your Emotional Proximit increases by 1% of 1 , which is 0.01 so $1.01$

In second test case since $Z$ is 0 , so you doesnt meet Rahul and your Emotional Proximit decreases by 1% of 1 , which is 0.01 so $0.99$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 1 1
```

**Output for this case**

```text
1.0100000000
```



#### Test case 2

**Input for this case**

```text
1 1 1 0
```

**Output for this case**

```text
0.9900000000
```



**Example 2**

**Input**

```text
2
100 3 5 0
1010 3 5 1
```

**Output**

```text
97.0000000000
1060.5000000000
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
100 3 5 0
```

**Output for this case**

```text
97.0000000000
```



#### Test case 2

**Input for this case**

```text
1010 3 5 1
```

**Output for this case**

```text
1060.5000000000
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this problem, we are given the initial Emotional Proximity $P$, two percentage values $X$ and $Y$, and a flag $Z$. The flag indicates whether you meet your friend Rahul:
- If $Z = 1$, you meet Rahul and your proximity increases by $Y\%$.
- If $Z = 0$, you do not meet Rahul and your proximity decreases by $X\%$.

The objective is to compute the final Emotional Proximity using one of the following formulas:

$$
\text{Final Proximity} =
\begin{cases}
P \times \left(1 + \frac{Y}{100}\right) & \text{if } Z = 1 \\
P \times \left(1 - \frac{X}{100}\right) & \text{if } Z = 0
\end{cases}
$$

Below we discuss two simple approaches to solve this problem.

---

### Approach 1: Basic Conditional Check

In this approach, we simply use an `if-else` condition to check the value of $Z$. If $Z = 1$, we calculate the increased value; otherwise, we calculate the decreased value.

**Explanation:**

1. Read the value of $T$ (the number of test cases).
2. For each test case, read the values $P$, $X$, $Y$, and $Z$.
3. If $Z = 1$, update $P$ as:
   $$
   P = P \times \left(1 + \frac{Y}{100}\right)
   $$
4. Else, update $P$ as:
   $$
   P = P \times \left(1 - \frac{X}{100}\right)
   $$
5. Print the computed value of $P$ with a precision of $10$ decimal places.

**C++ Implementation:**

```cpp
#include
#include
using namespace std;

int main() {
    int T;
    cin >> T;

    cout << fixed << setprecision(10);

    while (T--) {
        double P, X, Y;
        int Z;
        cin >> P >> X >> Y >> Z;

        if (Z == 1) {
            P = P * (1 + Y / 100);
        } else {
            P = P * (1 - X / 100);
        }

        cout << P << "\n";
    }

    return 0;
}
```

**Python Implementation:**

```python
T = int(input())
for _ in range(T):
    P, X, Y, Z = input().split()
    P = float(P)
    X = float(X)
    Y = float(Y)
    Z = int(Z)

    if Z == 1:
        P = P * (1 + Y / 100)
    else:
        P = P * (1 - X / 100)

    print("{:.10f}".format(P))
```

---

### Approach 2: Utilizing a Ternary Operator for Conciseness

In this approach, we compute the multiplier in a single expression. We use a ternary operator (or the inline conditional expression in Python) to determine the correct factor based on $Z$.

**Explanation:**

1. Read the input values.
2. Calculate a multiplier:
   - If $Z = 1$, the multiplier is $1 + \frac{Y}{100}$.
   - Otherwise, it is $1 - \frac{X}{100}$.
3. Multiply $P$ by the computed multiplier:
   $$
   P = P \times \text{multiplier}
   $$
4. Print the final result with formatting to $10$ decimal places.

**C++ Implementation:**

```cpp
#include
#include
using namespace std;

int main() {
    int T;
    cin >> T;

    cout << fixed << setprecision(10);

    while (T--) {
        double P, X, Y;
        int Z;
        cin >> P >> X >> Y >> Z;

        double multiplier = (Z == 1) ? (1 + Y / 100) : (1 - X / 100);
        P *= multiplier;

        cout << P << "\n";
    }

    return 0;
}
```

**Python Implementation:**

```python
T = int(input().strip())
for _ in range(T):
    P, X, Y, Z = input().split()
    P, X, Y, Z = float(P), float(X), float(Y), int(Z)

    multiplier = 1 + Y / 100 if Z == 1 else 1 - X / 100
    result = P * multiplier

    print("{:.10f}".format(result))
```

---

Both approaches have a time complexity of $\mathcal{O}(T)$ per test case and are straightforward because the calculations involve only basic arithmetic operations. For beginners, these methods illustrate how conditional statements and inline conditional expressions work, and they also show how to handle input/output formatting efficiently.

</details>
