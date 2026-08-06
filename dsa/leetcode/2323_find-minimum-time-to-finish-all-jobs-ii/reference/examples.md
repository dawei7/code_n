## Examples

**Example 1**

- **Input:** `jobs = [5, 2, 4], workers = [1, 7, 5]`
- **Output:** `2`
- **Explanation:**
  - Sort `jobs` to `[2, 4, 5]` and `workers` to `[1, 5, 7]`.
  - Pair 1: job 2 with worker 1 takes $\lceil 2/1 \rceil = 2$ days.
  - Pair 2: job 4 with worker 5 takes $\lceil 4/5 \rceil = 1$ day.
  - Pair 3: job 5 with worker 7 takes $\lceil 5/7 \rceil = 1$ day.
  - Maximum completion time is $\max(2, 1, 1) = 2$ days.

**Example 2**

- **Input:** `jobs = [3, 18, 15, 9], workers = [6, 5, 1, 3]`
- **Output:** `3`
- **Explanation:**
  - Sort `jobs` to `[3, 9, 15, 18]` and `workers` to `[1, 3, 5, 6]`.
  - Pair 1: $3 / 1 = 3$ days.
  - Pair 2: $9 / 3 = 3$ days.
  - Pair 3: $15 / 5 = 3$ days.
  - Pair 4: $18 / 6 = 3$ days.
  - Maximum completion time is 3 days.
