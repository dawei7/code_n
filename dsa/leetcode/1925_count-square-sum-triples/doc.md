# Count Square Sum Triples

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/count-square-sum-triples/) |
| Frontend ID | 1925 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A square triple is an ordered triple of integers `(a, b, c)` satisfying

$$
a^2+b^2=c^2.
$$

Given an upper bound `n`, count all square triples for which each of `a`, `b`, and `c` lies between $1$ and $n$, inclusive. The order of the first two values matters: when $a \ne b$, `(a, b, c)` and `(b, a, c)` are distinct triples and both contribute.

### Function Contract

**Inputs**

- `n`: the inclusive upper bound for every component, with $1 \le n \le 250$.

**Return value**

- Return the number of ordered triples `(a, b, c)` in $[1,n]^3$ satisfying $a^2+b^2=c^2$.

### Examples

**Example 1**

- Input: `n = 5`
- Output: `2`

The triples are `(3,4,5)` and `(4,3,5)`.

**Example 2**

- Input: `n = 10`
- Output: `4`

The two orientations of `(3,4,5)` and `(6,8,10)` qualify.

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Precompute the legal right-hand sides**

Create a set containing $c^2$ for every integer $c$ from $1$ through $n$. Membership in this set answers in expected constant time whether a sum of two squares is the square of an allowed integer.

**Enumerate the ordered legs**

Visit every ordered pair `(a, b)` in $[1,n]^2`. Compute `a * a + b * b` and increment the answer exactly when that value belongs to the precomputed square set.

Each qualifying ordered pair has at most one positive `c`, because squaring is strictly increasing on positive integers. Set membership therefore identifies exactly one legal triple without explicitly searching `c`. Conversely, every square triple contributes when its ordered pair `(a, b)` is visited, so none are missed. Iterating both full ranges naturally counts the reversed orientation separately.

#### Complexity detail

Building the $n$ squares takes $O(n)$ time and space. The nested loops examine $n^2$ ordered pairs with expected $O(1)$ set membership each, giving $O(n^2)$ time and $O(n)$ space.

#### Alternatives and edge cases

- **Enumerate `a`, `b`, and `c`:** Checking every possible triple is direct but costs $O(n^3)$ time.
- **Square root per pair:** Testing `isqrt(a * a + b * b)` avoids the set and uses $O(1)$ space, while retaining $O(n^2)$ time.
- **Count only `a < b` and double:** This is valid because no positive solution has $a=b$, but the ordered-loop form follows the contract more directly.
- **Values below five:** No positive Pythagorean triple fits, so the answer is zero.
- **Scaled triples:** Multiples such as `(6,8,10)` count independently from their primitive form.
- **Inclusive bound:** A triple with `c == n` is allowed.

</details>
