# Defeat The Monster 1

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MONSTER1 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 1 |
| Official Link | [MONSTER1](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_01/problems/MONSTER1) |

---

## Problem Statement

A monster has $H$ health points. Each time you hit it with a sword it loses $X$ health points. However, the monster always gains $Y$ health points right before every one of your hits.

The monster is considered defeated when the number of health points it has becomes zero or less than zero. You need to find if it is possible to defeat the monster.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains three space-separated integers $H$, $X$ and $Y$.

---

## Output Format

- For each test case, print a single line containing one integer. That integer should be $1$ if it is possible to defeat the monster and $0$ otherwise.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq H,X,Y \leq 10^{18}$

---

## Examples

**Example 1**

**Input**

```text
4
3 6 2
4 6 3
7 1 2
1 1 2
```

**Output**

```text
1
1
0
0
```

**Explanation**

**Example case 1:** The monster will have $3+2=5$ health points before the first hit. Therefore, it will be defeated after the first hit.

**Example case 2:** The monster will have $4+3=7$ health points before the first hit. After the first hit, the monster will have $7-6=1$ health point. Before the second hit, the monster will have $1+3=4$ health points. Therefore, it will be defeated after the second hit.

**Example case 3:** It is impossible to defeat the monster.

**Example case 4:** It is impossible to defeat the monster.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 6 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4 6 3
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
7 1 2
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
1 1 2
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# DSA Interview Preparation Editorial

In this lesson, we analyze a problem where you must determine if it is possible to defeat a monster. The monster starts with $H$ health points, and before every hit, it recovers $Y$ health points. Each hit reduces its health by $X$ points. The monster is defeated when its health becomes zero or less.

We will explore three different approaches to solve this problem.

---

## Approach 1: Direct Mathematical Check

### Idea
The key observation is that after every hit, the monster’s health decreases by the net amount
$$ X - Y. $$
- **If** $X \leq Y$, then the net damage is not positive; the monster either stays at the same health or regains more than it loses, making defeat impossible.
- **If** $X > Y$, then the monster loses a positive amount of health every hit, and eventually it will be defeated.

### Explanation
Since the net decrease per hit is $X - Y$, the monster’s health after $n$ hits is:
$$ H - n \times (X - Y). $$
For the monster to be defeated, we need:
$$ H - n \times (X - Y) \leq 0. $$
This inequality shows that if $X > Y$, there exists a finite number of hits
$$ n \geq \frac{H}{X-Y} $$
that will ensure the monster is defeated.

### Code Implementation

#### C++ Code
```cpp
#include
using namespace std;

int main(){
    int T;
    cin >> T;
    while(T--){
        long long H, X, Y;
        cin >> H >> X >> Y;
        if(X <= Y)
            cout << 0 << "\n";
        else
            cout << 1 << "\n";
    }
    return 0;
}
```

#### Python Code
```python
T = int(input())
for _ in range(T):
    H, X, Y = map(int, input().split())
    print(0 if X <= Y else 1)
```

---

## Approach 2: Mathematical Calculation of Required Hits

### Idea
Instead of simply checking the condition, we can calculate the exact number of hits required to defeat the monster using the formula:
$$ n = \left\lceil \frac{H}{X-Y} \right\rceil. $$
Then we check if the number of hits is within a feasible limit (for instance, not exceeding $10^{18}$ based on problem constraints).

### Explanation
1. **Calculate Effective Damage:**
   Let $damage = X - Y$.
2. **Compute Number of Hits:**
   The minimum number of hits required is:
   $$ n = \frac{H + damage - 1}{damage} $$
   This formula is a common trick to compute the ceiling of a division between two integers.
3. **Feasibility Check:**
   If $X \leq Y$, the process is impossible. Otherwise, if the computed $n$ is within the acceptable range, the monster can be defeated.

### Code Implementation

#### C++ Code
```cpp
#include
using namespace std;

int main(){
    int T;
    cin >> T;
    const unsigned long long MAX_HITS = 1000000000000000000ULL; // $10^{18}$
    while(T--){
        unsigned long long H, X, Y;
        cin >> H >> X >> Y;
        if(X <= Y) {
            cout << 0 << "\n";
        } else {
            unsigned long long damage = X - Y;
            unsigned long long hits = (H + damage - 1) / damage;
            if(hits <= MAX_HITS)
                cout << 1 << "\n";
            else
                cout << 0 << "\n";
        }
    }
    return 0;
}
```

#### Python Code
```python
import math
T = int(input())
MAX_HITS = 10**18
for _ in range(T):
    H, X, Y = map(int, input().split())
    if X <= Y:
        print(0)
    else:
        damage = X - Y
        hits = (H + damage - 1) // damage
        print(1 if hits <= MAX_HITS else 0)
```

---

## Approach 3: Simulation Approach (For Smaller Constraints)

### Idea
This approach simulates the process of the monster regenerating and then taking damage. Although it is straightforward, it is only practical when the numbers are small because the loop might run for a very long time for large inputs.

### Explanation
1. **Simulate the Process:**
   For each hit:
   - First, increase the monster’s health by $Y$.
   - Then, reduce it by $X$.
2. **Check for Defeat:**
   The simulation stops if the monster’s health goes to zero or below or if it becomes evident that it will never decrease (i.e., when $X \leq Y$).
3. **Iteration Limit:**
   An iteration limit is set to prevent infinite loops in cases where defeating the monster is impossible.

### Code Implementation

#### C++ Code
```cpp
#include
using namespace std;

int main(){
    int T;
    cin >> T;
    while(T--){
        long long H, X, Y;
        cin >> H >> X >> Y;
        long long hits = 0;
        bool defeated = false;
        // Limit iterations to avoid infinite loop for large constraints
        while(hits < 1000000) {
            H += Y;  // Monster regenerates health
            H -= X;  // Your hit decreases health
            hits++;
            if(H <= 0) {
                defeated = true;
                break;
            }
            if(X <= Y) {  // No progress can be made if damage is not positive
                break;
            }
        }
        cout << (defeated ? 1 : 0) << "\n";
    }
    return 0;
}
```

#### Python Code
```python
T = int(input())
for _ in range(T):
    H, X, Y = map(int, input().split())
    hits = 0
    defeated = False
    while hits < 10**6:  # Limit iterations for simulation
        H += Y   # Monster regenerates health
        H -= X   # Your hit decreases health
        hits += 1
        if H <= 0:
            defeated = True
            break
        if X <= Y:  # No progress can be made if damage is not positive
            break
    print(1 if defeated else 0)
```

---

## Conclusion

The core observation is that the net effect on the monster's health per hit is $X-Y$:
- **Approach 1** leverages this observation by simply checking if $X > Y$, resulting in an $O(1)$ solution.
- **Approach 2** calculates the required number of hits explicitly, offering insight into the mathematical formulation.
- **Approach 3** demonstrates a simulation method, which is useful for understanding the process but is only practical for small inputs.

Each approach reinforces the importance of understanding the problem constraints and applying the correct strategy based on those constraints.

</details>
