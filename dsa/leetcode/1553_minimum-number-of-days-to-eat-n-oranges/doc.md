# Minimum Number of Days to Eat N Oranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1553 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/) |

## Problem Description
### Goal
You begin with `n` oranges. On each day, choose exactly one allowed action: eat one orange; if the current amount is divisible by two, eat half of the oranges; or, if it is divisible by three, eat two thirds of the oranges.

Return the minimum number of days required to eat every orange. Divisibility is tested against the number remaining at the start of that day, and even when both division actions are available, only one action may be taken that day.

### Function Contract
**Inputs**

- `n`: the initial number of oranges, where $1 \le n \le 2 \times 10^9$.

**Return value**

The minimum number of daily actions needed to reduce the number of remaining oranges to zero.

### Examples
**Example 1**

- Input: `n = 10`
- Output: `4`
- Explanation: Eat one orange, then use the divisible-by-three action on nine, followed by the divisible-by-three action on three, and finally eat the last orange.

**Example 2**

- Input: `n = 6`
- Output: `3`
- Explanation: Eat three oranges by halving, then eat two thirds of the remaining three, then eat the last orange.

**Example 3**

- Input: `n = 1`
- Output: `1`
- Explanation: The only possible action eats the single orange.

### Required Complexity

- **Time:** $O((\log n)^2)$
- **Space:** $O((\log n)^2)$

<details>
<summary>Approach</summary>

#### General

**Skip forced one-orange days in groups**

Before using the divide-by-two action, exactly `oranges % 2` individual oranges must be eaten to reach a divisible amount. That route costs those remainder days, one division day, and the optimal time for `oranges // 2` remaining oranges. The divide-by-three route is analogous.

This yields the memoized recurrence

$$
D(x)
=
1+
\min
\left(
x \bmod 2 + D(\lfloor x/2 \rfloor),
x \bmod 3 + D(\lfloor x/3 \rfloor)
\right)
$$

for $x>1$, with $D(0)=0$ and $D(1)=1$.

**Why no other first decision is needed**

Any optimal plan that eventually uses division by two must first remove at least the remainder modulo two; eating more individual oranges before that division only delays reaching a smaller state that the recurrence will consider later. The same argument holds for division by three. A plan using only one-orange days is also represented through repeated remainder handling and the base cases.

Thus every optimal plan begins with one of the two recurrence routes, and each route describes a legal sequence followed by an optimal smaller subproblem. Taking their minimum is exact.

**Memoize overlapping quotient states**

Recursive paths repeatedly reach the same values formed by divisions by powers of two and three. Cache each result so every distinct quotient state is solved once. The arguments shrink geometrically, keeping the explored state set tiny even when `n` is near two billion.

#### Complexity detail

Every reached state has the form $lfloor n/(2^a3^b)\rfloor$ for nonnegative exponents $a$ and $b$. There are $O(\log n)$ relevant values of each exponent and therefore $O((\log n)^2)$ distinct memoized states. Each state performs constant work, so both time and memo storage are $O((\log n)^2)$. Recursion depth is only $O(\log n)$ and is covered by the stated space bound.

#### Alternatives and edge cases

- **Bottom-up DP through every count:** compute answers from zero through $n$, but this takes $O(n)$ time and space and is infeasible near the upper bound.
- **Unmemoized recursion:** follows the correct recurrence but recomputes the same quotient states many times.
- **Breadth-first search:** model remaining counts as states and daily actions as edges, but an unrestricted search can visit far more states than the quotient recurrence.
- At $n=1$, exactly one day is required.
- A number divisible by both two and three must still compare the two one-day division choices.
- Eating one orange can be optimal when it enables a much better division on the next day.
- The recurrence counts the division day separately from the individual remainder days.
- Large input values must not trigger allocation proportional to $n$.

</details>
