## General

**Reduce the problem to group sizes**

The groups must have strictly increasing student counts and strictly increasing grade sums. Surprisingly, the actual grade values do not determine the maximum number of groups; only the number of students matters. This is possible because every grade is positive and the students may be rearranged freely.

Suppose we want to form $k$ groups. Their positive integer sizes must be strictly increasing. The smallest possible such size sequence is

$$
1,2,3,\ldots,k.
$$

Any other strictly increasing sequence of $k$ positive sizes uses at least as many students. The minimum required count is therefore the triangular number

$$
1+2+\cdots+k=\frac{k(k+1)}{2}.
$$

If there are $n$ students, a necessary condition for $k$ groups is

$$
\frac{k(k+1)}{2}\le n,
$$

or equivalently,

$$
k^2+k\le 2n.
$$

This gives an upper bound: no organization of grades can create $k$ groups if there are not enough students to give the groups distinct increasing sizes.

**Why the student-count bound is also sufficient**

We still need to show that satisfying the size inequality lets us satisfy the grade-sum inequality. Sort all grades in non-decreasing order. Take the smallest one grade for the first group, the next two grades for the second group, and so on through a group of size $k$. If $n$ is larger than the triangular number, put all leftover, largest grades into the last group.

Consider two consecutive groups before leftovers are added. Every grade in the later group is at least every grade in the earlier group because of sorting. The later group also contains one more student, and every grade is strictly positive. Its sum must therefore be strictly greater. More formally, the first as many elements as the earlier group can be paired with elements in the later group that are at least as large, and the later group has one additional positive element. The paired contribution is no smaller, and the extra contribution makes the total strictly larger.

Adding leftover positive grades only to the last group increases both its size and sum, so it cannot break either strict inequality with the preceding group. Thus every $k$ satisfying the triangular bound is achievable. The largest feasible $k$ is exactly the answer.

The code does not actually sort or construct groups because the proof establishes existence. Once existence depends only on $n$, examining the individual grade values would be wasted work.

**Locating the largest feasible value with binary search**

The implementation sets `n = len(grades)` and searches the integer candidates represented by `range(n + 1)`. Candidate `x` corresponds to forming `x` groups. The key function

```python
lambda x: x * x + x
```

maps it to $x^2+x$. This transformed sequence is increasing for non-negative integers. The feasibility condition is that the key is at most `n * 2`.

Python's call

```python
bisect_right(range(n + 1), n * 2, key=lambda x: x * x + x)
```

finds the insertion position immediately to the right of all candidates whose key is at most $2n$. An important API detail is that `key` is applied to elements of the searched sequence. The search target is already supplied in transformed form as `2 * n`; Python does not apply the key function to that target.

If the feasible candidates are `0, 1, ..., k`, the right insertion position is `k + 1`. Subtracting one produces `k`, the largest feasible number of groups. Candidate `0` is included to make the boundary natural, although the non-empty input always permits at least one group.

For $n=6$, the transformed candidate values are `0, 2, 6, 12, ...`. The target is `12`, so `bisect_right` returns the position after candidate `3`, and subtracting one gives `3`. Indeed, sizes `1, 2, 3` use all six students. Candidate `4` would require ten students.

For $n=8$, $k=3$ remains largest because $3\cdot4=12\le16$, whereas $4\cdot5=20>16$. Six students can fill sizes `1, 2, 3` and the other two can be placed in the final group, yielding sizes `1, 2, 5`. The sum construction remains valid because those leftovers are among the largest grades.

**Why the binary-search result is correct**

Feasibility is monotone: if $k$ groups are possible, every smaller number is possible because its triangular requirement is lower. Conversely, once $k$ violates $k(k+1)\le2n$, every larger candidate also violates it because the key function strictly increases. This false-after-true structure is precisely what binary search needs.

The proof has two halves. The triangular-number argument proves that no candidate to the right of the boundary can work. The sorted constructive argument proves that every candidate through the boundary can work while satisfying both required strict inequalities. Therefore, the rightmost feasible candidate returned by the search is neither an overestimate nor an underestimate.

## Complexity detail

Let $n$ be the number of students. `bisect_right` performs binary search over `n + 1` virtual integers. It evaluates the constant-time key function $O(\log n)$ times, so the exact code takes $O(\log n)$ time under the ordinary cost model.

The variant manifest labels this solution $O(1)$ time. That label reflects the closed-form nature of the mathematical reduction and the fixed machine-integer range in the actual constraints; the answer could be computed with the quadratic formula using a constant number of arithmetic operations. However, the shipped implementation deliberately uses binary search, so its operational asymptotic cost with an unbounded scalable $n$ is $O(\log n)$. The distinction is worth making explicit rather than hiding the behavior of the exact code.

`range(n + 1)` is lazy in Python: it does not allocate an array of all candidates. The search stores only a few indices and arithmetic values, so auxiliary space is $O(1)$. It does not sort `grades`, copy it, or construct the groups used in the existence proof.

## Alternatives and edge cases

- **Quadratic formula:** Solving $k^2+k-2n\le0$ gives $k=\left\lfloor(\sqrt{8n+1}-1)/2\right\rfloor$. This is a true constant-operation formulation, but integer square-root handling is preferable to floating point near boundaries.
- **Greedy accumulation:** Repeatedly subtract group sizes `1, 2, 3, ...` from the available student count is easy to understand but takes $O(\sqrt n)$ time.
- **Sorting and constructing groups:** This can demonstrate a valid arrangement in $O(n\log n)$ time, but construction is unnecessary because only the maximum count is requested.
- **One student:** The candidates `0` and `1` are feasible, so the right insertion point minus one returns `1`.
- **Exact triangular number:** When $n=k(k+1)/2$, equality is allowed. `bisect_right` places the boundary after `k`, correctly including that candidate.
- **Students left over:** Extra students can all join the last group. Their positive grades only increase its size and sum.
- **Repeated or equal grades:** Strictly increasing sums are still possible because later groups contain more positive elements, even if every grade is identical.
- **Why positivity matters:** A zero or negative grade could invalidate the argument that one additional student forces a strictly larger sum. The input guarantee `grades[i] >= 1` is essential.
- **Keyed bisect semantics:** The target is `2 * n`, not a group count. Supplying `n` or applying the key to the target would search for the wrong boundary.
