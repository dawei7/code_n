# Petrol ki Problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PTRLP |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [PTRLP](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_03/problems/PTRLP) |

---

## Problem Statement

Alice is an engineer. They live in a circular world where the whole world is joined with a single circular road. She and her friends have a car with infinite fuel storing capacity.
They have a plan to go all around the world once and return to the same place again from where they started. But they initially have an empty tank. There are a total of $N$ Petrol pumps along the way. Considering 0 based indexing,The cost of going from ith Petrol pump to $i+1^{th}$ ***(Note that $n-1^{th}$ petrol pump takes you to $0^{th}$ petrol pump)*** Petrol Pump is $cost[i]$ and the amount of Petrol available at $i^{th}$ petrol pump is $petrol[i]$ where both the arrays cost and petrol will be given and $i \lt n$.
But they aren’t able to figure out where to start from to make such a trip, or if such a trip is even possible with their world. Help them figure this out.

---

## Input Format

The first line will contain $N $
The second line will contain $N$ integers separated by space where $i^{th}$ integer is $petrol[i]$
The third line will contain $N$ integers separated by space where $i^{th}$ integer is $cost[i]$

---

## Output Format

Output the number of the petrol pump (0-indexed) they should start from so that they can complete the trip and if they cannot complete the trip , output -1.

---

## Constraints

- $1 \leq N \leq 10^5$
- $0 \leq cost[i],petrol[i] \leq 10^4$

---

## Examples

**Example 1**

**Input**

```text
4
5 8 2 8
6 5 6 6
```

**Output**

```text
3
```

**Explanation**

Its only if they start from the last petrol pump that they start ,they can reach the same petrol pump again.

**Example 2**

**Input**

```text
3
2 3 4
3 4 3
```

**Output**

```text
-1
```

**Explanation**

No matter where they start, they cannot complete the trip.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Finding the Starting Petrol Pump

In this lesson, we explore a classic problem often known as the “Gas Station” problem. The challenge is to find a starting petrol pump (or gas station) such that, beginning with an empty tank, you can traverse a circular route and return to the same starting point without running out of fuel. Given two arrays, $petrol$ and $cost$, where each $petrol[i]$ represents the fuel you can obtain at pump $i$ and $cost[i]$ represents the fuel required to reach the next pump, our goal is to determine the valid starting index. If no such starting point exists, we output $-1$.

The key observation is that if the total net fuel, computed as
$$
T = \sum_{i=0}^{n-1} \left( petrol[i] - cost[i] \right),
$$
is negative, then no solution exists because even if you try all pumps, you won’t have enough fuel for the complete journey.

Below, we discuss two efficient approaches to solve this problem.

---

## Approach 1: Greedy Single-Pass Algorithm

### Idea
Instead of trying every possible start, we compute the net fuel surplus across the entire circle. We maintain two variables:
- **Total surplus**: $T = \sum_{i=0}^{n-1} \left( petrol[i] - cost[i] \right)$
- **Current surplus**: $S$, which tracks the fuel balance as we iterate.

If at any index $i$, the current surplus $S$ becomes negative, we reset it to $0$ and set the starting candidate to $i+1$, because no station between the old start and $i$ can serve as a valid starting point.

### Mathematical Explanation
We compute:
$$
T = \sum_{i=0}^{n-1} \left( petrol[i] - cost[i] \right)
$$
If $T < 0$, then a complete trip is impossible. While traversing, we update:
$$
S = S + \left( petrol[i] - cost[i] \right)
$$
If at any point $S < 0$, we set:
$$
S = 0 \quad \text{and} \quad \text{start} = i + 1.
$$

### Time Complexity
This approach processes the list in a single pass, giving it a time complexity of $O(n)$, making it very efficient.

### C++ Code
```cpp
#include
#include
using namespace std;

int main(){
    int n;
    cin >> n;
    vector petrol(n), cost(n);
    for (int i = 0; i < n; i++) {
        cin >> petrol[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> cost[i];
    }

    int total_surplus = 0, surplus = 0, start = 0;
    for (int i = 0; i < n; i++){
        int diff = petrol[i] - cost[i];
        total_surplus += diff;
        surplus += diff;
        if(surplus < 0){
            surplus = 0;
            start = i + 1;
        }
    }

    cout << (total_surplus >= 0 ? start : -1) << endl;
    return 0;
}
```

### Python Code
```python
n = int(input())
petrol = list(map(int, input().split()))
cost = list(map(int, input().split()))

total_surplus = 0
surplus = 0
start = 0

for i in range(n):
    diff = petrol[i] - cost[i]
    total_surplus += diff
    surplus += diff
    if surplus < 0:
        surplus = 0
        start = i + 1

print(start if total_surplus >= 0 else -1)
```

---

## Approach 2: Two-Pointer Technique (Variation of Greedy)

### Idea
This method traverses the petrol pumps once using a two-pointer strategy to treat the problem as an interval-sum problem. As we simulate the journey:
- If the current surplus becomes negative, we record the shortfall (or deficit) and move the starting pointer to the next index.
- Finally, we combine the recorded deficit with the remaining surplus. If the overall sum is non-negative, the journey is possible starting from the updated index.

### Explanation
We maintain:
- **$surplus$**: the current running surplus,
- **$deficit$**: the accumulated negative balance when the surplus drops below zero,
- **$start$**: the candidate starting index.

For each pump:
1. Update the surplus:
   $$
   surplus = surplus + \left( petrol[i] - cost[i] \right)
   $$
2. If $surplus < 0$, add the surplus (which is negative) to the deficit, reset the surplus, and update the start pointer:
   $$
   deficit = deficit + surplus,\quad start = i + 1,\quad \text{and}\quad surplus = 0.
   $$
3. At the end, if $surplus + deficit \geq 0$, the start pointer is valid.

### C++ Code
```cpp
#include
#include
using namespace std;

int main(){
    int n;
    cin >> n;
    vector petrol(n), cost(n);
    for (int i = 0; i < n; i++) {
        cin >> petrol[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> cost[i];
    }

    int start = 0, surplus = 0, deficit = 0;
    for (int i = 0; i < n; i++){
        surplus += petrol[i] - cost[i];
        if(surplus < 0){
            deficit += surplus;
            start = i + 1;
            surplus = 0;
        }
    }

    cout << (surplus + deficit >= 0 ? start : -1) << endl;
    return 0;
}
```

### Python Code
```python
n = int(input())
petrol = list(map(int, input().split()))
cost = list(map(int, input().split()))

start = 0
surplus = 0
deficit = 0

for i in range(n):
    surplus += petrol[i] - cost[i]
    if surplus < 0:
        deficit += surplus
        start = i + 1
        surplus = 0

print(start if surplus + deficit >= 0 else -1)
```

---

## Conclusion

- **Approach 1 (Greedy Single-Pass)** is both intuitive and efficient with a linear time solution. It is a recommended approach for practical use.
- **Approach 2 (Two-Pointer Technique)** offers a variation on the greedy approach by explicitly handling deficits along with surpluses, arriving at the same final decision.

Understanding these approaches develops a strong foundation for tackling similar optimization problems in technical interviews.

</details>
