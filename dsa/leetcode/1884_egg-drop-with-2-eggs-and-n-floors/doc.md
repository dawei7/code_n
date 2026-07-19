# Egg Drop With 2 Eggs and N Floors

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/) |
| Frontend ID | 1884 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A building has floors numbered from $1$ through $N$, and you have two identical eggs. An unknown threshold $f$ lies between $0$ and $N$, inclusive. An egg survives every drop from floor $f$ or below and breaks from every higher floor.

On each move, choose any still-unbroken egg and any building floor. A surviving egg can be reused, but a broken one is lost. Determine the smallest number of moves that guarantees identifying the exact value of $f$ for every possible threshold and every sequence of drop outcomes.

### Function Contract

**Inputs**

- `n`: the number $N$ of floors, where $1 \le N \le 1000$.

**Return value**

- Return the minimum worst-case number of egg drops needed to determine $f$ with certainty.

### Examples

**Example 1**

- Input: `n = 2`
- Output: `2`

Testing floors `1` and `2` distinguishes all three possible thresholds.

**Example 2**

- Input: `n = 100`
- Output: `14`

Fourteen moves can cover $14+13+\cdots+1=105$ floors, whereas thirteen cover only $91$.

**Example 3**

- Input: `n = 3`
- Output: `2`

Drop first from floor `2`; either outcome leaves at most one floor to test.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Balance the two possible outcomes**

Suppose at most $m$ moves may be used. Drop the first egg $m$ floors above the last confirmed safe floor. If it breaks, one egg and $m-1$ moves remain, so those $m-1$ lower candidate floors can be checked sequentially. If it survives, raise the next first-egg drop by $m-1$ floors. Continue with gaps $m-2,m-3,\ldots,1$.

**Count how many floors are covered**

This decreasing-gap strategy covers

$$
1+2+\cdots+m=\frac{m(m+1)}{2}
$$

floors while keeping every outcome within $m$ moves. Conversely, with two eggs and $m$ moves, the first drop can leave at most $m-1$ lower floors for a one-egg linear search; each subsequent surviving drop must reduce that allowance by one. No strategy can cover more than the same triangular number. Thus $m$ moves are sufficient and necessary exactly when $\frac{m(m+1)}{2}\ge N$.

**Solve the inequality exactly**

The positive root is $\frac{\sqrt{8N+1}-1}{2}$. Use integer square root to obtain its floor without floating-point rounding, then increment once if that candidate's triangular number is still below $N$.

#### Complexity detail

A fixed number of integer arithmetic operations and one integer square-root operation determine the answer, which is $O(1)$ time under the standard fixed-width integer model for the stated bounds. Only scalar variables are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Quadratic dynamic programming:** Trying every first drop for every floor count is correct but costs $O(N^2)$ time and $O(N)$ space.
- **Incremental triangular scan:** Adding successive gap sizes until reaching $N$ takes $O(\sqrt N)$ time and $O(1)$ space.
- **One floor:** One drop is necessary and sufficient.
- **Triangular boundary:** If $N=\frac{m(m+1)}{2}$ exactly, return $m$ without incrementing.
- **Just above a boundary:** Floor count $\frac{m(m+1)}{2}+1$ requires $m+1$ moves.
- **Extreme thresholds:** The guarantee includes $f=0$, where every drop breaks, and $f=N$, where none do.

</details>
