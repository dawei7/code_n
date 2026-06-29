# Make smaller bigger

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MSB |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 2 |
| Official Link | [MSB](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_02/problems/MSB) |

---

## Problem Statement

Alice has 2 positive integers $A$ and $B$. She can perform 2 kind of operations:
1. Multiply $A$ by $X$ - to get $A \cdot X$
2. Divide $B$ by $Y$  - to get $\left \lfloor \frac{B}{Y} \right \rfloor$

Help Alice find the minimum number of operations required in order to make $A$ greater than or equal to $B$, or determine that it is not possible.

---

## Input Format

- The first line contains $T$ - number of test cases. Then the queries follow.
- The first line of each test case contains two positive integers: $A$ and $B$
- The second line of each test case contains two positive integers: $X$ and $Y$

---

## Output Format

For each test case output the minimal number of operations that Alice needs to perform in order to make $A$ greater than or equal to $B$, or output $-1$ if it is not possible to do so.

---

## Constraints

- $1 \leq T \leq 500$
- $1 \leq A, B, X, Y \leq 10^{18}$

---

## Examples

**Example 1**

**Input**

```text
3
5 2 3 2
4 20 2 2
1 10 1 3
```

**Output**

```text
0
3
2
```

**Explanation**

In the first test case:

$5$ is already greater than $2$, so Alice doesn’t need to perform any operation

In the second test case:

If we multiply $4$ three times $2$, we get $32$ which is greater than $20$. It can be proven that this is the minimal number of operations.

In the third test case:

Since multiplying $1$ by $1$ doesn’t increase $A$, we will only use the second operation and we need to divide $10$ by $3$ two times ($\left \lfloor \frac{10}{3} \right \rfloor= 3$, and then $\left \lfloor \frac{3}{3} \right \rfloor = 1$).

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2 3 2
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
4 20 2 2
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
1 10 1 3
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson we explore a problem where we have two numbers, $A$ and $B$, and two operations available:
1. Multiply $A$ by $X$.
2. Divide $B$ by $Y$ (using floor division).

Our objective is to apply these operations (in any order) a minimum number of times so that eventually $A \ge B$. If it is impossible to reach that goal, we must output $-1$.

The challenge in this problem lies in efficiently managing the two operations: while multiplying $A$ can rapidly increase its value, dividing $B$ can decrease the target value. To address this, we utilize a **Combined Simulation Approach** that covers all cases in a unified manner.

**Combined Simulation Approach**

This approach works as follows:

1. **Initial Check:**
   If $A \ge B$, no operations are performed and we output 0.

2. **Edge Cases:**
   - If both operations are ineffective (i.e. when $X=1$ and $Y=1$), it is impossible to reach the goal, so output $-1$.
   - When only one of the operations is effective (for example, if $Y=1$ so that division does not reduce $B$, or if $X=1$ so that multiplication does not increase $A$), the code handles these cases individually.

3. **General Case:**
   For the typical scenario where both operations have a noticeable effect (i.e. typically when $X>1$ and $Y>1$), we simulate applying a sequence of division operations on $B$. For each possible number of divisions (say, $d$), we determine the number of multiplications required on $A$ so that $A \ge$ (reduced $B$). We then choose the minimum total operations among all tested scenarios.

   Since each division reduces $B$ by at least a factor of $Y$, the simulation remains efficient even when $B$ is large.

Below are the C++ and Python code implementations of the Combined Simulation Approach.

#### C++ Code (Combined Simulation Approach)
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
        unsigned long long A, B, X, Y;
        cin >> A >> B >> X >> Y;

        if(A >= B){
            cout << 0 << "\n";
            continue;
        }

        // If both operations are ineffective.
        if(X == 1 && Y == 1){
            cout << -1 << "\n";
            continue;
        }

        // Handle cases when only one operation is effective.
        if(Y == 1){
            if(X == 1){
                cout << -1 << "\n";
            } else {
                long long ops = 0;
                __int128 currentA = A;
                while(currentA < B){
                    currentA *= X;
                    ops++;
                }
                cout << ops << "\n";
            }
            continue;
        }

        if(X == 1){
            long long divOps = 0;
            unsigned long long currentB = B;
            bool possible = false;
            while(true){
                if(A >= currentB){
                    possible = true;
                    break;
                }
                if(currentB == 0)
                    break;
                unsigned long long nextB = currentB / Y;
                if(nextB == currentB)
                    break;
                currentB = nextB;
                divOps++;
            }
            if(possible)
                cout << divOps << "\n";
            else
                cout << -1 << "\n";
            continue;
        }

        // General case: both X > 1 and Y > 1.
        long long best = LLONG_MAX;
        unsigned long long currentB = B;
        for (long long d = 0; ; d++){
            if(A >= currentB){
                if(d < best)
                    best = d;
            } else {
                long long m = 0;
                __int128 currentA = A;
                while(currentA < currentB){
                    currentA *= X;
                    m++;
                }
                if(m + d < best)
                    best = m + d;
            }
            if(currentB == 0)
                break;
            unsigned long long nextB = currentB / Y;
            if(nextB == currentB)
                break;
            currentB = nextB;
        }
        cout << best << "\n";
    }
    return 0;
}
```

#### Python Code (Combined Simulation Approach)
```python
import sys
input_data = sys.stdin.read().strip().split()
t = int(input_data[0])
index = 1
for _ in range(t):
    A = int(input_data[index]); B = int(input_data[index+1])
    X = int(input_data[index+2]); Y = int(input_data[index+3])
    index += 4
    if A >= B:
        print(0)
        continue
    # If both operations are ineffective.
    if X == 1 and Y == 1:
        print(-1)
        continue
    if Y == 1:
        if X == 1:
            print(-1)
        else:
            ops = 0
            currentA = A
            while currentA < B:
                currentA *= X
                ops += 1
            print(ops)
        continue
    if X == 1:
        divOps = 0
        currentB = B
        possible = False
        while True:
            if A >= currentB:
                possible = True
                break
            if currentB == 0:
                break
            nextB = currentB // Y
            if nextB == currentB:
                break
            currentB = nextB
            divOps += 1
        if possible:
            print(divOps)
        else:
            print(-1)
        continue

    best = float('inf')
    currentB = B
    d = 0
    while True:
        if A >= currentB:
            best = min(best, d)
        else:
            m = 0
            currentA = A
            while currentA < currentB:
                currentA *= X
                m += 1
            best = min(best, m + d)
        if currentB == 0:
            break
        nextB = currentB // Y
        if nextB == currentB:
            break
        currentB = nextB
        d += 1
    print(best)
```

**Summary:**
The Combined Simulation Approach efficiently addresses the interplay between multiplication and division. By simulating different counts of division operations on $B$ and computing the corresponding multiplication steps required for $A$, this unified strategy reliably computes the minimum number of operations needed (or determines impossibility) across a wide range of input scenarios.

</details>
