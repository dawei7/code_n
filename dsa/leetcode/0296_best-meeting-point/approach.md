## General

Trying every grid cell as a meeting point would be wasteful. For each candidate, one would have to sum its distance to every home, even though Manhattan distance has a structure that identifies the optimum directly.

If friend $t$ lives at row $r_t$ and column $c_t$, and the meeting point is $(x,y)$, that friend's distance is

$$
\lvert r_t-x\rvert+\lvert c_t-y\rvert.
$$

Summing over all $k$ friends gives

$$
\sum_{t=1}^{k}\left(\lvert r_t-x\rvert+\lvert c_t-y\rvert\right)
=
\sum_{t=1}^{k}\lvert r_t-x\rvert
+
\sum_{t=1}^{k}\lvert c_t-y\rvert.
$$

The first sum depends only on the chosen row $x$, and the second depends only on the chosen column $y$. Changing the row cannot affect the column cost, and changing the column cannot affect the row cost. Therefore, the two-dimensional optimization separates into two independent one-dimensional problems:

1. Choose a row minimizing the sum of absolute row differences.
2. Choose a column minimizing the sum of absolute column differences.

The solution to each one-dimensional problem is a median.

**Why a median minimizes absolute distance**

Suppose the sorted coordinates on one axis are

$$
a_0\le a_1\le\cdots\le a_{k-1}.
$$

Pair the smallest coordinate with the largest, the second smallest with the second largest, and so on. For a pair $a_i\le a_j$, any proposed meeting coordinate $z$ pays

$$
\lvert a_i-z\rvert+\lvert a_j-z\rvert.
$$

This sum is at least $a_j-a_i$. Equality holds whenever $z$ lies anywhere in the interval $[a_i,a_j]$. Moving outside that interval increases the sum because both distances then grow in the same outward direction.

To minimize every nested extreme pair simultaneously, choose $z$ in the middle interval. With an odd number of coordinates, that interval collapses to the single middle coordinate. With an even number, any coordinate between the lower and upper middle values is optimal. Selecting either middle value is therefore always valid.

Another way to see the same fact is to imagine shifting $z$ one step right. Every point to the left contributes one additional unit, while every point to the right contributes one fewer unit. Before the median, more points lie to the right, so moving right can improve the total. After the median, more points lie to the left, so moving right makes the total worse. The transition occurs at the median.

The mean does not have this property for absolute differences. A far-away coordinate can pull the mean away from most friends, while the median depends on how many coordinates lie on each side rather than how far an outlier lies.

**Collecting the occupied coordinates**

The source scans every cell with row index `i`, column index `j`, and value `v`. Whenever `v` is 1, it appends `i` to `rows` and `j` to `cols`. Each friend contributes exactly one coordinate to each list, so the two lists have the same length $k$.

The scan visits rows from top to bottom. Within each row, it visits columns from left to right. Because every row index from an earlier outer-loop iteration is no larger than every row index from a later iteration, `rows` is automatically collected in non-decreasing order. Repeated homes in the same row simply contribute repeated equal row coordinates, which is necessary because every friend contributes separately to the distance.

The column list is different. After finishing one row, the scan returns to column zero of the next row. For the example homes $(0,0)$, $(0,4)$, and $(2,2)$, the collected columns are `[0, 4, 2]`, which are not sorted. The exact source therefore calls `cols.sort()` before choosing the column median.

**Selecting the two median coordinates**

The source uses `len(rows) >> 1` as the median index. A right shift by one is integer division by two for the nonnegative list length, so this is the same index as `len(rows) // 2`.

For odd $k$, index $k//2$ is the unique middle element. For even $k$, it is the upper of the two middle elements. Choosing the upper median is valid because every point between the two middle coordinates minimizes the sum of absolute distances.

The statements

`i = rows[len(rows) >> 1]`

and

`j = cols[len(cols) >> 1]`

therefore choose an optimal meeting row and an optimal meeting column. Both values come from home coordinates and hence lie inside the grid, although the median proof would also permit intermediate coordinates in the even case.

**Computing the minimum total**

The helper `f(arr, x)` calculates `sum(abs(v - x) for v in arr)`. Calling it on `rows` and the selected row gives the smallest possible vertical travel. Calling it on `cols` and the selected column gives the smallest possible horizontal travel. Their sum is the minimum Manhattan travel because Manhattan distance is exactly vertical travel plus horizontal travel.

For the first example, the collected data is:

- `rows = [0, 0, 2]`, already sorted;
- `cols = [0, 4, 2]`, then sorted to `[0, 2, 4]`.

The median row is 0 and the median column is 2. Vertical distance is

$$
\lvert0-0\rvert+\lvert0-0\rvert+\lvert2-0\rvert=2,
$$

and horizontal distance is

$$
\lvert0-2\rvert+\lvert4-2\rvert+\lvert2-2\rvert=4.
$$

The total is $2+4=6$.

**Why independent optimal choices form a global optimum**

Let $R(x)$ denote the total vertical cost at row $x$, and let $C(y)$ denote the total horizontal cost at column $y$. The total is $R(x)+C(y)$. The chosen median row $x^*$ satisfies $R(x^*)\le R(x)$ for every row $x$, and the chosen median column $y^*$ satisfies $C(y^*)\le C(y)$ for every column $y$. Adding those inequalities gives

$$
R(x^*)+C(y^*)\le R(x)+C(y)
$$

for every possible meeting point $(x,y)$. Thus, independently minimizing the axes does not miss a better two-dimensional tradeoff; no such tradeoff exists under an additive Manhattan metric.

## Complexity detail

Let $m$ be the number of grid rows, $n$ the number of columns, and $k$ the number of homes.

Scanning the entire matrix costs $O(mn)$ time. Sorting the $k$ collected column coordinates costs $O(k\log k)$ time in the worst case. The row coordinates need no sorting because the row-major traversal already produces them in non-decreasing order. The two calls to `f` each visit $k$ coordinates, adding $O(k)$ time. The exact source therefore runs in

$$
O(mn+k\log k)
$$

time. Since $k\le mn$, a looser bound is $O(mn\log(mn))$.

The two coordinate lists each contain $k$ integers, so their combined storage is $O(k)$. Python's in-place sort may use additional temporary memory depending on detected runs, but the package-level structural storage remains $O(k)$. The generator used by `sum` does not build a third list.

The local manifest states $O(mn)$ time and says both axes are obtained without sorting. That bound describes the column-major collection variant from the editorial, not the exact `solution.py`, which explicitly executes `cols.sort()`. This approach records the executable source's $O(mn+k\log k)$ bound without changing any other package artifact.

## Alternatives and edge cases

- **Collect columns in column-major order:** Scan each column from left to right and each row within that column. Then `cols` is already sorted, eliminating `cols.sort()` and achieving $O(mn)$ time with $O(k)$ coordinate storage. This is the linear method described by the manifest, but it is not the exact source's traversal.
- **Pair extremes without selecting a median:** Once a coordinate list is sorted, add `arr[right] - arr[left]` while moving both pointers inward. This directly sums the unavoidable cost of each extreme pair and produces the same minimum.
- **Sort both coordinate lists:** It is correct but wastes work on `rows`, whose order is already guaranteed by the row-major scan.
- **Try every grid cell:** Computing distance from every candidate to every home costs $O(mnk)$ time and can reach $O(m^2n^2)$ when most cells contain homes.
- **Breadth-first search from every candidate:** Obstacles do not exist and Manhattan distance has a direct formula, so BFS adds queues and visited matrices without changing the distance result.
- **Use the arithmetic mean:** The mean minimizes squared distance, not the sum of absolute distances. An outlier can pull it away from the median and increase the required total.
- **Choose row and column from the same friend:** The optimal row and optimal column are independent. Their combination need not be one friend's home; requiring that restriction can miss valid optimal meeting points.
- **Even number of homes:** Any coordinate between the two middle values on an axis is optimal. The source deliberately chooses the upper middle value through index `k // 2`.
- **Repeated rows or columns:** Repetitions must remain in the lists because they represent different friends. Removing duplicates would give too little weight to crowded coordinates and could change the median.
- **Two adjacent homes:** For `[[1,1]]`, the row cost is zero. Either column 0 or 1 minimizes the horizontal cost at 1; the upper median selects column 1 and returns 1.
- **All homes in one row:** The median row is that shared row, so vertical distance is zero. Only column distances contribute.
- **All homes in one column:** The median column is that shared column, so horizontal distance is zero. Only row distances contribute.
- **Dense grid:** There can be $mn$ homes. Coordinate collection still uses $O(k)$ space, and each home contributes once to each axis sum.
- **At least two homes:** The source can also compute a one-home answer, but the contract guarantees two or more, so both coordinate lists are certainly nonempty when the median index is read.
- **Meeting point on an empty cell:** This is allowed. The problem minimizes travel to a point in the grid; it does not require that point to contain a home.
- **Manhattan distance specifically:** Axis separation relies on the sum of absolute coordinate differences. Euclidean distance would not permit the same independent median argument.
