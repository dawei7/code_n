# Three Number Expression

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EXPRESSION_3 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 1 |
| Official Link | [EXPRESSION_3](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_01/problems/EXPRESSION_3) |

---

## Problem Statement

You are given $T$ testcases , in each testcase you are given three numbers $A$, $B$ and $C$ .
 Find that whether an expression of the form $`` x \hspace{0.2em} A \hspace{0.2em} y \hspace{0.2em} B \hspace{0.2em} z \hspace{0.2em} C "$ exists ( where $x$ , $y$ and $z$ can be $+$ or $-$ ) , such that the final result is $0$. If it exists print $``YES"$ (without quotes), else print $``NO"$(without quotes).

---

## Input Format

- First line contains $T$ , Number of Testcases

- Now each test case contains 3 integers $A$,$B$,$C$

---

## Output Format

- For each testcase print one line consisting of $``YES"$ or $``NO"$ (without quotes) as described in problem.

Output is Case-Insensitive i.e. $``Yes"$ , $``nO"$ , $``YeS"$ all will be considered correct.

---

## Constraints

- $1 \leq T \leq 100000$
- $1 \leq A,B,C \leq 10^{18}$

---

## Examples

**Example 1**

**Input**

```text
2
1 1 1 
1000000000000000000 1000000000000000000 1000000000000000
```

**Output**

```text
NO 
NO
```

**Explanation**

We can't make any expression using + or - in both the cases such that the final result equals 0.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 1
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
1000000000000000000 1000000000000000000 1000000000000000
```

**Output for this case**

```text
NO
```



**Example 2**

**Input**

```text
3
1 2 1
2 1 1
1000000000000000000 600000000000000000 400000000000000000
```

**Output**

```text
YES 
YES
YES
```

**Explanation**

In first testcase : + 1 - 2 + 1 = 0

In Second testcase : + 2 - 1 - 1 = 0

In third testcase : + 1000000000000000000 - 600000000000000000 - 400000000000000000 = 0

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2 1
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
2 1 1
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
1000000000000000000 600000000000000000 400000000000000000
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial on the Problem

In this problem, we are given three positive integers $A$, $B$, and $C$, and we need to determine whether it is possible to insert the operations $+$ or $-$ in between them (forming an expression of the form $ x\; A\; y\; B\; z\; C $, where $x$, $y$, and $z$ are either $+$ or $-$) such that the final result is $0$. Since all numbers are positive, the options for cancellation are limited. Let’s explore three different approaches to solve this problem.

## Approach 1: Brute Force Enumeration

Since there are three numbers and each can be either positive or negative, there are $2^3 = 8$ possible sign combinations. These combinations correspond to checking the following equations:
$$
\begin{aligned}
A+B+C &= 0 \\
A+B-C &= 0 \\
A-B+C &= 0 \\
A-B-C &= 0 \\
-A+B+C &= 0 \\
-A+B-C &= 0 \\
-A-B+C &= 0 \\
-A-B-C &= 0 \\
\end{aligned}
$$

Even though most combinations are unlikely to yield zero (because $A$, $B$, and $C$ are positive), checking all possibilities ensures that no valid assignment is missed.

### Code for Approach 1

**C++:**
```cpp
#include
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while(t--) {
        long long A, B, C;
        cin >> A >> B >> C;

        bool possible = false;
        if (A + B + C == 0) possible = true;
        if (A + B - C == 0) possible = true;
        if (A - B + C == 0) possible = true;
        if (A - B - C == 0) possible = true;
        if (-A + B + C == 0) possible = true;
        if (-A + B - C == 0) possible = true;
        if (-A - B + C == 0) possible = true;
        if (-A - B - C == 0) possible = true;

        cout << (possible ? "YES" : "NO") << "\n";
    }

    return 0;
}
```

**Python:**
```python
t = int(input())
for _ in range(t):
    A, B, C = map(int, input().split())
    possible = (A + B + C == 0 or
                A + B - C == 0 or
                A - B + C == 0 or
                A - B - C == 0 or
                -A + B + C == 0 or
                -A + B - C == 0 or
                -A - B + C == 0 or
                -A - B - C == 0)
    print("YES" if possible else "NO")
```

## Approach 2: Mathematical Observation

A closer examination of the problem reveals that the only way to reach a sum of zero is to have one number equal to the sum of the other two. This is because to cancel out two positive numbers, one of them must be positive and the other two negative (or vice versa). With this observation, we only need to check three conditions:

- $$+A - B - C = 0 \quad \Rightarrow \quad A = B + C$$
- $$-A + B - C = 0 \quad \Rightarrow \quad B = A + C$$
- $$-A - B + C = 0 \quad \Rightarrow \quad C = A + B$$

Thus, if any of these conditions hold, the answer is "YES"; otherwise, it is "NO".

### Code for Approach 2

**C++:**
```cpp
#include
using namespace std;

bool canFormZero(long long a, long long b, long long c) {
    return (a == b + c) || (b == a + c) || (c == a + b);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        long long a, b, c;
        cin >> a >> b >> c;

        cout << (canFormZero(a, b, c) ? "YES" : "NO") << "\n";
    }

    return 0;
}
```

**Python:**
```python
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a == b + c or b == a + c or c == a + b:
        print("YES")
    else:
        print("NO")
```

## Approach 3: Sorting and Checking

Another efficient method is to sort the three numbers. Once sorted, let the array be $[x, y, z]$, where $z$ is the largest number. For a valid sign assignment to exist, the largest number must be equal to the sum of the two smaller numbers (i.e., $z = x + y$). This is because the only plausible valid expression is to have $z$ with a positive sign and the other two with negative signs (or vice versa), which leads directly to the condition:
$$ z = x + y $$

### Code for Approach 3

**C++:**
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
        long long arr[3];
        cin >> arr[0] >> arr[1] >> arr[2];
        sort(arr, arr+3);
        cout << ((arr[2] == arr[0] + arr[1]) ? "YES" : "NO") << "\n";
    }
    return 0;
}
```

**Python:**
```python
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    arr.sort()
    print("YES" if arr[2] == arr[0] + arr[1] else "NO")
```

## Conclusion

- **Approach 1 (Brute Force):** Checks all 8 possible sign combinations. It is easy to understand but involves more comparisons.
- **Approach 2 (Mathematical Observation):** Recognizes that one number must equal the sum of the other two, reducing the checks to just three conditions.
- **Approach 3 (Sorting and Checking):** Sorts the input and verifies if the largest number is the sum of the other two, which is a very intuitive method given all numbers are positive.

For this problem, Approaches 2 and 3 are more efficient and intuitive. They demonstrate how understanding the properties of the numbers can simplify the solution.

</details>
