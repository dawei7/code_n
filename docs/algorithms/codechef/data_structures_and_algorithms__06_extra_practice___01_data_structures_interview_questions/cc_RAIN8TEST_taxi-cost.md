# Taxi Cost

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RAIN8TEST |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 1 |
| Official Link | [RAIN8TEST](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_01/problems/RAIN8TEST) |

---

## Problem Statement

If you travel to work by taxi, it costs you $X$ dollars. If you travel by foot it is, of course,
free of charge. You want to minimize the cost of travel, but you don’t want to walk
when it’s raining or it has rained the day before. Given the weather forecast for the
next $N$ days ($1$ if the rain is falling, $0$ otherwise), calculate the cost of travel.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains $2$ integers $N$ - number of days and $X$ - cost for taxi
- The second line contains $N$ space-separated integers $D_1, D_2 … D_n$

---

## Output Format

For each test case, output a single line containing one integer - Total cost of the travel.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq X \leq 10^9$

Sum of $N$ over all test cases $\leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
2
1 53
0
2 47
1
0
```

**Output**

```text
0
94
```

**Explanation**

- Test Case 1 : Day 1 : No rain. So, we can walk. Thus total cost is 0.
- Test Case 2 : Day 1 : Rain. So, we need to travel to work by taxi. Total cost on day 1 = 47.
Day 2 : No rain. But since it rained the previous day, we need to travel to work by taxi. Total cost on day 2 = 94

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Minimizing Travel Cost under Rainy Conditions

In this problem, you are given the travel cost $X$ for a taxi ride and a weather forecast for $N$ days. If it rains on a day (denoted by a $1$ in the forecast) or if it rained on the previous day, then you must take a taxi on that day, costing you $X$ dollars. Otherwise, you can walk to work at no cost. The goal is to compute the total travel cost over $N$ days.

## Approach 1: Simulation Using a Boolean Flag

### Explanation:
In this approach, we simulate the process day-by-day using a boolean flag, $\texttt{rainYesterday}$, to keep track of whether the previous day experienced rain.

For each day $i$ (with $0 \leq i < N$ in zero-indexed notation):
- If the forecast for day $i$ is $1$ (i.e., it is raining) **or** if $\texttt{rainYesterday}$ is true (meaning it rained on day $i-1$), then add $X$ to the total cost.
- Update $\texttt{rainYesterday}$ to reflect whether it is raining on the current day.

This method is both intuitive and efficient, running in $O(N)$ time per test case. The decision at each day is made independently based on the current day's forecast and the previous day's condition.

**Mathematical Representation:**

$$
\text{cost}_i = \begin{cases}
X, & \text{if } D_i = 1 \text{ or } (i > 0 \text{ and } D_{i-1} = 1) \\
0, & \text{otherwise.}
\end{cases}
$$

By summing all $\text{cost}_i$, we obtain the total travel cost for the $N$ days.

### Code Implementation

#### C++ Code:
```cpp
#include
#include
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        int N, X;
        cin >> N >> X;
        vector forecast(N);
        for (int i = 0; i < N; i++) {
            cin >> forecast[i];
        }
        long long totalCost = 0;
        bool rainYesterday = false;
        for (int i = 0; i < N; i++) {
            if (forecast[i] == 1 || rainYesterday) {
                totalCost += X;
            }
            rainYesterday = (forecast[i] == 1);
        }
        cout << totalCost << "\n";
    }
    return 0;
}
```

#### Python Code:
```python
def calculate_travel_cost(N, X, forecast):
    total_cost = 0
    rain_yesterday = False
    for day in range(N):
        if forecast[day] == 1 or rain_yesterday:
            total_cost += X
        rain_yesterday = (forecast[day] == 1)
    return total_cost

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        N = int(input_data[index])
        X = int(input_data[index + 1])
        index += 2
        forecast = list(map(int, input_data[index:index+N]))
        index += N
        results.append(calculate_travel_cost(N, X, forecast))
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()
```

## Approach 2: Direct Index-Based Check

### Explanation:
This approach also simulates the sequence of days but uses direct index comparisons instead of maintaining an auxiliary flag variable. The idea is to treat the first day as a special case and then check the condition for each subsequent day by directly comparing the current and previous day’s forecasts.

- **Day 1:** Check if $D_1 = 1$. If it is, add $X$ to the total cost.
- **Day $i$ ($2 \leq i \leq N$):** Check if either $D_i = 1$ or $D_{i-1} = 1$. If either condition holds, add $X$ to the total cost.

This method leverages direct array indexing to determine if a taxi ride is needed on any given day and is equally efficient with a time complexity of $O(N)$.

### Code Implementation

#### C++ Code:
```cpp
#include
#include
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        int N, X;
        cin >> N >> X;
        vector forecast(N);
        for (int i = 0; i < N; i++) {
            cin >> forecast[i];
        }
        long long totalCost = 0;
        if (forecast[0] == 1) {
            totalCost += X;
        }
        for (int i = 1; i < N; i++) {
            if (forecast[i] == 1 || forecast[i-1] == 1) {
                totalCost += X;
            }
        }
        cout << totalCost << "\n";
    }
    return 0;
}
```

#### Python Code:
```python
def calculate_travel_cost(N, X, forecast):
    total_cost = 0
    if forecast[0] == 1:
        total_cost += X
    for i in range(1, N):
        if forecast[i] == 1 or forecast[i-1] == 1:
            total_cost += X
    return total_cost

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        N = int(input_data[index])
        X = int(input_data[index + 1])
        index += 2
        forecast = list(map(int, input_data[index:index+N]))
        index += N
        results.append(calculate_travel_cost(N, X, forecast))
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()
```

Both approaches correctly compute the total cost in $O(N)$ time per test case, which makes them optimal given the provided constraints. Choosing between them depends on your coding style; Approach 1 uses a state variable to remember the previous day's condition, whereas Approach 2 directly checks the necessary condition by indexing.

</details>
