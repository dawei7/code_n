# Chef Airlines

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AIRTRAV |
| Difficulty Rating | 1500 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Queues |
| Official Link | [AIRTRAV](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_09/problems/AIRTRAV) |

---

## Problem Statement

You are a premium member of Chef Airlines which means you can store $miles$ in your Chef Airlines account. If you currently have $x$ miles in your Chef Airlines account then you can travel $x$ miles for free. You start from the airport labelled $0$ and wish to reach airport labelled $N$. Following are the rules of travel :

- If you are at the airport labelled $i$, you can travel to any airport labelled $j$, only if $j > i$;

- If you travel from airport labelled $i$ to airport labelled $j$, you end up exhausting $j - i$ miles from your Chef Airlines account. Consequently, you can travel from airport labelled $i$ to airport labelled $j$ if and only if $j - i \leq x$, where $x$ is the number of miles in your Chef Airlines account when you departed from the airport labelled $i$.

- Whenever you arrive at airport labelled $i$, you can add up to $M_i$ number of miles in your Chef Airlines account. There is no limit to the number of miles your Chef Airlines account can hold.

- You start by arriving at airport labelled $1$ with $0$ miles in your Chef Airlines account.

Determine the minimum number of airports you must visit in order to reach the airport labelled $N$. If it is not possible to do so, print $-1$.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- The first line of each testcase contains $N$ integers.
- The second line of each testcase contains $N$ integers : $M_1, M_2 . . . M_N$.

---

## Output Format

For each testcase, print the minimum number of airports you must visit in order to reach the airport labelled $N$. If it isn't possible to reach airport labelled $N$, print "-1" (without quotes).

---

## Constraints

- $1 \leq T \leq 15$
- $1 \leq N \leq 10^5$
- $0 \leq M_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
10
3 0 2 5 7 1 3 10 4 3
8
2 2 1 0 0 1 0 0
```

**Output**

```text
4
-1
```

**Explanation**

**Test-case 1:**
- You reach airport labelled $1$ with $0$ miles in your Chef Airlines account.
- You add $3$ miles to your Chef Airlines account. You now have $3$ miles in your Chef Airlines account.
- You reach airport labelled $3$ with $1$ miles remaining in your Chef Airlines account.
- You add $2$ miles to your Chef Airlines account. You now have $3$ miles in your Chef Airlines account.
- You reach airport labelled $5$ with $1$ mile remaining in your Chef Airlines account.
- You add $4$ miles to your Chef Airlines account. You now have a total of $5$ miles in your Chef Airlines account which is enough to reach airport labelled $N = 10$.

You visited a total of $4$ airports.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10
3 0 2 5 7 1 3 10 4 3
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
8
2 2 1 0 0 1 0 0
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# DSA Interview Preparation – Minimum Number of Airports (Refuel Stops) Editorial

In this lesson, we discuss how to determine the minimum number of airports you must visit (or “stops” you must make) to reach the final airport. At each airport you land on, you “pick up” some miles (fuel) that can be used for future travel. However, you may only travel from an airport $i$ to an airport $j$ (with $j > i$) if the difference $(j-i)$ is at most the miles you have stored. You must carefully choose which airports to stop at so that you can “refuel” optimally and reach your destination with the fewest stops.

---

## Approach: Greedy with Max Heap

### Idea

The greedy solution uses a max-heap (or priority queue) to always pick the airport with the maximum available miles when additional fuel is required. We simulate the journey from the first airport (indexed as $0$, corresponding to airport $1$ in the problem) to the final airport (index $N-1$, corresponding to airport $N$).

Define two key variables:
- **cur**: the farthest airport (index) you can reach with your current available miles.
- **stops**: the count of airports visited (each stop corresponds to “refueling” using a previously visited airport).

**Algorithm:**
1. Initialize `cur = 0` (current reach) and `stops = 1` (since you start at the first airport and add its miles).
2. Iterate over all airports (using index $i$ from $0$ to $N-1$). For each airport:
   - **While** $cur < i$, it means you cannot reach the current airport with the available fuel. Pick the largest fuel addition available from the previously passed airports by popping from the max-heap. Add that fuel to `cur` and increment `stops` by $1$.
   - If, even after refueling, you cannot reach $i$, then it is impossible to continue; return $-1$.
   - Finally, push the miles available at the current airport into the max-heap for future use.
3. When the loop finishes, `stops` is the minimum number of stops needed to reach the final airport.

### Code Implementation

Below are the implementations in both C++ and Python.

#### C++ Code
```cpp
#include
#include
using namespace std;

int solve(int arr[], int n) {
    int stops = 1;  // We start by visiting the first airport.
    int cur = 0;    // Maximum airport index reachable with current miles.
    priority_queue pq;

    for (int i = 0; i < n; i++) {
        // If current reach is less than i, refuel using the best previous option.
        while (!pq.empty() && cur < i) {
            cur += pq.top();
            pq.pop();
            stops++;
        }
        if (cur < i) return -1;  // Cannot reach this airport.
        pq.push(arr[i]);  // Save the miles from the current airport for future jumps.
    }
    return stops;
}

int main(){
    int t;
    cin >> t;

    while(t--){
        int n;
        cin >> n;
        int arr[n];

        for(int i = 0; i < n; i++){
            cin >> arr[i];
        }
        cout << solve(arr, n) << "\n";
    }
    return 0;
}
```

#### Python Code
```python
import heapq

def solve(arr):
    n = len(arr)
    stops = 1  # First airport is taken, hence count starts at 1.
    cur = 0    # Current farthest reachable airport index.
    max_heap = []  # Using min-heap with negative values to simulate max-heap.

    for i in range(n):
        # Refuel using the best option if current reach is insufficient.
        while max_heap and cur < i:
            cur += -heapq.heappop(max_heap)
            stops += 1
        if cur < i:
            return -1  # Not possible to reach airport i.
        # Push current airport's fuel into max_heap.
        heapq.heappush(max_heap, -arr[i])
    return stops

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))
```

### Complexity

The greedy approach runs in $O(N \log N)$ time due to the insertion and removal operations from the max-heap. This method is efficient under the problem constraints.

---

## Summary

- **Greedy with Max Heap Approach:**
  This method simulates the journey by maintaining the maximum reachable airport index and refuels only when necessary by choosing the best available option from previously visited airports. It is both optimal and efficient, making it suitable for large inputs.

</details>
