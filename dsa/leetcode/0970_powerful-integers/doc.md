# Powerful Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 970 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [powerful-integers](https://leetcode.com/problems/powerful-integers/) |

## Problem Description

### Goal

For non-negative integers $i$ and $j$, a powerful integer has the form $x^i+y^j$. Given positive bases `x` and `y` together with an inclusive upper limit `bound`, find every distinct powerful integer whose value is at most `bound`.

The exponents may independently be zero, so each base contributes $1$ as its first power. Return each qualifying value once, in any order, even when several exponent pairs produce the same sum.

### Function Contract

**Inputs**

- `x` and `y`: integer bases satisfying $1 \le x,y \le 100$.
- `bound`: an inclusive upper bound satisfying $0 \le \texttt{bound} \le 10^6$.
- Let $P_x$ and $P_y$ be the distinct powers of the two bases that need consideration, beginning with exponent zero and ending once further growth cannot participate in a bounded sum. Define $A=\lvert P_x\rvert$ and $B=\lvert P_y\rvert$.
- Let $R$ be the number of distinct returned sums.

**Return value**

Return every distinct value $x^i+y^j\le\texttt{bound}$ for integers $i,j\ge0$, in any order.

### Examples

**Example 1**

- Input: `x = 2, y = 3, bound = 10`
- Output: `[2,3,4,5,7,9,10]`

**Example 2**

- Input: `x = 3, y = 5, bound = 15`
- Output: `[2,4,6,8,10,14]`

### Required Complexity

- **Time:** $O(AB)$
- **Space:** $O(A+B+R)$

<details>
<summary>Approach</summary>

#### General

**Enumerate each distinct power once.** Build the sequence beginning at `1`. When a base is greater than `1`, repeatedly multiply by that base while the next power is no larger than `bound`. When the base equals `1`, stop immediately because every exponent produces the same value.

**Combine the finite power sequences.** Visit every pair from $P_x\times P_y$. If `x_power + y_power <= bound`, insert the sum into a set. The set removes collisions caused by different exponent pairs without affecting the unrestricted result order.

**Why larger powers can be ignored.** Both powers are positive. Once one power already exceeds `bound`, adding any power of the other positive base cannot restore a valid sum. The generated finite sequences therefore contain every power that might participate, and the Cartesian enumeration considers every qualifying exponent pair.

#### Complexity detail

Generating the two sequences costs $O(A+B)$, and their Cartesian product contains $AB$ pairs, so total time is $O(AB)$. The two power lists and the set of $R$ answers use $O(A+B+R)$ space.

#### Alternatives and edge cases

- **Nested multiplication loops:** Advance powers directly inside two loops and break when each base stops growing. This has the same asymptotic cost but needs explicit `base == 1` guards to avoid infinite loops.
- **Linear result deduplication:** Store answers in a list and scan it before each insertion. It remains correct but can add a factor of $R$ to the running time.
- **Enumerate exponent bounds blindly:** Trying a fixed exponent range works only when that range is proved sufficient for every allowed base and bound.
- **Base equals one:** Its distinct power sequence contains only `1`, regardless of exponent.
- **Bound below two:** No powerful integer qualifies because the smallest possible sum is $1+1=2$.
- **Duplicate sums:** Return a value once even if multiple exponent pairs generate it.

</details>
