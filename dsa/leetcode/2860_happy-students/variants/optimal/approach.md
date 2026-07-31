## General

**A group size determines its membership**

Suppose exactly $k$ students are selected. Every selected student must have a threshold strictly below $k$, while every unselected student must have a threshold strictly above $k$. A student whose threshold equals $k$ cannot be happy in either group. Consequently, if a valid group of size $k$ exists, it is forced: it contains exactly the students whose thresholds are less than $k$.

Sort the thresholds into non-decreasing order. For an internal size $1 \le k < n$, the first $k$ students are the only possible selected group. It is valid exactly when

$$
\texttt{ordered[k - 1]} < k < \texttt{ordered[k]}.
$$

The left inequality makes every selected threshold small enough, and the right inequality makes every unselected threshold large enough. Because sorting places all smaller values before all larger values, checking those two boundary entries proves the condition for every student, not merely for the two at the boundary.

Handle the endpoint sizes separately. Selecting nobody is valid when the smallest threshold is greater than $0$. Selecting everybody is valid when the largest threshold is less than $n$; this always follows from the stated input constraint, but checking it keeps the boundary rule explicit. Count both valid endpoints and every valid internal boundary.

## Complexity detail

Let $n$ be the number of students. Sorting a copied list takes $O(n \log n)$ time and $O(n)$ auxiliary space, after which the boundary scan takes $O(n)$ time and $O(1)$ additional space.

The benchmark uses $n$ as `size` and supplies legal threshold arrays. The reference method sorts once and scans once. A correct enumeration method tries all $n + 1$ possible group sizes and scans all $n$ thresholds for each one, completing all tiers while exhibiting $O(n^2)$ scaling.

## Alternatives and edge cases

- **Count every candidate directly:** For each $k$ from $0$ through $n$, count thresholds below, equal to, and above $k$. This is easy to derive but takes $O(n^2)$ time without preprocessing.
- **Frequency table:** Since every threshold lies in $[0,n-1]$, prefix counts over a frequency array can test all group sizes in $O(n)$ time and $O(n)$ space. It has a better asymptotic time bound, but the sorting solution is the accepted branch preserved here and generalizes without relying on the bounded value domain.
- **Empty group:** It is valid only when every threshold is positive, which sorting reduces to `ordered[0] > 0`.
- **Full group:** The constraint `nums[i] < n` guarantees that selecting all $n$ students is valid.
- **Equality at the boundary:** If any threshold equals the proposed group size, that student is unhappy whether selected or not, so the size must not be counted.
- **Duplicate thresholds:** Equal values do not represent different group choices; for any valid size, membership is uniquely determined by which thresholds are smaller than that size.
