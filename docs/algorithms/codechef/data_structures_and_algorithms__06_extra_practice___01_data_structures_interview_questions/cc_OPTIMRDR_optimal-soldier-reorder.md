# Optimal Soldier Reorder

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | OPTIMRDR |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [OPTIMRDR](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_04/problems/OPTIMRDR) |

---

## Problem Statement

All the $N$ soldiers are asked to assemble in a line, the $i^{th}$ soldier stands on $pos[i]$, somehow their head officer got to know that there are some mines on the line so soldiers are asked to move in safe positions. There are $N$ safe distinct positions denoted by $safe\_pos[i]$. Each soldier has to move on one of the safe positions. Help the head officer in assigning safe positions to each soldier so that the total time to move is minimum.

**Note:** They move with the speed of 1 unit/sec and only one soldier can stand in one safe position.

---

## Input Format

- The first line will contain $1$ integer $N$, the number of soldiers .
- The second line contains $N$ spaces separated integers, where $i^{th}$ integer shows $pos[i]$.
- The third line contains $N$ spaces separated integers, where $i^{th}$ integer shows $safe\_pos[i]$.

---

## Output Format

Output $N$ space-separated integers, $i^{th}$ integer denotes the safe position where $i^{th}$ soldier stands so that the total time to move is minimum. If there are multiple ways to assign output the lexicographically lowest sequence.

---

## Constraints

- $1 \leq N \leq 10^5$
- $1 \leq pos[i],safe\_pos[i] \leq 10^{18}$

---

## Examples

**Example 1**

**Input**

```text
3
5 3 2
1 3 5
```

**Output**

```text
5 3 1
```

**Explanation**

This arrangement gives the minimum time.i.e(1 second).

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this problem, we are given the initial positions of $N$ soldiers and $N$ safe positions. Our goal is to assign each soldier a unique safe position in such a way that the total time for the soldiers to move to these positions is minimized. Since each soldier moves at a speed of 1 unit per second, the time taken by a soldier to move from position $a$ to position $b$ is simply $|a - b|$. Our objective is to minimize

$$
\sum_{i=0}^{N-1} |pos[i] - assigned\_pos[i]|
$$

while ensuring that the assigned sequence of safe positions (when arranged in the order of the original soldier indices) is lexicographically smallest if multiple assignments yield the same minimal total time.

Below, we discuss the primary approach for solving this problem.

---

### Approach: Sorted Assignment (Optimal Greedy Approach)

**Idea:**
The key observation is that when trying to minimize the sum of absolute differences between two sets of numbers, the best strategy is to pair them in sorted order. This is supported by the rearrangement inequality. Here’s what we do:

1. **Sort Soldiers by their Positions:**
   Maintain the original indices along with the positions by pairing each value with its index.

2. **Sort Safe Positions:**
   Sort the array of safe positions.

3. **Pair Them in Order:**
   Assign the smallest safe position to the soldier with the smallest initial position, the second smallest safe position to the soldier with the second smallest initial position, and so on.

4. **Reorder to Original Order:**
   Once the pairing is complete, map the chosen safe positions back to the original order of the soldiers. This assignment minimizes the total distance (and hence the time) and guarantees a lexicographically smallest sequence among all minimal solutions.

**Time Complexity:**
$$
O(N \log N)
$$
owing to the sorting steps, which is efficient given $N \leq 10^5$.

**C++ Code:**
```cpp
#include
#include
#include

using namespace std;
typedef long long ll;

int main() {
    int N;
    cin >> N;

    vector pos(N), safe_pos(N);
    vector> soldiers(N);

    for (int i = 0; i < N; i++) {
        cin >> pos[i];
        soldiers[i] = {pos[i], i};
    }

    for (int i = 0; i < N; i++) {
        cin >> safe_pos[i];
    }

    sort(soldiers.begin(), soldiers.end());
    sort(safe_pos.begin(), safe_pos.end());

    vector result(N);
    for (int i = 0; i < N; i++) {
        result[soldiers[i].second] = safe_pos[i];
    }

    for (int i = 0; i < N; i++) {
        cout << result[i] << (i == N - 1 ? '\n' : ' ');
    }

    return 0;
}
```

**Python Code:**
```python
def main():
    import sys
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    pos = list(map(int, input_data[1:N+1]))
    safe_pos = list(map(int, input_data[N+1:2*N+1]))

    # Pair soldier position with its original index
    soldiers = [(pos[i], i) for i in range(N)]

    # Sort soldiers based on their positions and sort safe positions
    soldiers.sort(key=lambda x: x[0])
    safe_pos.sort()

    result = [0] * N
    for i in range(N):
        result[soldiers[i][1]] = safe_pos[i]

    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
```

---

### Intuition and Analysis

The **Sorted Assignment** approach exploits the fact that pairing elements from two sorted arrays minimizes the sum of absolute differences between corresponding elements. By aligning the smallest soldier position with the smallest safe position, and so forth, the overall movement time is minimized. Sorting both lists leads to a time complexity of $$O(N \log N)$$, ensuring that the solution is efficient for large $N$ (up to $10^5$). Additionally, by reordering the safe positions back to the soldiers’ original order, the solution guarantees that the assigned sequence is lexicographically minimal in case of ties.

Happy Coding!

</details>
