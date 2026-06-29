# Binary Search - Paint Walls

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP08 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Binary Search |
| Official Link | [PREP08](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_06/problems/PREP08) |

---

## Problem Statement

Chef has $N$ walls to paint where height of $i^{th}$ wall will be $C_i$. These integers, $C_1, C_2, \dots, C_N$, are given to you. There are $A$ painters available and each of them takes $B$ units of time to paint $1$ unit height of wall. Find the **minimum** time required to paint $N$ walls using following constraints:
1. A painter will only paint contiguous walls. This means that a painter painting walls $1$ and $3$ without painting wall $2$ will be invalid.
2. Any two painters can paint at the same time which mean painters can work simultaneously.
3. One wall cannot be painted partially by one painter and partially by another.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains three space-separated integers $N$, $A$, $B$ — the number of walls, painters and time to paint $1$ unit height of wall.
- The second line of each test case contains $N$ space-separated integers $C_1,C_2,\ldots,C_N$.

---

## Output Format

For each test case, output on a new line the **minimum** time required to paint $N$ walls.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N, B \leq 10^5$
- $1 \leq A \leq N$
- $1 \leq C_i \leq 10^5$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
2 2 5
4 5
5 2 10
2 8 2 6 6
```

**Output**

```text
25
120
```

**Explanation**

**Test case $1$**: One painter will paint first wall, other painter will paint second one. So first painter will use $20$ units time, other painter will use $25$ units time. So answer will be maximum of them which will be $25$.

**Test case $2$**: One painter will paint walls $[2, 8, 2]$, other will paint walls $[6, 6]$. So first painter will use $120$ units time, other painter will use $120$ units time. So answer will be maximum of them which will be $120$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2 5
4 5
```

**Output for this case**

```text
25
```



#### Test case 2

**Input for this case**

```text
5 2 10
2 8 2 6 6
```

**Output for this case**

```text
120
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Painter Partition Problem Editorial

In this lesson, we discuss a problem where we have $N$ walls with heights $C_1, C_2, \dots, C_N$, and we need to paint them using $A$ painters. Each painter takes $B$ units of time to paint one unit of wall height. Since each painter can only paint contiguous walls, the task is to partition the list of walls into $A$ contiguous segments in such a way that the maximum time taken to paint any segment is minimized. In other words, we want to minimize the maximum workload among all painters.

We focus on **one approach** to solve this problem:

---

## Approach 1: Binary Search with Greedy Feasibility Check

### Explanation

The idea is to search for the minimum possible "maximum time" a painter would take. The lower bound for the search is:
$$ L = \max_i (C_i) \times B $$
because a wall cannot be divided and the painter who paints the tallest wall will at least take this time.

The upper bound is:
$$ R = \left(\sum_{i=1}^{N} C_i\right) \times B $$
because if one painter paints all walls, that is the maximum time needed.

We use binary search in the range $[L, R]$. For a given guess (midpoint) $T$, we use a greedy algorithm:
1. Start assigning walls to painters.
2. For each wall, if adding it to the current painter’s workload exceeds $T$, we assign a new painter.
3. If we need more than $A$ painters to stay within $T$, the guess is too low.

This approach efficiently narrows down the minimum possible time and works in $O(N \times \log(\text{total time}))$, making it ideal for large inputs.

### Code Implementation

#### C++ Code
```cpp
#include
#include
#include
#include
using namespace std;
typedef long long ll;

bool canPaint(const vector& walls, ll painters, ll timeLimit, ll B) {
    ll count = 1, sum = 0;
    for (ll height : walls) {
        if (sum + height * B > timeLimit) {
            count++;
            sum = height * B;
            if (count > painters) return false;
        } else {
            sum += height * B;
        }
    }
    return true;
}

ll minTimeToPaint(const vector& walls, ll painters, ll B) {
    ll low = *max_element(walls.begin(), walls.end()) * B;
    ll high = accumulate(walls.begin(), walls.end(), 0LL) * B;

    while (low < high) {
        ll mid = low + (high - low) / 2;
        if (canPaint(walls, painters, mid, B))
            high = mid;
        else
            low = mid + 1;
    }
    return low;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while (T--) {
        ll N, A, B;
        cin >> N >> A >> B;
        vector walls(N);
        for (ll i = 0; i < N; i++) {
            cin >> walls[i];
        }
        cout << minTimeToPaint(walls, A, B) << "\n";
    }

    return 0;
}
```

#### Python Code
```python
def can_paint(walls, painters, time_limit, B):
    count = 1
    curr_sum = 0
    for height in walls:
        if curr_sum + height * B > time_limit:
            count += 1
            curr_sum = height * B
            if count > painters:
                return False
        else:
            curr_sum += height * B
    return True

def min_time_to_paint(walls, painters, B):
    low = max(walls) * B
    high = sum(walls) * B
    while low < high:
        mid = low + (high - low) // 2
        if can_paint(walls, painters, mid, B):
            high = mid
        else:
            low = mid + 1
    return low

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        N = int(input_data[index]); index += 1
        A = int(input_data[index]); index += 1
        B = int(input_data[index]); index += 1
        walls = list(map(int, input_data[index:index+N])); index += N
        results.append(min_time_to_paint(walls, A, B))
    print("\n".join(map(str, results)))
```

---

## Conclusion

The **Binary Search with Greedy Feasibility Check** approach is both efficient and straightforward, making it an excellent method for solving the Painter Partition Problem even for large inputs. By optimally narrowing down the search space, we ensure that the maximum time taken by any painter is minimized.

</details>
