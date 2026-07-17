# Calculate Money in Leetcode Bank

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1716 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/calculate-money-in-leetcode-bank/) |

## Problem Description
### Goal

Hercy deposits money every day. On the first Monday he deposits one dollar, then increases the daily deposit by one dollar from Tuesday through Sunday. Each later Monday starts one dollar higher than the preceding Monday, and that week again increases by one dollar each day.

Given a day count `n`, return the total money deposited from the first Monday through the end of day `n`.

### Function Contract
**Inputs**

- `n`: the inclusive number of saving days, with $1 \le n \le 1000$

**Return value**

The sum of the deposits made on days $1$ through $n$ under the weekly increasing pattern.

### Examples
**Example 1**

- Input: `n = 4`
- Output: `10`

The first four deposits are 1, 2, 3, and 4 dollars.

**Example 2**

- Input: `n = 10`
- Output: `37`

The first week contributes 28 dollars; the next Monday through Wednesday contribute 2, 3, and 4 dollars.

**Example 3**

- Input: `n = 20`
- Output: `96`

Two complete weeks contribute 28 and 35 dollars, and the following six days contribute 3 through 8 dollars.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Sum complete weeks as an arithmetic progression**

Write `n = 7 * w + d`, where $w$ is the number of complete weeks and $0 \le d < 7$. Week zero deposits `1` through `7`, totaling 28. Every later week adds one dollar to each of seven days, so complete-week totals are

$$
28, 35, 42, \ldots, 28+7(w-1).
$$

Their sum is

$$
28w+\frac{7w(w-1)}{2}.
$$

**Add the incomplete week**

After $w$ complete weeks, the next Monday deposit is $w+1$. The first $d$ days of that week form

$$
w+1,w+2,\ldots,w+d.
$$

Their sum is

$$
d(w+1)+\frac{d(d-1)}{2}.
$$

Adding the two formulas covers each of the first `n` days exactly once. Integer division and remainder recover $w$ and $d$ directly, so no simulation is required.

#### Complexity detail

The calculation uses a fixed number of divisions, multiplications, additions, and subtractions regardless of `n`, giving $O(1)$ time. It stores only the week count, remainder, and partial totals, for $O(1)$ space.

#### Alternatives and edge cases

- **Simulate every day:** following the deposit pattern directly is correct but takes $O(n)$ time.
- **Loop over complete weeks:** summing seven-day blocks reduces constants but still takes $O(n/7)$ time.
- **First day:** `n = 1` returns the first Monday deposit of one dollar.
- **Exact week:** when `d = 0`, the incomplete-week contribution is zero.
- **First day of a later week:** the new Monday is one dollar greater than the previous Monday, not the previous Sunday.
- **Maximum day count:** the same closed form applies at `n = 1000` without accumulation error.

</details>
