# Minimum Divisible Digits

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINDIG |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Queues |
| Official Link | [MINDIG](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_09/problems/MINDIG) |

---

## Problem Statement

You have given a set of digits which you can use (multiple number of times) to make two numbers $a$ and $b$  $(a \lt b)$ such that $(b-a)$ is divisible by given number $X$.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- First line of each testcase contains of a single integer $N$ - number of digits in the set and $X$
- Next line contains $N$ space separated integers in increasing order $D_1, D_2, D_3, ......, D_N$

---

## Output Format

- For each test case, output a single line containing two integers $a$ and $b$.
- If multiple answer are possible then minimise $b$, if still multiple answer are possible then minimise $a$.

---

## Constraints

- $ 1 \leq T \leq 10^3$
- $ 1 \leq X \leq 10^5 $
- $ 1 \leq N \leq 9 $
- $ 1 \leq D_i \leq 9$

Sum of $X$ over all test cases will not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
2
2 9
1 2
1 8
3
```

**Output**

```text
2 11
333 3333
```

**Explanation**

**Test Case 1** :

First 5 numbers that can be formed using 1 and 2 are - 1 2 11 12 21 22
- Take $b = 1$ : Can't take any value of $a$ with satisfies the above conditions.
- Take $b = 2$ : Again, can't take any value of $a$.
- Take $b = 11$ : Now, $a$ must be taken as 2 as $(11 - 2) = 9$ is divisible by 9.

From above steps we can verify that $b$ or $a$ can't be minimised further.

**Test Case 2** : $a = 333$ and $b = 3333$ is the correct answer as (3333-333) = 3000 is divisible by 8.
It can be proved that neither $b$ nor $a$ can be minimised further.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 9
1 2
```

**Output for this case**

```text
2 11
```



#### Test case 2

**Input for this case**

```text
1 8
3
```

**Output for this case**

```text
333 3333
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will discuss one interesting problem that asks us to form two numbers, $a$ and $b$ (with $a < b$), using a given set of digits (each digit being available any number of times) such that the difference $(b - a)$ is divisible by an integer $X$. The challenge is to choose $a$ and $b$ so that if more than one answer is possible, then $b$ is minimized and, if still ambiguous, $a$ is minimized.

The key insight here is that if two numbers give the same remainder when divided by $X$, then their difference is divisible by $X$. In other words, if
$$
a \bmod X = r \quad \text{and} \quad b \bmod X = r,
$$
then
$$
(b - a) \bmod X = 0.
$$

### **BFS (State Space Search) for the General Case**

For solving this problem in a unified way (regardless of the number of digits available), we use a Breadth-First Search (BFS) strategy. The idea is to generate numbers by appending digits one by one and to maintain a mapping of remainders modulo $X$ to the first number (represented as a string) that produced that remainder. When a freshly generated number yields a remainder that has already been seen, we have found two numbers:
- The stored number corresponding to that remainder (denoted as $a$).
- The newly built number (denoted as $b$).

Because BFS explores numbers in increasing order (by the number of digits) and the digits are processed in increasing order, this method guarantees that $b$ is minimized and, in the event of ties, $a$ is minimized.

Below is the implementation for this BFS approach in both **C++** and **Python**.

#### **C++ Code for the BFS Approach**
```cpp
#include
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
        int N, X;
        cin >> N >> X;
        vector digits(N);
        for (int i = 0; i < N; i++){
            cin >> digits[i];
        }

        // Remove duplicate digits (digits are initially provided in increasing order).
        vector uniqueDigits;
        uniqueDigits.push_back(digits[0]);
        for (int i = 1; i < digits.size(); i++){
            if(digits[i] != digits[i - 1])
                uniqueDigits.push_back(digits[i]);
        }

        // Initialize remainder mapping and BFS queue.
        vector rem_str(X, "");
        queue q;
        string ans_a = "", ans_b = "";
        bool found = false;

        // Initialize with the one-digit numbers.
        for (int d : uniqueDigits){
            int r = d % X;
            string s = to_string(d);
            if(rem_str[r] != ""){
                ans_a = rem_str[r];
                ans_b = s;
                found = true;
                break;
            }
            rem_str[r] = s;
            q.push(r);
        }

        vector visited(X, false);
        while(!q.empty() && !found){
            int r = q.front();
            q.pop();
            if(visited[r])
                continue;
            visited[r] = true;

            // Try appending each digit.
            for (int d : uniqueDigits){
                int new_r = (r * 10 + d) % X;
                string s = rem_str[r] + char('0' + d);
                if(rem_str[new_r] != ""){
                    ans_a = rem_str[new_r];
                    ans_b = s;
                    found = true;
                    break;
                }
                rem_str[new_r] = s;
                q.push(new_r);
            }
        }

        if(found)
            cout << ans_a << " " << ans_b << "\n";
        else
            cout << "-1 -1\n";
    }
    return 0;
}
```

#### **Python Code for the BFS Approach**
```python
from collections import deque
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    parts = input().split()
    if not parts:
        break
    N, X = map(int, parts)
    digits = list(map(int, input().split()))

    # Remove duplicate digits (input digits are in increasing order)
    unique_digits = []
    unique_digits.append(digits[0])
    for i in range(1, len(digits)):
        if digits[i] != digits[i-1]:
            unique_digits.append(digits[i])

    # The list rem_str will hold the first number (as a string) that produces a given remainder.
    rem_str = [""] * X
    q = deque()
    ans_a = ans_b = ""
    found = False

    # Initialize with all possible single-digit numbers.
    for d in unique_digits:
        r = d % X
        s = str(d)
        if rem_str[r] != "":
            ans_a = rem_str[r]
            ans_b = s
            found = True
            break
        rem_str[r] = s
        q.append(r)

    visited = [False] * X
    while q and not found:
        r = q.popleft()
        if visited[r]:
            continue
        visited[r] = True
        for d in unique_digits:
            new_r = (r * 10 + d) % X
            s = rem_str[r] + str(d)
            if rem_str[new_r] != "":
                ans_a = rem_str[new_r]
                ans_b = s
                found = True
                break
            rem_str[new_r] = s
            q.append(new_r)
        if found:
            break

    if found:
        print(ans_a, ans_b)
    else:
        print("-1 -1")
```

### **Summary of Our Approach**

- **BFS Approach (General Case):**
  - **Idea:** Use modular arithmetic with a BFS strategy. Begin with one-digit numbers and append digits while tracking remainders modulo $X$.
  - **Result:** When a remainder repeats, the stored number for that remainder is $a$ (minimal) and the newly formed number is $b$, ensuring that $(b - a)$ is divisible by $X$.

This BFS method handles all cases uniformly and guarantees the minimal pair $(a, b)$ that satisfy the problem conditions.

</details>
