# Defeat The Monster 2

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MONSTER2 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 2 |
| Official Link | [MONSTER2](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_02/problems/MONSTER2) |

---

## Problem Statement

A monster has $A$ health points and you have $B$ health points. Each time you hit the monster it loses $X$ health points. However, right before every one of your hits, the monster always gains $Y$ health points by taking away $Y$ of your health points.

A person (which refers to either you or the monster) is considered defeated when the number of health points it has becomes zero or less than zero. After a finite number of hits, either you or the monster will be defeated. You need to find whether you or the monster will be defeated.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains four space-separated integers $A$, $B$, $X$ and $Y$.

---

## Output Format

- For each test case, print a single line containing one integer. That integer should be $1$ if the monster will be defeated or $0$ if you will be defeated.

---

## Constraints

- $1 \leq T \leq 100$

- $1 \leq A,B,X,Y \leq 10^{9}$

---

## Examples

**Example 1**

**Input**

```text
3
4 6 4 2
2 2 1 2
4 5 3 1
```

**Output**

```text
1
0
1
```

**Explanation**

**Example case 1:** Before you hit the monster for the first time, it will take $Y=2$ of your health points so that it has $6$ health points and you are left with $4$ health points. After you hit the monster, it will have $2$ health. After that, the monster takes $Y=2$ of your health points, so that it has $4$ health points and you are left with $2$ health points. The next time you hit the monster, it will be defeated.

**Example case 2:** The monster will defeat you straight away by taking $Y=2$ of your health points.

**Example case 3:** The monster will be defeated after the second time you hit it.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 6 4 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2 2 1 2
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
4 5 3 1
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will explore a problem where you and a monster duel using health points. The monster starts with $A$ health points and you start with $B$ health points. Before each of your attacks, the monster gains $Y$ health points while simultaneously reducing your health by $Y$. Then you hit the monster and reduce its health by $X$. The monster is defeated when its health becomes zero or less, and you lose if your health reaches zero or less before you can defeat the monster.

The challenge is to decide whether you or the monster will be defeated after a finite number of moves.

Below, we describe the approach to solve this problem:

---

### Approach: Direct Mathematical Calculation

#### **Intuition:**

Before each hit, the monster “steals” $Y$ health from you. This means that you must have more than $Y$ health to perform any attack. Moreover, when you attack the monster, its net health reduction is $X - Y$ (since it gains $Y$ just before your attack). Therefore:
- **Immediate loss conditions:**
  - If $B \leq Y$, you cannot survive even one “health-reducing” event.
  - If $X \leq Y$, then every attack you make does not result in a net reduction of the monster’s health. In that case, the monster’s health never drops below its initial level.

- **Calculating Maximum Attacks You Can Perform:**
  Since your health decreases by $Y$ before every hit, you can perform at most
  $$\text{maxHits} = \left\lfloor \dfrac{B - 1}{Y} \right\rfloor$$
  hits (we subtract $1$ to ensure your health stays positive).

- **Calculating Attacks Needed to Defeat the Monster:**
  Each effective hit reduces the monster's health by
  $$X - Y.$$
  Thus, to reduce the monster’s health from $A$ to zero or below, you need
  $$\text{hitsNeeded} = \left\lceil \dfrac{A}{X - Y} \right\rceil$$
  hits.

- **Final Decision:**
  If $\text{hitsNeeded} \leq \text{maxHits}$, then you defeat the monster (output $1$); otherwise, you lose (output $0$).

This approach is efficient with a time complexity of $O(1)$ per test case and is well-suited for large inputs.

#### **Code Implementation:**

Below, we present the code in both C++ and Python for this approach.

**C++ Implementation:**

```cpp
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        long long A, B, X, Y;
        cin >> A >> B >> X >> Y;

        // If you don't have enough health for at least one hit or if the net damage is non-positive.
        if(B <= Y || X <= Y){
            cout << 0 << "\n";
            continue;
        }

        long long maxHits = (B - 1) / Y;
        long long diff = X - Y;
        long long hitsNeeded = (A + diff - 1) / diff;

        cout << (hitsNeeded <= maxHits ? 1 : 0) << "\n";
    }

    return 0;
}
```

**Python Implementation:**

```python
t = int(input())
for _ in range(t):
    A, B, X, Y = map(int, input().split())

    if B <= Y or X <= Y:
        print(0)
        continue

    maxHits = (B - 1) // Y
    diff = X - Y
    hitsNeeded = (A + diff - 1) // diff

    print(1 if hitsNeeded <= maxHits else 0)
```

---

### Summary

- **Direct Mathematical Calculation Approach:**
  - **Advantages:** Efficient ($O(1)$ per test case) and handles large inputs gracefully.
  - **Process:** Compute the maximum number of hits you can perform and the required number of hits to defeat the monster. By comparing these values, you determine the outcome.

This is the recommended solution for scenarios with strict performance constraints.

Happy coding and good luck with your DSA interview preparation!

</details>
