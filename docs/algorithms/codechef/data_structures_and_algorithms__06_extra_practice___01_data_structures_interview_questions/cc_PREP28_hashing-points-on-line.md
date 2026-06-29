# Hashing - Points on Line

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP28 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Hashing |
| Official Link | [PREP28](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_13/problems/PREP28) |

---

## Problem Statement

Given $N$ points of the form $(x_i, y_i)$ on a $2$-D plane. Find the **maximum** number of points that lie on the same straight line.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains an integer $N$  — the number of points.
- The next $N$ lines contain two space-separated integers $x_i$, $y_i$ — the coordinate of the $i^{th}$ point.

---

## Output Format

For each test case, output on a new line the **maximum** number of points that lie on the same straight line.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 1000$
- $-10^9 \leq x_i, y_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^3$.

---

## Examples

**Example 1**

**Input**

```text
3
5
3 6
5 8
10 15
1 4
12 15
2
5 5
5 5
4
1 2
5 2
10 5
10 15
```

**Output**

```text
4
2
2
```

**Explanation**

**Test case $1$**: $(3, 6)$, $(5, 8)$, $(1, 4)$, $(12, 15)$ will be in same line.

**Test case $2$**: Both points $(5, 5)$ will be in same line.

**Test case $3$**: Any two points will be in same line.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we discuss how to solve the problem of finding the maximum number of points lying on the same line on a 2D plane. The aim is to determine a line that passes through the most number of given points. We will explore two different approaches, each with its own methodology and nuances. Understanding these approaches will strengthen your problem-solving skills and expose you to various techniques used in DSA.

---

## Approach 1: Slope-based Solution Using Floating Point

This is one of the most common solutions. The idea is simple:
1. For every point $i$, iterate over every remaining point $j$.
2. Compute the slope between point $i$ and $j$ as
   $$ slope = \frac{y_j - y_i}{x_j - x_i}. $$
3. Handle special cases:
   - If the two points overlap, increment an `overlap` counter.
   - If the line is vertical (i.e., $x_i = x_j$), increment a `vertical` counter.
4. Use a dictionary (or hash map) to count the frequencies of the slopes relative to point $i$.
5. Update the answer by considering the maximum count among slopes, vertical lines, and overlapping points (adding the base point itself).

This method is efficient with a time complexity of $O(N^2)$ and is sufficient for the given constraints.

### C++ Code for Approach 1:
```cpp
#include
#include
#include
#include
#include
using namespace std;

int maxPointsOnLine(vector>& points) {
    int n = points.size();
    if(n <= 2) return n;
    int maxPoints = 1;

    for (int i = 0; i < n; ++i) {
        unordered_map slopeCount;
        int overlap = 0;
        int vertical = 0;
        for (int j = i + 1; j < n; ++j) {
            if(points[i] == points[j]){
                overlap++;
                continue;
            }
            if(points[i].first == points[j].first){
                vertical++;
                continue;
            }
            double slope = (double)(points[j].second - points[i].second) /
                           (points[j].first - points[i].first);
            slopeCount[slope]++;
        }

        int currentMax = vertical;
        for(auto &entry : slopeCount) {
            currentMax = max(currentMax, entry.second);
        }
        maxPoints = max(maxPoints, currentMax + overlap + 1);
    }
    return maxPoints;
}

int main(){
    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        vector> points(N);
        for(int i = 0; i < N; i++){
            cin >> points[i].first >> points[i].second;
        }
        cout << maxPointsOnLine(points) << endl;
    }
    return 0;
}
```

### Python Code for Approach 1:
```python
def maxPointsOnLine(points):
    n = len(points)
    if n <= 2:
        return n
    max_points = 1
    for i in range(n):
        slope_count = {}
        overlap = 0
        vertical = 0
        for j in range(i+1, n):
            if points[i] == points[j]:
                overlap += 1
                continue
            if points[i][0] == points[j][0]:
                vertical += 1
                continue
            slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
            slope_count[slope] = slope_count.get(slope, 0) + 1
        current_max = vertical
        for count in slope_count.values():
            current_max = max(current_max, count)
        max_points = max(max_points, current_max + overlap + 1)
    return max_points

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        points = []
        for _ in range(N):
            x, y = map(int, input().split())
            points.append((x, y))
        print(maxPointsOnLine(points))
```

---

## Approach 2: Slope as a Reduced Fraction

Floating point arithmetic can sometimes be imprecise. This approach avoids precision issues by representing slopes as reduced fractions. The main idea is:
1. For every pair of points $(x_i, y_i)$ and $(x_j, y_j)$, compute
   $$ \Delta x = x_j - x_i \quad \text{and} \quad \Delta y = y_j - y_i. $$
2. Compute the greatest common divisor (GCD) of $\Delta x$ and $\Delta y$, then reduce them:
   $$ (\Delta y, \Delta x) \to \left( \frac{\Delta y}{g}, \frac{\Delta x}{g} \right). $$
3. Normalize the pair such that the denominator is always positive.
4. Use a dictionary or map to count the occurrence of each normalized slope.
5. Handle overlapping points and vertical lines separately, then combine counts appropriately.

This method ensures that slopes which are mathematically identical are represented exactly the same, avoiding potential errors from floating point calculations.

### C++ Code for Approach 2:
```cpp
#include
#include
#include
#include
#include
#include
using namespace std;

int maxPointsOnLine(vector>& points) {
    int n = points.size();
    if(n <= 2) return n;
    int result = 1;

    for (int i = 0; i < n; ++i) {
        map, int> slopeMap;
        int overlap = 0, vertical = 0, currentMax = 0;
        for (int j = i + 1; j < n; ++j) {
            if(points[i] == points[j]){
                overlap++;
                continue;
            }
            int dx = points[j].first - points[i].first;
            int dy = points[j].second - points[i].second;
            if(dx == 0){
                vertical++;
                continue;
            }
            int g = gcd(dx, dy);
            dx /= g;
            dy /= g;
            // Normalize slope so that dx is positive
            if(dx < 0){
                dx = -dx;
                dy = -dy;
            }
            slopeMap[{dy, dx}]++;
            currentMax = max(currentMax, slopeMap[{dy, dx}]);
        }
        currentMax = max(currentMax, vertical);
        result = max(result, currentMax + overlap + 1);
    }
    return result;
}

int main(){
    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        vector> points(N);
        for (int i = 0; i < N; i++){
            cin >> points[i].first >> points[i].second;
        }
        cout << maxPointsOnLine(points) << endl;
    }
    return 0;
}
```

### Python Code for Approach 2:
```python
from math import gcd

def maxPointsOnLine(points):
    n = len(points)
    if n <= 2:
        return n
    max_points = 1
    for i in range(n):
        slope_map = {}
        overlap = 0
        vertical = 0
        for j in range(i+1, n):
            if points[i] == points[j]:
                overlap += 1
                continue
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            if dx == 0:
                vertical += 1
                continue
            g = gcd(dx, dy)
            dx //= g
            dy //= g
            if dx < 0:
                dx, dy = -dx, -dy
            slope_map[(dy, dx)] = slope_map.get((dy, dx), 0) + 1
        current_max = vertical
        if slope_map:
            current_max = max(current_max, max(slope_map.values()))
        max_points = max(max_points, current_max + overlap + 1)
    return max_points

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        points = [tuple(map(int, input().split())) for _ in range(N)]
        print(maxPointsOnLine(points))
```

---

## Conclusion

- **Approach 1** (using floating point slopes) is straightforward and works well under the problem constraints.
- **Approach 2** avoids precision pitfalls by using rational numbers (reduced fractions).

Both approaches have a time complexity of $O(N^2)$ and are efficient and reliable for competitive programming challenges. Choose the approach that best fits your requirements with respect to precision and simplicity.

Happy Coding!

</details>
