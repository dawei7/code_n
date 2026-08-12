# Counting Sundays - Optimal Approach

## Algorithm Explanation

We count how many Sundays fell on the $1^{\text{st}}$ day of the month between $1\text{ Jan }1901$ and $31\text{ Dec }2000$.

Using Python's standard `datetime.date(year, month, 1)`:
1. Iterate `year` from $1901$ to $2000$.
2. Iterate `month` from $1$ to $12$.
3. Check `weekday() == 6` (where Sunday is represented by index $6$).
4. Increment counter whenever true.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(Y \cdot M)$ where $Y = 100$ and $M = 12$ ($1200$ date checks).
- **Space Complexity:** $\mathcal{O}(1)$ - Constant auxiliary memory.
