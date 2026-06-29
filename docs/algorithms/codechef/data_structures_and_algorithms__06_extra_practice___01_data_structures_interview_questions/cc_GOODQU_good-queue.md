# Good Queue

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GOODQU |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [GOODQU](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_04/problems/GOODQU) |

---

## Problem Statement

You are a teacher at Berland School. There are $N$ students in your class who are standing in a queue. The queue looks **good** if students are standing in ascending order of their height. In one move you can ask any two students to swap their positions if those two students are standing adjacent to each other. You also want to give minimum inconvenience to students, so you have to do the rearrangement in a minimum number of moves.

The heights of the students is expressed can be represented in the form of any array. The height of the student standing at $i^{th}$ position is $A_i$.

Determine the minimum number of moves needed to make the queue look good, also determine the moves you make. It is guaranteed that you can make the queue good by using at most $10^5$ moves.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each test case will contain two lines of input.
- The first line of each test case contains a single integer $N$.
- The second line of each test case contains N integers, $A_1, A_2 . . . A_N$.

---

## Output Format

- In a single line, output a single integer $K$, denoting the minimum number of moves needed to make the queue look good.
- Print two integers $i$ and $j$, in the following $K$ lines, denoting the position of students whose positions you wish to swap.

---

## Constraints

- $1 \leq T \leq 200$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^5$

It is guaranteed that the sum of $N$ over all the test cases is less than or equal to $3*10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
5
1 5 4 8 3
4
1 2 5 5
```

**Output**

```text
4
2 3
4 5
3 4
2 3
0
```

**Explanation**

**Test-Case:1**
Let’s see how array looks after each move
After 1st move ( i.e. swapping 2nd and 3rd element of array )
1 4 5 8 3

After 2nd move ( i.e. swapping 4th and 5th element of array )
1 4 5 3 8

After 3rd move ( i.e. swapping 3rd and 4th element of array )
1 4 3 5 8

After 4th move ( i.e. swapping 2nd and 3rd element of array )
1 3 4 5 8

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we discuss a classic problem where we must sort a queue of students by their heights using only adjacent swaps. The goal is to transform the queue into a “good” queue with the minimum number of moves. Recall that the minimum number of adjacent swaps needed to sort an array is equal to the number of inversions in the array. In this editorial, we present an efficient approach to solve this problem when the number of inversions is small (i.e. at most $$10^5$$ moves).

---

## Approach: Selection Sort with Adjacent Swaps

**Idea:**
For each position $$i$$ in the array, we find the minimum element in the subarray $$A[i \ldots N-1]$$ and "bubble" it to the correct position using adjacent swaps. Formally, if the minimum element is located at index $$\text{min\_idx}$$, we perform $$\text{min\_idx} - i$$ swaps—one for each adjacent move until it reaches position $$i$$.

**Why It Works:**
Each swap moves the chosen element one position to the left. Thus, the total number of adjacent swaps is exactly
$$
\sum_{i=0}^{N-1} (\text{min\_idx}_i - i),
$$
which directly corresponds to the number of inversions that need to be fixed. This approach ensures the minimal number of moves.

**C++ Implementation:**
```cpp
#include
#include
#include
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    vector> moves;
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[min_idx]) {
                min_idx = j;
            }
        }
        for (int j = min_idx; j > i; j--) {
            swap(a[j], a[j - 1]);
            moves.push_back({j, j + 1});
        }
    }
    cout << moves.size() << "\n";
    for (const auto& move : moves) {
        cout << move.first << " " << move.second << "\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
```

**Python Implementation:**
```python
def solve():
    import sys
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    index = 1
    out = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index+n]))
        index += n
        moves = []
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if a[j] < a[min_idx]:
                    min_idx = j
            for j in range(min_idx, i, -1):
                a[j], a[j - 1] = a[j - 1], a[j]
                moves.append((j, j + 1))
        out.append(str(len(moves)))
        for move in moves:
            out.append(f"{move[0]} {move[1]}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
```

---

## Summary

We presented the **Selection Sort with Adjacent Swaps** approach to sort the array with the minimum number of moves. By identifying and "bubbling" the minimum element in each unsorted segment of the queue, the number of swaps performed directly corresponds to the number of inversions in the array. This optimal method ensures an efficient transformation of the queue into a “good” queue.

Happy coding and best of luck with your DSA interview preparations!

</details>
